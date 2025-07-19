#!/usr/bin/env python3
"""
Script to fix ALL GitBook figure conversions according to updated CLAUDE.md rules.

New rules:
1. GitBook: <figure><img src="..." alt="..."><figcaption><p>Caption</p></figcaption></figure>
   Mintlify: <Frame caption="Caption"><img src="..." alt="..." /></Frame>

2. GitBook: <figure><img src="..." alt="..."><figcaption></figcaption></figure>
   Mintlify: <Frame><img src="..." alt="..." /></Frame>

3. Simple <img> tags should also become <Frame><img /></Frame>
"""

import os
import re
import subprocess
from pathlib import Path

def get_original_figures_from_git(file_path):
    """Get original figure elements with and without captions from git history."""
    figures_data = {}
    
    try:
        # Get the original .md file from git history
        md_file_path = str(file_path).replace('.mdx', '.md')
        relative_md_path = Path(md_file_path).relative_to(Path.cwd())
        
        result = subprocess.run(
            ['git', 'show', f'HEAD:{relative_md_path}'],
            capture_output=True,
            text=True,
            cwd=Path.cwd()
        )
        
        if result.returncode == 0:
            content = result.stdout
            
            # Find all figures (with and without captions)
            figure_pattern = r'<figure><img([^>]*?)><figcaption>(?:<p>)?(.*?)(?:</p>)?</figcaption></figure>'
            matches = re.findall(figure_pattern, content, re.DOTALL)
            
            for img_attrs, caption_text in matches:
                caption_text = caption_text.strip()
                
                # Extract src to use as key
                src_match = re.search(r'src="([^"]*)"', img_attrs)
                if src_match:
                    original_src = src_match.group(1)
                    # Convert path format to match current paths
                    converted_src = original_src
                    if '../.gitbook/assets/' in original_src:
                        converted_src = original_src.replace('../.gitbook/assets/', '/images/')
                    elif '../../.gitbook/assets/' in original_src:
                        converted_src = original_src.replace('../../.gitbook/assets/', '/images/')
                    elif '../../../.gitbook/assets/' in original_src:
                        converted_src = original_src.replace('../../../.gitbook/assets/', '/images/')
                    
                    figures_data[converted_src] = {
                        'img_attrs': img_attrs,
                        'caption': caption_text if caption_text else None,
                        'original_src': original_src
                    }
    except Exception as e:
        print(f"  Warning: Could not check git history for {file_path}: {e}")
    
    return figures_data

def fix_all_figures(content, figures_data):
    """Convert all img tags and frames to proper Frame components."""
    
    # Pattern 1: Fix existing <Frame> that might be incorrect
    def fix_existing_frame(match):
        caption_attr = match.group(1) if match.group(1) else ""
        img_content = match.group(2)
        
        # Extract caption if present
        caption_match = re.search(r'caption="([^"]*)"', caption_attr)
        if caption_match:
            return f'<Frame caption="{caption_match.group(1)}">\n    {img_content}\n</Frame>'
        else:
            return f'<Frame>\n    {img_content}\n</Frame>'
    
    # Fix existing Frame components
    content = re.sub(
        r'<Frame([^>]*)>\s*([^<]*<img[^>]*/?>\s*[^<]*)\s*</Frame>',
        fix_existing_frame,
        content,
        flags=re.DOTALL
    )
    
    # Pattern 2: Convert standalone img tags to Frame components
    def convert_img_to_frame(match):
        img_tag = match.group(0)
        
        # Extract src to check if we have caption data
        src_match = re.search(r'src="([^"]*)"', img_tag)
        if src_match:
            src = src_match.group(1)
            
            # Check if this image should have a caption
            if src in figures_data and figures_data[src]['caption']:
                caption = figures_data[src]['caption']
                # Clean up the img tag
                if not img_tag.endswith('/>'):
                    img_tag = img_tag.rstrip('>') + ' />'
                return f'<Frame caption="{caption}">\n    {img_tag}\n</Frame>'
            else:
                # No caption needed, but still use Frame
                if not img_tag.endswith('/>'):
                    img_tag = img_tag.rstrip('>') + ' />'
                return f'<Frame>\n    {img_tag}\n</Frame>'
        
        # Fallback: just wrap in Frame
        if not img_tag.endswith('/>'):
            img_tag = img_tag.rstrip('>') + ' />'
        return f'<Frame>\n    {img_tag}\n</Frame>'
    
    # Convert standalone img tags (not already in Frame)
    # Look for img tags that are not already inside Frame components
    lines = content.split('\n')
    result_lines = []
    in_frame = False
    frame_depth = 0
    
    for line in lines:
        # Track Frame component depth
        frame_opens = len(re.findall(r'<Frame[^>]*>', line))
        frame_closes = len(re.findall(r'</Frame>', line))
        frame_depth += frame_opens - frame_closes
        in_frame = frame_depth > 0
        
        # If we find an img tag that's not in a Frame, convert it
        if not in_frame and '<img ' in line and not line.strip().startswith('//') and not line.strip().startswith('<!--'):
            img_match = re.search(r'<img[^>]*/?>', line)
            if img_match:
                img_tag = img_match.group(0)
                indentation = line[:line.find('<img')]
                
                # Check if this image should have a caption
                src_match = re.search(r'src="([^"]*)"', img_tag)
                if src_match and src_match.group(1) in figures_data:
                    fig_data = figures_data[src_match.group(1)]
                    if fig_data['caption']:
                        caption = fig_data['caption']
                        if not img_tag.endswith('/>'):
                            img_tag = img_tag.rstrip('>') + ' />'
                        result_lines.append(f'{indentation}<Frame caption="{caption}">')
                        result_lines.append(f'{indentation}    {img_tag}')
                        result_lines.append(f'{indentation}</Frame>')
                        continue
                
                # No caption, but still use Frame
                if not img_tag.endswith('/>'):
                    img_tag = img_tag.rstrip('>') + ' />'
                result_lines.append(f'{indentation}<Frame>')
                result_lines.append(f'{indentation}    {img_tag}')
                result_lines.append(f'{indentation}</Frame>')
                continue
        
        result_lines.append(line)
    
    return '\n'.join(result_lines)

def process_file(file_path):
    """Process a single MDX file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Get original figures data from git history
        figures_data = get_original_figures_from_git(file_path)
        
        # Apply figure fixes
        content = fix_all_figures(content, figures_data)
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, len(figures_data)
        
        return False, len(figures_data)
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, 0

def main():
    """Main function to process all MDX files."""
    
    # Get repository root
    script_dir = Path(__file__).parent.absolute()
    repo_root = script_dir.parent
    
    print("🖼️  Fixing ALL GitBook figure conversions to use Frame components...")
    print("=" * 70)
    
    # Find all .mdx files
    mdx_files = list(repo_root.glob('**/*.mdx'))
    
    # Filter out files in certain directories
    excluded_dirs = {'.tmp', 'node_modules', '.git', 'legacy'}
    mdx_files = [f for f in mdx_files if not any(part in excluded_dirs for part in f.parts)]
    
    fixed_count = 0
    total_files = len(mdx_files)
    
    print(f"Found {total_files} MDX files to process...")
    print()
    
    for file_path in mdx_files:
        relative_path = file_path.relative_to(repo_root)
        
        changed, figures_count = process_file(file_path)
        
        if changed:
            print(f"✅ Fixed: {relative_path} ({figures_count} figures)")
            fixed_count += 1
        else:
            if figures_count > 0:
                print(f"⚪ Already correct: {relative_path} ({figures_count} figures)")
            else:
                print(f"⚪ No figures: {relative_path}")
    
    print()
    print("=" * 70)
    print(f"📊 SUMMARY:")
    print(f"   - Files processed: {total_files}")
    print(f"   - Files fixed: {fixed_count}")
    
    if fixed_count > 0:
        print(f"\n🎉 All figures converted to Frame components!")
        print(f"📝 Rules applied:")
        print(f"   - Figures with captions: <Frame caption=\"...\">")
        print(f"   - Figures without captions: <Frame>")
    else:
        print(f"\n✨ All figures already properly converted!")

if __name__ == "__main__":
    main()