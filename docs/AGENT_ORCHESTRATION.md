# Cursor Agent Orchestration

## Team

QuantaHub starts with six agents total.

1. Master / Orchestrator
2. Platform Agent
3. Lab Engine Agent
4. Security / Infrastructure Agent
5. Frontend / UX Agent
6. Verifier / QA Agent

## Master Agent responsibility

The user primarily talks to the Master Agent. The Master reads the project rules, decomposes work, selects specialists, parallelizes only independent work, reconciles results, requests security review when required and sends completion candidates to Verifier.

A task is not complete because an implementation agent says so. Completion requires verification appropriate to the change.

## Boundaries

### Platform

CTFd integration/plugins/themes, users, challenges, flags, learning/progress, organizations, application APIs and relational data models. Does not directly control Docker/hypervisors.

### Lab Engine

Registry, manifests, sessions, scheduler, runner, runtime providers, TTL, cleanup, health and gateway integration. Does not casually rewrite training UX or CTFd internals.

### Security / Infrastructure

Threat model, network boundaries, egress, runtime hardening, secrets, mTLS/identity, reverse proxy, registry/supply chain and security review.

### Frontend / UX

Dashboard, paths, rooms, lab controls, terminal/web embedding, progress and responsive product UX. Must consume defined APIs rather than bypassing service boundaries.

### Verifier / QA

Independent tests and evidence. Validates unit/integration/E2E behavior, lifecycle, isolation, cleanup, regression and security requirements.

## Parallel-work rule

Parallelize only when agents are not editing the same ownership area or file set. Prefer separate worktrees/branches for concurrent implementation and integrate only after review.

## Canonical memory

Repository docs and rules are canonical. If a durable architecture decision changes, update the decision log and relevant policy rule in the same change.
