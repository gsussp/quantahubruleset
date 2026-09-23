#!/usr/bin/env python3
from pathlib import Path
import json
import sys
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "lab-manifest.schema.json"

if len(sys.argv) != 2:
    print("usage: validate_lab_manifest.py <manifest.json>")
    sys.exit(2)

manifest_path = Path(sys.argv[1])
schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

validator = Draft202012Validator(schema)
errors = sorted(validator.iter_errors(manifest), key=lambda e: list(e.absolute_path))

if errors:
    print("LAB MANIFEST INVALID")
    for e in errors:
        where = ".".join(str(x) for x in e.absolute_path) or "<root>"
        print(f"- {where}: {e.message}")
    sys.exit(1)

print("LAB MANIFEST VALID")
