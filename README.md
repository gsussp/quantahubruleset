# QuantaHub Ruleset

QuantaHub Ruleset is the canonical architecture, security, engineering, agent-orchestration and verification policy pack for the QuantaHub cyber-range platform.

## Purpose

QuantaHub is built on CTFd as a reusable platform shell while its cyber-range capabilities remain separate, isolated and replaceable. This repository exists so Cursor agents do not rediscover architecture decisions from chat history or improvise incompatible implementations.

The repository is designed to be installable as a Cursor Plugin. The plugin bundles:

- always-applied project rules,
- specialized subagent definitions,
- policy hooks,
- architecture and security guidance.

## Non-negotiable architectural idea

```text
CTFd / Platform Plane
        |
        v
Custom QuantaHub Layer
        |
        v
Lab Orchestrator
        |
        v
Runner / Sandbox Plane
```

CTFd is reused for platform capabilities where useful. It is not trusted as the lab-isolation boundary and must not directly own runner/container privileges.

## Cursor installation model

The intended model is to import this repository as a Cursor plugin. A second supported model is to vendor/sync the `plugin/rules` files into a project's `.cursor/rules/` directory.

Once installed, files with `alwaysApply: true` are included in Agent context automatically. The policy pack deliberately splits rules by concern instead of using one enormous prompt.

See `docs/CURSOR_INTEGRATION.md` for installation and enforcement guidance.

## Source of truth

- `docs/DECISIONS.md`: architectural decisions already agreed.
- `docs/SYSTEM_ARCHITECTURE.md`: system topology and boundaries.
- `docs/SECURITY_MODEL.md`: cyber-range threat model and controls.
- `docs/AGENT_ORCHESTRATION.md`: master + specialist agent model.
- `plugin/rules/*.mdc`: machine-consumable Cursor rules.
- `plugin/agents/*.md`: custom subagent definitions.
- `plugin/hooks/`: policy activation/audit hooks.

Do not treat chat transcripts as canonical project state. Update this repository when a durable decision changes.
