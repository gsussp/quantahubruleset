# Public Cyber-Range Abuse Controls

## Principle

QuantaHub intentionally gives users offensive tooling inside controlled training environments. Infrastructure must prevent the platform from becoming an attack relay, scanning service, malware distribution point or resource-abuse platform.

## Baseline controls

- default-deny lab Internet egress,
- per-user and per-organization concurrent session limits,
- resource quotas per lab profile,
- session TTL and idle timeout,
- rate limiting for session creation/reset,
- account and organization suspension capability,
- abuse/audit event trail for infrastructure actions,
- emergency global lab-disable and runner-drain controls.

## High-risk content

Malware, kernel exploitation and similar high-risk labs require stronger isolation class and explicit publication review. Public-facing malware samples must not be made downloadable outside the intended isolated workflow without a specific policy decision.

## Detection

Operational monitoring should surface:
- repeated blocked egress attempts,
- unusual session-creation volume,
- runner resource exhaustion,
- gateway authorization failures,
- cross-session probing,
- attempts to access management metadata/services.

## Privacy

Abuse monitoring should minimize learner-content collection. Do not default to storing full terminal histories when lower-level infrastructure signals are sufficient.

## Response

Define operational procedures for:
1. suspend new sessions,
2. isolate/drain affected runners,
3. revoke session tokens,
4. preserve necessary audit evidence,
5. restore clean capacity,
6. review root cause before re-enabling.
