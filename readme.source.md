```aura width=1200 height=280
<div style={{
  width: '100%', height: '100%', background: 'linear-gradient(135deg, #0a0a0f 0%, #1a1a2e 100%)',
  display: 'flex', alignItems: 'center', fontFamily: 'Inter',
  position: 'relative', overflow: 'hidden', borderRadius: 16,
  border: '1px solid rgba(110,80,220,0.18)'
}}>

  <style>{`
      @keyframes float-slow {
        0%, 100% { transform: translateY(0px); opacity: 0.8; }
        50% { transform: translateY(-20px); opacity: 1.2; }
      }
      @keyframes float-medium {
        0%, 100% { transform: translateX(0px); opacity: 0.7; }
        50% { transform: translateX(-30px); opacity: 1.1; }
      }
      @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 0.6; }
        50% { transform: scale(1.2); opacity: 0.9; }
      }
      #glow-1 { animation: float-slow 8s ease-in-out infinite; }
      #glow-2 { animation: float-medium 12s ease-in-out infinite; }
      #glow-3 { animation: pulse 6s ease-in-out infinite; }
    `}</style>

  <svg width="1200" height="280" style={{ position: 'absolute', top: 0, left: 0 }}>
    <defs>
      <radialGradient id="g1" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(110,20,210,0.5)" />
        <stop offset="70%" stopColor="rgba(90,15,180,0)" />
      </radialGradient>
      <radialGradient id="g2" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(40,60,255,0.4)" />
        <stop offset="70%" stopColor="rgba(30,50,200,0)" />
      </radialGradient>
      <radialGradient id="g3" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(0,190,230,0.3)" />
        <stop offset="70%" stopColor="rgba(0,190,230,0)" />
      </radialGradient>
    </defs>

    <ellipse id="glow-1" cx="200" cy="140" rx="300" ry="200" fill="url(#g1)" />
    <ellipse id="glow-2" cx="600" cy="140" rx="250" ry="180" fill="url(#g2)" />
    <ellipse id="glow-3" cx="1000" cy="140" rx="200" ry="150" fill="url(#g3)" />
  </svg>

  <div style={{ display:'flex', flexDirection:'column', marginLeft:60, gap:12, zIndex: 10, width: '100%' }}>
    <div style={{ display:'flex', fontSize:56, fontWeight:900, color:'#ffffff', letterSpacing:'-2px', lineHeight:1 }}>
      Edgar Bruney
    </div>
    <div style={{ display:'flex', fontSize:22, color:'rgba(180,165,255,0.9)', fontWeight:500, letterSpacing:'0.5px' }}>
      Agentic AI Engineer · Cloud Architect · Quantum Explorer
    </div>

  </div>
</div>
```


---

> ⚠️ **AI-Generated Disclaimer:** All information in this README was researched and written by an AI agent. It is automatically updated every day to keep data current. Content may not reflect real-time changes made outside of scheduled update cycles.

---

```aura width=1200 height=200
<div style={{
  width: '100%', height: '100%', background: 'linear-gradient(135deg, #0a0a0f 0%, #1a1a2e 100%)',
  display: 'flex', flexDirection: 'column', justifyContent: 'center', fontFamily: 'Inter',
  position: 'relative', overflow: 'hidden', borderRadius: 16,
  border: '1px solid rgba(110,80,220,0.18)', padding: '40px 60px'
}}>

  <style>{`
      @keyframes float-slow {
        0%, 100% { transform: translateY(0px); opacity: 0.8; }
        50% { transform: translateY(-20px); opacity: 1.2; }
      }
      #tech-glow { animation: float-slow 8s ease-in-out infinite; }
    `}</style>

  <svg width="1200" height="200" style={{ position: 'absolute', top: 0, left: 0 }}>
    <defs>
      <radialGradient id="tg1" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(110,20,210,0.4)" />
        <stop offset="70%" stopColor="rgba(90,15,180,0)" />
      </radialGradient>
    </defs>
    <ellipse id="tech-glow" cx="600" cy="100" rx="400" ry="150" fill="url(#tg1)" />
  </svg>

  <div style={{ display:'flex', flexDirection:'column', gap: 20, zIndex: 10 }}>
    
    <div style={{ display:'flex', flexDirection:'column', gap: 8 }}>
      <div style={{ fontSize: 18, fontWeight: 700, color: 'rgba(180,165,255,0.95)', letterSpacing: '1px' }}>
        CORE
      </div>
      <div style={{ fontSize: 16, color: 'rgba(255,255,255,0.85)', fontWeight: 400, letterSpacing: '0.3px' }}>
        Java · TypeScript · Python · Node.js · React
      </div>
    </div>

    <div style={{ display:'flex', flexDirection:'column', gap: 8 }}>
      <div style={{ fontSize: 18, fontWeight: 700, color: 'rgba(180,165,255,0.95)', letterSpacing: '1px' }}>
        CLOUD
      </div>
      <div style={{ fontSize: 16, color: 'rgba(255,255,255,0.85)', fontWeight: 400, letterSpacing: '0.3px' }}>
        IBM Cloud · AWS · GCP · Docker · Linux
      </div>
    </div>

    <div style={{ display:'flex', flexDirection:'column', gap: 8 }}>
      <div style={{ fontSize: 18, fontWeight: 700, color: 'rgba(180,165,255,0.95)', letterSpacing: '1px' }}>
        AI LAB
      </div>
      <div style={{ fontSize: 16, color: 'rgba(255,255,255,0.85)', fontWeight: 400, letterSpacing: '0.3px' }}>
        IBM Watson · IBM Bob · BeeAI · Gemini · Claude
      </div>
    </div>

  </div>
</div>
```

---

### Professional Journey

**Edgar Bruney Castañeda** is an experienced engineer at **IBM's CIO Organization** in **Zapopan, Jalisco, Mexico**, specializing in translating research-grade AI into production systems. A GitHub member since **2013** with over 13 years of experience in the tech industry, he has built a distinguished career focused on cutting-edge technology implementation and open-source contribution.

Currently working at the intersection of **agentic AI development** and **cloud architecture**, Edgar designs and implements multi-agent pipelines using frameworks like **BeeAI**, **CrewAI**, and **LangGraph**. His work spans from concept to deployed REST APIs with async jobs and live SSE streaming, with emphasis on practical applications that solve real-world problems. He specializes in verify-and-retry orchestration loops and production-ready AI systems that bridge the gap between research and enterprise deployment, demonstrating a unique ability to transform research-grade AI into practical enterprise solutions.

His most recent open-source work centers on the **Quantum Lab Agent System**: a five-agent A2A network — Developer, Status, Computing, and Experiment specialists — all orchestrated by a central Lab Agent and powered by **IBM Granite 4.2 8B** running locally via Ollama. The system features an Agent Stack Canvas integration for circuit visualization, live backend topology dashboards, and end-to-end QAOA Max-Cut experiments on real IBM Quantum hardware including `ibm_marrakesh`. Edgar is also a core organizer of **Quantum Guild GDL** (established August 17, 2026), a Guadalajara-based community co-organizing the **[Qiskit Fall Fest Guadalajara 2026](https://quantum-guild-gdl.github.io/qiskit_fall_fest_gdl/)** — a free, three-day community quantum computing festival (October 28–30, 2026, Mexico City time/CST) with Day 1 (October 28) held **in person at AstraZeneca GITC Guadalajara** (Blvd. Puerta de Hierro 4965, Zapopan) and October 29–30 streamed online. On **September 24, 2026**, Edgar integrated the **IBM SkillsBuild Quantum learning plan with earnable credentials** into the festival platform and updated registration dates and countdown schedules for the upcoming October opening.

Edgar's open-source contributions span major generative programming and agent orchestration frameworks. On **September 24, 2026**, he submitted **[PR #1676](https://github.com/generative-computing/mellea/pull/1676)** to **[generative-computing/mellea](https://github.com/generative-computing/mellea)** (1,818⭐, 161 forks) — the library for writing generative programs — implementing dynamic OpenAI adapter deregistration (`OpenAIBackend.remove_adapter()`) to cleanly release cached adapter compositions and reclaim namespace identifiers. On the same day, he expanded his agent infrastructure tooling by exploring **[strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk)** (8,419⭐, 1,256 forks) for end-to-end multi-cloud agent harness management. This follows his landmark upstream contribution on **September 22, 2026**, where his **[PR #3930](https://github.com/heygen-com/hyperframes/pull/3930)** to **[heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)** (53,088⭐, 4,844 forks) was **merged** into core, making IBM Bob Shell a first-class supported coding-agent runtime.

In addition, Edgar published **[TriForge](https://github.com/BrUn3y/triforge)** on **September 23, 2026** — a reusable project template transforming Codex, Claude Code, and IBM Bob Shell into an *auditable engineering council* where all three agents review independently in parallel before shipping code. The project includes a Python `agent_loop` coordinator, comprehensive test suite, real-time handoff logs, and an [interactive Archify architecture diagram](https://brun3y.github.io/triforge/) on GitHub Pages.

### Technical Expertise

Edgar holds multiple industry certifications:
- **IBM Generative & Agentic AI Expert Developer**
- **AWS Serverless Badge Holder**
- **Hybrid Cloud Microservices Architect**

His comprehensive technical stack includes:
- **AI/ML Frameworks:** BeeAI, CrewAI, LangGraph, Mellea (generative programming), AgentStack SDK, Harness SDK, A2A protocol, IBM Granite 4.2 8B (Ollama)
- **Cloud Platforms:** IBM Cloud, AWS, multi-cloud architecture design and implementation
- **Quantum Computing:** Qiskit, QASM 2.0/3.0, QAOA, VQE, Grover, Shor, Deutsch-Jozsa, QFT algorithms; real-hardware execution on IBM Quantum; active contributor to IBM's Qiskit Runtime (237⭐, 220 forks) and qiskit-addon-sqd (Sample-based Quantum Diagonalization, 100⭐, 43 forks); Agent Stack Canvas for circuit and topology visualization; hybrid quantum-classical multi-agent systems; Microsoft QDK (Q#, resource estimator, Quantum Katas)
- **Integration Technologies:** REST API design, Docker containerization, Slack integration (Socket Mode), Strava API, Google Fit API, Huawei Health API
- **Specializations:** Multi-agent pipeline design with A2A protocol, verify-and-retry orchestration loops, async jobs with live SSE streaming, enterprise AI deployment, generative programming and backend adapter management (Mellea), HTML-to-video rendering for agents (hyperframes / HeyGen), Kubernetes agent sandboxing (DAM platform), multi-agent peer-review orchestration (TriForge), interactive architecture diagram generation (Archify)

### Featured Projects

**[TriForge](https://github.com/BrUn3y/triforge)** — A reusable GitHub template published on September 23, 2026 that orchestrates Codex, Claude Code, and IBM Bob Shell as an *auditable engineering council*. All three agents consult in parallel, one implements, and the other two review independently — nothing ships without unanimous approval. The project ships with a Python `agent_loop` coordinator, animated communication demo, full test suite, and an [interactive Archify architecture diagram](https://brun3y.github.io/triforge/) on GitHub Pages. Every handoff is persisted in `live.log` and `transcript.jsonl` for complete auditability. Built with Python, `.bob/`, `.claude/`, and `.codex/` configuration layers side-by-side.

**[IBM Bob Shell Harness](https://github.com/BrUn3y/IBM_Bob_Harness)** (23⭐, 5 forks) — A Dockerized harness running IBM's Bob Shell headless in unrestricted mode, exposed via REST API with async jobs and live SSE streaming. Features Slack integration for autonomous AI operations with verify-and-retry orchestration loops. Released **v1.0.2** on August 27, 2026 with full Bob v2.x CLI support (`run` subcommand and `--mode` flag), followed by a September 7, 2026 update adding file-support improvements. The harness itself was actively used to merge pull requests and commit changes to the Qiskit Fall Fest Guadalajara site, demonstrating its real-world autonomous capabilities in production.

**[Mellea Contributions](https://github.com/generative-computing/mellea)** (1,818⭐, 161 forks) — On September 24, 2026, Edgar submitted **[PR #1676](https://github.com/generative-computing/mellea/pull/1676)** (*"fix: add OpenAI adapter deregistration"*) to `generative-computing/mellea`, introducing `OpenAIBackend.remove_adapter()` to enable dynamic adapter deregistration, cache invalidation, and qualified name recycling under concurrency locks.

**[hyperframes](https://github.com/BrUn3y/hyperframes)** — Edgar's fork of the viral **[HeyGen hyperframes](https://github.com/heygen-com/hyperframes)** project (53,088⭐, 4,844 forks), a framework for writing HTML and rendering it as video — purpose-built for AI agents. On September 14, 2026, Edgar submitted **[PR #3930](https://github.com/heygen-com/hyperframes/pull/3930)** upstream to add IBM Bob runtime support to the HyperFrames CLI. The PR was approved and **merged on September 22, 2026** by maintainer `jrusso1020`, permanently integrating IBM Bob Shell into HyperFrames as a first-class supported coding-agent runtime.

**[Quantum Lab Agent System](https://github.com/BrUn3y/quantum_lab_agent)** — A complete five-agent multi-agent workspace for IBM Quantum, built entirely with the A2A protocol and IBM Granite 4.2 8B. The orchestrator (`quantum_lab_agent`, port 8000) coordinates four specialist agents: a [Quantum Developer Agent](https://github.com/BrUn3y/quantum-developer-agent) for code generation (Grover, Shor, Deutsch-Jozsa, QFT…), a [Quantum Status Agent](https://github.com/BrUn3y/quantum-status-agent) for real-time backend monitoring and chip topology Canvas visualization, a [Quantum Computing Agent](https://github.com/BrUn3y/quantum-computing-agent) for circuit execution on simulators and real IBM Quantum hardware, and the [Quantum Experiment Agent](https://github.com/BrUn3y/quantum-experiment-agent) for hybrid QAOA/VQE experiments (QAOA Max-Cut for 2–8 node graphs on `ibm_marrakesh`).

**[Strava Agent](https://github.com/BrUn3y/Strava_Agent)** (5⭐, 1 fork) — An advanced conversational AI system built with BeeAI framework and AgentStack SDK that analyzes athletic performance directly from the Strava API. Features full A2A protocol support, AgentStack Server RESTful endpoints, and five organized agent skills for multi-agent integration. Complemented by [strava-analytics](https://github.com/BrUn3y/strava-analytics), a Python toolkit for analyzing running performance, CrossFit sessions, and calorie tracking.

**X Trends Agent** — A trend-analysis agent implemented across three different frameworks ([BeeAI](https://github.com/BrUn3y/x_trends_agent_BeeAI), [CrewAI](https://github.com/BrUn3y/x_trends_agent_CrewAI), [LangGraph](https://github.com/BrUn3y/x_trends_agent_LangGraph)), demonstrating framework-agnostic agent engineering capabilities and deep understanding of different AI architectures.

**Qiskit & Quantum Ecosystem** — Active contributor to Qiskit/qiskit-ibm-runtime (237⭐, 220 forks) and **qiskit-addon-sqd** (Sample-based Quantum Diagonalization, 100⭐, 43 forks), alongside exploration of the **[Microsoft QDK](https://github.com/microsoft/qdk)** (1,013⭐, 214 forks) — spanning Q#, the quantum resource estimator, and Quantum Katas.

### Beyond Code

Edgar is actively engaged in the tech community with significant leadership and educational initiatives:
- **Contributing to Generative AI Frameworks** — on **September 24, 2026**, Edgar contributed **[PR #1676](https://github.com/generative-computing/mellea/pull/1676)** to **[Mellea](https://github.com/generative-computing/mellea)** (1,818⭐, 161 forks), delivering OpenAI adapter deregistration for cleaner runtime lifecycle management in generative computing pipelines.
- **Co-organizing Quantum Guild GDL** — founded August 17, 2026, the guild is driving the **[Qiskit Fall Fest Guadalajara 2026](https://quantum-guild-gdl.github.io/qiskit_fall_fest_gdl/)**: a free, community-run quantum computing festival held **October 28–30, 2026** (Mexico City time/CST). Day 1 (October 28) takes place **in person at AstraZeneca GITC Guadalajara** (Blvd. Puerta de Hierro 4965, Zapopan, Jalisco); Days 2–3 (October 29–30) are streamed online. On **September 24, 2026**, Edgar added the **IBM SkillsBuild Quantum learning plan** with official digital badges to the festival portal and updated the registration schedule. Confirmed speakers include **Claudia Zendejas Morales** (Physicist, Grad Student @KU, Coordinator @QWorld, Qiskit Advocate), **Eva Nayeli Hernández Pulido** (IBM GreenStar DevOps & App Support, Quantum enthusiast), **Jesús Rolón** (Software Development Engineer at IBM), and **Yra Cano** (Senior Software Developer at IBM). Organizers alongside Edgar are Andrés Alejandre, Barbara Baena, Eva Nayeli Hernández Pulido, Juan Miguel Ávila Sánchez, Kassandra Delfín, and Tanya Franco.
- **Published TriForge** — on **September 23, 2026**, Edgar launched **[TriForge](https://github.com/BrUn3y/triforge)**, a first-of-its-kind open-source template that runs Codex, Claude Code, and IBM Bob Shell as an auditable, equal-peer engineering council with an [interactive architecture diagram](https://brun3y.github.io/triforge/) powered by **[Archify](https://github.com/tt-a1i/archify)** on GitHub Pages.
- **Merged into HyperFrames** — **[PR #3930](https://github.com/heygen-com/hyperframes/pull/3930)** to `heygen-com/hyperframes` (53,088⭐, 4,844 forks) was **merged on September 22, 2026**, permanently adding IBM Bob Shell as a supported coding-agent runtime in one of the most-starred open-source agent frameworks on GitHub.
- **Agent Infrastructure & Sandboxing** — active exploration of Kubernetes-native agent execution via **[dam-agents/dam](https://github.com/dam-agents/dam)** (branch `fix/cli-connect-required-presets`) and multi-cloud agent harnesses with **[strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk)** (8,419⭐, 1,256 forks).
- **Exploring the Microsoft QDK** — engaging with the **[Microsoft Quantum Development Kit](https://github.com/microsoft/qdk)** (1,013⭐, 214 forks), expanding quantum computing work to Q# and Microsoft's resource estimation tooling.
- **Writing on [Medium](https://medium.com/@brun3y)** about AI agents, athletic performance data, and cloud tooling, sharing practical insights from real-world implementations.
- **Open-source contributions** across 59 public repositories on GitHub, demonstrating continuous participation in the developer community and collaborative open-source engineering.
- **Community building** on GitHub with 17 followers and 27 following, maintaining connections across the global tech ecosystem and fostering knowledge exchange.

When stepping away from the screen, Edgar pursues his passion for **running** (actively training for a sub-21 minute 5K, tracking and analyzing every session with Python and AI tools) and enjoys **heavy music**. His application of AI technology to personal fitness optimization reflects his commitment to applying technology to personal growth.

`BeeAI · CrewAI · LangGraph` &nbsp;·&nbsp; `IBM Cloud` &nbsp;·&nbsp; `Qiskit` &nbsp;·&nbsp; `Running` &nbsp;·&nbsp; `Heavy Music`

---

<div align="center">

<img src="https://raw.githubusercontent.com/BrUn3y/Brun3y/output/github-snake-dark.svg" alt="contribution snake" width="70%" />

<br clear="right" />

</div>

---

### Open Source

- **[IBM Bob Shell Harness](https://github.com/BrUn3y/IBM_Bob_Harness)** (23⭐, 5 forks) — Dockerized harness that runs IBM's Bob Shell headless in unrestricted mode and exposes it over a REST API with Slack integration for autonomous AI operations.
- **[Strava Agent](https://github.com/BrUn3y/Strava_Agent)** (5⭐) — Advanced conversational AI system built with BeeAI framework and AgentStack SDK that analyzes athletic performance directly from the Strava API.
- **X Trends Agent** — Same trend-analysis agent, three frameworks: [BeeAI](https://github.com/BrUn3y/x_trends_agent_BeeAI) · [CrewAI](https://github.com/BrUn3y/x_trends_agent_CrewAI) · [LangGraph](https://github.com/BrUn3y/x_trends_agent_LangGraph).
- **[Quantum Lab Agent](https://github.com/BrUn3y/quantum_lab_agent)** / **[Quantum Experiment Agent](https://github.com/BrUn3y/quantum-experiment-agent)** — Quantum computing agents exploring AI and quantum circuits, including a hybrid agent powered by IBM Granite and AgentStack.
- **[hyperframes](https://github.com/BrUn3y/hyperframes)** — HTML-to-video renderer built for AI agents.
- **[strava-analytics](https://github.com/BrUn3y/strava-analytics)** — Python scripts to analyze running performance, CrossFit sessions, and calorie tracking from Strava.
- **Qiskit Contributions** — Active contributor to Qiskit/qiskit-ibm-runtime (237⭐, 220 forks) and documentation translation, supporting the quantum computing community.

---

### On Medium

I write on [Medium](https://medium.com/@brun3y) about AI agents, athletic performance data, and cloud tooling.

<table>
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
</table>

---



---

### 🎧 Now Playing on Spotify

<div align="center">

[![spotify-github-profile](https://spotify-github-profile.kittinanx.com/api/view?uid=brun3y&cover_image=true&theme=default&show_offline=false&background_color=121212&interchange=false&profanity=false&hide_remaster=false)](https://github.com/kittinan/spotify-github-profile)

</div>

---

### 🏆 Strava Personal Records

<div align="center">

<img src="./assets/strava-pr-5k.svg" alt="5K Personal Records" width="32%" />
<img src="./assets/strava-pr-10k.svg" alt="10K Personal Records" width="32%" />
<img src="./assets/strava-pr-21k.svg" alt="21K Personal Records" width="32%" />

</div>

<img src="./assets/strava-widget.svg" alt="Recent Strava Activities" width="100%" />

---

<div align="center">
<sub>ℹ️ Profile information collected and updated by AI assistant on September 26, 2026</sub>
</div>
