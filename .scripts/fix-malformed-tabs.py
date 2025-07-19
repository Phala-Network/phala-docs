#!/usr/bin/env python3
"""
Fix malformed Tab tags that are missing closing >
"""

import re
import subprocess
import sys

def fix_malformed_tabs_in_file(file_path):
    """Fix malformed Tab tags in a file"""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        original_content = content
        
        # Fix patterns like <Tab title="..."```language
        # Should become <Tab title="...">```language
        content = re.sub(r'<Tab title="([^"]*)"```([a-zA-Z]*)', r'<Tab title="\1">\n```\2', content)
        
        # Fix patterns like <Tab title="..."<pre class="language-...">
        # Should become <Tab title="...">```language
        content = re.sub(r'<Tab title="([^"]*)"<pre class="language-([^"]*)">', r'<Tab title="\1">\n```\2', content)
        
        # Fix malformed HTML in code blocks - remove malformed strong/code tags
        content = re.sub(r'<code class="lang-[^"]*">\*\*([^<]*?)\n</strong><strong>([^<]*?)\n</strong><strong>([^<]*?)\n</strong>([^<]*?)\n</code></pre>', r'```\n\1\n\2\n\3\n\4\n```', content)
        
        if content != original_content:
            with open(file_path, 'w') as f:
                f.write(content)
            return True
        return False
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Fix all malformed Tab tags"""
    # Get all .mdx files
    result = subprocess.run(['find', '.', '-name', '*.mdx', '-type', 'f'], capture_output=True, text=True)
    mdx_files = result.stdout.strip().split('\n')
    
    fixed_count = 0
    
    for file_path in mdx_files:
        if not file_path:
            continue
            
        if fix_malformed_tabs_in_file(file_path):
            print(f"Fixed malformed tabs in {file_path}")
            fixed_count += 1
    
    print(f"Fixed malformed tabs in {fixed_count} files")

if __name__ == "__main__":
    main()