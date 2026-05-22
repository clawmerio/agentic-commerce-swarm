# Roadmap

This roadmap separates credibility fixes, engineering maturity, and deeper product evolution. The current public repo is a staged prototype, not production automation.

## Next 30 Minutes

- Keep README and status language aligned with the public sequential runner.
- Add explicit reviewer path and test command.
- Keep public examples fictional and sanitized.
- Avoid describing LangGraph as implemented in public code until a graph exists.

## Next 2 Hours

- Add tests around role boundary helpers and score parsing edge cases.
- Add a fixture-based demo run that does not call an external LLM.
- Add a small architecture diagram to the README or docs.
- Add a `docs/PORTFOLIO.md` page with accurate GitHub, resume, and LinkedIn wording.
- Clarify why `langgraph` is still in dependencies, or remove it if the public runner stays sequential.

## 1 To 2 Day Improvements

- Restore a real public LangGraph `StateGraph` implementation, with tests, if graph orchestration is a portfolio goal.
- Add mock LLM clients for deterministic full-pipeline tests.
- Add structured run metadata: model, timestamp, score, artifact path, safety decision.
- Add stricter revision-loop enforcement when sanitizer or analyst output fails.
- Add deterministic proposal-to-patch tooling for demo-site changes, with human approval.

## Later

- Browser-based review UI or Kanban handoff board.
- Provider fallback and cost/token tracking.
- Evaluation rubrics stored as versioned config.
- Dashboard for run history and QA results.
- Deployment guide for a controlled internal workbench.

## Non-Goals For This Public Repo

- Running real customer campaigns.
- Editing production websites automatically.
- Claiming conversion uplift without measurement.
- Publishing private business data or transcripts.
- Calling the public code production-ready before tests, evals, and deployment guardrails exist.
