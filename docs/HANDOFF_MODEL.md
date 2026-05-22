# Handoff Model

This document describes the logical handoff model used by the current public prototype. There is no bundled Kanban UI or background daemon in this repository.

## Current Logical Handoff

```text
User
  -> Squad Lead
  -> Diagnostician
  -> Strategist
  -> Copywriter
  -> Sanitizer
  -> Analyst
  -> Designer
  -> WebDev
  -> QA Auditor
  -> Human Review
```

## Agent Contracts

| From | To | Artifact passed | Main constraint |
|---|---|---|---|
| User | Squad Lead | Raw request | Preserve intent. |
| Squad Lead | Diagnostician | Internal brief | Do not invent context. |
| Diagnostician | Strategist | Evidence-based diagnosis | Strategy must follow evidence. |
| Strategist | Copywriter | Strategic direction | Copy must match approved strategy. |
| Copywriter | Sanitizer | Draft copy | Reject unsafe or unsupported claims. |
| Sanitizer | Analyst | Sanitized copy plus risk notes | Score quality and explain revision needs. |
| Analyst | Designer | Approved copy and quality notes | Designer must not invent copy. |
| Designer | WebDev | Visual/layout brief | WebDev must use approved copy only. |
| WebDev | QA Auditor | Website-change proposal | Proposal must be reviewable. |
| QA Auditor | Human | Final report | Challenge claims before approval. |

## Current Revision Reality

The public runner records sanitizer and analyst feedback, but it does not yet enforce a robust automatic revision loop. Treat revision-loop enforcement as roadmap work until tests and deterministic control flow are added.

## Future Visual Handoff

A future UI could represent each role as a board stage:

```text
Backlog -> Brief -> Diagnosis -> Strategy -> Copy -> Safety -> QA -> Web Proposal -> Human Review -> Approved
```

Useful UI features would include:

- one card per request;
- visible current stage;
- revision count;
- QA blockers;
- artifact links;
- human approval button;
- rollback link.
