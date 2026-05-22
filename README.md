# Agentic Commerce Swarm

[![Tests](https://github.com/cimeria-labs/agentic-commerce-swarm/actions/workflows/tests.yml/badge.svg)](https://github.com/cimeria-labs/agentic-commerce-swarm/actions/workflows/tests.yml)

Agentic Commerce Swarm is a sanitized Python prototype for commercial LLM workflows. It turns a business request into a reviewable marketing/CRO proposal through staged specialist roles, local artifact generation, optional ChromaDB memory, safety review, QA review, and human approval.

The current public implementation is a sequential staged runner in `main.py`. It is not a production SaaS, not an autonomous website editor, and not a public LangGraph graph implementation. The original private project lineage was LangGraph-oriented, but this curated repository exposes the safer staged runner for reviewability.

## Problem

Commercial AI workflows often fail because one prompt mixes strategy, copywriting, design, implementation, compliance, and approval. That makes outputs hard to audit and risky to apply.

This project separates those responsibilities into explicit stages:

```text
User request
  -> Squad Lead
  -> Diagnostician
  -> Strategist
  -> Copywriter
  -> Sanitizer
  -> Analyst
  -> Designer
  -> WebDev
  -> QA Auditor
  -> Human review
```

## What Works Today

| Area | Current evidence |
|---|---|
| Staged LLM workflow | `main.py` executes each role in sequence. |
| Interactive CLI | `squad.py` provides a local entrypoint. |
| OpenAI-compatible model calls | `langchain-openai` is used through `ChatOpenAI`. |
| Persistent memory | `memory.py` uses ChromaDB when available and falls back safely. |
| Fictional demo site | `examples/demo-site/index.html` is used as public-safe context. |
| Markdown artifacts | Runs are saved as Markdown under `data/outputs` at runtime. |
| Sanitized example run | `examples/sanitized-runs/demo_run.md` shows public-safe output shape. |
| Safety and QA stages | Sanitizer, Analyst, and QA Auditor are explicit roles. |
| Automated tests | `pytest` covers score parsing, memory fallback, and state defaults. |

## What Is Not Included

- No autonomous production deployment.
- No automatic website modification.
- No real customer data.
- No production CRM/email/ad-spend connector.
- No visual Kanban UI.
- No daemon/background worker.
- No public LangGraph graph implementation yet.
- No guarantee of conversion lift.

## 60-Second Reviewer Path

1. Read the evidence-based status: [`STATUS.md`](STATUS.md).
2. Inspect the staged runner: [`main.py`](main.py).
3. Inspect the memory layer: [`memory.py`](memory.py).
4. Review architecture: [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).
5. Review the sanitized demo output: [`examples/sanitized-runs/demo_run.md`](examples/sanitized-runs/demo_run.md).
6. Run the tests:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest
```

To run the interactive workflow, create `.env` from `.env.example` and provide your own API key:

```env
OPENAI_API_KEY="your_api_key_here"
```

Then run:

```bash
python squad.py
```

## Architecture

```text
main.py
  |
  +-- loads environment
  +-- initializes LLM clients
  +-- initializes SwarmMemory
  +-- reads fictional demo-site context
  +-- executes specialist role prompts in sequence
  +-- saves Markdown output artifact
  +-- stores run summary in memory when ChromaDB works
  +-- returns QA report for human review
```

The project is intentionally proposal-first. The WebDev stage produces reviewable change proposals; it does not patch a production website.

## Tech Stack

- Python 3.11+
- LangChain / `langchain-openai`
- OpenAI-compatible chat models
- ChromaDB for local memory persistence
- python-dotenv
- Rich CLI utilities
- pytest

Note on LangGraph: the project lineage and dependency list include LangGraph, but the current public runner does not define or execute a LangGraph `StateGraph`. Treat a real public graph implementation as roadmap work unless it is added back explicitly.

## Repository Layout

```text
.
|-- main.py                       # Public staged workflow runner
|-- squad.py                      # Interactive CLI entrypoint
|-- memory.py                     # ChromaDB-backed memory with fallback
|-- requirements.txt              # Runtime dependencies
|-- requirements-dev.txt          # Test dependencies
|-- .env.example                  # Safe environment template
|-- STATUS.md                     # Current evidence and limitations
|-- docs/
|   |-- ARCHITECTURE.md
|   |-- ROADMAP.md
|   |-- SECURITY.md
|   |-- HANDOFF_MODEL.md
|   |-- WORKFLOW.md
|   `-- PUBLIC_RELEASE_CHECKLIST.md
|-- examples/
|   |-- demo-site/
|   `-- sanitized-runs/
`-- tests/
```

## Safety Model

This project is designed around human review:

```text
agent output
  -> sanitizer review
  -> analyst score
  -> QA challenge
  -> saved artifact
  -> human review
  -> manual implementation or controlled apply outside this repo
```

Public examples must remain fictional and sanitized.

## Portfolio Positioning

Use this repo as evidence of:

- staged LLM workflow design;
- role separation in AI automation;
- safety review and QA patterns;
- local memory with graceful fallback;
- human-in-the-loop commercial AI workflows;
- public sanitization of a private prototype.

Do not present it as production software or as a complete autonomous marketing system.

## Resume Bullet

Built a sanitized Python prototype for commercial LLM workflow orchestration, separating strategy, copywriting, safety review, QA, design guidance, and website-change proposals into staged roles with ChromaDB-backed memory, Markdown artifacts, and human-in-the-loop review.

## License

MIT. See [`LICENSE`](LICENSE).
