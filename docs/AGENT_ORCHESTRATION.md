# Cursor Agent Orchestration

## Team

QuantaHub uses the normal Cursor main Agent as the Master/Orchestrator plus five specialist subagents:

1. quanta-platform
2. quanta-lab-engine
3. quanta-security
4. quanta-frontend
5. quanta-verifier

There is no extra orchestration subagent by default.

## Main Agent responsibility

The user talks to the normal Cursor main Agent. The always-applied QuantaHub rules make that Agent the project coordinator. It reads canonical policy, decomposes work, selects specialists, parallelizes only independent work, reconciles results, requires security review when needed and sends meaningful implementations to Verifier.

A task is not complete because an implementation agent says so. Completion requires evidence appropriate to the change.

## Specialist boundaries

### quanta-platform

CTFd integration/plugins/themes, users, challenges, flags, learning/progress, tenancy, organizations, application APIs and relational data models. Does not directly control Docker/hypervisors.

### quanta-lab-engine

Registry, manifests, sessions, scheduler, runner, runtime providers, TTL, cleanup, health, resource profiles and gateway integration.

### quanta-security

Threat model, network/origin boundaries, egress, runtime hardening, secrets, mTLS/identity, authorization, abuse controls, registry/supply chain and security review.

### quanta-frontend

Dashboard, paths, rooms, lab controls, terminal/web embedding, progress, accessibility and responsive product UX. Consumes defined APIs rather than bypassing service boundaries.

### quanta-verifier

Independent tests and evidence. Validates unit/integration/E2E behavior, contracts/schemas, lifecycle, isolation, cleanup, authorization, regression and policy requirements.

## Parallel-work rule

Parallelize only when agents are not editing the same ownership area or file set. Prefer separate worktrees/branches for concurrent implementation and integrate only after review.

## Canonical memory

Repository docs and rules are canonical. If a durable architecture decision changes, update the decision log and relevant policy rule in the same change.
