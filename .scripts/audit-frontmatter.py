#!/usr/bin/env python3
"""
Audit all MDX files for missing frontmatter (title and description).
"""

import os
import re
from pathlib import Path

def check_frontmatter(file_path):
    """Check if a file has proper frontmatter with title and description."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file starts with frontmatter
        if not content.startswith('---'):
            return False, None, None
        
        # Extract frontmatter
        frontmatter_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not frontmatter_match:
            return False, None, None
        
        frontmatter = frontmatter_match.group(1)
        
        # Check for title
        title_match = re.search(r'^title:\s*(.*)$', frontmatter, re.MULTILINE)
        title = title_match.group(1).strip().strip('"\'') if title_match else None
        
        # Check for description
        desc_match = re.search(r'^description:\s*(.*)$', frontmatter, re.MULTILINE)
        description = desc_match.group(1).strip().strip('"\'') if desc_match else None
        
        return True, title, description
        
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False, None, None

def suggest_title_from_content(file_path):
    """Suggest a title based on the first heading in the file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove frontmatter if present
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                content = parts[2]
        
        # Find first heading
        heading_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if heading_match:
            title = heading_match.group(1).strip()
            # Clean up title (remove emojis, extra spaces)
            title = re.sub(r'[🚀🛡️🪙🥷📊⚡🔧🎯💻📝🌍🔗]', '', title).strip()
            return title
        
        # Fallback to filename
        return file_path.stem.replace('-', ' ').replace('_', ' ').title()
        
    except Exception as e:
        return file_path.stem.replace('-', ' ').replace('_', ' ').title()

def main():
    """Main function to audit frontmatter."""
    
    repo_root = Path.cwd()
    
    print("📋 Auditing MDX files for frontmatter...")
    print("=" * 60)
    
    # Find all .mdx files
    mdx_files = list(repo_root.glob('**/*.mdx'))
    
    # Filter out files in certain directories
    excluded_dirs = {'.tmp', 'node_modules', '.git', 'legacy'}
    mdx_files = [f for f in mdx_files if not any(part in excluded_dirs for part in f.parts)]
    
    missing_frontmatter = []
    missing_title = []
    missing_description = []
    
    total_count = len(mdx_files)
    
    print(f"Found {total_count} MDX files to check...")
    print()
    
    for file_path in mdx_files:
        relative_path = file_path.relative_to(repo_root)
        
        has_frontmatter, title, description = check_frontmatter(file_path)
        
        if not has_frontmatter:
            missing_frontmatter.append(relative_path)
            suggested_title = suggest_title_from_content(file_path)
            print(f"❌ No frontmatter: {relative_path}")
            print(f"   Suggested title: {suggested_title}")
        else:
            if not title:
                missing_title.append(relative_path)
                suggested_title = suggest_title_from_content(file_path)
                print(f"⚠️  Missing title: {relative_path}")
                print(f"   Suggested title: {suggested_title}")
            
            if not description:
                missing_description.append(relative_path)
                print(f"⚠️  Missing description: {relative_path}")
            
            if title and description:
                print(f"✅ Complete: {relative_path}")
                print(f"   Title: {title}")
                print(f"   Description: {description}")
        
        print()
    
    print("=" * 60)
    print("📊 SUMMARY:")
    print(f"   - Total files: {total_count}")
    print(f"   - Missing frontmatter: {len(missing_frontmatter)}")
    print(f"   - Missing title: {len(missing_title)}")
    print(f"   - Missing description: {len(missing_description)}")
    
    if missing_frontmatter or missing_title or missing_description:
        print(f"\n🔧 Files needing fixes: {len(missing_frontmatter) + len(missing_title) + len(missing_description)}")
    else:
        print(f"\n✨ All files have proper frontmatter!")

if __name__ == "__main__":
    main()