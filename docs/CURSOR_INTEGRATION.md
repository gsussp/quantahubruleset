# Cursor Integration

## Goal

Use this repository as persistent engineering policy instead of repeating prompts for every Cursor task.

## Best model: Cursor Plugin

This repository is prepared as a Cursor plugin/marketplace source. Install the plugin at project scope so QuantaHub rules and custom agents are available in the project.

Important: a random external GitHub repository is not automatically read on every Agent turn. It must be installed/imported as a Cursor plugin, or its rules must exist in the project's `.cursor/rules` hierarchy.

## Why rules are split

Cursor rules are persistent prompt context. Small focused rules are easier to apply, update and reason about than one huge master document.

The `00-master-governance.mdc` rule is `alwaysApply: true`. Other fundamental rules are also always-applied where architectural drift would be dangerous. Context-heavy specialist rules can be agent-decided or file-scoped later if token pressure becomes significant.

## Stronger enforcement

Rules guide the model; they are not a cryptographic policy boundary. Hooks can observe/block tool actions and are used as an additional policy layer. Security controls must still be implemented in code, tests, CI and infrastructure.

## Alternative: project-local rules

If plugin import is not desired, copy or sync `plugin/rules/*.mdc` into:

```text
<target-project>/.cursor/rules/quantahub/
```

Cursor supports nested rule folders.

A Git submodule may also be used if you want GitHub to remain canonical:

```text
<target-project>/.cursor/rules/quantahub/  -> rules repository/subtree
```

Keep rule files inside `.cursor/rules` as `.mdc` with valid frontmatter.

## Hard rule

Do not assume that linking to a GitHub URL in a prompt makes it persistent policy. Install/sync the policy into Cursor's supported rule/plugin system.
