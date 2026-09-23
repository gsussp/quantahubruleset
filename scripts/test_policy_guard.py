#!/usr/bin/env python3
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
GUARD = ROOT / "plugin" / "hooks" / "policy-guard.py"

cases = [
    ("docker run --rm nginx:latest", "allow"),
    ("docker run --privileged alpine", "deny"),
    ("docker run --network host alpine", "deny"),
    ("docker run -v /var/run/docker.sock:/var/run/docker.sock alpine", "deny"),
    ("kubectl apply -f deployment.yaml", "allow"),
]

failed = False
for command, expected in cases:
    proc = subprocess.run(
        [sys.executable, str(GUARD)],
        input=json.dumps({"command": command}),
        text=True,
        capture_output=True,
        check=True,
    )
    result = json.loads(proc.stdout)
    actual = result.get("permission")
    if actual != expected:
        failed = True
        print(f"FAIL: {command!r}: expected {expected}, got {actual}")
    else:
        print(f"PASS: {command!r}: {actual}")

if failed:
    sys.exit(1)
