#!/usr/bin/env python3
"""
Convert GitBook tab syntax to Mintlify tab syntax
"""

import re
import subprocess
import sys

def convert_tabs_in_file(file_path):
    """Convert GitBook tab syntax to Mintlify tab syntax in a file"""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        original_content = content
        
        # Replace {% tabs %} with <Tabs>
        content = re.sub(r'{% tabs %}', '<Tabs>', content)
        
        # Replace {% endtabs %} with </Tabs>
        content = re.sub(r'{% endtabs %}', '</Tabs>', content)
        
        # Replace {% tab title="..." %} with <Tab title="...">
        content = re.sub(r'{% tab title="([^"]*)" %}', r'<Tab title="\1">', content)
        
        # Replace {% endtab %} with </Tab>
        content = re.sub(r'{% endtab %}', '</Tab>', content)
        
        if content != original_content:
            with open(file_path, 'w') as f:
                f.write(content)
            return True
        return False
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Convert all GitBook tab syntax to Mintlify tab syntax"""
    # Get all .mdx files
    result = subprocess.run(['find', '.', '-name', '*.mdx', '-type', 'f'], capture_output=True, text=True)
    mdx_files = result.stdout.strip().split('\n')
    
    fixed_count = 0
    
    for file_path in mdx_files:
        if not file_path:
            continue
            
        if convert_tabs_in_file(file_path):
            print(f"Fixed tabs in {file_path}")
            fixed_count += 1
    
    print(f"Fixed tabs in {fixed_count} files")

if __name__ == "__main__":
    main()