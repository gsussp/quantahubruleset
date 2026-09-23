# QuantaHub Security Model

## Threat model

Users are expected to execute exploit payloads inside labs. Lab targets are intentionally vulnerable. Treat every lab session as potentially fully compromised.

Primary risks:
- container/VM escape,
- cross-tenant access,
- pivot from lab network into control plane,
- browser-origin/cookie abuse,
- Internet abuse from labs,
- resource exhaustion,
- runtime-management compromise,
- supply-chain compromise in imported labs,
- secrets leakage,
- gateway authorization bypass,
- stale/orphaned lab infrastructure.

## Mandatory controls

### Isolation

Each session receives an isolated network boundary. Session A must not communicate with Session B unless a specific shared scenario explicitly allows it.

Lab networks must not reach:
- PostgreSQL,
- Redis/Valkey,
- CTFd internal/admin networks,
- orchestration management interfaces,
- runner management plane,
- host/cloud metadata services,
- other sessions.

### Browser-origin isolation

Production platform/authentication origins and vulnerable lab web origins use different registrable domains. Authentication cookies are never scoped to the vulnerable lab domain.

Example:
- platform: `app.quantahub.example`
- labs: `*.quantahub-labs.example`

### Egress

Default deny for IPv4 and IPv6. External access requires a named policy and minimum necessary destinations/protocols. DNS, metadata and link-local access follow the canonical network policy.

### Runtime

Avoid privileged containers. Avoid host PID/IPC/network modes. Never mount Docker/container-runtime sockets into a lab. Do not mount sensitive host paths. Drop Linux capabilities by default and add only what a lab requires. Apply cgroup/resource controls and relevant seccomp/AppArmor/LSM policies.

Rootless runtime can reduce blast radius but is not a substitute for layered isolation.

### Runtime classes

- container: lower-risk web workloads,
- sandboxed container: meaningful user code execution,
- microVM/full VM: stronger isolation and higher-risk workloads.

### Resource controls

Every lab receives CPU, memory, PID, disk/IO and bandwidth policies. A fork bomb or memory allocator must not destabilize the runner fleet.

### Runner management

Do not expose unauthenticated Docker/runtime APIs or management ports. Orchestrator-to-runner communication must be authenticated. Prefer per-runner identity/certificates and outbound-established management connections where practical.

### Gateway

Use short-lived session-aware access tokens. Validate user/session ownership on every connection establishment. Do not trust hostname alone as authorization.

### Supply chain

Do not run arbitrary upstream HEAD in production. Pin commits/digests, review licenses, scan/build/test, generate SBOM/signing evidence when feasible, and publish only approved artifacts.

### Secrets

No production secrets in repository. Keep database credentials, signing keys, registry credentials and runner identities in a secret-management abstraction.

### Admin and authorization

Require MFA or equivalent strong controls for high-impact administration, short-lived sessions, explicit server-side authorization, tenant scoping and audit records. Follow `AUTHORIZATION_MODEL.md`.

### Abuse controls

Public cyber-range operation follows `ABUSE_AND_ACCEPTABLE_USE.md`: quotas, TTL, rate limits, suspension, monitoring and emergency controls.

### Emergency controls

Support global lab creation disable, token revocation, runner drain and controlled termination of active sessions.

## Logging principles

Separate operational telemetry from learner activity. Do not centrally collect full user terminal command history by default unless a defined training/security requirement exists and the policy is communicated.

## Security review rule

Any change touching runtime, networking, browser origins, gateway auth, secrets, authorization, abuse controls, supply chain, privileges, filesystem mounts or runner orchestration requires quanta-security review before completion.
