#!/bin/bash
# Convert error-codes.md from the teehouse monorepo to MDX format
# Usage: ./scripts/convert-error-codes.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
SOURCE_FILE="$REPO_ROOT/../../docs/error-codes.md"
OUTPUT_FILE="$REPO_ROOT/phala-cloud/references/error-codes.mdx"

# Modules used only by internal endpoints; keep them out of the public page.
# 07 Admin, 08 Core/Runtime/DevOps, 13 Changelog Publication, 15 Catalog Pricing
EXCLUDED_MODULES="07 08 13 15"
# Single codes from public modules that are only returned to admins.
EXCLUDED_CODES="ERR-03-011 ERR-03-012 ERR-03-013 ERR-03-059 ERR-04-011 ERR-06-011 ERR-06-013"

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
    # 5. Remove modules that are not part of the public API (EXCLUDED_MODULES)
    # 6. Remove single admin-only codes (EXCLUDED_CODES)
    # 7. Drop the Exception Class column and docstrings (internal names)
    # Using awk for portability (BSD sed on macOS does not support the
    # multi-command range form used previously).
    awk -v excluded="$EXCLUDED_MODULES" '
        BEGIN {
            n = split(excluded, ids, " ")
            for (i = 1; i <= n; i++) skip_id[ids[i]] = 1
        }
        /^## Adding New Errors/ { exit }
        /^## /                  { skipping = 0 }
        /^## Module [0-9][0-9]:/ { if (substr($3, 1, 2) in skip_id) skipping = 1 }
        skipping                { next }
        /^- \*\*Module [0-9][0-9]\*\*/ { if (substr($0, 12, 2) in skip_id) next }
        /^\*\*Source:\*\*/      { next }
                                { print }
    ' "$SOURCE_FILE" \
        | sed 's/ (`teehouse[^`]*`)//g' \
        | grep -v 'ERR-[0-9][0-9]-000' \
        | awk -v excluded="$EXCLUDED_CODES" '
            BEGIN {
                n = split(excluded, codes, " ")
                for (i = 1; i <= n; i++) skip_code["`" codes[i] "`"] = 1
            }
            /^\| `ERR-/ { split($0, cols, " "); if (cols[2] in skip_code) next }
            { print }
        ' \
        | awk -F'|' '
            # Keep only the code and the user-facing message.
            /^\|/ && NF == 5 {
                message = $4
                # Drop the developer docstring appended after the message.
                sub(/<br\/>\*.*\* *$/, " ", message)
                print "|" $2 "|" message "|"
                next
            }
            { print }
        '

} > "$OUTPUT_FILE"

echo "Generated: $OUTPUT_FILE"
