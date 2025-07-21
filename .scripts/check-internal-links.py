#!/usr/bin/env python3
"""
Check for broken internal links in MDX files.
Validates that all internal links point to existing files or valid anchors.
"""

import os
import re
import sys
import json
from pathlib import Path
from typing import Set, List, Dict, Tuple

def get_available_paths_from_docs_json() -> Set[str]:
    """Extract all available page paths from docs.json navigation."""
    def extract_pages(item):
        pages = set()
        if isinstance(item, str):
            pages.add(item)
        elif isinstance(item, dict):
            if "pages" in item:
                for page in item["pages"]:
                    pages.update(extract_pages(page))
        elif isinstance(item, list):
            for subitem in item:
                pages.update(extract_pages(subitem))
        return pages

    try:
        with open("docs.json", "r") as f:
            config = json.load(f)

        all_paths = set()
        if "navigation" in config and "anchors" in config["navigation"]:
            for anchor in config["navigation"]["anchors"]:
                if "groups" in anchor:
                    for group in anchor["groups"]:
                        all_paths.update(extract_pages(group))

        return all_paths
    except FileNotFoundError:
        print("⚠️  docs.json not found, skipping navigation validation")
        return set()
    except Exception as e:
        print(f"⚠️  Error reading docs.json: {e}")
        return set()

def find_mdx_files() -> List[Path]:
    """Find all MDX files in the project."""
    mdx_files = []
    for root, dirs, files in os.walk("."):
        # Skip hidden directories and common ignore patterns
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', 'tmp']]

        for file in files:
            if file.endswith(('.md', '.mdx')):
                mdx_files.append(Path(root) / file)

    return mdx_files

def extract_internal_links(content: str) -> List[Tuple[str, int]]:
    """Extract internal links from MDX content."""
    links = []

    # Pattern for markdown links: [text](path)
    markdown_pattern = r'\[([^\]]*)\]\(([^)]+)\)'

    for line_num, line in enumerate(content.split('\n'), 1):
        for match in re.finditer(markdown_pattern, line):
            link_text, link_url = match.groups()

            # Only check internal links (not external URLs)
            if not link_url.startswith(('http://', 'https://', 'mailto:', '#')):
                links.append((link_url, line_num))

    return links

def validate_link(link_path: str, current_file: Path, available_paths: Set[str]) -> Tuple[bool, str]:
    """Validate if a link path exists."""
    # Remove anchor part if present
    clean_path = link_path.split('#')[0]

    # Skip empty paths (anchor-only links)
    if not clean_path:
        return True, "anchor-only link"

    # Convert to absolute path from root
    if clean_path.startswith('/'):
        # Absolute path from root
        check_path = clean_path.lstrip('/')
    else:
        # Relative path from current file
        current_dir = current_file.parent
        resolved_path = (current_dir / clean_path).resolve()
        try:
            check_path = str(resolved_path.relative_to(Path.cwd()))
        except ValueError:
            return False, "path outside project"

    # Remove .mdx/.md extensions for navigation check
    nav_path = re.sub(r'\.(mdx?|md)$', '', check_path)

    # Check if path exists in navigation
    if nav_path in available_paths:
        return True, "found in navigation"

    # Check if file exists on filesystem
    if Path(check_path).exists():
        return True, "file exists"

    # Check with .mdx extension
    if Path(check_path + '.mdx').exists():
        return True, "file exists (.mdx)"

    # Check with .md extension
    if Path(check_path + '.md').exists():
        return True, "file exists (.md)"

    return False, "not found"

def main():
    print("🔗 Checking internal links in MDX files...")
    print("=" * 50)

    # Get available paths from docs.json
    available_paths = get_available_paths_from_docs_json()
    print(f"📋 Found {len(available_paths)} paths in navigation")

    # Find all MDX files
    mdx_files = find_mdx_files()
    print(f"📄 Found {len(mdx_files)} MDX files to check")
    print("-" * 50)

    broken_links = []
    total_links = 0

    for mdx_file in mdx_files:
        try:
            with open(mdx_file, 'r', encoding='utf-8') as f:
                content = f.read()

            links = extract_internal_links(content)
            total_links += len(links)

            if links:
                print(f"📄 {mdx_file} ({len(links)} links)")

                for link_path, line_num in links:
                    is_valid, reason = validate_link(link_path, mdx_file, available_paths)

                    if is_valid:
                        print(f"  ✅ Line {line_num:3d}: {link_path}")
                    else:
                        print(f"  ❌ Line {line_num:3d}: {link_path} ({reason})")
                        broken_links.append({
                            'file': str(mdx_file),
                            'line': line_num,
                            'link': link_path,
                            'reason': reason
                        })

        except Exception as e:
            print(f"❌ Error processing {mdx_file}: {e}")

    # Summary
    print("\n" + "=" * 50)
    print("📊 LINK VALIDATION SUMMARY")
    print("=" * 50)

    print(f"📄 Files checked: {len(mdx_files)}")
    print(f"🔗 Total links: {total_links}")
    print(f"✅ Valid links: {total_links - len(broken_links)}")
    print(f"❌ Broken links: {len(broken_links)}")

    if broken_links:
        print(f"\n🔍 BROKEN LINKS DETAILS:")
        print("-" * 30)

        for link in broken_links:
            print(f"File: {link['file']}")
            print(f"  ↳ Line {link['line']}: {link['link']}")
            print(f"  ↳ Reason: {link['reason']}")
            print()

        print("💡 RECOMMENDATIONS:")
        print("   - Check file paths and ensure they exist")
        print("   - Verify links point to pages listed in docs.json navigation")
        print("   - Use root-relative paths (starting with /) for consistency")

        return 1
    else:
        print(f"\n🎉 All {total_links} internal links are valid!")
        return 0

if __name__ == "__main__":
    sys.exit(main())
