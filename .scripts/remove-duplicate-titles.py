#!/usr/bin/env python3

import os
import re
import yaml
from pathlib import Path

def extract_frontmatter_and_content(content):
    """Extract YAML frontmatter and content from MDX file."""
    if not content.startswith('---'):
        return None, content
    
    # Find the end of frontmatter
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None, content
    
    try:
        frontmatter = yaml.safe_load(parts[1])
        content_part = '---' + parts[2] if parts[2].startswith('\n') else '---\n' + parts[2]
        return frontmatter, content_part
    except yaml.YAMLError:
        return None, content

def remove_duplicate_h1(content, title):
    """Remove H1 heading if it matches the frontmatter title."""
    lines = content.split('\n')
    new_lines = []
    
    for i, line in enumerate(lines):
        # Skip H1 headings that match the title (with or without emoji)
        if line.startswith('# '):
            h1_text = line[2:].strip()
            # Remove emoji and extra spaces for comparison
            h1_clean = re.sub(r'[^\w\s]', '', h1_text).strip()
            title_clean = re.sub(r'[^\w\s]', '', title).strip()
            
            if h1_clean.lower() == title_clean.lower():
                # Skip this H1 line and any immediately following empty lines
                continue
        
        new_lines.append(line)
    
    return '\n'.join(new_lines)

def process_file(file_path):
    """Process a single MDX file to remove duplicate titles."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        frontmatter, content_part = extract_frontmatter_and_content(content)
        
        if not frontmatter or 'title' not in frontmatter:
            return False
        
        title = frontmatter['title']
        new_content_part = remove_duplicate_h1(content_part, title)
        
        if new_content_part != content_part:
            # Reconstruct the full content
            frontmatter_yaml = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)
            new_content = f"---\n{frontmatter_yaml}---{new_content_part[3:]}"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ Fixed duplicate title in: {file_path}")
            return True
        
        return False
        
    except Exception as e:
        print(f"✗ Error processing {file_path}: {e}")
        return False

def main():
    """Process all MDX files to remove duplicate titles."""
    root_dir = Path('.')
    mdx_files = list(root_dir.glob('**/*.mdx'))
    
    print(f"Processing {len(mdx_files)} MDX files...")
    
    fixed_count = 0
    for file_path in mdx_files:
        if process_file(file_path):
            fixed_count += 1
    
    print(f"\nCompleted! Fixed duplicate titles in {fixed_count} files.")

if __name__ == "__main__":
    main()