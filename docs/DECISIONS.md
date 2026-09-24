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

## D-013 — CTFd is the application chassis; QuantaHub owns richer learning semantics
Status: Accepted

CTFd remains the foundational application/platform chassis for identity, sessions, challenges, flags, teams, scoreboard, admin and extension points. QuantaHub-native learning semantics such as Paths, Modules, Rooms, progress and lab workspace do not need to be forced into CTFd challenge objects when a plugin-owned domain model is cleaner.

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

## D-020 — All QuantaHub Cursor rules are Always Apply
Status: Accepted

Cursor does not decide which QuantaHub policy rule is relevant. All QuantaHub rules are included on every Agent task.

## D-021 — Canonical GitHub policy freshness is checked before every prompt
Status: Accepted

The installed plugin version must exactly match `main/VERSION` from `gsussp/quantahubruleset`. Stale, mismatched or unverifiable policy blocks prompt submission.

## D-022 — Technical tie-breakers are deterministic
Status: Accepted

Equivalent technical choices are resolved by `docs/DECISION_POLICY.md`; the user is not asked unless the decision is product/business/legal, destructive, secret/credential-related, contradictory or requires relaxing a security invariant.

## D-023 — Policy changes require a VERSION bump
Status: Accepted

CI rejects governed repository changes when the canonical VERSION has not changed. This prevents remote freshness checks from missing changed policy content.

## D-024 — Canonical Quanta UI system
Status: Accepted

`docs/ui/README.md` is the mandatory UI/UX entry point and `docs/ui/QUANTA_UI_SYSTEM.md` is the detailed design authority. UI work must also obey rules 13–17.

## D-025 — External platforms are inspiration, not templates
Status: Accepted

Hack The Box and TryHackMe may inform broad qualities such as technical credibility, learning clarity and workspace ergonomics. QuantaHub must not copy their visual identity, page layouts, proprietary artwork, wording or distinctive branded components.

## D-026 — Quanta is dark-first, technical and restrained
Status: Accepted

The visual language uses layered dark surfaces, controlled accent colors, outline technical iconography, disciplined spacing/radii and the Quanta Node/Grid/Pulse motifs. Cyber clichés, excessive neon, decorative fake terminals and spectacle-first motion are rejected.

## D-027 — Preserve CTFd frontend conventions before introducing a new application framework
Status: Accepted

M1.5 extends CTFd through plugin/theme/Jinja/progressive-enhancement patterns. A separate SPA framework is not introduced solely for visual polish. New frontend dependencies require license, maintenance, bundle and necessity review.

## D-028 — UI quality gates are mandatory
Status: Accepted

Meaningful UI changes require responsive viewport evidence, accessibility checks, relevant state coverage and visual QA. Backend/unit tests alone do not prove UI completion.

## D-029 — Lab Workspace and terminal are first-class product surfaces
Status: Accepted

The Lab Workspace is designed as a responsive professional security workspace. Terminal rendering uses a replaceable adapter boundary; M1.5 may simulate deterministic commands but must distinguish SIMULATED/DEMO from future LIVE sessions.

## D-030 — Milestone 1.5 is UI/UX Foundation + Interactive Product Prototype
Status: Accepted

After Milestone 1, M1.5 establishes design tokens, responsive shell, personalized dashboard, learning surfaces, Skill Graph prototype, Lab Workspace, terminal prototype, mock lifecycle/state harness, motion, recovery UX, accessibility and visual QA before Milestone 2 adds real runtime connectivity.
