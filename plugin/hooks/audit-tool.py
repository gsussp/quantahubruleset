#!/usr/bin/env python3
import json, sys
try:
    event = json.load(sys.stdin)
except Exception:
    event = {}
# Non-blocking hook. Project CI/tests remain the real enforcement boundary.
print(json.dumps({"permission":"allow"}))
