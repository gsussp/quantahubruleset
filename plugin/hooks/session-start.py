#!/usr/bin/env python3
import json
import sys

try:
    json.load(sys.stdin)
except Exception:
    pass

print(json.dumps({
    "additional_context": (
        "QuantaHub policy pack v0.2 is active. The current Cursor main Agent is the "
        "Master/Orchestrator. Treat always-applied QuantaHub rules as canonical. "
        "Use the five specialist subagents proactively by ownership boundary. "
        "Security-sensitive changes require quanta-security review and meaningful "
        "implementation requires quanta-verifier evidence before completion."
    )
}))
