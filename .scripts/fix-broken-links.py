#!/usr/bin/env python3
"""
Script to fix broken links found by mint broken-links command.
Fixes:
1. .md links -> .mdx links
2. /image/ paths -> /images/ paths  
3. Broken reference paths
"""

import os
import re
import glob
from pathlib import Path

def fix_md_to_mdx_links(content):
    """Fix .md links to .mdx links."""
    # Pattern to match markdown links ending with .md
    patterns = [
        # [text](file.md)
        (r'\]\(([^)]*?)\.md\)', r'](\1.mdx)'),
        # [text](file.md#anchor)
        (r'\]\(([^)]*?)\.md(#[^)]*?)\)', r'](\1.mdx\2)'),
        # [text](path/file.md)
        (r'\]\(([^)]*?)\.md\)', r'](\1.mdx)'),
    ]
    
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)
    
    return content

def fix_image_paths(content):
    """Fix /image/ paths to /images/ paths."""
    # Fix /image/ to /images/
    content = re.sub(r'/image/', '/images/', content)
    return content

def fix_broken_references(content):
    """Fix common broken reference patterns."""
    fixes = [
        # Remove broken-reference links entirely
        (r'\[([^\]]*?)\]\(broken-reference\)', r'\1'),
        # Fix legacy paths
        (r'\]\(../../legacy/ai-agent-contract/\)', r'](#legacy-content-removed)'),
        # Fix other-products paths
        (r'../../other-products/subbridge/broken-reference/', ''),
        # Fix developers paths  
        (r'../../developers/([^/]*?)/broken-reference/', r'../\1/'),
        # Remove empty links
        (r'\[([^\]]*?)\]\(\)', r'\1'),
    ]
    
    for pattern, replacement in fixes:
        content = re.sub(pattern, replacement, content)
    
    return content

def fix_self_references(content, file_path):
    """Fix self-referencing links like file.md#anchor."""
    filename = file_path.stem  # Get filename without extension
    
    # Fix self-references like filename.md#anchor to just #anchor
    pattern = rf'\]\({filename}\.mdx?(#[^)]*?)\)'
    replacement = r'](\1)'
    content = re.sub(pattern, replacement, content)
    
    return content

def process_file(file_path):
    """Process a single MDX file to fix broken links."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply fixes
        content = fix_md_to_mdx_links(content)
        content = fix_image_paths(content)
        content = fix_broken_references(content)
        content = fix_self_references(content, file_path)
        
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
    
    # Get repository root
    script_dir = Path(__file__).parent.absolute()
    repo_root = script_dir.parent
    
    print("🔗 Fixing broken links found by mint broken-links...")
    print("=" * 60)
    
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
        
        if process_file(file_path):
            print(f"✅ Fixed links: {relative_path}")
            fixed_count += 1
        else:
            print(f"⚪ No changes: {relative_path}")
    
    print()
    print("=" * 60)
    print(f"📊 SUMMARY: Fixed broken links in {fixed_count} out of {total_count} files")
    
    if fixed_count > 0:
        print("\n🎉 Broken links fixed!")
        print("📝 Applied fixes:")
        print("   - .md links → .mdx links")
        print("   - /image/ paths → /images/ paths")
        print("   - Removed broken references")
        print("   - Fixed self-referencing links")
    else:
        print("\n✨ No broken links needed fixing!")

if __name__ == "__main__":
    main()