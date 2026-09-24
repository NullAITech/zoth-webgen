# 🌐 Zoth WebGen Studio & Autonomous Site Foundry

[![Version](https://img.shields.io/badge/version-2.4.0-00f0ff?style=for-the-badge&logo=target&logoColor=white)](https://github.com/NullAITech/zoth-webgen)
[![License](https://img.shields.io/badge/license-Apache%202.0-e8c872?style=for-the-badge&logo=apache&logoColor=black)](LICENSE)
[![Zero-Egress](https://img.shields.io/badge/security-Zero--Egress%20Air--Gapped-34d399?style=for-the-badge&logo=safari&logoColor=white)](https://github.com/NullAITech/zoth-studio-v2)
[![Polyglot](https://img.shields.io/badge/exports-React%20%7C%20Astro%20%7C%20Svelte%20%7C%20Vue%20%7C%20HTML5-bd34fe?style=for-the-badge&logo=vuedotjs&logoColor=white)](https://github.com/NullAITech/zoth-webgen)
[![Org](https://img.shields.io/badge/org-NullAI%20Tech-gold?style=for-the-badge&logo=github&logoColor=black)](https://github.com/NullAITech)

> **Describe a website in plain language. Select layout specs, preview live responsive UI in device frames, inspect deterministic AST token trees, and export polyglot code or standalone zero-dependency bundles.**

---

## 🏛️ Overview

**Zoth WebGen** is the official local-first autonomous website generator and component foundry developed by [NullAI Tech](https://nullai.tech) for [Zoth Studio v2](https://github.com/NullAITech/zoth-studio-v2) and [Zoth OS](https://github.com/NullAITech/zoth-os).

Unlike conventional cloud-tethered website builders that transmit user data and proprietary design assets to remote servers, Zoth WebGen runs entirely within your sovereign local environment with **100% zero cloud egress**.

```
┌────────────────────────────────────────────────────────────────────────┐
│                   ZOTH WEBGEN AUTONOMOUS FOUNDRY                       │
├─────────────────┬─────────────────┬──────────────────┬─────────────────┤
│ 1. Spec Prompt  │ 2. Theme & Look │ 3. Engine Select │ 4. Live Preview │
│ Natural lang /  │ Sovereign Gold, │ Fast WASM,       │ Desktop, Tablet │
│ starter ideas   │ Cyberpunk,      │ Ollama Local AI, │ & Mobile iframe │
│ & skill chips   │ Matrix, Minimal │ Triad Multi-Agent│ device frames   │
├─────────────────┴─────────────────┴──────────────────┴─────────────────┤
│ 5. Polyglot Exporter: React 19 + Tailwind, Astro 5, Svelte 5, Vue, HTML5│
│ 6. Sovereign Deploy: Zero-Egress local loopback bundle or static zip   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## ⚡ 6-Step Autonomous Creation Pipeline

1. **Ideation & Natural Language Spec**:
   - Choose from curated starter layout presets (SaaS Dashboard, Cyberpunk Portfolio, AI Swarm Console, Docs Hub, Solana Mint Deck, Biomorphic Neuro Shop) or articulate custom specifications.
   - Attach targeted generation skills: *Visual Design, SEO / AEO Entity Graph, WCAG AAA Accessibility, 3D & Particle Motion, Small Business Conversion, Lead Generation Forms*.

2. **Brand Identity & Aesthetic Tokens**:
   - Calibrate name and layout aesthetics across 4 high-contrast themes:
     - **Sovereign Imperial Gold** (`#D4AF37` / `#08080B`)
     - **Cyberpunk Neon Cyan & Magenta** (`#00F0FF` / `#D946EF`)
     - **Monospaced Matrix Terminal** (`#22C55E` / `#010A03`)
     - **Editorial Minimalist Light** (`#0F172A` / `#FFFFFF`)

3. **Compiler Engine Selection**:
   - **Fast WASM Isolate**: In-browser client-side deterministic AST synthesis (<25ms).
   - **Local / Offline Ollama**: Runs against local quantized weights (`qwen2.5-coder`, `llama3.3`).
   - **Multi-Agent Triad**: Tri-agent review team (Architect, UI Designer, Code Auditor).

4. **Live Interactive Sneak-Peek Preview**:
   - Real-time DOM viewport rendering inside hardware-calibrated device frames:
     - 📱 **Mobile Viewport** (`375px`)
     - 📟 **Tablet Viewport** (`768px`)
     - 💻 **Desktop Viewport** (`100%`)
   - Interactive prompt iteration: Want a change? Type your tweak and watch updates re-render instantly.

5. **Polyglot Code Exporter**:
   - Instant conversion into 5 production-grade runtimes:
     - **React 19 + Tailwind CSS**
     - **Astro 5 MPA** (Zero-JS static HTML + islands)
     - **Svelte 5 Runes**
     - **Vue 3.4 Composition API**
     - **Zero-JS Pure HTML5 / CSS3**

6. **Deterministic AST & Bundle Sealing**:
   - Cryptographic AST validation hash seal.
   - Standalone single-file HTML bundle export with inline SVG, responsive media queries, and dark/light mode toggles.

---

## 🚀 Quick Start

### Option 1: Standalone Web Interface
Open `index.html` in any modern web browser or serve locally:

```bash
# Clone the repository
git clone https://github.com/NullAITech/zoth-webgen.git
cd zoth-webgen

# Launch local preview server
npx serve .
# or
python3 -m http.server 8080
```

### Option 2: Run via Zoth CLI
If you have [Zoth Studio](https://github.com/NullAITech/zoth-studio-v2) installed:

```bash
npx zoth pull zoth-webgen
zoth webgen "Dark portfolio for an AI security researcher" --theme=cyberpunk --framework=react
```

### Option 3: Python Automation Engine
```bash
python3 webgen_engine.py --template=saas-dashboard --theme=gold --out=./dist/site
```

---

## 📦 Directory Structure

```
zoth-webgen/
├── index.html            # Standalone interactive WebGen Studio UI
├── webgen_engine.py      # Universal Python site generation engine
├── package.json          # Node.js project manifest & scripts
├── LICENSE               # Apache 2.0 License
└── README.md             # Documentation & specifications
```

---

## 🛡️ Sovereign Ecosystem Integration

Zoth WebGen is engineered to operate harmoniously within the NullAI Tech ecosystem:

- **[Zoth Studio v2](https://github.com/NullAITech/zoth-studio-v2)**: The flagship air-gapped sovereign development studio and operator cockpit.
- **[Zoth OS](https://github.com/NullAITech/zoth-os)**: Sovereign Linux operating system with dual Kali + Parrot parity, offline AI tools, and Tor Ghostmode.
- **[Polyglot Framework Exporter](https://github.com/NullAITech/polyglot-framework-exporter)**: React/JSX AST compiler and multi-framework transpiler.
- **[Neuro-Memory Daemon](https://github.com/NullAITech/neuro-memory-daemon)**: STDP synaptic memory for cross-session design token retention.

---

## 📄 License

Released under the **Apache License 2.0**. Free for personal, commercial, and sovereign air-gapped deployments. Maintained by [NullAI Tech](https://github.com/NullAITech).
