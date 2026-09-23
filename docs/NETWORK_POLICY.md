# Network Policy

## Zones

- Public/Edge
- Control Plane
- Management Plane
- Runner Management
- Per-session Lab Networks

## Default policy

All lab-session traffic is deny-by-default except explicit topology requirements.

## Lab egress

Default:
- IPv4 Internet: deny
- IPv6 Internet: deny
- RFC1918/control/management ranges: deny
- link-local/metadata ranges: deny
- other lab-session networks: deny

Named egress policies may allow only the destinations/protocols needed by a specific lab.

## DNS

Labs use a controlled DNS path. Public recursive resolvers are not automatically reachable. DNS egress must not bypass general network policy.

## Metadata and host services

Explicitly block cloud metadata/link-local and host management services, including provider-specific metadata endpoints where applicable.

## Ingress

Users connect through Lab Gateway/brokers. Runners do not publish arbitrary lab ports directly to the public Internet.

## Browser-origin isolation

Production platform/authentication and intentionally vulnerable web labs use different registrable domains.

Example:
- platform: `app.quantahub.example`
- labs: `*.quantahub-labs.example`

Do not share authentication cookies with the lab registrable domain.

## Session isolation

Session A cannot reach Session B unless a documented multiplayer lab explicitly requires shared topology. Shared scenarios require a distinct manifest/security profile.

## Verification

Network policy tests must prove prohibited traffic fails, including IPv6 when enabled on the host/runtime.
