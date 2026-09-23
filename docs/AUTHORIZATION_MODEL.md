# Authorization and Tenant Model

## Roles

Minimum roles:
- USER
- INSTRUCTOR
- ORG_ADMIN
- CONTENT_EDITOR
- PLATFORM_ADMIN

## Tenant scope

Every organization-owned object includes a tenant/organization scope. Authorization checks must evaluate both role and resource scope.

## Minimum permission model

### USER
- read assigned/public learning content,
- create/manage own allowed lab sessions,
- submit own answers/flags,
- read own progress.

### INSTRUCTOR
- USER permissions,
- read learner progress within assigned organization/cohorts,
- assign supported learning content,
- manage course-facing settings permitted by organization policy.

### ORG_ADMIN
- manage organization membership/roles within organization,
- manage organization-level training configuration,
- read organization reports.

### CONTENT_EDITOR
- create/edit/publish learning content subject to publication workflow,
- cannot gain infrastructure/runtime privileges from content permissions.

### PLATFORM_ADMIN
- platform-wide administration,
- subject to MFA, short sessions, audit and least privilege.

## Non-negotiable rules

- Client-side UI hiding is not authorization.
- Every privileged API action performs server-side authorization.
- Tenant ID supplied by a client is untrusted input.
- Cross-tenant reads/writes are denied by default.
- Platform administrators do not automatically receive lab-runtime shell access.
- Service identities have separate permissions from human roles.
- Sensitive role changes create audit events.

## Testing

Verifier must include negative tests for cross-tenant access and privilege escalation for any authorization-sensitive change.
