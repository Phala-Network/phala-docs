#!/usr/bin/env python3
"""
Fix links to follow Mintlify conventions:
1. Use root-relative paths (starting with /)
2. Remove .mdx extensions from internal links
3. Keep external links as-is
"""

import os
import re
from pathlib import Path

def convert_to_root_relative(link_path, current_file_path):
    """Convert a relative link to root-relative path without .mdx extension."""
    
    # Skip external links
    if link_path.startswith('http') or link_path.startswith('mailto'):
        return link_path
    
    # Skip anchors
    if link_path.startswith('#'):
        return link_path
    
    # If already root-relative, just remove .mdx
    if link_path.startswith('/'):
        return re.sub(r'\.mdx$', '', link_path)
    
    # Handle relative paths
    current_dir = current_file_path.parent
    
    # Resolve the relative path
    try:
        if link_path.startswith('./'):
            link_path = link_path[2:]  # Remove ./
        
        target_path = current_dir / link_path
        target_path = target_path.resolve()
        
        # Get path relative to repo root
        repo_root = Path.cwd()
        relative_to_root = target_path.relative_to(repo_root)
        
        # Convert to root-relative path without .mdx
        root_relative = '/' + str(relative_to_root)
        root_relative = re.sub(r'\.mdx$', '', root_relative)
        
        return root_relative
        
    except Exception as e:
        print(f"  Warning: Could not resolve {link_path}: {e}")
        return link_path

def fix_mintlify_links(content, file_path):
    """Fix all links in content to follow Mintlify conventions."""
    
    def replace_link(match):
        link_text = match.group(1)
        link_url = match.group(2)
        
        # Handle anchor links within the same page
        if '#' in link_url and not link_url.startswith('#'):
            url_part, anchor_part = link_url.split('#', 1)
            if url_part:  # Has a file part
                new_url = convert_to_root_relative(url_part, file_path)
                return f'[{link_text}]({new_url}#{anchor_part})'
            else:  # Just an anchor
                return f'[{link_text}](#{anchor_part})'
        else:
            new_url = convert_to_root_relative(link_url, file_path)
            return f'[{link_text}]({new_url})'
    
    # Pattern to match markdown links [text](url)
    link_pattern = r'\[([^\]]*)\]\(([^)]+)\)'
    
    # Replace all links
    content = re.sub(link_pattern, replace_link, content)
    
    return content

def process_file(file_path):
    """Process a single MDX file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply link fixes
        content = fix_mintlify_links(content, file_path)
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main function to process all MDX files."""
    
    repo_root = Path.cwd()
    
    print("🔗 Converting links to Mintlify format (root-relative, no .mdx)...")
    print("=" * 70)
    
    # Find all .mdx files
    mdx_files = list(repo_root.glob('**/*.mdx'))
    
    # Filter out files in certain directories
    excluded_dirs = {'.tmp', 'node_modules', '.git', 'legacy'}
    mdx_files = [f for f in mdx_files if not any(part in excluded_dirs for part in f.parts)]
    
    fixed_count = 0
    total_count = len(mdx_files)
    
    print(f"Found {total_count} MDX files to process...")
    print()
    
    for file_path in mdx_files:
        relative_path = file_path.relative_to(repo_root)
        
        print(f"Processing: {relative_path}")
        if process_file(file_path):
            print(f"✅ Fixed links: {relative_path}")
            fixed_count += 1
        else:
            print(f"⚪ No changes: {relative_path}")
    
    print()
    print("=" * 70)
    print(f"📊 SUMMARY: Fixed links in {fixed_count} out of {total_count} files")
    
    if fixed_count > 0:
        print("\n🎉 Links converted to Mintlify format!")
        print("📝 Applied changes:")
        print("   - Relative paths → Root-relative paths (/path/to/page)")
        print("   - Removed .mdx extensions from internal links")
        print("   - Preserved external links and anchors")
    else:
        print("\n✨ All links already in Mintlify format!")

if __name__ == "__main__":
    main()