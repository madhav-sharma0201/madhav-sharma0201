<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,40:7C3AED,100:00D9FF&height=180&section=header&text=Madhav%20Sharma&fontSize=48&fontColor=FFFFFF&animation=fadeIn&fontAlignY=34&desc=Full-Stack%20Engineer%20%C2%B7%20AI%20%2F%20ML%20%C2%B7%20Cloud%20Native&descAlignY=55&descSize=16&font=JetBrains%20Mono"/>
</div>

<h3 align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=24&duration=3800&pause=900&color=00D9FF&center=true&vCenter=true&width=880&lines=Hey+there!+I'm+Madhav+%F0%9F%91%8B;Full-Stack+Engineer+%E2%80%94+React+%C2%B7+Node+%C2%B7+Microservices+%F0%9F%92%BB;I+build+multi-agent+AI+systems+%F0%9F%A4%96;Fine-tune%2C+serve+and+ship+LLMs+%F0%9F%A7%A0;Merged+upstream+into+CNCF+Kubescape+%E2%98%B8%EF%B8%8F" alt="Typing SVG" />
</h3>

<p align="center">
  <a href="mailto:madhavsharma2023@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail" />
  </a>
  <a href="https://github.com/madhav-sharma0201/falcon-ai">
    <img src="https://img.shields.io/badge/Falcon%20AI-7C3AED?style=for-the-badge&logo=react&logoColor=white" alt="Falcon AI" />
  </a>
  <a href="https://github.com/madhav-sharma0201?tab=repositories">
    <img src="https://img.shields.io/badge/Repositories-181717?style=for-the-badge&logo=github&logoColor=white" alt="Repos" />
  </a>
  <!-- Add your LinkedIn: replace YOUR-HANDLE below and delete these comment markers.
  <a href="https://www.linkedin.com/in/YOUR-HANDLE/">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  -->
  <img src="https://komarev.com/ghpvc/?username=madhav-sharma0201&label=Profile+Views&color=00d9ff&style=for-the-badge" alt="Profile Views" />
</p>

---

## 🧠 About Me

- 💻 **Full-stack engineer** — I build complete products: React 19 front-ends, Express microservice backends, MongoDB/Redis data layers, and the auth, billing and storage plumbing in between
- 🤖 **AI/ML** — I build **multi-agent systems** on LangGraph, **RAG pipelines** over vector stores, and I **fine-tune and serve my own models** (QLoRA → FastAPI → Kubernetes)
- 🦅 Currently building **[Falcon AI](https://github.com/madhav-sharma0201/falcon-ai)** — a LangGraph supervisor routing to 8 specialist agents across a 5-service backend, with RAG, S3 artifacts and metered credits
- ☸️ Also contribute **upstream to [Kubescape](https://github.com/kubescape/kubescape)** (CNCF) — real merged PRs on failure boundaries and cluster connection handling
- 🧪 The bugs I enjoy most are the boring-looking ones — race conditions, stale caches, ports reported before they're bound
- 💡 I don't claim anything I can't link to a diff

---

## 🧰 Tech Stack

<p align="center"><b>Frontend</b></p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=react,redux,tailwind,vite,js,ts,html,css&theme=dark" />
</p>

<p align="center"><b>Backend &amp; Data</b></p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=nodejs,express,mongodb,redis,postgres,firebase,docker,nginx&theme=dark" />
</p>

<p align="center"><b>AI / ML &amp; Cloud</b></p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=python,pytorch,fastapi,sklearn,aws,terraform,kubernetes,go&theme=dark" />
</p>

---

## 🚀 Featured Projects

### 🦅 Falcon AI — [Repo](https://github.com/madhav-sharma0201/falcon-ai)
> **A multi-agent AI platform on a LangGraph supervisor.** Eight specialist agents (chat, coding, search, vision, PDF-RAG, PDF gen, PPT gen, image gen) behind a routing graph, across a five-service backend.

The routing layer decides in three tiers, cheapest first: an explicit client override, then **deterministic file rules** (an image goes to `vision`, a PDF to `pdf_rag`), and only then an **LLM classifier** — so the common cases never pay for a classification round-trip. RAG runs over **Qdrant**, conversation memory is **cache-first through Redis** with a Mongo fallback, generated decks and PDFs land in **S3 behind presigned URLs**, and credits are **metered per agent** through a single owning service.

![React](https://img.shields.io/badge/React_19-61DAFB?style=flat&logo=react&logoColor=black)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat&logo=nodedotjs&logoColor=white)
![Express](https://img.shields.io/badge/Express_5-000000?style=flat&logo=express&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat&logo=langchain&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=mongodb&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat&logo=redis&logoColor=white)
![Qdrant](https://img.shields.io/badge/Qdrant-DC244C?style=flat&logo=qdrant&logoColor=white)
![AWS S3](https://img.shields.io/badge/AWS_S3-569A31?style=flat&logo=amazons3&logoColor=white)
![Razorpay](https://img.shields.io/badge/Razorpay-0C2451?style=flat&logo=razorpay&logoColor=white)

---

### 🤖 Text-to-SQL LLMOps Pipeline — [Repo](https://github.com/madhav-sharma0201/sql-llmops-pipeline)
> **Fine-tuned and shipped my own model end to end.** Llama-3.2-3B with **4-bit QLoRA (Unsloth)** on **78,577 DDL/query pairs** — training loss **3.05 → 0.50** in 60 steps while touching only **0.75% of parameters**. **97.8% SQL execution accuracy**, hallucinations under **2.5%**, quantized to **2.2 GB VRAM (NF4)**. Served as an async **FastAPI** microservice (~140 ms GPU latency) on **AWS EKS**, provisioned with **Terraform** and delivered by **ArgoCD** GitOps.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/QLoRA_+_Unsloth-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat&logo=terraform&logoColor=white)
![AWS EKS](https://img.shields.io/badge/AWS_EKS-FF9900?style=flat&logo=amazonwebservices&logoColor=white)
![ArgoCD](https://img.shields.io/badge/ArgoCD-EF7B4D?style=flat&logo=argo&logoColor=white)

---

### ⚡ Distributed Rate Limiter — [Repo](https://github.com/madhav-sharma0201/ratelimiter)
> **Token bucket** rate limiter proving **shared state and atomicity across 3 stateless backends**. The naive read-then-write is a race; the fix pushes refill, capacity check, and deduction into a single **atomic Redis Lua script**. Hit "Burst" on the dashboard to fire 20 concurrent requests across all three instances and watch one shared limit hold exactly.

![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat&logo=nodedotjs&logoColor=white)
![Redis](https://img.shields.io/badge/Redis_Lua_EVAL-DC382D?style=flat&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat&logo=vite&logoColor=white)

---

### 🏫 Graphura — School Management ERP *(Internship)*
> Full-stack feature work on a production School ERP — **8 PRs merged** *(private repo, so not publicly linkable)*: academics reports & timetables, marks entry/marksheet/results, staff management, parent profiles & meetings, dropout and admission trend dashboards.

![React](https://img.shields.io/badge/React-61DAFB?style=flat&logo=react&logoColor=black)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat&logo=nodedotjs&logoColor=white)
![Express](https://img.shields.io/badge/Express-000000?style=flat&logo=express&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=mongodb&logoColor=white)

---

### ☸️ kubescape-fleet-spike — [Repo](https://github.com/madhav-sharma0201/kubescape-fleet-spike)
> Architectural spike in **Go** for **multi-cluster fleet posture aggregation**, validated against real scan output captured from three `kind` clusters. Race-tested, `go vet` clean.

Building this is how I found the upstream bug: aggregating reports from three clusters only works if each one says which cluster it came from, and `clusterName` was empty in all of them. That became issue [#2856](https://github.com/kubescape/kubescape/issues/2856) and, eventually, [#2898](https://github.com/kubescape/kubescape/pull/2898).

![Go](https://img.shields.io/badge/Go-00ADD8?style=flat&logo=go&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)
![Tests](https://img.shields.io/badge/tests-race--tested-2ea043?style=flat&logo=go&logoColor=white)

---

### 🎤 TEDxSGNS Youth — [Repo](https://github.com/madhav-sharma0201/TEDxSite)
> Responsive event site for **TEDxSGNS Youth**, built with React + Vite.

![React](https://img.shields.io/badge/React-61DAFB?style=flat&logo=react&logoColor=black)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat&logo=vite&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)

---

## 🌍 Open Source — CNCF Kubescape

> Alongside product work, I contribute upstream. **This table regenerates itself daily from the GitHub API** — it is never hand-maintained.

<!-- PRS:START -->
| PR | Title | Repo | Status |
|---|---|---|---|
| [#2898](https://github.com/kubescape/kubescape/pull/2898) | fix(printer): label the report with the context the scan actually used | `kubescape/kubescape` | ✅ Merged |
| [#2810](https://github.com/kubescape/kubescape/pull/2810) | refactor(core): expose cluster connection failure as a sentinel error | `kubescape/kubescape` | ✅ Merged |
| [#2788](https://github.com/kubescape/kubescape/pull/2788) | fix(core): return cluster connection failures from Scan instead of terminating | `kubescape/kubescape` | ✅ Merged |
| [#2785](https://github.com/kubescape/kubescape/pull/2785) | test(cautils): use t.Setenv so env vars are restored between runs | `kubescape/kubescape` | ✅ Merged |
| [#2783](https://github.com/kubescape/kubescape/pull/2783) | fix(resourcehandler): repair NewOPASessionObj call broken by merge | `kubescape/kubescape` | ✅ Merged |
| [#2761](https://github.com/kubescape/kubescape/pull/2761) | fix(cautils): report the bound port from GetPortForwardLocalhost | `kubescape/kubescape` | ✅ Merged |
| [#160](https://github.com/kubescape/k8s-interface/pull/160) | fix(k8sinterface): refresh API discovery for a newly initialized live client | `kubescape/k8s-interface` | ✅ Merged |
<!-- PRS:END -->

**The one I'd point at — [#2898](https://github.com/kubescape/kubescape/pull/2898).** While building my fleet-posture spike I noticed `clusterName` came back empty in every scan report, so I filed [#2856](https://github.com/kubescape/kubescape/issues/2856). Someone fixed it — but that fix landed **22 minutes after** a separate PR changed where the scan's context name comes from, and the two disagreed. Point `--kubeconfig` at a file whose current-context differs from the ambient one, and the report gets labelled with the *ambient* cluster while the scan actually ran against the *selected* one. That's worse than the empty field it replaced: an empty `clusterName` is obviously unusable, a wrong one looks authoritative — and anyone scanning several contexts in CI would mis-attribute their results. #2898 makes the label follow the scan.

The rest cluster on **failure boundaries**: [#2788](https://github.com/kubescape/kubescape/pull/2788) made `Kubescape.Scan` return an error for an unreachable cluster instead of calling `logger.Fatal`, [#2810](https://github.com/kubescape/kubescape/pull/2810) exposed that as a **sentinel error** so callers can branch on it, and [#160](https://github.com/kubescape/k8s-interface/pull/160) refreshes **API discovery** for a newly initialized live client — `InitializeMapResources` otherwise keeps the *first* cluster's discovery after you build a client for a second one.

<p align="center">
  <img src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Fsearch%2Fissues%3Fq%3Dauthor%3Amadhav-sharma0201%2Btype%3Apr%2Bis%3Amerged%2Bis%3Apublic&query=%24.total_count&label=Public%20Merged%20PRs&color=2ea043&style=for-the-badge&logo=git&logoColor=white" />
  <img src="https://img.shields.io/badge/CNCF%20Project-Kubescape-326CE5?style=for-the-badge&logo=cncf&logoColor=white" />
  <img src="https://img.shields.io/github/stars/kubescape/kubescape?style=for-the-badge&label=Upstream%20Stars&color=FFD700&logo=github&logoColor=white" />
</p>

---

## 📊 GitHub Stats

<p align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=madhav-sharma0201&theme=tokyonight" width="98%" />
</p>

<p align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=madhav-sharma0201&theme=tokyonight" height="200" />
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=madhav-sharma0201&theme=tokyonight" height="200" />
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=madhav-sharma0201&theme=tokyonight&utcOffset=5.5" height="200" />
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=madhav-sharma0201&theme=tokyonight&hide_border=true" height="180" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=madhav-sharma0201&theme=tokyo-night&hide_border=true&area=true&custom_title=Contribution%20Graph" width="98%" />
</p>

---

## 🐍 Watch the contributions get eaten

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/madhav-sharma0201/madhav-sharma0201/output/snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/madhav-sharma0201/madhav-sharma0201/output/snake.svg" />
    <img alt="snake eating my contributions" src="https://raw.githubusercontent.com/madhav-sharma0201/madhav-sharma0201/output/snake.svg" width="98%" />
  </picture>
</div>

---

<div align="center">

### 💬 Currently

**Building** Falcon AI — multi-agent orchestration at product scale · **Exploring** agent evaluation and retrieval quality · **Open to** full-stack and AI/ML roles and collaboration

<br/>

> *"Any fool can write code that a computer can understand. Good programmers write code that humans can understand."*
> — Martin Fowler

<br/>

<a href="mailto:madhavsharma2023@gmail.com">
  <img src="https://img.shields.io/badge/Let's%20build%20something-00D9FF?style=for-the-badge&logo=minutemailer&logoColor=black" />
</a>

</div>

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00D9FF,60:7C3AED,100:0D1117&height=120&section=footer"/>
</div>
