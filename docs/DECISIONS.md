# QuantaHub Decision Log

## D-001 — CTFd is the starting platform shell
Status: Accepted

QuantaHub will reuse CTFd instead of rebuilding commodity capabilities such as users, challenges, flags, teams, scoreboard, admin workflows and basic competition mechanics.

CTFd must be extended through themes, plugins, APIs and adapters whenever possible. Avoid deep core forks because upstream upgrades become increasingly difficult.

## D-002 — Cyber-range engine is independent of CTFd
Status: Accepted

Lab orchestration, runner scheduling, isolation, TTL, cleanup, lab registry and gateway routing are QuantaHub-owned components. CTFd must never directly receive Docker socket or hypervisor-level privileges.

## D-003 — Control plane and lab/data plane are separate trust domains
Status: Accepted

Vulnerable workloads are intentionally hostile. They must not share the same trust boundary as authentication, database, Redis/Valkey, admin services, secrets or orchestration state.

## D-004 — Start simple but preserve runtime abstraction
Status: Accepted

Initial labs may run as containers, but the orchestrator API must not be hard-wired to Docker-specific semantics. Runtime providers should eventually support sandboxed containers, microVMs and full VMs.

## D-005 — Three isolation classes
Status: Accepted

1. Standard container: low-risk web training workloads.
2. Sandboxed container, e.g. gVisor: user obtains meaningful code execution.
3. MicroVM/full VM, e.g. Firecracker/KVM: kernel, malware, AD, Windows and stronger isolation requirements.

## D-006 — Default lab egress is deny
Status: Accepted

A compromised training target must not become an Internet attack proxy. Any external connectivity is explicit, allowlisted and tied to a named lab profile.

## D-007 — User access goes through gateways
Status: Accepted

Users do not connect to runner management addresses or arbitrary published container ports. HTTP/WebSocket/terminal access is brokered by QuantaHub gateways using session authorization.

## D-008 — Production never executes arbitrary upstream Git directly
Status: Accepted

Open-source labs enter through an import pipeline: license review, commit pinning, review, build, scan, test, SBOM/signing as feasible, and publication to a controlled registry. Runners execute approved immutable artifacts.

## D-009 — Lab lifecycle is an explicit state machine
Status: Accepted

Minimum states: REQUESTED, QUEUED, SCHEDULING, PROVISIONING, STARTING, HEALTH_CHECK, READY, STOPPING, EXPIRED, CLEANING, TERMINATED, FAILED/LOST.

## D-010 — Deterministic cleanup is mandatory
Status: Accepted

Session termination removes workloads, networks, volumes/temp state, routes, DNS entries, gateway mappings, temporary credentials/tokens and resource reservations. An orphan reaper reconciles runtime state against control-plane state.

## D-011 — Capacity is measured primarily by concurrent active labs
Status: Accepted

Registered-user count is not a reliable infrastructure sizing metric. Active lab sessions, runtime type and per-lab resource profiles drive capacity.

## D-012 — Backend begins as a modular monolith
Status: Accepted

Commodity platform modules can live in a modular monolith initially. Lab Orchestrator remains a separate service because it operates in a materially different trust domain.

## D-013 — CTFd is not mandatory for every learning workflow
Status: Accepted

CTFd remains excellent for CTF/competition/challenge use. QuantaHub learning paths, rooms and lab workflows may be managed by custom modules where this produces a cleaner product model.

## D-014 — Rule repository is canonical agent memory
Status: Accepted

Cursor agents must rely on version-controlled architecture/policy artifacts, not remembered chat context. Architecture changes require documentation updates.

## D-015 — Agent team uses one orchestrator plus five specialists
Status: Accepted

Initial model: Master/Orchestrator, Platform, Lab Engine, Security/Infrastructure, Frontend/UX, Verifier/QA. Add more agents only when boundaries are stable and a real specialization need exists.
