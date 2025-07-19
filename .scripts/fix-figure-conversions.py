#!/usr/bin/env python3
"""
Script to fix GitBook figure conversions to proper Mintlify Figure components.

Converts:
<figure><img src="../.gitbook/assets/gpu-tee-api.png" alt="diagram of apis"><figcaption><p>This is a TEE API</p></figcaption></figure>

To:
<Figure caption="This is a TEE API">
    <img src="../.gitbook/assets/gpu-tee-api.png" alt="diagram of apis" />
</Figure>

Also fixes simple <img> tags that should have captions back to Figure components.
"""

import os
import re
import glob
from pathlib import Path

def fix_figure_elements(content):
    """Convert GitBook figure elements to Mintlify Figure components."""
    
    # Pattern 1: Full figure with caption
    # <figure><img src="..." alt="..."><figcaption><p>Caption text</p></figcaption></figure>
    def replace_figure_with_caption(match):
        img_attrs = match.group(1)
        caption_text = match.group(2).strip()
        
        # Clean up the image attributes and ensure proper closing
        img_tag = f'<img{img_attrs}'
        if not img_tag.endswith('/>') and not img_tag.endswith('>'):
            img_tag += ' />'
        elif img_tag.endswith('>') and not img_tag.endswith('/>'):
            img_tag = img_tag[:-1] + ' />'
        
        return f'<Figure caption="{caption_text}">\n    {img_tag}\n</Figure>'
    
    # Replace figures with captions
    content = re.sub(
        r'<figure><img([^>]*?)><figcaption><p>(.*?)</p></figcaption></figure>',
        replace_figure_with_caption,
        content,
        flags=re.DOTALL
    )
    
    # Pattern 2: Figure with empty caption  
    # <figure><img src="..." alt="..."><figcaption></figcaption></figure>
    def replace_figure_empty_caption(match):
        img_attrs = match.group(1)
        
        # For empty captions, just use a simple img tag
        img_tag = f'<img{img_attrs}'
        if not img_tag.endswith('/>') and not img_tag.endswith('>'):
            img_tag += ' />'
        elif img_tag.endswith('>') and not img_tag.endswith('/>'):
            img_tag = img_tag[:-1] + ' />'
        
        return img_tag
    
    content = re.sub(
        r'<figure><img([^>]*?)><figcaption></figcaption></figure>',
        replace_figure_empty_caption,
        content
    )
    
    # Pattern 3: Standalone figure tags (incomplete)
    # <figure><img src="..." alt="...">
    content = re.sub(
        r'<figure><img([^>]*?)>(?!</figure>)',
        r'<img\1 />',
        content
    )
    
    return content

def restore_figures_from_git_diff(file_path):
    """
    Try to restore original figure elements by checking git diff to see what was there before.
    This helps us understand if there were captions that got lost in conversion.
    """
    try:
        import subprocess
        
        # Get the git diff for this file to see original figure elements
        result = subprocess.run(
            ['git', 'log', '--follow', '-p', '--', str(file_path)],
            capture_output=True,
            text=True,
            cwd=file_path.parent
        )
        
        if result.returncode == 0:
            diff_content = result.stdout
            
            # Look for original figure patterns in the git history
            figure_patterns = re.findall(
                r'<figure><img([^>]*?)><figcaption>(?:<p>)?(.*?)(?:</p>)?</figcaption></figure>',
                diff_content,
                re.DOTALL
            )
            
            return figure_patterns
    except:
        pass
    
    return []

def process_file(file_path):
    """Process a single MDX file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply figure fixes
        content = fix_figure_elements(content)
        
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
    
    print("🖼️  Fixing GitBook figure conversions to Mintlify format...")
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
        print("\n🎉 Figure conversions applied!")
        print("📝 Converted GitBook <figure><figcaption> to Mintlify <Figure caption=\"\">")
    else:
        print("\n✨ No figure elements needed fixing!")

if __name__ == "__main__":
    main()