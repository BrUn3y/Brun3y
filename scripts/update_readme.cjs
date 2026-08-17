#!/usr/bin/env node
"use strict";

/**
 * Daily README updater for Edgar Bruney (BrUn3y/Brun3y)
 * Rotates layout, taglines, and section focus every day.
 * All information gathered from public internet sources by AI.
 */

const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

// ── Seed: day-of-year gives 365 distinct rotations ──────────────────────────
const now = new Date();
const startOfYear = new Date(now.getFullYear(), 0, 0);
const dayOfYear = Math.floor((now - startOfYear) / 86_400_000);
const seed = dayOfYear % 7; // 7 layout variants

const TIMESTAMP = now.toISOString().replace("T", " ").slice(0, 19) + " UTC";
const DATE_LABEL = now.toISOString().slice(0, 10);

// ── Static widgets (always present, never rotated away) ───────────────────────
const BADGES = `<a href="https://linkedin.com/in/bruney"><img src="https://img.shields.io/badge/LinkedIn-000000?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
<a href="https://medium.com/@brun3y"><img src="https://img.shields.io/badge/Medium-000000?style=flat&logo=medium&logoColor=white" alt="Medium" /></a>
<a href="https://x.com/BrUn3y"><img src="https://img.shields.io/badge/X-000000?style=flat&logo=x&logoColor=white" alt="X" /></a>
<img src="https://komarev.com/ghpvc/?username=BrUn3y&label=Views&color=000000&style=flat" alt="Views" />`;

const SNAKE = `<img src="https://raw.githubusercontent.com/BrUn3y/Brun3y/output/github-snake-dark.svg" alt="contribution snake" align="right" width="48%" />`;

const STACK = `<img src="./assets/tech-stack.svg" alt="Tech Stack" width="100%" />`;

const STATS_WIDGETS = `<img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=BrUn3y&theme=github_dark" alt="GitHub stats" />
<img src="https://github-readme-streak-stats.herokuapp.com/?user=BrUn3y&theme=github-dark-blue&hide_border=true&background=0D1117&stroke=30363D&ring=53B14F&fire=53B14F&currStreakLabel=E6EDF3" alt="GitHub streak" />`;

const SPOTIFY = `[![spotify-github-profile](https://spotify-github-profile.kittinanx.com/api/view?uid=brun3y&cover_image=true&theme=default&show_offline=false&background_color=121212&interchange=false&profanity=false&hide_remaster=false)](https://github.com/kittinan/spotify-github-profile)`;

const PROJECTS = `- **[IBM Bob Shell Harness](https://github.com/BrUn3y/IBM_Bob_Harness)** — Dockerized harness that runs IBM's Bob Shell headless in unrestricted mode and exposes it over a REST API.
- **[Strava Agent](https://github.com/BrUn3y/Strava_Agent)** — Conversational BeeAI agent that analyzes athletic performance directly from the Strava API.
- **X Trends Agent** — Same trend-analysis agent, three frameworks: [BeeAI](https://github.com/BrUn3y/x_trends_agent_BeeAI) · [CrewAI](https://github.com/BrUn3y/x_trends_agent_CrewAI) · [LangGraph](https://github.com/BrUn3y/x_trends_agent_LangGraph).`;

const WRITING_TABLE = `<table>
  <tr>
    <td>
      <a href="https://medium.com/@brun3y/how-my-ai-agent-is-engineering-a-5km-pr-a2e9966869f4">
        <img src="./assets/medium/1.svg" alt="How My AI Agent is Engineering a 5KM PR" />
      </a>
    </td>
    <td>
      <a href="https://medium.com/@brun3y/ibm-bob-shell-skills-sh-supercharging-your-personal-ai-d074dbd5ec7c">
        <img src="./assets/medium/2.svg" alt="IBM Bob Shell + Skills.sh: Supercharging Your Personal AI" />
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://medium.com/@brun3y/i-finally-got-positive-results-following-my-strava-ai-agent-76ab080d8808">
        <img src="./assets/medium/3.svg" alt="I Finally Got Positive Results Following My Strava AI Agent" />
      </a>
    </td>
    <td>
      <a href="https://medium.com/@brun3y/my-personal-ai-agent-for-strava-bdcb43d4fa3a">
        <img src="./assets/medium/4.svg" alt="My Personal AI Agent for Strava" />
      </a>
    </td>
  </tr>
</table>`;

const STRAVA_PRS = `<div align="center">

<img src="./assets/strava-pr-5k.svg" alt="5K Personal Records" width="32%" />
<img src="./assets/strava-pr-10k.svg" alt="10K Personal Records" width="32%" />
<img src="./assets/strava-pr-21k.svg" alt="21K Personal Records" width="32%" />

</div>`;

const STRAVA_WIDGET = `<img src="./assets/strava-widget.svg" alt="Recent Strava Activities" width="100%" />`;

const FOOTER_LINKS = `<a href="https://linkedin.com/in/bruney"><img src="https://img.shields.io/badge/LinkedIn-000000?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
<a href="https://medium.com/@brun3y"><img src="https://img.shields.io/badge/Medium-000000?style=flat&logo=medium&logoColor=white" alt="Medium" /></a>
<a href="https://x.com/BrUn3y"><img src="https://img.shields.io/badge/X-000000?style=flat&logo=x&logoColor=white" alt="X" /></a>
<a href="https://wa.me/Brun3y"><img src="https://img.shields.io/badge/WhatsApp-Brun3y-000000?style=flat&logo=whatsapp&logoColor=white" alt="WhatsApp: Brun3y" /></a>`;

// ── Rotating content pools ────────────────────────────────────────────────────

const taglines = [
  "Full Stack Engineer & AI Agent Builder @ IBM",
  "Agentic AI Engineer · Cloud Architect · Quantum Explorer",
  "Building autonomous agents that actually do things · IBM CIO Org",
  "From Zapopan to the cloud — shipping AI systems at IBM",
  "Full Stack × AI Agents × Quantum Computing · IBM Engineer",
  "10+ years shipping code · Now building the agentic layer",
  "IBM Engineer · Runner chasing sub-21 · Heavy music · AI labs",
];

const about_intros = [
  `I'm **Edgar Bruney** — a Full Stack & Systems Engineer based in **Zapopan, Mexico**, building production AI systems inside **IBM's CIO Organization**. On GitHub since **2013**, with a decade of shipping scalable cloud applications behind me.`,

  `Meet **Edgar Bruney** — an engineer who joined GitHub in **2013** and never stopped shipping. Today I work inside **IBM's CIO Organization** in **Zapopan, Mexico**, translating research-grade AI into real production systems.`,

  `I'm **Edgar Bruney Castañeda Torres** — Systems Computer Engineer turned agentic AI practitioner, currently embedded in **IBM's CIO Org** in **Zapopan, Jalisco**. My GitHub history stretches back to **2013**.`,

  `**Edgar Bruney** here — Full Stack Engineer at **IBM** with 10+ years building for the cloud. I call **Zapopan, Mexico** home, and my code has lived on GitHub since **2013**.`,

  `**Edgar Bruney** — IBM engineer, AI agent enthusiast, and occasional quantum tinkerer operating out of **Zapopan, Mexico**. I've been pushing commits since **2013**.`,

  `You're looking at the GitHub profile of **Edgar Bruney Castañeda Torres** — a Full Stack Engineer at **IBM's CIO Organization**, based in **Zapopan, Mexico**, building since **2013**.`,

  `I'm **Edgar Bruney**, a decade-long engineer now at **IBM** focusing on agentic AI systems. Zapopan-based, cloud-native, GitHub-resident since **2013**.`,
];

const PROFESSIONAL_JOURNEY = `**Edgar Bruney** is an experienced engineer at **IBM's CIO Organization** in **Zapopan, Jalisco, Mexico**, specializing in translating research-grade AI into production systems. A GitHub member since **2013** with over 13 years of experience in the tech industry, he has built a distinguished career focused on cutting-edge technology implementation and open-source contribution.

Currently working at the intersection of **agentic AI development** and **cloud architecture**, Edgar designs and implements multi-agent pipelines using frameworks like **BeeAI**, **CrewAI**, and **LangGraph**. His work spans from concept to deployed REST APIs with async jobs and live SSE streaming, with emphasis on practical applications that solve real-world problems. He specializes in verify-and-retry orchestration loops and production-ready AI systems that bridge the gap between research and enterprise deployment, demonstrating a unique ability to transform research-grade AI into practical enterprise solutions.`;

const TECHNICAL_EXPERTISE = `Edgar holds multiple industry certifications:
- **IBM Generative & Agentic AI Expert Developer**
- **AWS Serverless Badge Holder**
- **Hybrid Cloud Microservices Architect**

His comprehensive technical stack includes:
- **AI/ML Frameworks:** BeeAI, CrewAI, LangGraph, AgentStack SDK, A2A protocol
- **Cloud Platforms:** IBM Cloud, AWS, multi-cloud architecture design and implementation
- **Quantum Computing:** Qiskit experiments and community contributions, active contributor to IBM's Qiskit Runtime (235⭐, 218 forks)
- **Integration Technologies:** REST API design, Docker containerization, Slack integration (Socket Mode), Strava API, Google Fit API
- **Specializations:** Multi-agent pipeline design, verify-and-retry orchestration loops, async jobs with live SSE streaming, enterprise AI deployment`;

const about_bodies = [
  `My current focus is **AI agents**: autonomous systems built on **BeeAI, CrewAI, and LangGraph** that solve real problems — a [Strava performance coach](https://medium.com/@brun3y/my-personal-ai-agent-for-strava-bdcb43d4fa3a) that trained me toward a **sub-21' 5K**, containerized **IBM Bob Shell** workflows, and X trend-analysis tools. I also explore **quantum computing** with **Qiskit** and co-lead Guadalajara's IBM Quantum community (60+ attendees at our first session).

Off the keyboard I chase running PRs and code to **heavy music**.`,

  `Right now I'm deep in **agentic AI** — designing multi-agent pipelines with **BeeAI**, **CrewAI**, and **LangGraph** that go from idea to deployed REST API. I built a [personal running coach agent](https://medium.com/@brun3y/my-personal-ai-agent-for-strava-bdcb43d4fa3a) on top of the **Strava API** that actually moved my 5K time, and I containerized **IBM Bob Shell** into a headless REST harness. Beyond that: **Qiskit** experiments, multi-cloud architecture, and co-organizing **quantum computing meetups** in Guadalajara.

When I step away from the screen, I run — targeting **sub-21 minutes** for 5K — and listen to **heavy music**.`,

  `The thread connecting my work: **autonomous agents doing real things**. I've built Strava coaches, X trend analyzers (same agent, three frameworks: **BeeAI / CrewAI / LangGraph**), and REST-exposed **IBM Bob Shell** harnesses. I hold the **IBM Generative & Agentic AI Expert Developer** certification and co-organize the **IBM Quantum Guadalajara** community where we run hands-on Qiskit sessions.

Personal side: hybrid athlete training toward a **sub-21' 5K**, **space exploration** nerd, and heavy music devotee.`,

  `I ship agentic systems for a living: autonomous **BeeAI**, **CrewAI**, and **LangGraph** pipelines, containerized AI harnesses, and cloud-native microservices on **IBM Cloud, AWS, and GCP**. A notable personal project: an AI agent that analyzes my **Strava** training data and produces a weekly running plan — it helped me break a plateau on the way to my **sub-21' 5K** goal. I also hold the **IBM Generative & Agentic AI Expert** badge and explore **Qiskit**.

Side passions: running, heavy music, and space.`,

  `My work sits at the intersection of **enterprise cloud** and **agentic AI**. Inside IBM I design microservices and cloud solutions; outside work hours I prototype AI agents with **BeeAI**, **CrewAI**, and **LangGraph** — including a [conversational Strava coach](https://medium.com/@brun3y/my-personal-ai-agent-for-strava-bdcb43d4fa3a) and multi-platform X trend analyzers. I'm also co-building a **quantum computing community** in Guadalajara through IBM.

When I'm not at a keyboard: running sub-21' 5K, listening to heavy music, watching space launches.`,

  `Certified **IBM Generative & Agentic AI Expert Developer**, **AWS Serverless** badge holder, and **Hybrid Cloud Microservices Architect** — but the thing I'm most proud of is shipping agents that work in the real world. My open-source projects range from a containerized **IBM Bob Shell REST API** to a **Strava performance agent** that helped me improve my actual race times.

Also: quantum nerd, heavy music fan, sub-21' 5K chaser.`,

  `My journey from Java/Web dev to AI agent architect runs through 10+ years at **IBM** and hundreds of GitHub commits. Today I build production-grade autonomous systems with **BeeAI**, **CrewAI**, and **LangGraph**, containerize AI workloads with **Docker**, and push the boundaries of **Qiskit** experiments in the **IBM Quantum Guadalajara** community.

Life outside code: marathon-adjacent running (5K target: sub-21'), heavy music, and space obsession.`,
];

const about_tags = [
  "`AI Agents` &nbsp;·&nbsp; `Quantum / Qiskit` &nbsp;·&nbsp; `Multi-Cloud` &nbsp;·&nbsp; `Space` &nbsp;·&nbsp; `Sub-21' 5K` &nbsp;·&nbsp; `Heavy Music`",
  "`BeeAI · CrewAI · LangGraph` &nbsp;·&nbsp; `IBM Cloud` &nbsp;·&nbsp; `Qiskit` &nbsp;·&nbsp; `Running` &nbsp;·&nbsp; `Heavy Music`",
  "`Full Stack` &nbsp;·&nbsp; `Agentic AI` &nbsp;·&nbsp; `Quantum` &nbsp;·&nbsp; `Docker` &nbsp;·&nbsp; `Sub-21' 5K`",
  "`IBM CIO Org` &nbsp;·&nbsp; `AI Agents` &nbsp;·&nbsp; `Space Nerd` &nbsp;·&nbsp; `Runner` &nbsp;·&nbsp; `Heavy Music`",
  "`Certified IBM AI Expert` &nbsp;·&nbsp; `AWS Serverless` &nbsp;·&nbsp; `Qiskit` &nbsp;·&nbsp; `5K Runner` &nbsp;·&nbsp; `Open Source`",
  "`Cloud-Native` &nbsp;·&nbsp; `Agentic` &nbsp;·&nbsp; `Quantum` &nbsp;·&nbsp; `Strava Agent` &nbsp;·&nbsp; `Heavy Music`",
  "`Multi-Cloud` &nbsp;·&nbsp; `BeeAI` &nbsp;·&nbsp; `Qiskit` &nbsp;·&nbsp; `Sub-21' 5K` &nbsp;·&nbsp; `Zapopan MX`",
];

const section_headers = [
  ["About", "Stack", "Projects", "Writing", "GitHub Activity", "Now Playing"],
  ["Who I Am", "Tech Stack", "Open Source", "On Medium", "Stats", "Listening To"],
  ["Bio", "Tools & Tech", "Things I've Built", "Articles", "Activity", "Now Playing"],
  ["Profile", "My Stack", "OSS Projects", "Blog Posts", "GitHub Stats", "On Spotify"],
  ["The Person", "Technologies", "Built & Shipped", "Writing", "Contributions", "Music"],
  ["About Me", "Stack", "Projects", "Reads", "GitHub", "Currently Playing"],
  ["Edgar Bruney", "Tech I Use", "Side Projects", "Medium Posts", "Stats & Streaks", "Playlist"],
];

// ── Layout variants ───────────────────────────────────────────────────────────

function buildLayout(s) {
  const h = section_headers[s];
  const tagline = taglines[s];
  const intro = about_intros[s];
  const body = about_bodies[s];
  const tags = about_tags[s];

const layouts = [
    // 0 — Original structure, snake on right of about
    () => `<img src="./.github/assets/readme-aura-component-0-868374c9.svg" alt="Edgar Bruney — ${tagline}" width="100%" />

<div align="center">

${BADGES}

---

### ${h[5]}

${SPOTIFY}

</div>

---

### ${h[0]}

${SNAKE}

${intro}

${body}

${tags}

<sub>ℹ️ This bio was compiled from publicly available information across the internet and written with the help of AI.</sub>

<br clear="right" />

---

### Professional Journey

${PROFESSIONAL_JOURNEY}

### Technical Expertise

${TECHNICAL_EXPERTISE}

---

### ${h[1]}

<div>

${STACK}

</div>

---

### ${h[2]}

${PROJECTS}

---

### ${h[3]}

${WRITING_TABLE}

---

### 🏆 Strava Personal Records

${STRAVA_PRS}

${STRAVA_WIDGET}

---

<div align="center">

### ${h[4]}

${STATS_WIDGETS}

</div>

---

<div align="center">

${FOOTER_LINKS}

</div>`,

    // 1 — Stack first, then about with snake below
    () => `<img src="./.github/assets/readme-aura-component-0-868374c9.svg" alt="Edgar Bruney — ${tagline}" width="100%" />

<div align="center">

${BADGES}

---

### ${h[5]}

${SPOTIFY}

</div>

---

### ${h[1]}

<div>

${STACK}

</div>

---

### ${h[0]}

${intro}

${body}

${tags}

<sub>ℹ️ This bio was compiled from publicly available information across the internet and written with the help of AI.</sub>

---

<div align="center">

${SNAKE.replace('align="right" width="48%"', 'width="70%"')}

<br clear="right" />

</div>

---

### Professional Journey

${PROFESSIONAL_JOURNEY}

### Technical Expertise

${TECHNICAL_EXPERTISE}

---

### ${h[2]}

${PROJECTS}

---

### ${h[3]}

${WRITING_TABLE}

---

### 🏆 Strava Personal Records

${STRAVA_PRS}

${STRAVA_WIDGET}

---

<div align="center">

### ${h[4]}

${STATS_WIDGETS}

</div>

---

<div align="center">

${FOOTER_LINKS}

</div>`,

    // 2 — Writing first, stats prominent
    () => `<img src="./.github/assets/readme-aura-component-0-868374c9.svg" alt="Edgar Bruney — ${tagline}" width="100%" />

<div align="center">

${BADGES}

---

### ${h[5]}

${SPOTIFY}

</div>

---

### ${h[0]}

${SNAKE}

${intro}

${body}

${tags}

<sub>ℹ️ This bio was compiled from publicly available information across the internet and written with the help of AI.</sub>

<br clear="right" />

---

### Professional Journey

${PROFESSIONAL_JOURNEY}

### Technical Expertise

${TECHNICAL_EXPERTISE}

---

### ${h[3]}

${WRITING_TABLE}

---

### ${h[2]}

${PROJECTS}

---

### ${h[1]}

<div>

${STACK}

</div>

---

### 🏆 Strava Personal Records

${STRAVA_PRS}

${STRAVA_WIDGET}

---

<div align="center">

### ${h[4]}

${STATS_WIDGETS}

</div>

---

<div align="center">

${FOOTER_LINKS}

</div>`,

    // 3 — Compact about, projects center-stage
    () => `<img src="./.github/assets/readme-aura-component-0-868374c9.svg" alt="Edgar Bruney — ${tagline}" width="100%" />

<div align="center">

${BADGES}

---

### ${h[5]}

${SPOTIFY}

</div>

---

<table><tr><td width="52%">

### ${h[0]}

${intro}

${body}

${tags}

<sub>ℹ️ This bio was compiled from publicly available information across the internet and written with the help of AI.</sub>

</td><td>

### ${h[4]}

${STATS_WIDGETS.split("\n")[0]}

${STATS_WIDGETS.split("\n")[1]}

</td></tr></table>

---

### Professional Journey

${PROFESSIONAL_JOURNEY}

### Technical Expertise

${TECHNICAL_EXPERTISE}

---

### ${h[2]}

${PROJECTS}

---

### ${h[1]}

<div>

${STACK}

</div>

---

### ${h[3]}

${WRITING_TABLE}

---

### 🏆 Strava Personal Records

${STRAVA_PRS}

${STRAVA_WIDGET}

---

<div align="center">

${FOOTER_LINKS}

</div>`,

    // 4 — Stats top, then about
    () => `<img src="./.github/assets/readme-aura-component-0-868374c9.svg" alt="Edgar Bruney — ${tagline}" width="100%" />

<div align="center">

${BADGES}

---

${STATS_WIDGETS}

---

### ${h[5]}

${SPOTIFY}

</div>

---

### ${h[0]}

${SNAKE}

${intro}

${body}

${tags}

<sub>ℹ️ This bio was compiled from publicly available information across the internet and written with the help of AI.</sub>

<br clear="right" />

---

### Professional Journey

${PROFESSIONAL_JOURNEY}

### Technical Expertise

${TECHNICAL_EXPERTISE}

---

### ${h[1]}

<div>

${STACK}

</div>

---

### ${h[2]}

${PROJECTS}

---

### ${h[3]}

${WRITING_TABLE}

---

### 🏆 Strava Personal Records

${STRAVA_PRS}

${STRAVA_WIDGET}

---

<div align="center">

${FOOTER_LINKS}

</div>`,

    // 5 — Spotify / music angle up top
    () => `<img src="./.github/assets/readme-aura-component-0-868374c9.svg" alt="Edgar Bruney — ${tagline}" width="100%" />

<div align="center">

${BADGES}

---

### ${h[5]}

${SPOTIFY}

</div>

---

### ${h[0]}

${SNAKE}

${intro}

${body}

${tags}

<sub>ℹ️ This bio was compiled from publicly available information across the internet and written with the help of AI.</sub>

<br clear="right" />

---

### Professional Journey

${PROFESSIONAL_JOURNEY}

### Technical Expertise

${TECHNICAL_EXPERTISE}

---

### ${h[1]}

<div>

${STACK}

</div>

---

### ${h[2]}

${PROJECTS}

---

### ${h[3]}

${WRITING_TABLE}

---

### 🏆 Strava Personal Records

${STRAVA_PRS}

${STRAVA_WIDGET}

---

<div align="center">

### ${h[4]}

${STATS_WIDGETS}

</div>

---

<div align="center">

${FOOTER_LINKS}

</div>`,

    // 6 — Minimal / clean, everything prose-first
    () => `<img src="./.github/assets/readme-aura-component-0-868374c9.svg" alt="Edgar Bruney — ${tagline}" width="100%" />

<div align="center">

${BADGES}

---

#### ${h[5]}

${SPOTIFY}

</div>

---

${intro}

${SNAKE}

${body}

${tags}

<sub>ℹ️ This bio was compiled from publicly available information across the internet and written with the help of AI.</sub>

<br clear="right" />

---

### Professional Journey

${PROFESSIONAL_JOURNEY}

### Technical Expertise

${TECHNICAL_EXPERTISE}

---

#### ${h[1]}

<div>

${STACK}

</div>

---

#### ${h[2]}

${PROJECTS}

---

#### ${h[3]}

${WRITING_TABLE}

---

### 🏆 Strava Personal Records

${STRAVA_PRS}

${STRAVA_WIDGET}

---

<div align="center">

#### ${h[4]}

${STATS_WIDGETS}

---

${FOOTER_LINKS}

</div>`,
  ];

  return layouts[s]();
}

// ── Footer timestamp ──────────────────────────────────────────────────────────

function addTimestamp(content) {
  return (
    content +
    `

---

<div align="center">
<sub>

🤖 **Auto-updated by AI** on **${DATE_LABEL}** at **${TIMESTAMP}**
All information gathered from publicly available sources across the internet.
Content rotates daily — layout variant ${seed + 1}/7.

</sub>
</div>`
  );
}

// ── Main ──────────────────────────────────────────────────────────────────────

const readmePath = path.join(__dirname, "..", "README.md");
const newContent = addTimestamp(buildLayout(seed));
fs.writeFileSync(readmePath, newContent, "utf8");
console.log(`README updated — layout ${seed + 1}/7 (day ${dayOfYear}) — ${TIMESTAMP}`);
