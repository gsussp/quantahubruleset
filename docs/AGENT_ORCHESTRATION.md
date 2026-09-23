# Cursor Agent Orchestration

## Deterministic team

The normal Cursor main Agent is the QuantaHub Master/Orchestrator. Five specialist subagents exist:

1. quanta-platform
2. quanta-lab-engine
3. quanta-security
4. quanta-frontend
5. quanta-verifier

There is no extra orchestration subagent.

## Main Agent responsibility

The user talks only to the normal Cursor main Agent.

The main Agent:
1. receives all 13 QuantaHub rules on every task,
2. applies docs/DECISION_POLICY.md when a technical choice is equivalent,
3. identifies affected ownership boundaries,
4. launches required specialist agents automatically,
5. parallelizes only independent work,
6. reconciles specialist output,
7. requires quanta-security for security-boundary changes,
8. requires quanta-verifier before meaningful completion.

The user should not need to manually invoke specialist agents.

## Isolated subagent context

Cursor subagents start with isolated context. Therefore every QuantaHub specialist prompt explicitly states that QuantaHub policy and deterministic decision rules are mandatory.

Specialists may not invent architecture inconsistent with canonical QuantaHub rules because context is isolated.

## Specialist ownership

### quanta-platform
CTFd integration/plugins/themes, users, challenges, flags, learning/progress, tenancy, organizations, application APIs and relational data models.

### quanta-lab-engine
Registry, manifests, sessions, scheduler, runner, runtime providers, TTL, cleanup, health, resource profiles and gateway integration.

### quanta-security
Read-only independent reviewer for threat model, trust/origin boundaries, egress, runtime hardening, secrets, identity, authorization, abuse controls and supply chain.

### quanta-frontend
Dashboard, paths, rooms, lab controls, terminal/web embedding, accessibility and responsive product UX.

### quanta-verifier
Read-only independent verifier for tests, schemas/contracts, lifecycle, cleanup, isolation, authorization and policy requirements.

## Parallel-work rule

Parallelize only when agents do not edit the same ownership area. Use isolated worktrees/branches for concurrent implementation when necessary.

Security and Verifier are reviewers, not implementation shortcuts. Findings are returned to the appropriate implementation owner for fixes.

## Canonical memory

Repository rules/docs are canonical. Chat history is not. Durable decisions update DECISIONS.md and affected rules/docs.
