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

for p in [
    ROOT / ".cursor-plugin" / "marketplace.json",
    ROOT / "plugin" / ".cursor-plugin" / "plugin.json",
    ROOT / "plugin" / "hooks" / "hooks.json",
    ROOT / "schemas" / "lab-manifest.schema.json",
]:
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

agents = {"platform.md","lab-engine.md","security.md","frontend.md","verifier.md"}
agents_dir = ROOT / "plugin" / "agents"
if agents_dir.exists():
    present_agents = {p.name for p in agents_dir.glob("*.md")}
    missing = sorted(agents - present_agents)
    if missing:
        errors.append("missing required specialist agents: " + ", ".join(missing))
else:
    errors.append("missing plugin/agents")

for p in rules_dir.glob("*.mdc"):
    text = p.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{p}: missing frontmatter")
    if "description:" not in text:
        errors.append(f"{p}: missing description")
    if "alwaysApply:" not in text:
        errors.append(f"{p}: missing alwaysApply")

if errors:
    print("POLICY VALIDATION FAILED")
    for e in errors:
        print("-", e)
    sys.exit(1)

print("POLICY VALIDATION PASSED")
