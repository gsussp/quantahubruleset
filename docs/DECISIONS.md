# QuantaHub Decision Log

## D-001 — CTFd is the starting platform shell
Status: Accepted

Reuse CTFd for commodity capabilities such as users, challenges, flags, teams, scoreboard, admin workflows and competition mechanics. Prefer themes/plugins/APIs/adapters over deep core forks.

## D-002 — Cyber-range engine is independent of CTFd
Status: Accepted

Lab orchestration, scheduling, isolation, TTL, cleanup, registry and gateway routing are QuantaHub-owned. CTFd never receives runtime/hypervisor management privileges.

## D-003 — Control plane and lab plane are separate trust domains
Status: Accepted

Intentionally vulnerable workloads do not share the trust boundary of identity, database, cache, admin, secrets or orchestration state.

## D-004 — Preserve runtime abstraction
Status: Accepted

Initial labs may run as containers, but orchestrator domain contracts are not hard-wired to Docker. Runtime providers may include sandboxed containers, microVMs and full VMs.

## D-005 — Three isolation classes
Status: Accepted

1. Standard container for lower-risk web training.
2. Sandboxed container for meaningful code execution.
3. MicroVM/full VM for stronger isolation, kernel/malware/AD/Windows scenarios.

## D-006 — Default lab egress is deny
Status: Accepted

IPv4 and IPv6 egress are denied unless a named lab policy explicitly permits minimum required access.

## D-007 — User access goes through gateways
Status: Accepted

Users do not connect to runner management addresses or arbitrary public container ports. Session-aware gateways/brokers mediate access.

## D-008 — Production never executes arbitrary upstream Git directly
Status: Accepted

Open-source labs pass license review, revision pinning, controlled build, testing/scanning and approved artifact publication.

## D-009 — Lab lifecycle is an explicit state machine
Status: Accepted

Minimum states: REQUESTED, QUEUED, SCHEDULING, PROVISIONING, STARTING, HEALTH_CHECK, READY, STOPPING, EXPIRED, CLEANING, TERMINATED, FAILED/LOST.

## D-010 — Deterministic cleanup is mandatory
Status: Accepted

Session termination removes workloads, networks, ephemeral state, routes, DNS/gateway mappings, temporary credentials/tokens and reservations. Reconciliation handles orphans.

## D-011 — Capacity is measured primarily by active labs
Status: Accepted

Concurrent sessions, runtime classes and resource profiles drive capacity more than registered-user count.

## D-012 — Backend begins as a modular monolith
Status: Accepted

Commodity platform modules may start together. Lab Orchestrator remains separately deployable/permissioned because it operates across a different trust boundary.

## D-013 — CTFd is not mandatory for every learning workflow
Status: Accepted

CTFd remains useful for CTF/competition/challenge flows while learning paths/rooms may use QuantaHub-native modules.

## D-014 — Ruleset repository is canonical agent memory
Status: Accepted

Cursor agents rely on version-controlled policy and architecture rather than remembered chat context.

## D-015 — Main Cursor Agent is Master; five specialist subagents
Status: Accepted

The normal Cursor main Agent is the Master/Orchestrator. Specialist agents are Platform, Lab Engine, Security/Infrastructure, Frontend/UX and Verifier/QA. No extra orchestration subagent is used by default.

## D-016 — Vulnerable lab origins use a separate registrable domain
Status: Accepted

Platform/authentication and intentionally vulnerable lab web origins must not share the same registrable domain in production.

## D-017 — Lab Manifest is machine validated
Status: Accepted

Published labs validate against the canonical JSON Schema before they may enter the approved registry.

## D-018 — Policy pack is CI validated
Status: Accepted

Plugin manifests, hooks, rule frontmatter, specialist-agent inventory and schema examples are validated automatically before release.

## D-019 — Public cyber range has explicit abuse controls
Status: Accepted

Quotas, TTL, rate limits, suspension, default-deny egress, monitoring and emergency controls are architectural requirements rather than later operational additions.
