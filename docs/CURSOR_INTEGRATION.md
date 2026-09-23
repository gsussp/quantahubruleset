# Cursor Integration

## Goal

Cursor must work under QuantaHub policy continuously without requiring the user to remind it to read rules or choose which policy applies.

## Required model: Cursor Plugin

Install the `plugin/` directory as the QuantaHub Cursor Plugin. The normal Cursor main Agent is the Master/Orchestrator.

The plugin contains:
- all 13 QuantaHub rules,
- five specialist subagents,
- session policy context,
- per-prompt canonical GitHub freshness enforcement,
- high-risk shell policy enforcement.

## All rules are Always Apply

Deterministic mode intentionally uses:

```yaml
alwaysApply: true
```

for every QuantaHub rule.

Cursor does not decide which QuantaHub rule is relevant. All rules are available on every Agent task.

This uses more context than selective rules by design; consistency is more important than context minimization for this project.

## Canonical GitHub freshness check

Before every user prompt is submitted, `beforeSubmitPrompt` executes:

```text
plugin/hooks/remote-policy-check.py
```

It compares:
- local installed plugin version,
- canonical `main/VERSION` from `gsussp/quantahubruleset`.

Exact match is required.

Strict behavior:
- equal -> prompt continues,
- stale/mismatched -> blocked,
- GitHub cannot be reached -> blocked,
- local policy version unreadable -> blocked.

The remote repository is therefore consulted before every prompt without executing mutable remote code.

## Why remote rules are not downloaded on every prompt

Cursor's `beforeSubmitPrompt` hook can block/allow a prompt but does not inject arbitrary updated policy context. The installed Always Apply rules are the context source. Remote GitHub is the freshness authority.

Automatically downloading and executing mutable policy/hook code on every prompt would also create a supply-chain risk.

## Local plugin testing

Place the contents of this repository's `plugin/` directory in:

```text
~/.cursor/plugins/local/quantahub-policy/
```

The target directory must contain:

```text
.cursor-plugin/plugin.json
rules/
agents/
hooks/
```

A Python 3 interpreter available as `python` is required by the command hooks.

## Agent behavior

The main Agent:
1. receives every QuantaHub rule automatically,
2. follows `DECISION_POLICY.md` instead of asking for equivalent technical choices,
3. delegates to specialists automatically,
4. requires security review for security-boundary changes,
5. requires verifier evidence before meaningful completion.

## Project-local fallback

Copying rules/agents to `.cursor/` can provide context, but it does not reproduce plugin hook enforcement. For QuantaHub development, the plugin form is required.

## Hard rule

Do not develop QuantaHub with a stale, unverifiable, selectively-loaded or partially-installed policy pack.
