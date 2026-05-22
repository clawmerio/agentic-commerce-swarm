# Project Status

Agentic Commerce Swarm is a curated public prototype for staged commercial LLM workflows. The public version prioritizes reviewability, sanitized examples, and honest scope over exposing the full private development lineage.

## Status Summary

| Area | Status | Evidence | Notes |
|---|---|---|---|
| Staged workflow runner | Implemented | `main.py` | Sequential role execution, not a public LangGraph graph. |
| Interactive CLI | Implemented | `squad.py` | Local command-line entrypoint. |
| LLM role prompts | Implemented | `main.py` | Specialist prompts for brief, diagnosis, strategy, copy, safety, QA, design, and web proposal. |
| Memory layer | Implemented with fallback | `memory.py` | ChromaDB is used when available; failures do not block runs. |
| Output artifacts | Implemented | `_save_output()` in `main.py` | Runtime outputs are saved as Markdown. |
| Sanitized demo artifacts | Implemented | `examples/` | Fictional demo site and public-safe demo run. |
| Tests | Minimal but present | `tests/` | Smoke tests cover parser, memory fallback, and state defaults. |
| LangGraph graph | Not public in current code | `README.md`, `main.py` | LangGraph is project lineage / future work unless a real graph is restored. |
| Deterministic apply flow | Not included | `docs/ROADMAP.md` | Public version generates proposals only. |
| Production deployment | Not included | `docs/SECURITY.md` | Human review required before real-world use. |

## What Is Safe To Claim

- The repo implements a staged Python LLM workflow.
- It demonstrates role separation for commercial AI automation.
- It includes ChromaDB-backed memory with graceful fallback.
- It has public-safe demo artifacts.
- It includes lightweight automated tests.
- It is a prototype/workbench, not production software.

## What Not To Claim

- Do not claim the current public code runs a LangGraph `StateGraph`.
- Do not claim autonomous website editing.
- Do not claim production readiness.
- Do not claim real customer or conversion results.
- Do not claim enterprise-grade evaluation or deployment.

## Current Verification

Run:

```bash
python -m pytest
```

Current tests validate:

- score parsing behavior;
- memory fallback behavior;
- `SwarmState` defaults;
- `SwarmMemory.save_run()` does not raise in the tested path.

## Main Remaining Risks

- LLM role behavior is mostly prompt-driven and not regression-tested.
- Tests do not mock LLM calls or validate full pipeline execution.
- `requirements.txt` includes lineage/future dependencies that are not all exercised by public code.
- Quality scoring depends on model output format.
- No deterministic apply/patch flow is included.

## Recommended Next Step

Add non-LLM regression tests around role boundaries and output parsing, then either:

1. restore a real public LangGraph implementation; or
2. remove LangGraph from positioning and dependencies entirely.

Either option would reduce evaluator confusion.
