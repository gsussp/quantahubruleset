# Changelog

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
