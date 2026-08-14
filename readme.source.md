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
    <div style={{ display:'flex', gap:12, marginTop:8, flexWrap: 'wrap' }}>
      {[
        'BeeAI', 'CrewAI', 'LangGraph', 'IBM Cloud', 'Qiskit', 'Docker'
      ].map(function(tag, i) {
        return (
          <div key={tag + '-' + i} style={{
            display:'flex', padding:'6px 16px', borderRadius:20,
            background:'rgba(80,40,220,0.2)', border:'1px solid rgba(100,70,240,0.4)',
            color:'rgba(205,195,255,0.95)', fontSize:14, fontWeight:700,
          }}>{tag}</div>
        );
      })}
    </div>
  </div>
</div>
```

---

```aura width=900 height=120
<div style={{ position: 'relative', display: 'flex', gap: 18, alignItems: 'center', justifyContent: 'center', width: '100%', height: '100%', background: 'linear-gradient(135deg, #0a0a0f 0%, #12121a 100%)', borderRadius: 24, overflow: 'hidden', fontFamily: 'Inter, sans-serif', border: '1.5px solid rgba(255,255,255,0.1)', padding: '0 20px' }}>
  <style>{`
    @keyframes orb-float-1 { 0%, 100% { transform: translate(0,0) scale(1); opacity: 0.65; } 50% { transform: translate(30px,-22px) scale(1.2); opacity: 1; } }
    @keyframes orb-float-2 { 0%, 100% { transform: translate(0,0) scale(1); opacity: 0.6; } 50% { transform: translate(-28px,18px) scale(1.18); opacity: 0.95; } }
    @keyframes orb-float-3 { 0%, 100% { transform: translate(0,0) scale(1); opacity: 0.55; } 50% { transform: translate(25px,-15px) scale(1.15); opacity: 0.9; } }
    @keyframes orb-float-4 { 0%, 100% { transform: translate(0,0) scale(1); opacity: 0.5; } 50% { transform: translate(-22px,12px) scale(1.12); opacity: 0.85; } }
    @keyframes ring-pulse-1 { 0%, 100% { opacity: 0.15; transform: scale(1) rotate(0deg); } 50% { opacity: 0.35; transform: scale(1.08) rotate(180deg); } }
    @keyframes ring-pulse-2 { 0%, 100% { opacity: 0.12; transform: scale(1) rotate(0deg); } 50% { opacity: 0.28; transform: scale(1.06) rotate(-180deg); } }
    @keyframes ring-pulse-3 { 0%, 100% { opacity: 0.08; transform: scale(1); } 50% { opacity: 0.2; transform: scale(1.04); } }
    @keyframes btn-glow { 0%, 100% { box-shadow: 0 0 18px rgba(255,255,255,0.06), inset 0 0 12px rgba(255,255,255,0.03); transform: translateY(0px); } 50% { box-shadow: 0 0 32px rgba(255,255,255,0.18), inset 0 0 20px rgba(255,255,255,0.08); transform: translateY(-2px); } }
    @keyframes icon-bounce { 0%, 100% { transform: scale(1) rotate(0deg); } 50% { transform: scale(1.15) rotate(5deg); } }
    #so1 { animation: orb-float-1 11s ease-in-out infinite; }
    #so2 { animation: orb-float-2 13s ease-in-out infinite 1.8s; }
    #so3 { animation: orb-float-3 12s ease-in-out infinite 3.5s; }
    #so4 { animation: orb-float-4 14s ease-in-out infinite 1s; }
    #ring1 { animation: ring-pulse-1 10s ease-in-out infinite; }
    #ring2 { animation: ring-pulse-2 10s ease-in-out infinite 2.5s; }
    #ring3 { animation: ring-pulse-3 10s ease-in-out infinite 5s; }
    #ring4 { animation: ring-pulse-3 10s ease-in-out infinite 7.5s; }
    .social-btn { animation: btn-glow 6s ease-in-out infinite; transition: all 0.3s ease; }
    .social-btn:hover { transform: translateY(-4px) scale(1.05); }
    .social-icon { animation: icon-bounce 4s ease-in-out infinite; }
  `}</style>
  
  <svg width="900" height="120" style={{ position: 'absolute', top: 0, left: 0 }}>
    <defs>
      <radialGradient id="sog1" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(108,195,130,0.75)" />
        <stop offset="50%" stopColor="rgba(108,195,130,0.3)" />
        <stop offset="100%" stopColor="rgba(108,195,130,0)" />
      </radialGradient>
      <radialGradient id="sog2" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(230,100,115,0.7)" />
        <stop offset="50%" stopColor="rgba(230,100,115,0.28)" />
        <stop offset="100%" stopColor="rgba(230,100,115,0)" />
      </radialGradient>
      <radialGradient id="sog3" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(80,160,220,0.65)" />
        <stop offset="50%" stopColor="rgba(80,160,220,0.25)" />
        <stop offset="100%" stopColor="rgba(80,160,220,0)" />
      </radialGradient>
      <radialGradient id="sog4" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(195,155,255,0.6)" />
        <stop offset="50%" stopColor="rgba(195,155,255,0.22)" />
        <stop offset="100%" stopColor="rgba(195,155,255,0)" />
      </radialGradient>
      <filter id="glow-filter">
        <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
        <feMerge>
          <feMergeNode in="coloredBlur"/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>
    </defs>
    <ellipse id="so1" cx="140" cy="60" rx="180" ry="130" fill="url(#sog1)" filter="url(#glow-filter)" />
    <ellipse id="so2" cx="360" cy="60" rx="170" ry="125" fill="url(#sog2)" filter="url(#glow-filter)" />
    <ellipse id="so3" cx="580" cy="60" rx="160" ry="120" fill="url(#sog3)" filter="url(#glow-filter)" />
    <ellipse id="so4" cx="800" cy="60" rx="150" ry="115" fill="url(#sog4)" filter="url(#glow-filter)" />
    <circle id="ring1" cx="450" cy="60" r="65" fill="none" stroke="rgba(255,255,255,0.18)" strokeWidth="1.5" />
    <circle id="ring2" cx="450" cy="60" r="100" fill="none" stroke="rgba(255,255,255,0.15)" strokeWidth="1.2" />
    <circle id="ring3" cx="450" cy="60" r="140" fill="none" stroke="rgba(255,255,255,0.1)" strokeWidth="0.9" />
    <circle id="ring4" cx="450" cy="60" r="185" fill="none" stroke="rgba(255,255,255,0.06)" strokeWidth="0.6" />
  </svg>

  <a href="https://linkedin.com/in/bruney" style={{ textDecoration: 'none', zIndex: 10 }}>
    <div className="social-btn" style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '14px 28px', background: 'rgba(108,195,130,0.12)', border: '2px solid rgba(108,195,130,0.35)', borderRadius: 16, backdropFilter: 'blur(15px)', cursor: 'pointer' }}>
      <span className="social-icon" style={{ fontSize: 26 }}>💼</span>
      <span style={{ color: 'rgba(108,195,130,1)', fontSize: 16, fontWeight: 800, letterSpacing: '0.8px', textShadow: '0 0 10px rgba(108,195,130,0.4)' }}>LinkedIn</span>
    </div>
  </a>

  <a href="https://medium.com/@brun3y" style={{ textDecoration: 'none', zIndex: 10 }}>
    <div className="social-btn" style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '14px 28px', background: 'rgba(230,100,115,0.12)', border: '2px solid rgba(230,100,115,0.35)', borderRadius: 16, backdropFilter: 'blur(15px)', cursor: 'pointer' }}>
      <span className="social-icon" style={{ fontSize: 26 }}>📝</span>
      <span style={{ color: 'rgba(230,100,115,1)', fontSize: 16, fontWeight: 800, letterSpacing: '0.8px', textShadow: '0 0 10px rgba(230,100,115,0.4)' }}>Medium</span>
    </div>
  </a>

  <a href="https://x.com/BrUn3y" style={{ textDecoration: 'none', zIndex: 10 }}>
    <div className="social-btn" style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '14px 28px', background: 'rgba(80,160,220,0.12)', border: '2px solid rgba(80,160,220,0.35)', borderRadius: 16, backdropFilter: 'blur(15px)', cursor: 'pointer' }}>
      <span className="social-icon" style={{ fontSize: 26 }}>🐦</span>
      <span style={{ color: 'rgba(80,160,220,1)', fontSize: 16, fontWeight: 800, letterSpacing: '0.8px', textShadow: '0 0 10px rgba(80,160,220,0.4)' }}>X</span>
    </div>
  </a>

  <div className="social-btn" style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '14px 28px', background: 'rgba(195,155,255,0.12)', border: '2px solid rgba(195,155,255,0.35)', borderRadius: 16, backdropFilter: 'blur(15px)', zIndex: 10, cursor: 'pointer' }}>
    <span className="social-icon" style={{ fontSize: 26 }}>👁️</span>
    <span style={{ color: 'rgba(195,155,255,1)', fontSize: 16, fontWeight: 800, letterSpacing: '0.8px', textShadow: '0 0 10px rgba(195,155,255,0.4)' }}>Views</span>
  </div>
</div>
```

---

### Tech Stack

<div>

**Core** &nbsp; ![Java](https://img.shields.io/badge/-Java-000?style=flat&logo=openjdk&logoColor=white) ![TypeScript](https://img.shields.io/badge/-TypeScript-000?style=flat&logo=typescript&logoColor=white) ![Python](https://img.shields.io/badge/-Python-000?style=flat&logo=python&logoColor=white) ![Node.js](https://img.shields.io/badge/-Node.js-000?style=flat&logo=nodedotjs&logoColor=white) ![React](https://img.shields.io/badge/-React-000?style=flat&logo=react&logoColor=white)

**Cloud** &nbsp; ![IBM Cloud](https://img.shields.io/badge/-IBM_Cloud-000?style=flat&logo=ibmcloud&logoColor=white) ![AWS](https://img.shields.io/badge/-AWS-000?style=flat&logo=amazonwebservices&logoColor=white) ![GCP](https://img.shields.io/badge/-GCP-000?style=flat&logo=googlecloud&logoColor=white) ![Docker](https://img.shields.io/badge/-Docker-000?style=flat&logo=docker&logoColor=white) ![Linux](https://img.shields.io/badge/-Linux-000?style=flat&logo=linux&logoColor=white)

**AI Lab** &nbsp; ![Watson](https://img.shields.io/badge/-IBM_Watson-000?style=flat&logo=ibmwatson&logoColor=white) ![BeeAI](https://img.shields.io/badge/-BeeAI-000?style=flat) ![Gemini](https://img.shields.io/badge/-Gemini-000?style=flat&logo=googlegemini&logoColor=white) ![Claude](https://img.shields.io/badge/-Claude-000?style=flat&logo=anthropic&logoColor=white)

</div>

---

### Professional Journey

**Edgar Bruney** is an experienced engineer at **IBM's CIO Organization** in **Zapopan, Jalisco, Mexico**, specializing in translating research-grade AI into production systems. A GitHub member since **2013** with over 13 years of experience in the tech industry, he has built a distinguished career focused on cutting-edge technology implementation and open-source contribution.

Currently working at the intersection of **agentic AI development** and **cloud architecture**, Edgar designs and implements multi-agent pipelines using frameworks like **BeeAI**, **CrewAI**, and **LangGraph**. His work spans from concept to deployed REST APIs with async jobs and live SSE streaming, with emphasis on practical applications that solve real-world problems. He specializes in verify-and-retry orchestration loops and production-ready AI systems that bridge the gap between research and enterprise deployment, demonstrating a unique ability to transform research-grade AI into practical enterprise solutions.

### Technical Expertise

Edgar holds multiple industry certifications:
- **IBM Generative & Agentic AI Expert Developer**
- **AWS Serverless Badge Holder**
- **Hybrid Cloud Microservices Architect**

His comprehensive technical stack includes:
- **AI/ML Frameworks:** BeeAI, CrewAI, LangGraph, AgentStack SDK, A2A protocol
- **Cloud Platforms:** IBM Cloud, AWS, multi-cloud architecture design and implementation
- **Quantum Computing:** Qiskit experiments and community contributions, active contributor to IBM's Qiskit Runtime (235⭐, 218 forks)
- **Integration Technologies:** REST API design, Docker containerization, Slack integration (Socket Mode), Strava API, Google Fit API
- **Specializations:** Multi-agent pipeline design, verify-and-retry orchestration loops, async jobs with live SSE streaming, enterprise AI deployment

### Featured Projects

**[IBM Bob Shell Harness](https://github.com/BrUn3y/IBM_Bob_Harness)** (21⭐, 5 forks) — A Dockerized harness running IBM's Bob Shell headless in unrestricted mode, exposed via REST API with async jobs and live SSE streaming. Features Slack integration for autonomous AI operations with verify-and-retry orchestration loops. This project showcases expertise in containerization, API development, and production-grade AI deployment, representing a bridge between enterprise AI tools and practical automation.

**[Strava Agent](https://github.com/BrUn3y/Strava_Agent)** (5⭐, 1 fork) — An advanced conversational AI system built with BeeAI framework and AgentStack SDK that analyzes athletic performance directly from the Strava API. This personal project helped improve his 5K running time toward sub-21 minutes, demonstrating the practical application of AI in personal fitness optimization and data-driven athletic training.

**X Trends Agent** — A trend-analysis agent implemented across three different frameworks ([BeeAI](https://github.com/BrUn3y/x_trends_agent_BeeAI), [CrewAI](https://github.com/BrUn3y/x_trends_agent_CrewAI), [LangGraph](https://github.com/BrUn3y/x_trends_agent_LangGraph)), demonstrating framework-agnostic agent engineering capabilities and deep understanding of different AI architectures. This multi-framework approach showcases adaptability and comprehensive knowledge of the agentic AI ecosystem.

**[Quantum Lab Agent](https://github.com/BrUn3y/quantum_lab_agent)** — Quantum computing-related project exploring the intersection of AI agents and quantum computing technologies, pushing the boundaries at the cutting edge of both AI and quantum computing fields.

**Qiskit Contributions** — Active contributor to Qiskit/qiskit-ibm-runtime (235⭐, 218 forks) and documentation translation projects, supporting the global quantum computing community and making quantum computing more accessible worldwide through multilingual documentation efforts.

### Beyond Code

Edgar is actively engaged in the tech community with significant leadership and educational initiatives:
- **Co-organizing quantum computing meetups** in Guadalajara, with 60+ attendees at the inaugural session, fostering local quantum computing education and networking. This community leadership helps establish Guadalajara as an emerging hub for quantum computing in Latin America.
- **Writing on [Medium](https://medium.com/@brun3y)** about AI agents, athletic performance data, and cloud tooling, sharing practical insights from real-world implementations and providing valuable perspectives on applying AI to solve practical problems.
- **Open-source contributions** across 50 repositories with 47 starred projects, demonstrating active participation in the developer community and commitment to collaborative development.
- **Community building** with 12 followers and 28 following on GitHub, maintaining connections across the global tech ecosystem and fostering knowledge exchange.

When stepping away from the screen, Edgar pursues his passion for **running** (actively training for a sub-21 minute 5K using a data-driven AI approach) and enjoys **heavy music**. His application of AI technology to personal fitness optimization reflects his commitment to applying technology to personal growth.

`BeeAI · CrewAI · LangGraph` &nbsp;·&nbsp; `IBM Cloud` &nbsp;·&nbsp; `Qiskit` &nbsp;·&nbsp; `Running` &nbsp;·&nbsp; `Heavy Music`

---

<div align="center">

<img src="https://raw.githubusercontent.com/BrUn3y/Brun3y/output/github-snake-dark.svg" alt="contribution snake" width="70%" />

<br clear="right" />

</div>

---

### Open Source

- **[IBM Bob Shell Harness](https://github.com/BrUn3y/IBM_Bob_Harness)** (21⭐, 5 forks) — Dockerized harness that runs IBM's Bob Shell headless in unrestricted mode and exposes it over a REST API with Slack integration for autonomous AI operations.
- **[Strava Agent](https://github.com/BrUn3y/Strava_Agent)** (5⭐) — Advanced conversational AI system built with BeeAI framework and AgentStack SDK that analyzes athletic performance directly from the Strava API.
- **X Trends Agent** — Same trend-analysis agent, three frameworks: [BeeAI](https://github.com/BrUn3y/x_trends_agent_BeeAI) · [CrewAI](https://github.com/BrUn3y/x_trends_agent_CrewAI) · [LangGraph](https://github.com/BrUn3y/x_trends_agent_LangGraph).
- **[Quantum Lab Agent](https://github.com/BrUn3y/quantum_lab_agent)** — Quantum computing-related project exploring AI and quantum computing technologies.
- **Qiskit Contributions** — Active contributor to Qiskit/qiskit-ibm-runtime (235⭐, 218 forks) and documentation translation, supporting the quantum computing community.

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

### 🎵 Now Playing

```aura width=1200 height=180
<div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', width: '100%', height: '100%', background: 'linear-gradient(135deg, #0a0a0f 0%, #12121a 100%)', borderRadius: 28, overflow: 'hidden', fontFamily: 'Inter, sans-serif', border: '2px solid rgba(30,215,96,0.35)', padding: '20px 30px', gap: 30 }}>
  <style>{`
    @keyframes spotify-glow { 0%, 100% { box-shadow: 0 0 25px rgba(30,215,96,0.2); } 50% { box-shadow: 0 0 40px rgba(30,215,96,0.4); } }
    @keyframes text-glow { 0%, 100% { text-shadow: 0 0 12px rgba(255,255,255,0.3); } 50% { text-shadow: 0 0 20px rgba(255,255,255,0.5); } }
    @keyframes pulse-scale { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.02); } }
    .spotify-container { animation: spotify-glow 6s ease-in-out infinite; }
    .spotify-text { animation: text-glow 5s ease-in-out infinite; }
    .cover-image { animation: pulse-scale 4s ease-in-out infinite; }
  `}</style>

  <div className="cover-image" style={{ flexShrink: 0, width: 140, height: 140, borderRadius: 16, background: 'linear-gradient(135deg, rgba(30,215,96,0.3), rgba(30,215,96,0.1))', border: '2px solid rgba(30,215,96,0.5)', display: 'flex', flexDirection: 'row', alignItems: 'center', justifyContent: 'center', overflow: 'hidden', boxShadow: '0 8px 32px rgba(30,215,96,0.3)' }}>
    <span style={{ fontSize: 60, opacity: 0.6 }}>🎵</span>
  </div>

  <div style={{ display: 'flex', flexDirection: 'column', justifyContent: 'center', gap: 12, flex: 1, minWidth: 0 }}>
    <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', gap: 12 }}>
      <span style={{ fontSize: 32 }}>🎧</span>
      <span className="spotify-text" style={{ fontSize: 28, fontWeight: 900, color: 'rgba(30,215,96,1)', letterSpacing: '1px' }}>Now Playing on Spotify</span>
    </div>
    
    <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
      <div className="spotify-text" style={{ fontSize: 32, fontWeight: 900, color: '#ffffff', lineHeight: 1.2, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
        Song Title
      </div>
      <div style={{ fontSize: 22, fontWeight: 600, color: 'rgba(255,255,255,0.75)', lineHeight: 1.2, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
        Artist Name
      </div>
    </div>

    <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', gap: 10 }}>
      <div style={{ flex: 1, height: 6, background: 'rgba(30,215,96,0.2)', borderRadius: 10, overflow: 'hidden', display: 'flex' }}>
        <div style={{ width: '45%', height: '100%', background: 'linear-gradient(90deg, rgba(30,215,96,0.8), rgba(30,215,96,1))', borderRadius: 10, display: 'flex' }}></div>
      </div>
      <span style={{ fontSize: 13, color: 'rgba(255,255,255,0.5)', fontWeight: 700, minWidth: 80, textAlign: 'right' }}>2:15 / 5:00</span>
    </div>
  </div>

  <div style={{ flexShrink: 0, display: 'flex', flexDirection: 'row', alignItems: 'center', justifyContent: 'center', width: 70, height: 70, borderRadius: '50%', background: 'rgba(30,215,96,0.2)', border: '2px solid rgba(30,215,96,0.5)', cursor: 'pointer', transition: 'all 0.3s ease' }}>
    <span style={{ fontSize: 36 }}>▶️</span>
  </div>
</div>
```

---

### 🏃 Fitness Stats - August 2026

<div align="center">

```aura width=900 height=320
<div style={{ position: 'relative', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', width: '100%', height: '100%', background: 'linear-gradient(135deg, #0a0a0f 0%, #12121a 100%)', borderRadius: 28, overflow: 'hidden', fontFamily: 'Inter, sans-serif', padding: '28px', border: '1.5px solid rgba(255,255,255,0.1)' }}>
  <style>{`
    @keyframes orb-float-fitness-1 { 0%, 100% { transform: translate(0,0) scale(1); opacity: 0.75; } 50% { transform: translate(40px,-30px) scale(1.25); opacity: 1.1; } }
    @keyframes orb-float-fitness-2 { 0%, 100% { transform: translate(0,0) scale(1); opacity: 0.7; } 50% { transform: translate(-35px,25px) scale(1.22); opacity: 1.05; } }
    @keyframes orb-float-fitness-3 { 0%, 100% { transform: translate(0,0) scale(1); opacity: 0.65; } 50% { transform: translate(32px,-22px) scale(1.18); opacity: 1; } }
    @keyframes ring-pulse-fitness-1 { 0%, 100% { opacity: 0.18; transform: scale(1) rotate(0deg); } 50% { opacity: 0.4; transform: scale(1.1) rotate(180deg); } }
    @keyframes ring-pulse-fitness-2 { 0%, 100% { opacity: 0.15; transform: scale(1) rotate(0deg); } 50% { opacity: 0.32; transform: scale(1.08) rotate(-180deg); } }
    @keyframes ring-pulse-fitness-3 { 0%, 100% { opacity: 0.1; transform: scale(1); } 50% { opacity: 0.25; transform: scale(1.06); } }
    @keyframes ring-pulse-fitness-4 { 0%, 100% { opacity: 0.06; transform: scale(1); } 50% { opacity: 0.18; transform: scale(1.04); } }
    @keyframes card-glow-fitness { 0%, 100% { box-shadow: 0 0 25px rgba(255,255,255,0.1), inset 0 0 15px rgba(255,255,255,0.04); transform: translateY(0px) scale(1); } 50% { box-shadow: 0 0 45px rgba(255,255,255,0.22), inset 0 0 25px rgba(255,255,255,0.1); transform: translateY(-3px) scale(1.02); } }
    @keyframes title-glow-fitness { 0%, 100% { opacity: 0.95; text-shadow: 0 0 20px rgba(255,255,255,0.3); } 50% { opacity: 1; text-shadow: 0 0 35px rgba(255,255,255,0.5); } }
    @keyframes icon-bounce-fitness { 0%, 100% { transform: scale(1) rotate(0deg); } 50% { transform: scale(1.2) rotate(8deg); } }
    @keyframes progress-fill { 0% { width: 0%; } 100% { width: var(--progress-width); } }
    #fito1 { animation: orb-float-fitness-1 12s ease-in-out infinite; }
    #fito2 { animation: orb-float-fitness-2 14s ease-in-out infinite 2s; }
    #fito3 { animation: orb-float-fitness-3 11s ease-in-out infinite 3.5s; }
    #fitr1 { animation: ring-pulse-fitness-1 10s ease-in-out infinite; }
    #fitr2 { animation: ring-pulse-fitness-2 10s ease-in-out infinite 2.5s; }
    #fitr3 { animation: ring-pulse-fitness-3 10s ease-in-out infinite 5s; }
    #fitr4 { animation: ring-pulse-fitness-4 10s ease-in-out infinite 7.5s; }
    .fitness-card { animation: card-glow-fitness 7s ease-in-out infinite; transition: all 0.4s ease; }
    .fitness-card:hover { transform: translateY(-6px) scale(1.05); }
    .fitness-title { animation: title-glow-fitness 6s ease-in-out infinite; }
    .fitness-icon { animation: icon-bounce-fitness 5s ease-in-out infinite; }
  `}</style>

  <svg width="900" height="320" style={{ position: 'absolute', top: 0, left: 0 }}>
    <defs>
      <radialGradient id="fitog1" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(108,195,130,0.8)" />
        <stop offset="45%" stopColor="rgba(108,195,130,0.4)" />
        <stop offset="100%" stopColor="rgba(108,195,130,0)" />
      </radialGradient>
      <radialGradient id="fitog2" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(230,100,115,0.75)" />
        <stop offset="45%" stopColor="rgba(230,100,115,0.35)" />
        <stop offset="100%" stopColor="rgba(230,100,115,0)" />
      </radialGradient>
      <radialGradient id="fitog3" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(80,160,220,0.7)" />
        <stop offset="45%" stopColor="rgba(80,160,220,0.32)" />
        <stop offset="100%" stopColor="rgba(80,160,220,0)" />
      </radialGradient>
      <filter id="glow-filter-fitness">
        <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
        <feMerge>
          <feMergeNode in="coloredBlur"/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>
    </defs>
    <ellipse id="fito1" cx="180" cy="240" rx="240" ry="190" fill="url(#fitog1)" filter="url(#glow-filter-fitness)" />
    <ellipse id="fito2" cx="720" cy="100" rx="230" ry="180" fill="url(#fitog2)" filter="url(#glow-filter-fitness)" />
    <ellipse id="fito3" cx="560" cy="260" rx="220" ry="170" fill="url(#fitog3)" filter="url(#glow-filter-fitness)" />
    <circle id="fitr1" cx="450" cy="160" r="70" fill="none" stroke="rgba(255,255,255,0.22)" strokeWidth="1.5" />
    <circle id="fitr2" cx="450" cy="160" r="110" fill="none" stroke="rgba(255,255,255,0.18)" strokeWidth="1.2" />
    <circle id="fitr3" cx="450" cy="160" r="155" fill="none" stroke="rgba(255,255,255,0.14)" strokeWidth="1" />
    <circle id="fitr4" cx="450" cy="160" r="205" fill="none" stroke="rgba(255,255,255,0.08)" strokeWidth="0.7" />
  </svg>

  <div style={{ position: 'relative', zIndex: 10, width: '100%', display: 'flex', flexDirection: 'column' }}>
    <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', justifyContent: 'center', gap: 12, marginBottom: 28 }}>
      <span className="fitness-icon" style={{ fontSize: 38, fontWeight: 700 }}>🏃</span>
      <span className="fitness-title" style={{ fontSize: 26, fontWeight: 900, color: '#ffffff', letterSpacing: '1.5px' }}>Fitness Stats - August 2026</span>
    </div>

    <div style={{ display: 'flex', flexDirection: 'row', gap: 24, justifyContent: 'center', flexWrap: 'wrap' }}>
      <div className="fitness-card" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', padding: '24px 32px', background: 'rgba(108,195,130,0.16)', border: '2.5px solid rgba(108,195,130,0.45)', borderRadius: 22, minWidth: 180, backdropFilter: 'blur(15px)' }}>
        <span className="fitness-icon" style={{ fontSize: 42, marginBottom: 8 }}>👟</span>
        <span style={{ fontSize: 38, fontWeight: 900, color: 'rgba(108,195,130,1)', marginBottom: 8, textShadow: '0 0 20px rgba(108,195,130,0.6)' }}>32,834</span>
        <span style={{ fontSize: 14, color: 'rgba(255,255,255,0.65)', letterSpacing: '2px', textTransform: 'uppercase', fontWeight: 800, marginBottom: 10 }}>Steps</span>
        <div style={{ width: '100%', height: 6, background: 'rgba(108,195,130,0.2)', borderRadius: 10, overflow: 'hidden', marginBottom: 8 }}>
          <div style={{ width: '65%', height: '100%', background: 'linear-gradient(90deg, rgba(108,195,130,0.8), rgba(108,195,130,1))', borderRadius: 10 }}></div>
        </div>
        <span style={{ fontSize: 13, color: 'rgba(255,255,255,0.45)', fontWeight: 700 }}>3,283/day avg</span>
      </div>

      <div className="fitness-card" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', padding: '24px 32px', background: 'rgba(230,100,115,0.16)', border: '2.5px solid rgba(230,100,115,0.45)', borderRadius: 22, minWidth: 180, backdropFilter: 'blur(15px)' }}>
        <span className="fitness-icon" style={{ fontSize: 42, marginBottom: 8 }}>🔥</span>
        <span style={{ fontSize: 38, fontWeight: 900, color: 'rgba(230,100,115,1)', marginBottom: 8, textShadow: '0 0 20px rgba(230,100,115,0.6)' }}>1,642</span>
        <span style={{ fontSize: 14, color: 'rgba(255,255,255,0.65)', letterSpacing: '2px', textTransform: 'uppercase', fontWeight: 800, marginBottom: 10 }}>Calories</span>
        <div style={{ width: '100%', height: 6, background: 'rgba(230,100,115,0.2)', borderRadius: 10, overflow: 'hidden', marginBottom: 8 }}>
          <div style={{ width: '32%', height: '100%', background: 'linear-gradient(90deg, rgba(230,100,115,0.8), rgba(230,100,115,1))', borderRadius: 10 }}></div>
        </div>
        <span style={{ fontSize: 13, color: 'rgba(255,255,255,0.45)', fontWeight: 700 }}>164/day avg</span>
      </div>

      <div className="fitness-card" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', padding: '24px 32px', background: 'rgba(80,160,220,0.16)', border: '2.5px solid rgba(80,160,220,0.45)', borderRadius: 22, minWidth: 180, backdropFilter: 'blur(15px)' }}>
        <span className="fitness-icon" style={{ fontSize: 42, marginBottom: 8 }}>⏱️</span>
        <span style={{ fontSize: 38, fontWeight: 900, color: 'rgba(80,160,220,1)', marginBottom: 8, textShadow: '0 0 20px rgba(80,160,220,0.6)' }}>625</span>
        <span style={{ fontSize: 14, color: 'rgba(255,255,255,0.65)', letterSpacing: '2px', textTransform: 'uppercase', fontWeight: 800, marginBottom: 10 }}>Active Min</span>
        <div style={{ width: '100%', height: 6, background: 'rgba(80,160,220,0.2)', borderRadius: 10, overflow: 'hidden', marginBottom: 8 }}>
          <div style={{ width: '78%', height: '100%', background: 'linear-gradient(90deg, rgba(80,160,220,0.8), rgba(80,160,220,1))', borderRadius: 10 }}></div>
        </div>
        <span style={{ fontSize: 13, color: 'rgba(255,255,255,0.45)', fontWeight: 700 }}>62/day avg</span>
      </div>
    </div>

    <div style={{ display: 'flex', flexDirection: 'row', justifyContent: 'center', marginTop: 24 }}>
      <span style={{ fontSize: 11, color: 'rgba(255,255,255,0.35)', letterSpacing: '3px', textTransform: 'uppercase', fontWeight: 700 }}>Updated via Google Health API (Fitbit)</span>
    </div>
  </div>
</div>
```

</div>

#### 🏃 Recent Strava Activities

<div align="center">

| Activity | Distance | Time | Pace | Date |
|----------|----------|------|------|------|
| Entrenamiento con pesas a la hora d... | 0.00 km | 56m 15s | N/A | Aug 09, 2026 |
| Remo a la hora del almuerzo | 4.50 km | 10m 6s | N/A | Aug 09, 2026 |
| Entrenamiento a la hora del almuerz... | 0.00 km | 30m 35s | N/A | Aug 08, 2026 |

</div>

---

<div align="center">
<sub>ℹ️ Profile information collected and updated by AI assistant on August 14, 2026</sub>
</div>
