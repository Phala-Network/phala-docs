#!/usr/bin/env python3
"""
Script to restore and fix GitBook figure conversions with proper captions.

This script:
1. Checks git history for original figure elements with captions
2. Restores captions that were lost during conversion
3. Converts to proper Mintlify Figure component format

Example conversion:
GitBook: <figure><img src="..." alt="..."><figcaption><p>Caption text</p></figcaption></figure>
Mintlify: <Figure caption="Caption text"><img src="..." alt="..." /></Figure>
"""

import os
import re
import subprocess
from pathlib import Path

def get_original_figures_from_git(file_path):
    """Get original figure elements with captions from git history."""
    figures_with_captions = {}
    
    try:
        # Get the original .md file from git history
        md_file_path = str(file_path).replace('.mdx', '.md')
        
        # Convert to relative path from repo root
        relative_md_path = Path(md_file_path).relative_to(Path.cwd())
        
        result = subprocess.run(
            ['git', 'show', f'HEAD:{relative_md_path}'],
            capture_output=True,
            text=True,
            cwd=Path.cwd()
        )
        
        if result.returncode == 0:
            content = result.stdout
            
            # Find all figures with captions
            figure_pattern = r'<figure><img([^>]*?)><figcaption>(?:<p>)?(.*?)(?:</p>)?</figcaption></figure>'
            matches = re.findall(figure_pattern, content, re.DOTALL)
            
            for img_attrs, caption_text in matches:
                caption_text = caption_text.strip()
                if caption_text:  # Only process non-empty captions
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
                        
                        figures_with_captions[converted_src] = {
                            'img_attrs': img_attrs,
                            'caption': caption_text,
                            'original_src': original_src
                        }
    except Exception as e:
        print(f"  Warning: Could not check git history for {file_path}: {e}")
    
    return figures_with_captions

def fix_figure_captions(content, figures_with_captions):
    """Fix figure elements by restoring captions and converting to Mintlify format."""
    
    if not figures_with_captions:
        return content
    
    # Find current img tags that should have captions
    img_pattern = r'<img([^>]*?)/?>'
    
    def replace_img_with_figure(match):
        img_attrs = match.group(1)
        
        # Extract src to match with our captions
        src_match = re.search(r'src="([^"]*)"', img_attrs)
        if not src_match:
            return match.group(0)  # Return original if no src found
        
        src = src_match.group(1)
        
        # Check if this image should have a caption
        if src in figures_with_captions:
            caption = figures_with_captions[src]['caption']
            
            # Clean up img attributes and ensure proper self-closing
            img_tag = f'<img{img_attrs}'
            if not img_tag.endswith('/>') and not img_tag.endswith('>'):
                img_tag += ' />'
            elif img_tag.endswith('>') and not img_tag.endswith('/>'):
                img_tag = img_tag[:-1] + ' />'
            
            # Convert to Figure component
            return f'<Figure caption="{caption}">\n    {img_tag}\n</Figure>'
        
        # Return original img tag if no caption needed
        return match.group(0)
    
    # Replace img tags that should have captions
    content = re.sub(img_pattern, replace_img_with_figure, content)
    
    return content

def process_file(file_path):
    """Process a single MDX file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Get original figures with captions from git history
        figures_with_captions = get_original_figures_from_git(file_path)
        
        if figures_with_captions:
            print(f"  Found {len(figures_with_captions)} figures with captions in git history")
            for src, data in figures_with_captions.items():
                print(f"    - {src}: \"{data['caption'][:50]}{'...' if len(data['caption']) > 50 else ''}\"")
            
            # Apply figure caption fixes
            content = fix_figure_captions(content, figures_with_captions)
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, len(figures_with_captions)
        
        return False, 0
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, 0

def main():
    """Main function to process all MDX files."""
    
    # Get repository root
    script_dir = Path(__file__).parent.absolute()
    repo_root = script_dir.parent
    
    print("🖼️  Restoring GitBook figure captions and converting to Mintlify format...")
    print("=" * 70)
    
    # List of files that should have captions based on our research
    files_with_captions = [
        'cloud/getting-started/start-from-cloud-ui.mdx',
        'compute-providers/basic-info/staking-mechanism.mdx', 
        'dstack/design-documents/whitepaper.mdx',
        'phala-cloud/getting-started/explore-templates/start-from-template.mdx',
        'phala-cloud/phala-cloud-user-guides/advanced-deployment-options/start-from-cloud-cli.mdx',
        'phala-cloud/phala-cloud-user-guides/create-cvm/debugging-and-analyzing-logs/check-logs.mdx',
        'phala-cloud/phala-cloud-user-guides/create-cvm/set-secure-environment-variables.mdx',
        'references/advanced-topics/run-local-testnet.mdx',
        'references/subbridge/asset-integration-guide.mdx',
        'references/subbridge/technical-details.mdx',
    ]
    
    fixed_count = 0
    total_captions_restored = 0
    
    print(f"Processing {len(files_with_captions)} files that should have figure captions...")
    print()
    
    for file_rel_path in files_with_captions:
        file_path = repo_root / file_rel_path
        
        if not file_path.exists():
            print(f"⚠️  File not found: {file_rel_path}")
            continue
        
        print(f"📁 Processing: {file_rel_path}")
        
        changed, captions_count = process_file(file_path)
        
        if changed:
            print(f"✅ Fixed: Restored {captions_count} figure captions")
            fixed_count += 1
            total_captions_restored += captions_count
        else:
            print(f"⚪ No changes needed")
        
        print()
    
    print("=" * 70)
    print(f"📊 SUMMARY:")
    print(f"   - Files processed: {len(files_with_captions)}")  
    print(f"   - Files fixed: {fixed_count}")
    print(f"   - Total captions restored: {total_captions_restored}")
    
    if fixed_count > 0:
        print(f"\n🎉 Figure captions restored and converted to Mintlify format!")
        print(f"📝 Use <Figure caption=\"...\"> component for images with captions")
    else:
        print(f"\n✨ All figure captions already properly converted!")

if __name__ == "__main__":
    main()