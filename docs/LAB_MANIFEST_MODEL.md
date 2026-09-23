# Lab Manifest Model

A QuantaHub published lab version should eventually encode at least:

```yaml
id: string
name: string
version: string
source:
  repository: string
  commit_or_digest: string
  license: string
  attribution: string
runtime:
  class: container|sandboxed-container|microvm|full-vm
  provider: string
topology:
  services: []
resources:
  profile: string
network:
  ingress: []
  egress_policy: deny|named-policy
lifecycle:
  ttl_seconds: integer
  reset_supported: boolean
health:
  checks: []
access:
  web: []
  terminal: boolean
```

Production runner artifacts are approved/versioned artifacts, not arbitrary upstream checkout state.
