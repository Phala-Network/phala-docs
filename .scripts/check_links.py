#!/usr/bin/env python3
"""
Check all extracted documentation links for:
1. File existence on disk
2. Redirect coverage in docs.json
3. Navigation accessibility (reachability through docs.json)
"""
import json
import os
from pathlib import Path
from typing import Set, List, Dict, Any

def load_docs_config(docs_json_path: str) -> dict:
    """Load complete docs.json configuration"""
    with open(docs_json_path, 'r') as f:
        return json.load(f)

def load_redirects(docs_config: dict) -> Dict[str, str]:
    """Load redirects mapping from docs.json"""
    redirects = {}
    for redirect in docs_config.get("redirects", []):
        source = redirect["source"].lstrip("/")
        destination = redirect["destination"].lstrip("/")
        redirects[source] = destination

    return redirects

def extract_navigation_links(nav_item: Any, links: Set[str]):
    """Recursively extract all page paths from navigation structure"""
    if isinstance(nav_item, str):
        # Clean the link (remove leading slash)
        clean_link = nav_item.lstrip("/")
        if clean_link:
            links.add(clean_link)
    elif isinstance(nav_item, dict):
        # Handle pages in groups
        if "pages" in nav_item:
            for page in nav_item["pages"]:
                extract_navigation_links(page, links)
        # Handle tab structures
        if "groups" in nav_item:
            for group in nav_item["groups"]:
                extract_navigation_links(group, links)
        # Handle other nested structures
        for key, value in nav_item.items():
            if key not in ["group", "tab", "icon", "pages", "groups"]:
                extract_navigation_links(value, links)
    elif isinstance(nav_item, list):
        for item in nav_item:
            extract_navigation_links(item, links)

def get_all_navigation_links(docs_config: dict) -> Set[str]:
    """Extract all links from docs.json navigation structure"""
    nav_links = set()

    navigation = docs_config.get("navigation", {})

    # Extract from tabs
    if "tabs" in navigation:
        for tab in navigation["tabs"]:
            extract_navigation_links(tab, nav_links)

    # Extract from anchors (legacy structure)
    if "anchors" in navigation:
        for anchor in navigation["anchors"]:
            extract_navigation_links(anchor, nav_links)

    return nav_links

def get_all_redirect_links(docs_config: dict) -> Set[str]:
    """Extract all source and destination paths from redirects"""
    redirect_links = set()

    for redirect in docs_config.get("redirects", []):
        source = redirect["source"].lstrip("/")
        destination = redirect["destination"].lstrip("/")

        if source:
            redirect_links.add(source)
        if destination:
            redirect_links.add(destination)

    return redirect_links

def check_file_exists(link: str) -> bool:
    """Check if a documentation file exists for the given link"""
    # Common file extensions for documentation
    extensions = ['.md', '.mdx', '']

    for ext in extensions:
        file_path = Path(f"{link}{ext}")
        if file_path.exists() and file_path.is_file():
            return True

    return False

def main():
    # Load extracted links from all .txt files in .scripts/used_links
    links = []
    used_links_dir = Path('.scripts/used_links')
    for txt_file in used_links_dir.glob('*.txt'):
        with open(txt_file, 'r') as f:
            links.extend([line.strip() for line in f.readlines() if line.strip()])

    # Load docs.json configuration
    docs_config = load_docs_config('docs.json')
    redirects = load_redirects(docs_config)

    # Get navigation and redirect links for accessibility check
    nav_links = get_all_navigation_links(docs_config)
    redirect_links = get_all_redirect_links(docs_config)
    accessible_links = nav_links.union(redirect_links)

    # Check each link
    existing_files = []
    broken_links = []
    redirected_links = []
    unreachable_files = []

    print(f"Checking {len(links)} documentation links...")
    print("=" * 60)

    for link in links:
        file_exists = check_file_exists(link)
        is_accessible = link in accessible_links

        if file_exists:
            existing_files.append(link)
            # Check if existing file is unreachable
            if not is_accessible:
                unreachable_files.append(link)
        elif link in redirects:
            destination = redirects[link]
            if check_file_exists(destination):
                redirected_links.append((link, destination))
            else:
                broken_links.append(f"{link} -> {destination} (redirect target missing)")
        else:
            broken_links.append(link)

    # Report results
    print(f"\n✅ EXISTING FILES ({len(existing_files)}):")
    print("-" * 40)
    for link in sorted(existing_files):
        status = "📍 UNREACHABLE" if link in unreachable_files else "🔗 ACCESSIBLE"
        print(f"  {link} {status}")

    print(f"\n🔄 REDIRECTED LINKS ({len(redirected_links)}):")
    print("-" * 40)
    for source, dest in sorted(redirected_links):
        print(f"  {source} -> {dest}")

    print(f"\n❌ BROKEN LINKS ({len(broken_links)}):")
    print("-" * 40)
    for link in sorted(broken_links):
        print(f"  {link}")

    if unreachable_files:
        print(f"\n📍 UNREACHABLE FILES ({len(unreachable_files)}):")
        print("-" * 40)
        print("  Files exist on disk but are not accessible through navigation:")
        for link in sorted(unreachable_files):
            print(f"  {link}")

    # Save results to files
    with open('tmp/existing_files.txt', 'w') as f:
        for link in sorted(existing_files):
            f.write(f"{link}\n")

    with open('tmp/redirected_links.txt', 'w') as f:
        for source, dest in sorted(redirected_links):
            f.write(f"{source} -> {dest}\n")

    with open('tmp/broken_links.txt', 'w') as f:
        for link in sorted(broken_links):
            f.write(f"{link}\n")

    with open('tmp/unreachable_files.txt', 'w') as f:
        for link in sorted(unreachable_files):
            f.write(f"{link}\n")

    print(f"\n📊 SUMMARY:")
    print(f"  Total links checked: {len(links)}")
    print(f"  Existing files: {len(existing_files)}")
    print(f"    - Accessible: {len(existing_files) - len(unreachable_files)}")
    print(f"    - Unreachable: {len(unreachable_files)}")
    print(f"  Redirected links: {len(redirected_links)}")
    print(f"  Broken links: {len(broken_links)}")
    print(f"  File success rate: {((len(existing_files) + len(redirected_links)) / len(links) * 100):.1f}%")
    print(f"  Accessibility rate: {((len(existing_files) - len(unreachable_files) + len(redirected_links)) / len(links) * 100):.1f}%")

    print(f"\n📁 Results saved to:")
    print(f"  - tmp/existing_files.txt")
    print(f"  - tmp/redirected_links.txt")
    print(f"  - tmp/broken_links.txt")
    print(f"  - tmp/unreachable_files.txt")

    return len(broken_links) == 0 and len(unreachable_files) == 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
