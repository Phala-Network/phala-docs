# Documentation Baseline Report — PR #162 (confidential-ai-doc)

Generated: 2026-06-19
Branch: confidential-ai-doc
Scope: 56 changed files (new Confidential AI docs + dstack-cloud section)

## Health Summary

| Health     | Count | Percentage |
|------------|-------|------------|
| good       | 51    | 91%        |
| fair       | 4     | 7%         |
| needs work | 1     | 2%         |

## Broken Links

None found.

## Orphaned Files

None — all pages present in docs.json navigation.

## Terminology Issues

| Term | Variants Found | Files | Status |
|------|---------------|-------|--------|
| E2EE | Unexpanded in 4 files | 7 | Needs first-use expansion |
| TCB | Unexpanded in 4 files | 5 | Needs first-use expansion |
| RA-TLS | Unexpanded in 7 files | 8 | Needs first-use expansion |
| Remote Attestation / TEE Attestation | Mixed usage in 2 files | 5 | Needs decision |
| on-chain KMS | 1 lowercase vs 6 title-case | 6 | Needs standardization |
| docker-compose (prose) | 2 prose instances use hyphenated form | 15 | Should be "Docker Compose" |
| Dstack-TEE | GitHub org name, not a casing error | 7 | No action |
| Confidential AI | Consistently title case | 15+ | Clean |
| channel binding | Title case in headings only | 5 | Clean |
| GCP / Google Cloud | GCP dominates, 2 natural prose uses of Google Cloud | 14 | Clean |

## Structural Issues

### Heading skip (1)

- `confidential-model/confidential-ai-api.mdx:135` — h2 `## Available Models` then h4 `#### Phala Models`, skips h3

### Code blocks without language tag (9)

| File | Content |
|------|---------|
| `dstack-cloud/attestation-integration.mdx:59` | Pseudocode — needs `text` or `python` |
| `dstack-cloud/register-enclave-measurement.mdx:72` | PCR hash output — needs `text` |
| `confidential-model/images-and-vision.mdx:47` | LLM output — needs `text` |
| `confidential-model/streaming.mdx:66` | Output — needs `text` |
| `getting-started/deploy-first-cvm.mdx:200` | URL template — needs `text` |
| `networking/expose-http-service.mdx:42` | URL template — needs `text` |
| `networking/quickstart.mdx:30` | URL template — needs `text` |
| `troubleshooting/troubleshooting.mdx:73` | Error output — needs `text` |
| `troubleshooting/troubleshooting.mdx:96` | Error output — needs `text` |

### Long paragraphs (>5 sentences) — 24 instances across 17 files

Worst offenders (8+ sentences):

- `confidential-model/api-reference/receipts.mdx:84` — 13 sentences
- `confidential-model/api-reference/attestation.mdx:120` — 12 sentences
- `confidential-model/tcb-and-claims.mdx:60` — 10 sentences
- `dstack-cloud/upgrade.mdx:184` — 9 sentences
- `dstack-cloud/nitro-enclave.mdx:21` — 8 sentences
- `dstack-cloud/governance.mdx:98` — 8 sentences
- `dstack-cloud/runbook.mdx:216` — 8 sentences
- `dstack-cloud/register-enclave-measurement.mdx:100` — 8 sentences
- `confidential-model/playground.mdx:24` — 8 sentences
- `confidential-model/receipts-and-sessions.mdx:31` — 8 sentences
- `confidential-model/channel-binding.mdx:32` — 8 sentences
- `verify/verify-attestation.mdx:74` — 8 sentences

### "There is/are" openers (2)

- `dstack-cloud/register-enclave-measurement.mdx:14`
- `dstack-cloud/run-on-nitro.mdx:6`

## Per-File Detail

| File | Type | Lines | Words | Issues | Health |
|------|------|-------|-------|--------|--------|
| dstack-cloud/code-walkthrough.mdx | how-to | 133 | 399 | 6 | needs work |
| dstack-cloud/governance.mdx | how-to | 142 | 916 | 3 | fair |
| dstack-cloud/manage-governance.mdx | explanation | 165 | 932 | 3 | fair |
| dstack-cloud/register-enclave-measurement.mdx | tutorial | 207 | 922 | 3 | fair |
| dstack-cloud/runbook.mdx | how-to | 267 | 1062 | 3 | fair |
| (remaining 51 files) | — | — | — | 0-2 | good |
