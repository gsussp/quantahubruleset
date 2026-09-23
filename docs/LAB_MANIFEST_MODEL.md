# Lab Manifest Model

The canonical machine-readable contract is:

```text
schemas/lab-manifest.schema.json
```

Every published lab version must validate against that schema before entering the approved registry.

## Core fields

```text
id
name
version

source
  repository
  revision
  license
  attribution

runtime
  class
  provider
  privileged=false
  hostNetwork=false
  hostPID=false
  hostIPC=false
  dockerSocket=false

resources
  profile
  cpu
  memoryMb
  pids
  diskMb
  bandwidthKbps

network
  egressPolicy
  ingress
  dnsPolicy

lifecycle
  ttlSeconds
  resetSupported

access
  web
  terminal
  ssh
  rdp
```

The schema is intentionally restrictive. Runtime features that weaken isolation are not accepted as normal manifest options.

See `examples/lab-manifest.example.json` for a valid example.

Production runner artifacts are approved/versioned artifacts, never arbitrary mutable upstream checkout state.
