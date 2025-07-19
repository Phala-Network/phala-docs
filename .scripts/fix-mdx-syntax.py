#!/usr/bin/env python3
"""
Script to fix common MDX parsing errors from GitBook to Mintlify conversion.
Fixes:
1. {% stepper %} and {% step %} GitBook components
2. <figure><img></figure> incorrect HTML structure
3. Various JSX syntax issues
"""

import os
import re
import glob
from pathlib import Path

def fix_gitbook_components(content):
    """Fix GitBook-specific components."""
    
    # Replace {% stepper %} with a Steps component wrapper
    content = re.sub(r'{% stepper %}', '<Steps>', content)
    content = re.sub(r'{% endstepper %}', '</Steps>', content)
    
    # Replace {% step %} with Step component
    content = re.sub(r'{% step %}', '<Step>', content)
    content = re.sub(r'{% endstep %}', '</Step>', content)
    
    # Replace other common GitBook components
    content = re.sub(r'{% hint style="([^"]*)" %}', r'<Note type="\1">', content)
    content = re.sub(r'{% endhint %}', '</Note>', content)
    
    # Replace {% code %} blocks
    content = re.sub(r'{% code title="([^"]*)" %}', r'```\n# \1', content)
    content = re.sub(r'{% endcode %}', '```', content)
    
    return content

def fix_html_structure(content):
    """Fix incorrect HTML structure."""
    
    # Fix <figure><img></figure> -> <img />
    # This regex captures the img tag and removes the wrapping figure
    content = re.sub(
        r'<figure><img([^>]*?)><figcaption></figcaption></figure>',
        r'<img\1 />',
        content
    )
    
    # Fix standalone <figure><img> without proper closing
    content = re.sub(
        r'<figure><img([^>]*?)>(?!</figure>)',
        r'<img\1 />',
        content
    )
    
    return content

def fix_jsx_expressions(content):
    """Fix invalid JSX expressions."""
    
    # Fix empty JSX expressions like {{ }}
    content = re.sub(r'\{\{\s*\}\}', '', content)
    
    # Fix invalid component names starting with numbers or containing invalid chars
    # This is a conservative approach - we'll comment out problematic JSX
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        # If line contains JSX that starts with number or invalid chars, comment it out
        if re.search(r'<[0-9]', line) or re.search(r'<[^a-zA-Z/]', line):
            fixed_lines.append(f'<!-- {line} -->')
        else:
            fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_asset_paths(content):
    """Fix asset paths to be relative to public directory."""
    
    # Convert .gitbook/assets/ to /images/ (assuming assets will be moved to public/images/)
    content = re.sub(r'\.gitbook/assets/', '/images/', content)
    
    return content

def process_file(file_path):
    """Process a single MDX file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply fixes
        content = fix_gitbook_components(content)
        content = fix_html_structure(content)
        content = fix_jsx_expressions(content)
        content = fix_asset_paths(content)
        
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
    
    print("🔧 Fixing MDX syntax errors for Mintlify...")
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
            print(f"✅ Fixed: {relative_path}")
            fixed_count += 1
        else:
            print(f"⚪ No changes: {relative_path}")
    
    print()
    print("=" * 60)
    print(f"📊 SUMMARY: Fixed {fixed_count} out of {total_count} files")
    
    if fixed_count > 0:
        print("\n🎉 MDX syntax fixes applied! You can now test with 'mint dev'")
        print("\n📝 Note: GitBook components have been converted to basic HTML/MDX.")
        print("   You may want to use Mintlify's native components later.")
    else:
        print("\n✨ No files needed fixing!")

if __name__ == "__main__":
    main()