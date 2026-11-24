#!/usr/bin/env python3
"""Validate the canonical ACI mirror and Private AI documentation invariants."""

import hashlib
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SHARED = ROOT / "snippets/aci"


def check_manifest():
    errors = []
    expected = {}
    for line in (SHARED / "MANIFEST").read_text().splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([A-Za-z0-9_-]+\.mdx)", line)
        if not match:
            errors.append(f"Invalid ACI manifest entry: {line!r}")
            continue
        digest, name = match.groups()
        if name in expected:
            errors.append(f"Duplicate ACI manifest entry: {name}")
        expected[name] = digest
    actual = {path.name for path in SHARED.iterdir() if path.name not in {"MANIFEST", "SOURCE"}}
    if not expected or actual != set(expected):
        errors.append(f"ACI manifest file set mismatch: missing={sorted(set(expected) - actual)}, extra={sorted(actual - set(expected))}")
    for name, digest in expected.items():
        path = SHARED / name
        if path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            errors.append(f"ACI snippet differs from MANIFEST: {name}; edit shared text in redpill-ai/redpill-docs and sync it here")
    if not re.fullmatch(r"[0-9a-f]{40}\n", (SHARED / "SOURCE").read_text()):
        errors.append("ACI SOURCE must contain the full canonical Git commit and a trailing newline")
    return errors


def main():
    try:
        errors = check_manifest()
        for path in (ROOT / "phala-cloud/confidential-ai").rglob("*.mdx"):
            for number, line in enumerate(path.read_text().splitlines(), 1):
                if re.match(r"^api\s*:", line):
                    value = line.split(":", 1)[1].strip().strip("\"'")
                    parts = value.split()
                    try:
                        url = urlsplit(parts[1]) if len(parts) == 2 else None
                    except ValueError:
                        url = None
                    if url is None or url.scheme not in {"http", "https"} or not url.netloc:
                        errors.append(f"{path.relative_to(ROOT)}:{number}: api metadata must use an absolute URL")
        files = subprocess.run(
            ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
            cwd=ROOT, check=True, capture_output=True,
        ).stdout.split(b"\0")
        prohibited = (b"mr" + b"-kms", b"mr" + b"_kms")
        for name in files:
            if not name:
                continue
            path = ROOT / name.decode("utf-8", errors="surrogateescape")
            if path.is_file() and any(term in path.read_bytes().lower() for term in prohibited):
                errors.append(f"{path.relative_to(ROOT)}: prohibited KMS measurement name")
    except (OSError, UnicodeError, subprocess.CalledProcessError) as error:
        print(f"Private AI validation could not complete: {error}", file=sys.stderr)
        return 1
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Private AI checks passed: canonical ACI manifest, absolute API URLs, and measurement names")
    return 0


if __name__ == "__main__":
    sys.exit(main())
