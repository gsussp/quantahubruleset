# QuantaHub Ruleset

Canonical architecture, security, engineering, Cursor-agent orchestration and verification policy for the QuantaHub cyber-range platform.

Current policy version: **0.2.0**

## Architecture

```text
CTFd / Platform Core
        |
        v
QuantaHub Platform Layer
        |
        v
Lab Orchestrator
        |
        v
Runner / Sandbox Plane
```

Vulnerable lab execution is a separate trust domain and uses a separate registrable web domain from platform/authentication origins.

## Cursor model

The normal Cursor main Agent is the **Master/Orchestrator**.

Five specialist subagents:
- `quanta-platform`
- `quanta-lab-engine`
- `quanta-security`
- `quanta-frontend`
- `quanta-verifier`

The plugin bundles:
- constitutional always-applied rules,
- contextual specialist rules,
- five specialist subagents,
- fail-closed high-risk shell hooks,
- machine-readable Lab Manifest schema.

## Machine enforcement

- `schemas/lab-manifest.schema.json` validates published lab manifests.
- `plugin/hooks/policy-guard.py` blocks selected high-confidence unsafe runtime commands.
- `.github/workflows/policy-ci.yml` validates policy structure and hook syntax.
- Security/runtime/application controls remain authoritative; AI rules are not a substitute for technical isolation.

## Canonical documents

- `docs/DECISIONS.md`
- `docs/SYSTEM_ARCHITECTURE.md`
- `docs/SECURITY_MODEL.md`
- `docs/API_CONTRACTS.md`
- `docs/AUTHORIZATION_MODEL.md`
- `docs/NETWORK_POLICY.md`
- `docs/ABUSE_AND_ACCEPTABLE_USE.md`
- `docs/BACKUP_RECOVERY.md`
- `docs/RELEASE_POLICY.md`
- `docs/UPSTREAM_DEPENDENCIES.md`
- `docs/AGENT_ORCHESTRATION.md`
- `docs/CURSOR_INTEGRATION.md`

Chat transcripts are not canonical project state. Durable decisions belong in this repository.

## License

Apache-2.0.
