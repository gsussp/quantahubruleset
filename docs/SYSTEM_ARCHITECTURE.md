# QuantaHub System Architecture

## 1. System intent

QuantaHub is a multi-tenant cyber-training and cyber-range platform. It combines a training/CTF product plane with disposable hostile lab environments. The platform must support a small MVP without creating a dead-end architecture.

## 2. Trust-domain topology

```text
Internet
  |
  +--> Platform domain (control plane)
  |       |
  |       v
  |   Edge / API Gateway
  |       |
  |       +--> CTFd / Platform Core --> PostgreSQL / Cache
  |       |
  |       +--> Lab Orchestrator
  |
  +--> Separate lab registrable domain
          |
          v
      Lab Gateway
          |
          v
   Authorized Session Route
          |
        mTLS
          |
   +------+------+------+
   |      |      |      |
 Runner-1 Runner-2 ... Runner-N
   |             |
 isolated lab networks/sandboxes
```

Platform and vulnerable lab web origins use different registrable domains.

### Control plane

Owns identity, training content, progress, challenge metadata, organizations, admin workflows, lab requests, scheduler state and audit state.

### Lab/data plane

Owns execution of intentionally vulnerable workloads. It is replaceable and assumed hostile.

## 3. Major components

### CTFd base

Use for commodity capabilities where it saves engineering time. Prefer supported extension points. Never give CTFd host-runtime privileges.

### QuantaHub Platform Layer

Modules may include identity integration, learning paths, rooms/modules, XP/levels/badges, progress, organizations/instructors, certificates and lab-session UI integration.

### Lab Orchestrator

Responsibilities:
- validate lab requests and manifests,
- create session records,
- schedule compatible runners,
- drive lifecycle state machine,
- issue authorized runner jobs,
- publish readiness/failure events,
- enforce TTL,
- request reset/stop/destroy,
- reconcile lost/orphan sessions.

The orchestrator exposes generic operations such as provision/start/health/reset/stop/destroy. Runtime-specific details belong behind runtime-provider interfaces.

### Runner Agent

Each runner contains Runtime Manager, Network Manager, Resource Controller, Artifact Manager, Session Supervisor, Health Monitor and Cleanup/Reaper.

The runner communicates with the orchestrator over authenticated management channels, preferably mTLS. Do not expose unauthenticated runtime APIs.

### Lab Gateway

Maps authorized session identities to runtime routes and handles HTTP/WebSocket and, where applicable, terminal/SSH/RDP brokers. Users do not receive runner management addresses.

### Lab Registry

Stores approved immutable lab versions. Published labs reference pinned sources/artifacts and validate against `schemas/lab-manifest.schema.json`.

## 4. Runtime abstraction

Runtime providers implement a stable contract:
- provision(session, manifest),
- start(session),
- health(session),
- reset(session),
- stop(session),
- destroy(session).

Initial provider may be container-based. Future providers may include gVisor, Firecracker and KVM/QEMU.

## 5. Lab topology model

A lab may contain multiple services or machines, including attacker, target, database, telemetry and analyst systems. Topology definitions include runtime class, resources, networks, ingress/egress, health checks and ephemeral secrets.

## 6. Session state machine

```text
REQUESTED -> QUEUED -> SCHEDULING -> PROVISIONING -> STARTING
       -> HEALTH_CHECK -> READY -> STOPPING/EXPIRED
       -> CLEANING -> TERMINATED
```

Failure paths enter FAILED or LOST. Every transition should be idempotent or safely retryable.

## 7. Persistence

PostgreSQL is the durable source of truth for business/session metadata. Redis/Valkey may be used for cache, short locks, rate limits and transient coordination, not as the only durable state store.

## 8. Queue/event model

Provisioning is asynchronous. HTTP callers receive a session/job identity and observe status via polling, SSE or WebSocket. Durable events can include LAB_REQUESTED, LAB_READY, LAB_FAILED, LAB_EXPIRED, FLAG_ACCEPTED and ROOM_COMPLETED.

## 9. Contracts

Platform Core, Orchestrator, Runner and Gateway use explicit versioned contracts documented in `API_CONTRACTS.md`. Platform code does not issue raw container/hypervisor commands.

## 10. Scaling model

Scale by adding runners. Scheduling considers runtime compatibility, free CPU/RAM/disk, current session count, node health and possibly region. Kubernetes is not a day-one dependency; it may be added later without changing core domain contracts.
