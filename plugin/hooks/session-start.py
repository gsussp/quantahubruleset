#!/usr/bin/env python3
import json
import sys

try:
    json.load(sys.stdin)
except Exception:
    pass

print(json.dumps({
    "additional_context": (
        "QuantaHub deterministic policy pack v0.3 is active. All QuantaHub rules are "
        "Always Apply. The Cursor main Agent is Master/Orchestrator. Do not ask the "
        "user to choose between equivalent technical approaches when DECISION_POLICY.md "
        "provides a default. Use specialist agents automatically. Security-sensitive "
        "changes require quanta-security review and meaningful implementation requires "
        "quanta-verifier evidence."
    )
}))
