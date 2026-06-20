# Phala Docs Scripts

## Precommit checks

```bash
# Check historical links are not broken
python3 .scripts/check_links.py
# Check if all the redirects are handled properly
python3 .scripts/validate-redirects.py
```

When a new page is added, we should always update used\_links to include it.

## RedPill docs-v2 sync

```bash
.scripts/check-redpill-confidential-ai-sync.sh
```

Checks the local `../redpill-docs-v2` clone against the pinned upstream commit in `.scripts/redpill-docs-v2.pin`, clones the repo if missing, and writes a drift report to `tmp/redpill-confidential-ai-sync.md`.

When RedPill docs change:

1. Review the report and update Phala docs with the same content semantics.
2. Preserve Phala structure and replace RedPill API URLs with `https://inference.phala.com/v1`.
3. Run `.scripts/check-redpill-confidential-ai-sync.sh --update-pin` after the Phala docs are updated.
