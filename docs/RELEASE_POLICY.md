# Release and Compatibility Policy

## Versioning

QuantaHub Ruleset uses semantic versioning.

- PATCH: clarifications and non-breaking policy fixes.
- MINOR: new rules, agents, hooks, schemas or backward-compatible contract requirements.
- MAJOR: breaking policy/plugin layout or contract expectations.

## Required release artifacts

A release should update:
- plugin version,
- marketplace metadata version,
- CHANGELOG,
- any compatibility notes,
- schemas/contracts if changed.

## Validation gate

Do not publish a ruleset release unless policy CI passes.

## Compatibility

Document known minimum/maximum compatible Cursor behavior when plugin/hook APIs materially change.

## Deprecation

Breaking policy or schema fields should receive a deprecation/migration path where practical rather than disappearing without notice.
