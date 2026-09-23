# Cursor Integration

## Goal

Use this repository as persistent engineering policy instead of repeating prompts for every Cursor task.

## Recommended model: Cursor Plugin

Install the `plugin/` directory as the QuantaHub Cursor Plugin. It packages rules, five specialist subagents and hooks. The normal Cursor main Agent acts as the QuantaHub Master/Orchestrator.

A random GitHub URL is not persistent policy. The plugin must be installed, or its components must be copied/synced into Cursor-supported project locations.

## Local validation/install workflow

For local plugin testing, place the contents of this repository's `plugin/` directory in:

```text
~/.cursor/plugins/local/quantahub-policy/
```

That target directory must contain `.cursor-plugin/plugin.json`. Restart Cursor or reload the window, then verify the plugin in Customize.

The policy guard requires a Python 3 interpreter available as `python`. Security-critical shell hooks use `failClosed: true`; if the guard cannot run, matching high-risk shell actions are blocked rather than silently allowed.

## Project-local fallback

If plugin installation is not desired:

```text
<project>/.cursor/rules/quantahub/   <- copy plugin/rules/*
<project>/.cursor/agents/            <- copy plugin/agents/*
```

Hooks are not activated merely by copying rules/agents. Use the plugin form when hook enforcement is required.

## Git submodule option

Do not mount the whole ruleset repository directly as `.cursor/rules/quantahub`; the actual rule files live under `plugin/rules`.

Instead:

```text
vendor/quantahubruleset/             <- Git submodule
.cursor/rules/quantahub/             <- generated/synced copy of vendor/quantahubruleset/plugin/rules/
.cursor/agents/                       <- generated/synced copy of vendor/quantahubruleset/plugin/agents/
```

Automate that sync in project bootstrap/CI if this fallback is used.

## Context strategy

Always-applied constitutional rules are intentionally small:
- master governance,
- CTFd boundaries,
- control/lab trust boundary,
- agent orchestration,
- definition of done.

Specialist rules are contextual and selected when their descriptions match the work.

## Enforcement model

Rules guide the model. Hooks add preventive guardrails for selected high-confidence dangerous shell operations. JSON Schema and CI provide machine validation. Runtime/application security controls remain authoritative and must not depend on agent compliance alone.

## Hard rule

Never assume "the Agent read the GitHub repository" unless the policy plugin or project-local components are actually installed.
