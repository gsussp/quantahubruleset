# Remote Policy Sync

## Goal

Every Cursor prompt must verify that the locally installed QuantaHub policy pack matches the canonical GitHub `main` policy version.

Canonical source:

```text
https://github.com/gsussp/quantahubruleset
```

Version authority:

```text
https://raw.githubusercontent.com/gsussp/quantahubruleset/main/VERSION
```

## Strict behavior

Before every submitted prompt:

1. read the local plugin VERSION,
2. fetch canonical remote VERSION,
3. compare exact versions,
4. allow only when equal.

If:
- remote version is newer,
- versions differ,
- remote version cannot be checked,
- local VERSION is missing,

the prompt is blocked.

This is intentional strict mode. Cursor must not continue using a stale or unverifiable policy pack.

## Why rules are not downloaded on every prompt

The remote check proves freshness. The installed plugin contains the reviewed rule/hook code. Automatically downloading and executing mutable remote code on every prompt would create an avoidable supply-chain risk.

Update the installed plugin, verify CI, then continue.
