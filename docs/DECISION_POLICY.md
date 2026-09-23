# Deterministic Engineering Decision Policy

## Purpose

Cursor must not stop and ask the user to choose between equivalent engineering approaches when QuantaHub policy can decide. This document defines default decisions and tie-breakers.

## General tie-breaker

When multiple valid approaches exist, choose in this order:

1. Existing project convention already in use.
2. Existing dependency already present in the codebase.
3. Simpler operational model.
4. Smaller security blast radius.
5. Easier rollback and testing.
6. Better compatibility with CTFd and current architecture.
7. Lower infrastructure cost.
8. Fewer moving parts.

Do not introduce a new framework, database, queue, service mesh, orchestration platform or build system when an existing component can solve the problem cleanly.

## Platform defaults

- CTFd remains the base platform shell.
- Extend CTFd with plugins, themes, APIs and adapters.
- Avoid deep CTFd core forks.
- Platform backend remains a modular monolith unless a trust boundary or scaling requirement clearly justifies separation.
- Lab Orchestrator remains a separate service.
- PostgreSQL is the durable source of truth.
- Redis or Valkey is for cache, rate limits, locks and transient coordination.
- Do not add another database without an accepted architecture decision.

## Application language and framework defaults

- Match the existing repository language/framework where one already exists.
- For CTFd-side extensions, use the Python/Flask/Jinja conventions supported by the pinned CTFd version.
- For a new standalone Lab Orchestrator or control API, prefer Python with FastAPI/Pydantic unless the existing project already establishes another supported stack.
- Prefer SQLAlchemy/Alembic for new Python relational persistence unless the existing component already uses another migration layer.
- Prefer standard library and existing dependencies before adding new packages.

## Frontend defaults

- Prefer CTFd theme/plugin extension and progressive enhancement before creating a separate SPA.
- Reuse existing CSS/component conventions before adding a new design system.
- Do not bypass API boundaries or authorization for frontend convenience.
- Accessibility and responsive behavior are part of definition of done.

## API defaults

- REST/JSON is the default control API.
- Use explicit versioning for externally consumed or cross-service contracts.
- Use asynchronous job/session semantics for lab provisioning.
- Use SSE for simple server-to-browser status streams; use WebSocket only when bidirectional realtime behavior is required.
- Require idempotency for create/reset/stop/destroy operations.

## Runtime defaults

Choose runtime class from threat level:

1. container — lower-risk web lab without meaningful host-level execution requirements,
2. sandboxed-container — arbitrary code execution is expected,
3. microVM/full-vm — kernel, malware, Windows, AD or stronger isolation requirement.

Never select a weaker runtime merely to reduce implementation effort.

## Networking defaults

- Default deny egress.
- Separate network boundary per session.
- Separate registrable domain for vulnerable lab web origins.
- No direct public runner ports.
- No runtime socket exposure.
- Prefer explicit allowlists to broad CIDR/network exceptions.

## Security defaults

- Least privilege.
- Fail closed for security-critical policy enforcement.
- Short-lived credentials/tokens.
- Service identity is separate from human identity.
- MFA for high-impact administration.
- Negative security tests are mandatory for boundary changes.
- Never weaken a security invariant silently to make a test pass.

## Dependency defaults

Before adding a dependency:

1. verify the feature cannot be implemented reasonably with existing dependencies,
2. verify maintenance activity and license,
3. pin an appropriate compatible version/range,
4. add tests,
5. document any operational/security implications.

For open-source labs, a public repository without a suitable license is not automatically approved.

## Git defaults

- Work on a branch for meaningful changes.
- Keep commits scoped.
- Prefer PR + CI before merge.
- Do not mix unrelated refactors with security-critical changes.
- Update DECISIONS.md and affected rules/docs when a durable architecture decision changes.

## Testing defaults

Minimum verification is based on affected boundary:

- pure logic: unit tests,
- persistence/API: unit + integration,
- cross-service contract: contract + integration,
- user flow: E2E where practical,
- runtime/lab lifecycle: lifecycle + cleanup,
- security boundary: negative tests proving forbidden behavior fails.

## Failure behavior

When a deterministic default exists, use it and continue.

Ask the user only when:
- the choice changes product behavior/business policy,
- there is a legal/licensing decision requiring owner acceptance,
- credentials/secrets/paid services require user action,
- requirements are contradictory,
- a security invariant would have to be intentionally relaxed,
- destructive/irreversible action requires explicit approval.

Otherwise do not ask.
