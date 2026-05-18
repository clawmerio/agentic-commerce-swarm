# Agentic Commerce Swarm

[![Tests](https://github.com/cimeria-labs/agentic-commerce-swarm/actions/workflows/tests.yml/badge.svg)](https://github.com/cimeria-labs/agentic-commerce-swarm/actions/workflows/tests.yml)

> Experimental multi-agent commercial orchestration workbench for marketing/CRO proposals, safety review, persistent memory and human-in-the-loop approval.

## Overview

**Agentic Commerce Swarm** is a curated portfolio version of a commercial automation prototype originally developed from a LangGraph-oriented multi-agent workflow. It explores how specialized AI agent roles can transform a high-level business request into a structured campaign and website-improvement proposal while preserving reviewability, role separation and safety constraints.

The current public version is intentionally conservative and sanitized: it generates proposals and review artifacts. It does **not** autonomously modify production websites, publish campaigns, spend ad budget or operate real customer accounts.

Instead of using a single chatbot to generate generic content, Agentic Commerce Swarm uses a staged pipeline of specialized roles:

```text
User request
↓
Squad Lead
↓
Diagnostician
↓
Strategist
↓
Copywriter
↓
Sanitizer
↓
Analyst
↓
Designer
↓
WebDev
↓
QA Auditor
↓
Human-in-the-loop approval
```

## Why this project matters

Many LLM automations fail because they mix strategy, copywriting, design, implementation and approval inside one unstructured conversation.

This project separates those responsibilities into explicit role contracts and adds:

- persistent memory;
- output artifact generation;
- quality review;
- sanitizer/compliance checks;
- reviewable website-change proposals;
- human approval before any real-world change;
- sanitized demo data for public portfolio use.

The goal is to demonstrate a practical pattern for **agentic business operations**, not to present a finished production SaaS.

---

## Current status

This repository should be treated as a **functional prototype / experimental workbench**.

| Area | Status |
|---|---|
| Original LangGraph-based multi-agent prototype | Implemented/tested in the project lineage before public sanitization |
| Public staged multi-agent role pipeline | Implemented |
| Interactive CLI workflow | Implemented |
| LLM-backed role execution | Implemented |
| Persistent memory with ChromaDB | Implemented with graceful fallback |
| Markdown output artifacts | Implemented |
| Sanitizer / compliance role | Implemented as a pipeline role |
| QA auditor role | Implemented as final challenge layer |
| Human-in-the-loop approval | Implemented as review workflow, not autonomous execution |
| Public demo site | Implemented with fictional data |
| Public sanitized demo run | Implemented |
| Automated tests | Minimal smoke tests |
| Rubric-based evaluation | Partial / roadmap |
| Deterministic apply flow | Roadmap |
| Visual Kanban handoff UI | Roadmap |
| Daemon/background mode | Roadmap |
| Production deployment | Not included |

### Implementation note

The original/private project lineage included LangGraph-based multi-agent orchestration. This public repository is a curated and sanitized portfolio version: it preserves the agent roles, staged handoff model, memory layer, safety review and HITL workflow, while currently exposing a simplified staged Python runner in `main.py` instead of the full original LangGraph graph implementation.

This distinction is intentional: the public version prioritizes safety, clarity and portfolio reviewability without exposing private business data, local paths or raw internal artifacts.

---

## Architecture

### Agent roles

| Agent | Responsibility |
|---|---|
| Squad Lead | Converts the user request into a conservative internal brief |
| Diagnostician | Reviews current context and previous outputs before strategy |
| Strategist | Defines the narrowest conversion path supported by evidence |
| Copywriter | Produces campaign and website copy |
| Sanitizer | Checks unsafe, non-compliant or risky content |
| Analyst | Scores quality and can force revision loops in future versions |
| Designer | Defines layout and visual direction without inventing copy |
| WebDev | Maps approved copy into website-change proposals |
| QA Auditor | Challenges the full pipeline before human review |
| Human Reviewer | Decides whether anything should be applied outside the repo |

### Runtime flow

```text
main.py
├── loads environment
├── initializes LLM clients
├── initializes persistent memory
├── executes role stages in sequence
├── reads fictional demo-site context
├── saves versioned Markdown outputs
├── stores run summaries in memory when available
└── returns final QA report for human review
```

### Memory layer

The memory layer is designed to preserve learning across runs while staying safe for public use.

Current memory behavior:

- uses ChromaDB persistence when available;
- stores run summaries, strategy, copy, QA report and score;
- fails gracefully if local memory cannot be initialized;
- keeps generated local memory out of Git.

Future memory categories may include:

- approved campaigns;
- rejected outputs and reasons;
- strategies;
- web development proposals;
- QA findings.

---

## Tech stack

- Python
- LangGraph in the original multi-agent orchestration lineage
- LangChain
- OpenAI-compatible chat models through `langchain-openai`
- ChromaDB for local memory persistence
- python-dotenv
- Rich CLI utilities
- pytest for smoke validation

See [`requirements.txt`](requirements.txt) and [`requirements-dev.txt`](requirements-dev.txt) for dependencies.

---

## Repository structure

```text
.
├── main.py                     # Main staged orchestrator for the public sanitized version
├── squad.py                    # Interactive CLI entrypoint
├── memory.py                   # ChromaDB memory layer
├── requirements.txt            # Runtime dependencies
├── requirements-dev.txt        # Test dependencies
├── .env.example                # Safe environment template
├── docs/
│   ├── ARCHITECTURE.md         # Architecture notes
│   ├── WORKFLOW.md             # Development workflow
│   ├── ROADMAP.md              # Current and future scope
│   ├── SECURITY.md             # Secrets and data policy
│   ├── HANDOFF_MODEL.md        # Logical agent handoff
│   └── PUBLIC_RELEASE_CHECKLIST.md
├── examples/
│   ├── demo-site/              # Fictional demo website
│   └── sanitized-runs/         # Public-safe example outputs
└── tests/                      # Minimal smoke tests
```

---

## Setup

Create a local environment:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# or
.venv\\Scripts\\activate   # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

For development and tests:

```bash
pip install -r requirements-dev.txt
pytest
```

Create your local environment file:

```bash
cp .env.example .env
```

Then add your own API key locally:

```env
OPENAI_API_KEY="your_api_key_here"
```

Run the interactive CLI:

```bash
python squad.py
```

Example prompt:

```text
Create a conversion-focused campaign and website improvement proposal for a fictional clinic scheduling AI assistant.
```

---

## Demo artifacts

Public-safe artifacts are available in:

```text
examples/demo-site/index.html
examples/sanitized-runs/demo_run.md
```

They use fictional data and demonstrate the expected structure of a pipeline output without exposing private business information.

---

## Safety model

This project is designed around the idea that AI-generated business changes should be reviewed before being applied.

Core safety principles:

- no credentials in Git;
- no raw customer data in public examples;
- no direct production edits without human review;
- copy, design and web implementation remain separate roles;
- outputs are saved as artifacts before promotion;
- real business data must be sanitized before publication;
- historical transcripts should not override verified code.

Preferred workflow:

```text
agent output
↓
QA report
↓
human review
↓
approved artifact
↓
manual implementation or controlled apply
```

---

## What this repository is good for

This repo is useful as a portfolio case for:

- AI automation engineering;
- multi-agent orchestration patterns;
- commercial automation prototypes;
- LangGraph-oriented agent workflow design;
- LLM memory systems;
- human-in-the-loop workflows;
- AI-assisted website optimization;
- quality and compliance layers for agentic systems;
- public sanitization of a private prototype.

---

## What this repository is not

This repo is not:

- a production SaaS;
- a marketplace publisher;
- an autonomous ad-spending agent;
- a real customer case study;
- a guarantee of conversion uplift;
- a full public mirror of the original/private LangGraph implementation;
- a system that should be pointed at production assets without review.

---

## Curriculum positioning

**Project title:** Agentic Commerce Swarm  
**Short description:** Curated multi-agent commercial orchestration workbench evolved from a LangGraph-oriented prototype, combining specialized LLM roles, persistent memory, sanitizer checks, QA review and human-in-the-loop approval for marketing/CRO proposals.

Example resume bullet:

> Built and curated a multi-agent commercial automation workbench evolved from a LangGraph-oriented prototype, combining specialized LLM roles, persistent ChromaDB memory, safety review, QA scoring and human-in-the-loop approval before website-change proposals.

---

## License

MIT. See [`LICENSE`](LICENSE).

---

## Important note

This repository is a curated and sanitized portfolio version. It intentionally avoids exposing private paths, credentials, raw customer data or business-sensitive artifacts.

If real-world examples are added, use sanitized demo data only.
