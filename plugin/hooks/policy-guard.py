#!/usr/bin/env python3
import json
import re
import sys

try:
    event = json.load(sys.stdin)
except Exception:
    print(json.dumps({
        "permission": "deny",
        "user_message": "QuantaHub policy guard could not parse hook input.",
        "agent_message": "Policy guard parse failure; do not bypass it."
    }))
    sys.exit(0)

command = str(event.get("command", ""))

hard_denies = [
    (r"(^|\s)--privileged(\s|$|=)", "Privileged container execution is forbidden."),
    (r"(^|\s)--network(?:=|\s+)host(\s|$)", "Host networking is forbidden for lab workloads."),
    (r"hostNetwork\s*[:=]\s*true", "hostNetwork=true is forbidden for lab workloads."),
    (r"hostPID\s*[:=]\s*true", "hostPID=true is forbidden for lab workloads."),
    (r"hostIPC\s*[:=]\s*true", "hostIPC=true is forbidden for lab workloads."),
    (r"/var/run/docker\.sock", "Docker socket access/mounts are forbidden for lab workloads."),
    (r"/run/containerd/containerd\.sock", "Container runtime socket access/mounts are forbidden."),
]

for pattern, reason in hard_denies:
    if re.search(pattern, command, re.IGNORECASE):
        print(json.dumps({
            "permission": "deny",
            "user_message": reason,
            "agent_message": reason + " Use an isolated runtime/provider path consistent with QuantaHub policy."
        }))
        sys.exit(0)

print(json.dumps({"permission": "allow"}))
