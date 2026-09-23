# Backup and Recovery Policy

## Scope

Durable state includes at minimum:
- PostgreSQL business/session metadata,
- content/version metadata not otherwise reproducible from Git,
- organization/user/progress state,
- signing/configuration metadata required for service recovery.

Disposable lab runtime state is not treated as durable backup data unless a product feature explicitly requires snapshots.

## Principles

- Backups are encrypted.
- Backup credentials are separate from normal application credentials.
- Restore procedures are tested, not merely documented.
- Database schema migrations include rollback/recovery consideration.
- Secret material follows the secret-management recovery process and is not embedded in database dumps without deliberate design.

## Initial targets

Before production, define explicit:
- RPO,
- RTO,
- backup frequency,
- retention,
- restore-test cadence.

Do not invent production guarantees before these values are operationally tested.

## Recovery order

Typical recovery dependency order:
1. secrets/service identity,
2. PostgreSQL,
3. cache/queue as reconstructable,
4. Platform Core/CTFd,
5. Orchestrator,
6. Gateways,
7. Runner fleet.

Runner/lab capacity can be rebuilt from approved registry artifacts and manifests.
