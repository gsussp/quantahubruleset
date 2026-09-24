# QuantaHub UI Canonical Entry Point

This directory is the mandatory starting point for QuantaHub UI/UX planning, implementation and review.

## Read order

1. `docs/ui/QUANTA_UI_SYSTEM.md`
2. `plugin/rules/13-ui-governance.mdc`
3. `plugin/rules/14-ui-components.mdc`
4. `plugin/rules/15-ui-learning-experience.mdc`
5. `plugin/rules/16-ui-lab-experience.mdc`
6. `plugin/rules/17-ui-quality-gates.mdc`
7. `docs/DECISION_POLICY.md`
8. relevant architecture/security/API documents for the affected surface

The `quanta-frontend` specialist MUST read this entry point before any UI planning, implementation or review.

## Product direction

QuantaHub combines:
- technical credibility and density,
- guided learning clarity,
- a professional cyber workspace,
- Quanta-specific node/grid/pulse identity,
- responsive, accessible, state-aware interaction.

HTB and TryHackMe may inspire high-level product qualities only. Quanta must not copy their visual identity or proprietary components.

## M1.5 scope

Milestone 1.5 is **UI / UX Foundation + Interactive Product Prototype**.

It establishes:
- design tokens,
- typography/icons,
- responsive application shell,
- personalized learner dashboard,
- Learn/Path/Room experience,
- Lab Workspace,
- terminal rendering and simulated command adapter,
- mock lab lifecycle state harness,
- motion system,
- loading/empty/error/recovery states,
- accessibility and visual QA.

It does not implement the real Runner, real vulnerable workloads, production terminal gateway, SSH/RDP or real recommendation intelligence.

## Backend-later principle

Where backend data does not exist yet, use explicit mock providers/adapters with stable view-model contracts. Do not hard-code fake product state directly into templates. Mocks must be replaceable by API-backed implementations without rewriting the UI and must not be presented as live backend truth.
