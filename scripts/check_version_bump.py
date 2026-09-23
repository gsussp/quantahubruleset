#!/usr/bin/env python3
import os
import subprocess
import sys

def git(*args):
    return subprocess.check_output(["git", *args], text=True).strip()

base_ref = os.environ.get("GITHUB_BASE_REF", "").strip()

try:
    if base_ref:
        base = f"origin/{base_ref}"
        git("rev-parse", "--verify", base)
    else:
        base = "HEAD^"
        git("rev-parse", "--verify", base)
except subprocess.CalledProcessError:
    print("VERSION BUMP CHECK SKIPPED: no comparison base available")
    sys.exit(0)

changed = [p for p in git("diff", "--name-only", f"{base}...HEAD").splitlines() if p]

if not changed:
    print("VERSION BUMP CHECK PASSED: no changes")
    sys.exit(0)

governed = [
    p for p in changed
    if p not in {"VERSION", "CHANGELOG.md"}
]

if not governed:
    print("VERSION BUMP CHECK PASSED: only VERSION/CHANGELOG changed")
    sys.exit(0)

try:
    old_version = git("show", f"{base}:VERSION").strip()
except subprocess.CalledProcessError:
    old_version = ""

new_version = open("VERSION", "r", encoding="utf-8").read().strip()

if not old_version:
    print(f"VERSION BUMP CHECK PASSED: VERSION introduced as {new_version}")
    sys.exit(0)

if old_version == new_version:
    print("VERSION BUMP CHECK FAILED")
    print("Governed files changed but VERSION did not change.")
    for path in governed:
        print("-", path)
    sys.exit(1)

print(f"VERSION BUMP CHECK PASSED: {old_version} -> {new_version}")
