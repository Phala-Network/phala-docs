#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE_REPO="${REDPILL_DOCS_V2_REPO:-"$ROOT/../redpill-docs-v2"}"
PIN_FILE="$ROOT/.scripts/redpill-docs-v2.pin"
REPORT_FILE="${REDPILL_SYNC_REPORT:-"$ROOT/tmp/redpill-confidential-ai-sync.md"}"
REMOTE_URL="${REDPILL_DOCS_V2_URL:-https://github.com/redpill-ai/redpill-docs-v2}"
UPDATE_PIN=0
FAIL_ON_CHANGE=1

usage() {
  cat <<'EOF'
Usage: .scripts/check-redpill-confidential-ai-sync.sh [options]

Checks whether Phala Confidential AI docs are synced to the pinned RedPill docs-v2 commit.

Options:
  --update-pin       Write the latest fetched RedPill origin/main commit to .scripts/redpill-docs-v2.pin.
                    Use this only after Phala docs have been updated and reviewed.
  --no-fail          Report drift but exit 0.
  --source PATH      Use a specific local redpill-docs-v2 clone.
  --report PATH      Write the markdown drift report to PATH.
  -h, --help         Show this help.

Environment:
  REDPILL_DOCS_V2_REPO    Local clone path. Defaults to ../redpill-docs-v2.
  REDPILL_DOCS_V2_URL     Clone URL. Defaults to https://github.com/redpill-ai/redpill-docs-v2.
  REDPILL_SYNC_REPORT     Report path. Defaults to tmp/redpill-confidential-ai-sync.md.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --update-pin)
      UPDATE_PIN=1
      shift
      ;;
    --no-fail)
      FAIL_ON_CHANGE=0
      shift
      ;;
    --source)
      SOURCE_REPO="$2"
      shift 2
      ;;
    --report)
      REPORT_FILE="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [[ ! -d "$SOURCE_REPO/.git" ]]; then
  echo "Missing RedPill docs-v2 clone: $SOURCE_REPO"
  echo "Cloning $REMOTE_URL ..."
  git clone "$REMOTE_URL" "$SOURCE_REPO" --quiet
fi

git -C "$SOURCE_REPO" fetch origin main --quiet

PINNED="$(tr -d '[:space:]' < "$PIN_FILE")"
REMOTE="$(git -C "$SOURCE_REPO" rev-parse origin/main)"
mkdir -p "$(dirname "$REPORT_FILE")"

echo "Pinned RedPill docs-v2 commit: $PINNED"
echo "Remote RedPill docs-v2 commit: $REMOTE"

if [[ "$PINNED" == "$REMOTE" ]]; then
  echo "Phala Confidential AI docs are pinned to the latest fetched RedPill docs-v2 main."
  cat > "$REPORT_FILE" <<EOF
# RedPill Confidential AI Sync

Status: synced

- Pinned: \`$PINNED\`
- Remote: \`$REMOTE\`
EOF
  exit 0
fi

map_target() {
  case "$1" in
    get-started/introduction.mdx|get-started/quickstart.mdx)
      echo "phala-cloud/confidential-ai/overview.mdx; phala-cloud/confidential-ai/confidential-model/confidential-ai-api.mdx"
      ;;
    get-started/models.mdx|api-reference/models.mdx)
      echo "phala-cloud/confidential-ai/confidential-model/api-reference/models.mdx"
      ;;
    get-started/authentication.mdx)
      echo "phala-cloud/confidential-ai/confidential-model/confidential-ai-api.mdx"
      ;;
    confidential-ai/how-it-works.mdx)
      echo "phala-cloud/confidential-ai/overview.mdx"
      ;;
    confidential-ai/attestation-report.mdx|api-reference/attestation.mdx|api-reference/attestation-report.mdx)
      echo "phala-cloud/confidential-ai/confidential-model/api-reference/attestation.mdx; phala-cloud/confidential-ai/verify/verify-attestation.mdx"
      ;;
    confidential-ai/receipts.mdx|api-reference/receipts.mdx)
      echo "phala-cloud/confidential-ai/confidential-model/receipts-and-sessions.mdx; phala-cloud/confidential-ai/confidential-model/api-reference/receipts.mdx; phala-cloud/confidential-ai/verify/verify-signature.mdx"
      ;;
    confidential-ai/attested-sessions.mdx|api-reference/sessions.mdx)
      echo "phala-cloud/confidential-ai/confidential-model/receipts-and-sessions.mdx; phala-cloud/confidential-ai/confidential-model/api-reference/sessions.mdx"
      ;;
    confidential-ai/channel-binding.mdx)
      echo "phala-cloud/confidential-ai/confidential-model/channel-binding.mdx"
      ;;
    confidential-ai/providers.mdx|confidential-ai/confidential-models.mdx)
      echo "phala-cloud/confidential-ai/confidential-model/providers.mdx; phala-cloud/confidential-ai/confidential-model/api-reference/models.mdx"
      ;;
    confidential-ai/tcb-and-claims.mdx)
      echo "phala-cloud/confidential-ai/confidential-model/tcb-and-claims.mdx"
      ;;
    confidential-ai/trust-boundary.mdx)
      echo "phala-cloud/confidential-ai/confidential-model/trust-boundary.mdx"
      ;;
    confidential-ai/e2e-encryption.mdx|guides/e2ee-encryption.mdx)
      echo "phala-cloud/confidential-ai/confidential-model/e2ee-encryption.mdx"
      ;;
    confidential-ai/compliance.mdx|confidential-ai/open-source.mdx)
      echo "phala-cloud/confidential-ai/confidential-model/compliance-and-open-source.mdx"
      ;;
    confidential-ai/faqs.mdx)
      echo "phala-cloud/confidential-ai/faqs.mdx"
      ;;
    guides/verify-a-response.mdx)
      echo "phala-cloud/confidential-ai/verify/verify-signature.mdx"
      ;;
    guides/error-handling.mdx)
      echo "phala-cloud/confidential-ai/confidential-model/error-handling.mdx"
      ;;
    guides/migration-from-openai.mdx|guides/migration-from-openrouter.mdx|guides/integrations/*)
      echo "phala-cloud/confidential-ai/confidential-model/migration-and-integrations.mdx"
      ;;
    guides/function-calling.mdx)
      echo "phala-cloud/confidential-ai/confidential-model/tool-calling.mdx"
      ;;
    guides/vision.mdx)
      echo "phala-cloud/confidential-ai/confidential-model/images-and-vision.mdx"
      ;;
    guides/streaming.mdx)
      echo "phala-cloud/confidential-ai/confidential-model/streaming.mdx"
      ;;
    api-reference/chat-completions.mdx)
      echo "phala-cloud/confidential-ai/confidential-model/api-reference/chat-completions.mdx"
      ;;
    api-reference/responses.mdx)
      echo "phala-cloud/confidential-ai/confidential-model/api-reference/responses.mdx"
      ;;
    api-reference/messages.mdx)
      echo "phala-cloud/confidential-ai/confidential-model/api-reference/messages.mdx"
      ;;
    api-reference/completions.mdx)
      echo "phala-cloud/confidential-ai/confidential-model/api-reference/completions.mdx"
      ;;
    api-reference/embeddings.mdx)
      echo "phala-cloud/confidential-ai/confidential-model/api-reference/embeddings.mdx"
      ;;
    api-reference/signature.mdx)
      echo "phala-cloud/confidential-ai/confidential-model/api-reference/signature.mdx"
      ;;
    openapi.yaml|docs.json)
      echo "docs.json; phala-cloud/confidential-ai/confidential-model/api-reference/*"
      ;;
    *)
      echo "Manual review required"
      ;;
  esac
}

CHANGES="$(git -C "$SOURCE_REPO" diff --name-status "$PINNED..origin/main" -- \
  get-started \
  guides/verify-a-response.mdx \
  guides/e2ee-encryption.mdx \
  guides/error-handling.mdx \
  guides/function-calling.mdx \
  guides/vision.mdx \
  guides/streaming.mdx \
  guides/migration-from-openai.mdx \
  guides/migration-from-openrouter.mdx \
  guides/integrations \
  api-reference \
  confidential-ai \
  openapi.yaml \
  docs.json)"

{
  echo "# RedPill Confidential AI Sync"
  echo
  echo "Status: out of sync"
  echo
  echo "- Pinned: \`$PINNED\`"
  echo "- Remote: \`$REMOTE\`"
  echo "- Source repo: \`$SOURCE_REPO\`"
  echo
  echo "## Rules"
  echo
  echo "- Preserve Phala docs structure and product framing."
  echo "- Do not directly copy the RedPill navigation or page layout."
  echo "- Replace RedPill API base URL with \`https://inference.phala.com/v1\`."
  echo "- Keep RedPill-specific account, dashboard, support, and brand links out of Phala docs."
  echo "- After reviewing and updating Phala docs, run this script with \`--update-pin\`."
  echo
  echo "## Changed Source Files"
  echo
  if [[ -z "$CHANGES" ]]; then
    echo "No tracked Confidential AI source files changed, but the pinned commit is stale."
  else
    while IFS=$'\t' read -r status file rest; do
      [[ -z "${status:-}" ]] && continue
      target="$(map_target "$file")"
      echo "- \`$status\` \`$file\` -> $target"
    done <<< "$CHANGES"
  fi
  echo
  echo "## Source Diff"
  echo
  echo '```diff'
  git -C "$SOURCE_REPO" diff --stat "$PINNED..origin/main" -- \
    get-started \
    guides/verify-a-response.mdx \
    guides/e2ee-encryption.mdx \
    guides/error-handling.mdx \
    guides/function-calling.mdx \
    guides/vision.mdx \
    guides/streaming.mdx \
    guides/migration-from-openai.mdx \
    guides/migration-from-openrouter.mdx \
    guides/integrations \
    api-reference \
    confidential-ai \
    openapi.yaml \
    docs.json
  echo '```'
} > "$REPORT_FILE"

cat "$REPORT_FILE"

if [[ "$UPDATE_PIN" -eq 1 ]]; then
  printf '%s\n' "$REMOTE" > "$PIN_FILE"
  echo
  echo "Updated $PIN_FILE to $REMOTE."
  exit 0
fi

if [[ "$FAIL_ON_CHANGE" -eq 1 ]]; then
  echo
  echo "RedPill docs-v2 has changed. Update Phala Confidential AI docs, then run:"
  echo "  .scripts/check-redpill-confidential-ai-sync.sh --update-pin"
  exit 1
fi
