#!/usr/bin/env python3
"""
Script to fix all remaining image paths from relative to absolute.
"""

import re
from pathlib import Path

def fix_image_paths(content):
    """Fix all image paths to use absolute paths."""
    
    # Pattern to match images with relative paths
    # Matches: ../images/, ../../images/, ../../../images/, etc.
    img_pattern = r'src="(\.\./)+images/([^"]*)"'
    
    def replace_path(match):
        filename = match.group(2)
        return f'src="/images/{filename}"'
    
    # Apply the replacement
    content = re.sub(img_pattern, replace_path, content)
    
    return content

def process_file(file_path):
    """Process a single MDX file to fix image paths."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply path fixes
        content = fix_image_paths(content)
        
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
    
    print("🔗 Fixing all remaining image paths...")
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
            print(f"✅ Fixed paths: {relative_path}")
            fixed_count += 1
        else:
            print(f"⚪ No changes: {relative_path}")
    
    print()
    print("=" * 60)
    print(f"📊 SUMMARY: Fixed image paths in {fixed_count} out of {total_count} files")
    
    if fixed_count > 0:
        print("\n🎉 All image paths now use absolute paths!")
    else:
        print("\n✨ No path fixes needed!")

if __name__ == "__main__":
    main()