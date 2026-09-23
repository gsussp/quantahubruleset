#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        errors.append(f"{path}: invalid JSON: {e}")
        return None

required_json = [
    ROOT / ".cursor-plugin" / "marketplace.json",
    ROOT / "plugin" / ".cursor-plugin" / "plugin.json",
    ROOT / "plugin" / "hooks" / "hooks.json",
    ROOT / "schemas" / "lab-manifest.schema.json",
    ROOT / "examples" / "lab-manifest.example.json",
]

loaded = {}
for p in required_json:
    if not p.exists():
        errors.append(f"missing required file: {p}")
    else:
        loaded[p] = load_json(p)

version_path = ROOT / "VERSION"
if not version_path.exists():
    errors.append("missing VERSION")
    version = None
else:
    version = version_path.read_text(encoding="utf-8").strip()

plugin_manifest = loaded.get(ROOT / "plugin" / ".cursor-plugin" / "plugin.json")
marketplace = loaded.get(ROOT / ".cursor-plugin" / "marketplace.json")
hooks = loaded.get(ROOT / "plugin" / "hooks" / "hooks.json")

if version and plugin_manifest and str(plugin_manifest.get("version")) != version:
    errors.append("plugin version does not match VERSION")

if version and marketplace:
    market_version = str(marketplace.get("metadata", {}).get("version", ""))
    if market_version != version:
        errors.append("marketplace version does not match VERSION")

if hooks:
    hook_map = hooks.get("hooks", {})
    if "beforeSubmitPrompt" not in hook_map:
        errors.append("beforeSubmitPrompt remote policy freshness hook is required")
    if "beforeShellExecution" not in hook_map:
        errors.append("beforeShellExecution policy guard is required")

expected_rules = {
    "00-master-governance.mdc",
    "01-ctfd-boundaries.mdc",
    "02-control-data-plane.mdc",
    "03-lab-engine.mdc",
    "04-runtime-isolation.mdc",
    "05-network-security.mdc",
    "06-open-source-lab-supply-chain.mdc",
    "07-data-state.mdc",
    "08-security-secrets-admin.mdc",
    "09-agent-orchestration.mdc",
    "10-verification.mdc",
    "11-git-change-management.mdc",
    "12-learning-product.mdc",
}

rules_dir = ROOT / "plugin" / "rules"
if rules_dir.exists():
    present = {p.name for p in rules_dir.glob("*.mdc")}
    missing = sorted(expected_rules - present)
    unexpected = sorted(present - expected_rules)
    if missing:
        errors.append("missing required rules: " + ", ".join(missing))
    if unexpected:
        errors.append("unexpected rules: " + ", ".join(unexpected))
else:
    errors.append("missing plugin/rules")

expected_agents = {"platform.md","lab-engine.md","security.md","frontend.md","verifier.md"}
agents_dir = ROOT / "plugin" / "agents"
if agents_dir.exists():
    present_agents = {p.name for p in agents_dir.glob("*.md")}
    missing = sorted(expected_agents - present_agents)
    unexpected = sorted(present_agents - expected_agents)
    if missing:
        errors.append("missing required specialist agents: " + ", ".join(missing))
    if unexpected:
        errors.append("unexpected specialist agents: " + ", ".join(unexpected))
else:
    errors.append("missing plugin/agents")

if rules_dir.exists():
    for p in rules_dir.glob("*.mdc"):
        text = p.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"{p}: missing frontmatter")
        if "description:" not in text:
            errors.append(f"{p}: missing description")
        if "alwaysApply: true" not in text:
            errors.append(f"{p}: every QuantaHub rule must be alwaysApply=true in deterministic mode")
        if "alwaysApply: false" in text:
            errors.append(f"{p}: contextual rules are forbidden in deterministic mode")

required_docs = [
    "DECISIONS.md",
    "DECISION_POLICY.md",
    "REMOTE_POLICY_SYNC.md",
    "SYSTEM_ARCHITECTURE.md",
    "SECURITY_MODEL.md",
    "API_CONTRACTS.md",
    "AUTHORIZATION_MODEL.md",
    "NETWORK_POLICY.md",
    "ABUSE_AND_ACCEPTABLE_USE.md",
    "BACKUP_RECOVERY.md",
    "RELEASE_POLICY.md",
    "UPSTREAM_DEPENDENCIES.md",
    "AGENT_ORCHESTRATION.md",
    "CURSOR_INTEGRATION.md",
]
for name in required_docs:
    if not (ROOT / "docs" / name).exists():
        errors.append(f"missing required document: docs/{name}")

for path in [
    ROOT / "plugin" / "hooks" / "policy-guard.py",
    ROOT / "plugin" / "hooks" / "remote-policy-check.py",
    ROOT / "plugin" / "hooks" / "session-start.py",
    ROOT / "scripts" / "test_policy_guard.py",
    ROOT / "scripts" / "test_remote_policy_check.py",
]:
    if not path.exists():
        errors.append(f"missing required enforcement file: {path}")

if not (ROOT / "LICENSE").exists():
    errors.append("missing LICENSE")

if errors:
    print("POLICY VALIDATION FAILED")
    for e in errors:
        print("-", e)
    sys.exit(1)

print(f"POLICY VALIDATION PASSED v{version}")
