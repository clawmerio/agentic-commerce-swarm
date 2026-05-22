# Architecture

Agentic Commerce Swarm is organized as a staged LLM workflow. The current public implementation is intentionally simple: `main.py` executes role methods in sequence and saves a reviewable artifact.

## Current Public Runtime

```text
User request
  |
  v
AgenticCommerceSwarm.run()
  |
  +-- squad_lead()
  +-- diagnostician()
  +-- strategist()
  +-- copywriter()
  +-- sanitizer()
  +-- analyst()
  +-- designer()
  +-- webdev()
  +-- qa_auditor()
  |
  +-- save Markdown artifact
  +-- save memory summary when ChromaDB is available
  v
Human review
```

This is not a public LangGraph implementation. The private/original lineage was LangGraph-oriented, and `langgraph` remains in the dependency list, but the current public code does not construct or execute a `StateGraph`.

## Components

| Component | File | Responsibility |
|---|---|---|
| Workflow runner | `main.py` | Owns state object, role prompts, LLM calls, artifact save, memory save. |
| CLI | `squad.py` | Provides the interactive local entrypoint. |
| Memory | `memory.py` | Stores/searches run summaries in ChromaDB when available. |
| Demo site | `examples/demo-site/index.html` | Fictional website context for diagnosis and proposals. |
| Sanitized run | `examples/sanitized-runs/demo_run.md` | Public-safe example of expected output shape. |
| Tests | `tests/` | Lightweight smoke and parser validation. |

## Agent Responsibilities

| Stage | Responsibility | Boundary |
|---|---|---|
| Squad Lead | Convert the request into a conservative internal brief. | Does not invent business facts. |
| Diagnostician | Review the brief and demo-site context. | Does not write final copy. |
| Strategist | Define audience, angle, CTA logic, and constraints. | Uses only supported context. |
| Copywriter | Produce campaign and website copy. | Avoids fake metrics and guarantees. |
| Sanitizer | Check copy for unsafe or unsupported claims. | Flags risk before downstream stages. |
| Analyst | Score output and explain revision needs. | Current loop enforcement is limited. |
| Designer | Provide layout and visual guidance. | Must not invent copy. |
| WebDev | Map copy/design into reviewable website-change proposals. | Does not modify production files. |
| QA Auditor | Challenge the full pipeline before human review. | Produces final risk notes. |

## State Model

`SwarmState` is a dataclass that carries the request and each stage output:

```text
task
squad_brief
diagnosis
strategy
final_copy
sanitizer_report
analyst_report
design_brief
webdev_proposal
qa_report
quality_score
approved_for_human_review
```

The workflow is easy to inspect because each stage writes to a named field rather than mutating an opaque conversation.

## Memory Model

`SwarmMemory` uses ChromaDB persistence when local setup supports it:

```text
task + strategy + final_copy + qa_report + quality_score
  -> ChromaDB collection: agentic_commerce_runs
```

If ChromaDB cannot initialize or query, the memory layer returns safely without blocking the workflow.

## Safety Boundary

The public architecture is proposal-first:

```text
generate proposal
  -> save artifact
  -> QA review
  -> human review
  -> manual implementation or controlled apply outside this repo
```

No code in the current public repository should be described as silently applying production website changes.

## Current Limitations

- Full pipeline tests are not present because live LLM calls require external credentials.
- The analyst score parser depends on model output format.
- Revision loops are architected but not strongly enforced in the public runner.
- LangGraph is not used in the public runtime.
- No deterministic patch/apply layer is included.
