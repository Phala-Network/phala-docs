#!/bin/bash
# Convert error-codes.md from phala-cloud-monorepo to MDX format
# Usage: ./scripts/convert-error-codes.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
SOURCE_FILE="$REPO_ROOT/../phala-cloud-monorepo/docs/error-codes.md"
OUTPUT_FILE="$REPO_ROOT/phala-cloud/references/error-codes.mdx"

if [ ! -f "$SOURCE_FILE" ]; then
    echo "Error: Source file not found at $SOURCE_FILE"
    exit 1
fi

# Create output directory if needed
mkdir -p "$(dirname "$OUTPUT_FILE")"

# Generate MDX with frontmatter
{
    # Add frontmatter
    cat <<'FRONTMATTER'
---
title: Error Codes
description: Reference for Phala Cloud API error codes
---
FRONTMATTER

    # Process source file:
    # 1. Remove **Source:** lines
    # 2. Remove "Adding New Errors" section and everything after
    # 3. Remove teehouse module path references (internal implementation details)
    # 4. Remove -000 errors (base class exceptions, not user-facing)
    sed -n '1,/^## Adding New Errors/{ /^## Adding New Errors/d; /^\*\*Source:\*\*/d; p }' "$SOURCE_FILE" \
        | sed 's/ (`teehouse[^`]*`)//g' \
        | grep -v 'ERR-[0-9][0-9]-000'

} > "$OUTPUT_FILE"

echo "Generated: $OUTPUT_FILE"
