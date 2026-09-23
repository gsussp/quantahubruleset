#!/usr/bin/env python3
import json, sys
try:
    _ = json.load(sys.stdin)
except Exception:
    _ = {}
print(json.dumps({
    "additional_context": "QuantaHub policy pack is active. Treat installed QuantaHub always-apply rules as canonical architecture/security constraints. Delegate security-sensitive work for security review and do not report implementation complete without verification."
}))
