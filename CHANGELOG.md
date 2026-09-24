# Changelog

## 0.4.0

- Added canonical UI entry point at `docs/ui/README.md`.
- Added detailed Quanta UI system covering visual identity, responsive shell, Dashboard, learning UX, Lab Workspace, terminal simulation, motion, accessibility and visual QA.
- Added Always Apply UI rules 13–17.
- Made `quanta-frontend` read canonical UI policy before any UI planning, implementation or review.
- Added personalized Dashboard policy: Continue Learning, Active Lab, Recommended Next, domain progress, Skill Graph preview, weekly/recent activity and future widget personalization.
- Added Lab Workspace policy with responsive multi-pane/tab behavior, lifecycle state mapping, timer/recovery UX and Focus Mode.
- Added terminal adapter policy with explicit MockTerminalAdapter -> future GatewayTerminalAdapter replacement path and clear SIMULATED/DEMO vs LIVE distinction.
- Added deterministic backend-later provider/view-model boundaries so mock UI state can later be replaced by APIs without rewriting screens.
- Added Quanta Node, Grid and Pulse signature motifs.
- Added motion hierarchy: CSS first, Web Animations API where appropriate, GSAP optional only for justified complex coordinated motion.
- Added responsive, accessibility and visual QA completion gates.
- Clarified CTFd as the application chassis while allowing Quanta-native learning semantics in plugin-owned domain models.
- Bumped policy inventory from 13 to 18 Always Apply rules.

## 0.3.0

- Switched all 13 QuantaHub rules to `alwaysApply: true`.
- Added deterministic engineering tie-breakers in `DECISION_POLICY.md`.
- Added canonical `VERSION` file.
- Added strict `beforeSubmitPrompt` GitHub freshness check on every prompt.
- Stale, mismatched or unverifiable policy versions now block prompt submission.
- Added CI tests for remote freshness enforcement.
- CI now verifies rule inventory and that no contextual QuantaHub rule remains.
- Plugin, marketplace and VERSION must match exactly.

## 0.2.0

- Main Cursor Agent became the Master/Orchestrator.
- Added fail-closed security hooks and executable policy guard.
- Added machine-readable Lab Manifest JSON Schema.
- Added policy validation CI.
- Added separate-origin/domain requirement for vulnerable labs.
- Added API, authorization, network, abuse, recovery, release and upstream dependency policies.
- Added Apache-2.0 licensing metadata.

## 0.1.0

- Initial QuantaHub architecture, security, agent and Cursor policy pack.
