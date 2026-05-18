# Architecture

Agentic Commerce Swarm is organized as a staged multi-agent pipeline.

## Pipeline

```text
User Request
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
Human Review
```

## Components

| Component | File | Role |
|---|---|---|
| Orchestrator | `main.py` | Runs the staged agent pipeline |
| CLI | `squad.py` | Provides an interactive local entrypoint |
| Memory | `memory.py` | Stores and retrieves past run context |
| Docs | `docs/` | Explains architecture, workflow, safety and roadmap |
| Examples | `examples/` | Holds sanitized demo artifacts |

## Agent contracts

Each agent has a bounded responsibility.

- The Squad Lead preserves user intent.
- The Diagnostician reviews evidence before strategy.
- The Strategist chooses a conversion direction.
- The Copywriter owns customer-facing text.
- The Sanitizer checks unsafe or unsupported content.
- The Analyst scores quality.
- The Designer provides visual guidance only.
- The WebDev maps approved copy into implementation proposals.
- The QA Auditor challenges the full output before human review.

## Memory model

The memory layer is intentionally simple in the public version. It stores run summaries in ChromaDB when available and fails gracefully if local persistence is not configured.

Future versions can split memory into dedicated collections:

- campaigns;
- rejected outputs;
- strategies;
- website proposals;
- QA findings.

## Safety boundary

The system should generate proposals, not silently modify production assets.

Preferred flow:

```text
Generate proposal
↓
Save artifact
↓
QA review
↓
Human approval
↓
Intentional apply/deploy
```
