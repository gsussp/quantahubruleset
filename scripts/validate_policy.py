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

for p in required_json:
    if not p.exists():
        errors.append(f"missing required file: {p}")
    else:
        load_json(p)

required_rules = {
    "00-master-governance.mdc",
    "01-ctfd-boundaries.mdc",
    "02-control-data-plane.mdc",
    "09-agent-orchestration.mdc",
    "10-verification.mdc",
}
rules_dir = ROOT / "plugin" / "rules"
if rules_dir.exists():
    present = {p.name for p in rules_dir.glob("*.mdc")}
    missing = sorted(required_rules - present)
    if missing:
        errors.append("missing required rules: " + ", ".join(missing))
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

always_allowed = {
    "00-master-governance.mdc",
    "01-ctfd-boundaries.mdc",
    "02-control-data-plane.mdc",
    "09-agent-orchestration.mdc",
    "10-verification.mdc",
}

for p in rules_dir.glob("*.mdc"):
    text = p.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{p}: missing frontmatter")
    if "description:" not in text:
        errors.append(f"{p}: missing description")
    if "alwaysApply:" not in text:
        errors.append(f"{p}: missing alwaysApply")
    if "alwaysApply: true" in text and p.name not in always_allowed:
        errors.append(f"{p}: should be contextual, not alwaysApply=true")

required_docs = [
    "DECISIONS.md",
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

if not (ROOT / "LICENSE").exists():
    errors.append("missing LICENSE")

if errors:
    print("POLICY VALIDATION FAILED")
    for e in errors:
        print("-", e)
    sys.exit(1)

print("POLICY VALIDATION PASSED")
