# API and Service Contract Policy

## Purpose

Platform Core, Lab Orchestrator, Runner Agents and Gateways communicate only through explicit, versioned contracts. Internal implementation details must not leak across trust boundaries.

## Contract boundaries

### Platform Core -> Lab Orchestrator

Allowed responsibilities:
- request lab session creation,
- query session state,
- request stop/reset/extend,
- receive readiness/failure metadata.

The Platform Core does not pass raw Docker/containerd/hypervisor commands.

### Lab Orchestrator -> Runner Agent

Allowed responsibilities:
- signed/authorized lifecycle commands,
- immutable Lab Manifest reference,
- ephemeral session identity,
- resource/network profile,
- health and cleanup instructions.

Runner Agents reject unsupported or invalid manifest fields rather than improvising.

### Lab Gateway -> Session State

Gateway validates:
- authenticated user,
- active session ownership/authorization,
- permitted endpoint,
- session expiry,
- short-lived connection credential.

## Versioning

Contracts are versioned. Breaking changes require:
1. documented migration,
2. compatibility window,
3. verifier coverage,
4. rollback plan.

## Transport security

Service-to-service management channels must use authenticated transport. Prefer mTLS for runner/orchestrator identity. Never rely solely on source IP for service identity.

## Error model

Errors must be structured and distinguish at least:
- validation failure,
- authorization failure,
- unsupported runtime/profile,
- capacity unavailable,
- provisioning failure,
- health failure,
- cleanup failure,
- dependency unavailable.

## Idempotency

Create/stop/reset/destroy endpoints and runner jobs must be designed for safe retries. Use request/session/job identities to prevent duplicate destructive side effects.
