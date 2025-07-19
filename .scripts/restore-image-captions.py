#!/usr/bin/env python3
"""
Script to restore image captions using Mintlify Frame components.
Converts images with descriptive alt text back to Frame components with captions.
"""

import re
from pathlib import Path

def restore_captions_in_content(content):
    """Convert images with descriptive alt text to Frame components with captions."""
    
    # Pattern to match images with descriptive alt text that should be captions
    # Look for images with alt text that looks like captions (contains spaces, describes the image)
    img_pattern = r'<img src="([^"]*)" alt="([^"]*)" (?:[^>]*)?/?>'
    
    def replace_with_frame(match):
        src = match.group(1)
        alt_text = match.group(2)
        
        # Check if alt text looks like a caption (not just "Screenshot" or empty)
        if (alt_text and 
            alt_text not in ["Screenshot", "Image", "Picture", ""] and
            (len(alt_text) > 10 or any(word in alt_text.lower() for word in 
                ["figure", "showing", "interface", "deployment", "configuration", 
                 "architecture", "logs", "attestation", "dashboard", "notebook",
                 "endpoints", "resources", "secrets", "staking", "docker", "cvm",
                 "worker", "mining", "node", "blockchain", "network", "setup"]))):
            
            # Create Frame component with caption
            return f'<Frame caption="{alt_text}">\n  <img src="{src}" alt="{alt_text}" />\n</Frame>'
        else:
            # Keep as regular image
            return match.group(0)
    
    # Apply the replacement
    content = re.sub(img_pattern, replace_with_frame, content)
    
    return content

def process_file(file_path):
    """Process a single MDX file to restore captions."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply caption restoration
        content = restore_captions_in_content(content)
        
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
    
    print("🖼️  Restoring image captions using Frame components...")
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
            print(f"✅ Restored captions: {relative_path}")
            fixed_count += 1
        else:
            print(f"⚪ No changes: {relative_path}")
    
    print()
    print("=" * 60)
    print(f"📊 SUMMARY: Restored captions in {fixed_count} out of {total_count} files")
    
    if fixed_count > 0:
        print("\n🎉 Image captions restored using Frame components!")
        print("   Images with descriptive content now have proper captions.")
    else:
        print("\n✨ No caption restoration needed!")

if __name__ == "__main__":
    main()