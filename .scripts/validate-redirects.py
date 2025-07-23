#!/usr/bin/env python3
"""
Script to validate redirects in Mintlify docs.json
Extracts all available page paths and checks that redirect targets are valid
"""

import json
import sys
from typing import Set, List, Dict, Any


def extract_pages_from_navigation(nav_item) -> Set[str]:
    """Recursively extract all page paths from navigation structure"""
    pages = set()

    if isinstance(nav_item, str):
        # Single page path
        pages.add(nav_item)
    elif isinstance(nav_item, dict):
        if "pages" in nav_item:
            # Group with pages
            for page in nav_item["pages"]:
                pages.update(extract_pages_from_navigation(page))
        elif "group" in nav_item and "pages" in nav_item:
            # Named group with pages
            for page in nav_item["pages"]:
                pages.update(extract_pages_from_navigation(page))
    elif isinstance(nav_item, list):
        # List of items
        for item in nav_item:
            pages.update(extract_pages_from_navigation(item))

    return pages


def get_all_available_paths(docs_config: Dict[str, Any]) -> Set[str]:
    """Extract all available page paths from docs.json"""
    available_paths = set()

    # Extract from navigation
    if "navigation" in docs_config:
        nav = docs_config["navigation"]

        # Handle tabs structure (current format)
        if "tabs" in nav:
            for tab in nav["tabs"]:
                # Handle tabs with "groups" array (like Phala Cloud)
                if "groups" in tab:
                    for group in tab["groups"]:
                        available_paths.update(extract_pages_from_navigation(group))
                # Handle tabs with "pages" array directly (like Network, Dstack, Confidential AI)
                elif "pages" in tab:
                    for page in tab["pages"]:
                        available_paths.update(extract_pages_from_navigation(page))

        # Handle anchors structure (legacy format)
        if "anchors" in nav:
            for anchor in nav["anchors"]:
                if "groups" in anchor:
                    for group in anchor["groups"]:
                        available_paths.update(extract_pages_from_navigation(group))

        # Handle direct navigation items
        if "pages" in nav:
            available_paths.update(extract_pages_from_navigation(nav["pages"]))

    return available_paths


def validate_redirects(docs_config: Dict[str, Any], available_paths: Set[str]) -> List[Dict[str, str]]:
    """Validate that all redirect destinations point to valid paths"""
    invalid_redirects = []

    if "redirects" not in docs_config:
        return invalid_redirects

    for redirect in docs_config["redirects"]:
        source = redirect.get("source", "")
        destination = redirect.get("destination", "")

        # Keep destination path as-is (with leading slash) for comparison
        if destination not in available_paths:
            invalid_redirects.append({
                "source": source,
                "destination": destination,
                "reason": "Destination path not found in navigation"
            })

    return invalid_redirects


def main():
    """Main function to run redirect validation"""
    try:
        # Load docs.json
        with open("docs.json", "r") as f:
            docs_config = json.load(f)

        print("🔍 Extracting available page paths from navigation...")
        available_paths = get_all_available_paths(docs_config)

        print(f"✅ Found {len(available_paths)} available page paths")

        print("\n📋 Available paths:")
        for path in sorted(available_paths):
            print(f"  - {path}")

        print(f"\n🔗 Validating {len(docs_config.get('redirects', []))} redirects...")
        invalid_redirects = validate_redirects(docs_config, available_paths)

        if not invalid_redirects:
            print("✅ All redirects are valid!")
            return 0
        else:
            print(f"❌ Found {len(invalid_redirects)} invalid redirects:")
            for redirect in invalid_redirects:
                print(f"  - {redirect['source']} → {redirect['destination']}")
                print(f"    Reason: {redirect['reason']}")
            return 1

    except FileNotFoundError:
        print("❌ Error: docs.json not found in current directory")
        return 1
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing docs.json: {e}")
        return 1
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
