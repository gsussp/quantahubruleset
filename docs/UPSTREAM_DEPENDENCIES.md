# Upstream Dependency Policy

## CTFd

- Pin a tested CTFd release/version range.
- Prefer plugins/themes/APIs over deep core forks.
- Review upstream release notes before upgrades.
- Run QuantaHub integration and authorization tests against the candidate version.
- Maintain rollback capability for failed upgrades.
- Record unavoidable core patches explicitly.

## Container images and vulnerable labs

- Pin by immutable digest or pinned revision.
- Do not rely on mutable `latest` tags for production publication.
- Re-import/review when upstream changes materially.

## Cursor plugin API

Ruleset releases that rely on new Cursor plugin/hook/subagent behavior must document the expectation and validation result.

## Dependency updates

Security updates can be expedited, but verification requirements do not disappear. High-risk changes may reduce scope, not validation rigor.
