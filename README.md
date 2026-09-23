# QuantaHub Ruleset

Canonical deterministic architecture, security, engineering, Cursor-agent orchestration and verification policy for the QuantaHub cyber-range platform.

Current policy version: **0.3.0**

## Deterministic Cursor mode

QuantaHub uses a strict policy model:

```text
User prompt
    |
    v
Remote GitHub VERSION check
    |
    +-- stale/unreachable --> BLOCK
    |
    v
13/13 rules Always Apply
    |
    v
Cursor Main Agent = Master/Orchestrator
    |
    +--> quanta-platform
    +--> quanta-lab-engine
    +--> quanta-security
    +--> quanta-frontend
    +--> quanta-verifier
```

Cursor does not choose which QuantaHub rule to read. **Every rule is loaded for every Agent task.**

`docs/DECISION_POLICY.md` defines deterministic technical defaults so the Agent does not ask the user to choose between equivalent implementation approaches.

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

## Machine enforcement

- `VERSION` is the canonical policy version.
- `beforeSubmitPrompt` checks GitHub `main/VERSION` before every prompt.
- `plugin/hooks/policy-guard.py` blocks selected unsafe runtime commands.
- `schemas/lab-manifest.schema.json` validates published lab manifests.
- GitHub Actions validates rule inventory, Always Apply state, version consistency, schemas and hook tests.

## Canonical documents

- `docs/DECISIONS.md`
- `docs/DECISION_POLICY.md`
- `docs/REMOTE_POLICY_SYNC.md`
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
