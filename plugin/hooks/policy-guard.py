#!/usr/bin/env python3
import json
import re
import sys

try:
    event = json.load(sys.stdin)
except Exception:
    event = {}

payload = json.dumps(event, ensure_ascii=False)
text = payload.lower()

hard_denies = [
    (r"--privileged\b", "Privileged container execution is forbidden by QuantaHub policy."),
    (r"--network[= ]host\b", "Host networking is forbidden for lab workloads."),
    (r"hostnetwork\s*[:=]\s*true", "hostNetwork=true is forbidden for lab workloads."),
    (r"hostpid\s*[:=]\s*true", "hostPID=true is forbidden for lab workloads."),
    (r"hostipc\s*[:=]\s*true", "hostIPC=true is forbidden for lab workloads."),
    (r"/var/run/docker\.sock", "Mounting the Docker socket into workloads is forbidden."),
    (r"docker\.sock", "Docker socket access is forbidden for lab workloads."),
    (r"/run/containerd/containerd\.sock", "Container runtime socket access is forbidden."),
]

for pattern, reason in hard_denies:
    if re.search(pattern, text, re.IGNORECASE):
        print(json.dumps({
            "permission": "deny",
            "reason": reason
        }))
        sys.exit(0)

print(json.dumps({"permission": "allow"}))
