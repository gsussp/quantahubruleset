#!/usr/bin/env python3
from pathlib import Path
import json
import os
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
HOOK = ROOT / "plugin" / "hooks" / "remote-policy-check.py"

def run_with_version(version):
    with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as f:
        f.write(version + "\n")
        temp_path = Path(f.name)
    try:
        env = os.environ.copy()
        env["QUANTAHUB_POLICY_VERSION_URL"] = temp_path.as_uri()
        proc = subprocess.run(
            [sys.executable, str(HOOK)],
            input=json.dumps({"prompt": "test", "attachments": []}),
            text=True,
            capture_output=True,
            env=env,
            check=True,
        )
        return json.loads(proc.stdout)
    finally:
        temp_path.unlink(missing_ok=True)

same = run_with_version("0.3.0")
if same.get("continue") is not True:
    print("FAIL: matching remote version should allow prompt")
    sys.exit(1)

stale = run_with_version("9.9.9")
if stale.get("continue") is not False:
    print("FAIL: mismatched remote version should block prompt")
    sys.exit(1)

print("REMOTE POLICY CHECK TESTS PASSED")
