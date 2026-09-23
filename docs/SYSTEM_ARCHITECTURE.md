# QuantaHub System Architecture

## 1. System intent

QuantaHub is a multi-tenant cyber-training and cyber-range platform. It combines a training/CTF product plane with disposable hostile lab environments. The platform must support a small MVP without creating a dead-end architecture.

## 2. Trust-domain topology

```text
Internet
  |
  v
Edge / CDN / WAF
  |
  v
Reverse Proxy / API Gateway
  |
  +-------------------------+
  |                         |
  v                         v
Platform / CTFd         Lab Gateway
  |                         |
  v                         v
Platform Core          Authorized Session Route
  |                         |
  v                         v
PostgreSQL/Cache       Lab Orchestrator
                            |
                          mTLS
                            |
                 +----------+----------+
                 |          |          |
                 v          v          v
              Runner-1   Runner-2   Runner-N
                 |          |          |
              Sandboxes / isolated lab networks
```

### Control plane

Owns identity, training content, progress, challenge metadata, organizations, admin workflows, lab requests, scheduler state and audit state.

### Lab/data plane

Owns execution of intentionally vulnerable workloads. It is replaceable and assumed hostile.

## 3. Major components

### CTFd base

Use for commodity capabilities where it saves engineering time. Prefer supported extension points. Never give CTFd host-runtime privileges.

### QuantaHub Platform Layer

Modules may include:

- identity integration,
- learning paths,
- rooms/modules,
- XP/levels/badges,
- progress,
- organizations/instructors,
- certificates,
- lab-session UI integration.

### Lab Orchestrator

Responsibilities:

- validate lab requests,
- create session records,
- schedule compatible runners,
- drive lifecycle state machine,
- issue signed/authorized runner jobs,
- publish readiness/failure events,
- enforce TTL,
- request reset/stop/destroy,
- reconcile lost/orphan sessions.

The orchestrator exposes generic operations such as start, stop, reset, health and destroy. Runtime-specific details belong behind runtime-provider interfaces.

### Runner Agent

Each runner contains:

- Runtime Manager,
- Network Manager,
- Resource Controller,
- Image/Artifact Manager,
- Session Supervisor,
- Health Monitor,
- Cleanup/Reaper.

The runner speaks to the orchestrator over authenticated channels, preferably mTLS. Do not expose unauthenticated Docker APIs.

### Lab Gateway

Maps authorized session identities to runtime routes. It handles HTTP/WebSocket and, where applicable, terminal/SSH/RDP brokers. A user should not need or receive runner management IPs.

### Lab Registry

Stores approved lab identities and immutable versions. A published lab references a pinned source/artifact and a standardized manifest rather than arbitrary upstream HEAD state.

## 4. Runtime abstraction

Runtime providers should support a common contract:

- provision(session, manifest),
- start(session),
- health(session),
- reset(session),
- stop(session),
- destroy(session).

Initial provider may be container-based. Future providers may include gVisor, Firecracker and KVM/QEMU.

## 5. Lab topology model

A lab is not necessarily one container. The manifest must support multi-node topologies such as:

```text
attacker -> target -> database
```

or defensive training:

```text
attacker -> Windows endpoint -> telemetry -> SIEM -> analyst workstation
```

Topology definitions include runtime class, resources, network membership, ingress, egress, health checks and ephemeral secrets.

## 6. Session state machine

```text
REQUESTED -> QUEUED -> SCHEDULING -> PROVISIONING -> STARTING
       -> HEALTH_CHECK -> READY -> STOPPING/EXPIRED
       -> CLEANING -> TERMINATED
```

Failure paths enter FAILED or LOST. Every state transition should be idempotent or safely retryable.

## 7. Persistence

PostgreSQL is the source of truth for durable business/session metadata. Redis/Valkey may be used for cache, short locks, rate limits and transient coordination, not as the only durable state store.

## 8. Queue/event model

Provisioning is asynchronous. HTTP callers receive a session/job identity and observe status via polling, SSE or WebSocket. Durable events can include LAB_REQUESTED, LAB_READY, LAB_FAILED, LAB_EXPIRED, FLAG_ACCEPTED and ROOM_COMPLETED.

## 9. Scaling model

Scale by adding runners. Scheduling considers runtime compatibility, free CPU/RAM/disk, current session count, node health and possibly region. Kubernetes is not a day-one dependency; it can be added later as another runtime/scheduling integration.
