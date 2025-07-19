#!/usr/bin/env python3
"""
Add proper frontmatter (title and description) to all MDX files that need it.
"""

import os
import re
from pathlib import Path

def get_title_from_content(file_path):
    """Extract title from the first heading in the file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove frontmatter if present
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                content = parts[2]
        
        # Find first heading
        heading_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if heading_match:
            title = heading_match.group(1).strip()
            # Clean up title (remove emojis)
            title = re.sub(r'[🚀🛡️🪙🥷📊⚡🔧🎯💻📝🌍🔗🙃🏃‍♀🦿🔒❓⛓👩‍🏎🔐🪨❓🤹🌉🔐🆘🤯⚖💎🗳👐💎🔐❓]', '', title).strip()
            return title
        
        # Fallback to filename
        return file_path.stem.replace('-', ' ').replace('_', ' ').title()
        
    except Exception as e:
        return file_path.stem.replace('-', ' ').replace('_', ' ').title()

def generate_description(title, file_path):
    """Generate a description based on the title and file path."""
    
    # Custom descriptions for different sections
    path_str = str(file_path)
    
    if 'gpu-tee' in path_str:
        if 'api' in path_str:
            return f"Secure LLM inference API running in GPU Trusted Execution Environment (TEE) for confidential AI computing."
        elif 'benchmark' in path_str:
            return f"Performance benchmarks and metrics for LLM inference in GPU TEE environments."
        elif 'faqs' in path_str:
            return f"Frequently asked questions about GPU TEE and confidential AI computing."
        else:
            return f"Run Large Language Models securely in GPU Trusted Execution Environment (TEE) for confidential AI."
    
    elif 'dstack' in path_str:
        if 'getting-started' in path_str:
            return f"Set up and deploy your first confidential application using Dstack TEE infrastructure."
        elif 'design-documents' in path_str:
            return f"Technical design documents and architecture details for the Dstack TEE platform."
        elif 'hardware' in path_str:
            return f"Hardware requirements and specifications for running Dstack TEE infrastructure."
        else:
            return f"Deploy confidential applications with Dstack - a TEE-based infrastructure platform."
    
    elif 'compute-providers' in path_str:
        if 'basic-info' in path_str:
            if 'rewards' in path_str:
                return f"Understand how compute providers earn PHA rewards through the Gemini tokenomics system."
            elif 'staking' in path_str:
                return f"Learn about the staking mechanism for Phala Network compute providers."
            else:
                return f"Essential information for becoming a compute provider on Phala Network."
        elif 'gatekeeper' in path_str:
            return f"Manage blockchain consensus and validation as a Gatekeeper on Phala Network."
        elif 'workers' in path_str:
            return f"Deploy and manage worker nodes to provide computing power on Phala Network."
        else:
            return f"Provide computing power and earn rewards as a compute provider on Phala Network."
    
    elif 'phala-cloud' in path_str or 'cloud' in path_str:
        if 'getting-started' in path_str:
            return f"Quick start guide for deploying confidential applications on Phala Cloud."
        elif 'template' in path_str:
            return f"Ready-to-use templates for rapid deployment on Phala Cloud TEE infrastructure."
        elif 'cvm' in path_str:
            return f"Create and manage Confidential Virtual Machines (CVMs) on Phala Cloud."
        elif 'production' in path_str:
            return f"Best practices and guidelines for production deployments on Phala Cloud."
        elif 'attestation' in path_str or 'security' in path_str:
            return f"Security features and remote attestation capabilities of Phala Cloud TEE."
        elif 'use-cases' in path_str:
            if 'ai' in path_str:
                return f"Build confidential AI applications with Trusted Execution Environment technology."
            elif 'fhe' in path_str or 'mpc' in path_str:
                return f"Combine TEE with FHE and MPC for enhanced privacy-preserving computations."
            elif 'zk' in path_str:
                return f"Integrate Zero-Knowledge proofs with TEE for verifiable private computing."
            else:
                return f"Explore real-world applications and use cases for TEE technology."
        else:
            return f"Deploy confidential applications with Phala Cloud's managed TEE infrastructure."
    
    elif 'overview' in path_str:
        if 'pha-token' in path_str:
            if 'governance' in path_str:
                return f"Participate in Phala Network governance using PHA tokens and democratic processes."
            elif 'delegation' in path_str:
                return f"Delegate PHA tokens to earn rewards and support network security."
            else:
                return f"Learn about PHA token utility, staking, and participation in the Phala ecosystem."
        else:
            return f"Overview of Phala Network's decentralized computing infrastructure and features."
    
    elif 'references' in path_str:
        if 'subbridge' in path_str:
            return f"Cross-chain bridge for transferring assets between Phala and other blockchains."
        elif 'support' in path_str:
            return f"Support resources, endpoints, and compatibility information for Phala Network."
        elif 'hackathon' in path_str:
            return f"Resources and guides for building on Phala Network during hackathons."
        elif 'advanced' in path_str:
            return f"Advanced technical topics and development patterns for Phala Network."
        else:
            return f"Reference documentation and resources for Phala Network development."
    
    elif 'tech-specs' in path_str:
        return f"Technical specifications and blockchain architecture details for Phala Network."
    
    # Generic fallback
    return f"Documentation for {title.lower()} on Phala Network."

def add_frontmatter_to_file(file_path):
    """Add or update frontmatter for a single file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file already has frontmatter
        has_frontmatter = content.startswith('---')
        
        # Get title from content
        title = get_title_from_content(file_path)
        description = generate_description(title, file_path)
        
        if has_frontmatter:
            # Update existing frontmatter
            frontmatter_match = re.match(r'^---\n(.*?)\n---(.*)$', content, re.DOTALL)
            if frontmatter_match:
                existing_frontmatter = frontmatter_match.group(1)
                body_content = frontmatter_match.group(2)
                
                # Check if title exists
                if not re.search(r'^title:', existing_frontmatter, re.MULTILINE):
                    existing_frontmatter = f"title: {title}\n{existing_frontmatter}"
                
                # Check if description exists
                if not re.search(r'^description:', existing_frontmatter, re.MULTILINE):
                    existing_frontmatter = f"{existing_frontmatter}\ndescription: {description}"
                
                new_content = f"---\n{existing_frontmatter}\n---{body_content}"
            else:
                # Malformed frontmatter, replace it
                new_content = f"---\ntitle: {title}\ndescription: {description}\n---\n\n{content[content.find('---', 3) + 3:]}"
        else:
            # Add new frontmatter
            new_content = f"---\ntitle: {title}\ndescription: {description}\n---\n\n{content}"
        
        # Only write if content changed
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main function to add frontmatter to all MDX files."""
    
    repo_root = Path.cwd()
    
    print("📝 Adding frontmatter to MDX files...")
    print("=" * 50)
    
    # Find all .mdx files
    mdx_files = list(repo_root.glob('**/*.mdx'))
    
    # Filter out files in certain directories
    excluded_dirs = {'.tmp', 'node_modules', '.git', 'legacy'}
    mdx_files = [f for f in mdx_files if not any(part in excluded_dirs for part in f.parts)]
    
    updated_count = 0
    total_count = len(mdx_files)
    
    print(f"Found {total_count} MDX files to process...")
    print()
    
    for file_path in mdx_files:
        relative_path = file_path.relative_to(repo_root)
        
        if add_frontmatter_to_file(file_path):
            print(f"✅ Updated: {relative_path}")
            updated_count += 1
        else:
            print(f"⚪ No changes: {relative_path}")
    
    print()
    print("=" * 50)
    print(f"📊 SUMMARY: Updated frontmatter in {updated_count} out of {total_count} files")
    
    if updated_count > 0:
        print(f"\n🎉 Frontmatter added successfully!")
        print(f"📝 All files now have title and description fields")
    else:
        print(f"\n✨ All files already have proper frontmatter!")

if __name__ == "__main__":
    main()