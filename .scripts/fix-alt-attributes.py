#!/usr/bin/env python3
"""
Fix alt attributes in Frame elements to match original alt attributes from git diff
"""

import re
import subprocess
import sys

def get_original_alt_from_diff():
    """Extract original alt attributes from git diff"""
    try:
        # Get git diff output
        result = subprocess.run(['git', 'diff'], capture_output=True, text=True)
        diff_content = result.stdout
        
        # Find patterns like: <figure><img src="..." alt="original_alt" ...><figcaption><p>Caption</p></figcaption></figure>
        # followed by: <Frame caption="Caption"><img src="..." alt="wrong_alt" /></Frame>
        
        original_alts = {}
        lines = diff_content.split('\n')
        
        for i, line in enumerate(lines):
            if line.startswith('-') and '<figure>' in line and '<img' in line:
                # Extract original alt attribute
                alt_match = re.search(r'alt="([^"]*)"', line)
                if alt_match:
                    original_alt = alt_match.group(1)
                    
                    # Look for the caption text
                    caption_match = re.search(r'<figcaption>(?:<p>)?(.*?)(?:</p>)?</figcaption>', line)
                    if caption_match:
                        caption_text = caption_match.group(1).strip()
                        if caption_text:
                            original_alts[caption_text] = original_alt
                    else:
                        # Handle empty figcaption case
                        if '<figcaption></figcaption>' in line:
                            # Get the image src to use as key
                            src_match = re.search(r'src="([^"]*)"', line)
                            if src_match:
                                src = src_match.group(1)
                                original_alts[src] = original_alt
        
        return original_alts
    except Exception as e:
        print(f"Error reading git diff: {e}")
        return {}

def fix_alt_attributes():
    """Fix alt attributes in converted Frame elements"""
    original_alts = get_original_alt_from_diff()
    
    if not original_alts:
        print("No original alt attributes found in git diff")
        return
    
    print(f"Found {len(original_alts)} original alt attributes")
    
    # Get all .mdx files
    result = subprocess.run(['find', '.', '-name', '*.mdx', '-type', 'f'], capture_output=True, text=True)
    mdx_files = result.stdout.strip().split('\n')
    
    fixed_count = 0
    
    for file_path in mdx_files:
        if not file_path:
            continue
            
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            
            original_content = content
            
            # Find Frame elements and fix alt attributes
            frame_pattern = r'<Frame caption="([^"]*)">\s*<img src="([^"]*)" alt="([^"]*)" />\s*</Frame>'
            
            def fix_alt(match):
                caption = match.group(1)
                src = match.group(2)
                current_alt = match.group(3)
                
                # Look up original alt by caption first, then by src
                original_alt = original_alts.get(caption)
                if original_alt is None:
                    # Try to match by src filename
                    src_filename = src.split('/')[-1]
                    for key, alt in original_alts.items():
                        if src_filename in key:
                            original_alt = alt
                            break
                
                if original_alt is not None and original_alt != current_alt:
                    return f'<Frame caption="{caption}">\n  <img src="{src}" alt="{original_alt}" />\n</Frame>'
                
                return match.group(0)
            
            content = re.sub(frame_pattern, fix_alt, content, flags=re.MULTILINE)
            
            if content != original_content:
                with open(file_path, 'w') as f:
                    f.write(content)
                print(f"Fixed alt attributes in {file_path}")
                fixed_count += 1
        
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    print(f"Fixed alt attributes in {fixed_count} files")

if __name__ == "__main__":
    fix_alt_attributes()