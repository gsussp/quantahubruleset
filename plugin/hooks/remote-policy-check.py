#!/usr/bin/env python3
import json
import os
import sys
import urllib.request
from pathlib import Path

DEFAULT_REMOTE_VERSION_URL = "https://raw.githubusercontent.com/gsussp/quantahubruleset/main/VERSION"
REMOTE_VERSION_URL = os.environ.get("QUANTAHUB_POLICY_VERSION_URL", DEFAULT_REMOTE_VERSION_URL)
PLUGIN_ROOT = Path(__file__).resolve().parents[1]
PLUGIN_MANIFEST = PLUGIN_ROOT / ".cursor-plugin" / "plugin.json"

def block(message):
    print(json.dumps({"continue": False, "user_message": message}))
    sys.exit(0)

try:
    json.load(sys.stdin)
except Exception:
    block("QuantaHub policy freshness check could not parse Cursor hook input.")

try:
    manifest = json.loads(PLUGIN_MANIFEST.read_text(encoding="utf-8"))
    local_version = str(manifest["version"]).strip()
except Exception:
    block("QuantaHub local policy version is unreadable. Reinstall the policy plugin.")

try:
    req = urllib.request.Request(
        REMOTE_VERSION_URL,
        headers={"User-Agent": "QuantaHub-Cursor-Policy/0.3"}
    )
    with urllib.request.urlopen(req, timeout=4) as response:
        remote_version = response.read().decode("utf-8").strip()
except Exception:
    block(
        "QuantaHub cannot verify the canonical ruleset on GitHub. "
        "Strict policy mode blocks work until the remote policy version can be checked."
    )

if not remote_version:
    block("QuantaHub canonical VERSION is empty. Work is blocked.")

if local_version != remote_version:
    block(
        f"QuantaHub policy is stale or mismatched. Local={local_version}, "
        f"canonical={remote_version}. Update/reinstall the QuantaHub policy plugin before continuing."
    )

print(json.dumps({"continue": True}))
