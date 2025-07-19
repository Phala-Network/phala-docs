#!/usr/bin/env python3
"""
Script to fix remaining broken links after initial fixes.
"""

import os
import re
from pathlib import Path

def fix_specific_links(content, file_path):
    """Fix specific broken links based on the broken-links output."""
    
    # Get the relative path for context
    relative_path = str(file_path.relative_to(Path.cwd()))
    
    # Fix based on specific files
    if 'compute-providers/gatekeeper/index.mdx' in relative_path:
        content = re.sub(r'collator\.md', 'collator.mdx', content)
        content = re.sub(r'gatekeeper\.md', 'gatekeeper.mdx', content)
    
    elif 'compute-providers/basic-info/budget-balancer.mdx' in relative_path:
        content = re.sub(r'worker-rewards\.md', 'worker-rewards.mdx', content)
    
    elif 'phala-cloud/getting-started/explore-templates/index.mdx' in relative_path:
        content = re.sub(r'launch-an-eliza-agent\.md', 'launch-an-eliza-agent.mdx', content)
        content = re.sub(r'start-from-template\.md', 'start-from-template.mdx', content)
    
    # Fix path issues
    elif 'cloud/getting-started/' in relative_path:
        # These are in cloud/getting-started/ but linking to files in the same directory
        content = re.sub(r'sign-up-for-cloud-account\.mdx', '../getting-started/sign-up-for-cloud-account.mdx', content)
        content = re.sub(r'start-from-cloud-ui\.mdx', '../getting-started/start-from-cloud-ui.mdx', content)
        content = re.sub(r'start-from-cloud-cli\.mdx', '../../phala-cloud/phala-cloud-user-guides/advanced-deployment-options/start-from-cloud-cli.mdx', content)
        content = re.sub(r'start-from-template\.mdx', '../../phala-cloud/getting-started/explore-templates/start-from-template.mdx', content)
        content = re.sub(r'start-from-scratch\.mdx', '#start-from-scratch', content)  # Convert to anchor
    
    elif 'cloud/use-cases/tee_with_fhe_and_mpc.mdx' in relative_path:
        content = re.sub(r'\.\./cloud/create-cvm/create-with-docker-compose\.mdx', '../../phala-cloud/phala-cloud-user-guides/create-cvm/create-with-docker-compose.mdx', content)
    
    # Fix overview/pha-token paths - remove broken reference paths
    elif 'overview/pha-token/governance/' in relative_path:
        content = re.sub(r'\.\./\.\./\.\./pha-token/governance/broken-reference/', '', content)
    
    # Fix overview/pha-token/introduction.mdx
    elif 'overview/pha-token/introduction.mdx' in relative_path:
        content = re.sub(r'\]\(governance/\)', '](governance/index.mdx)', content)
        content = re.sub(r'\]\(delegation/\)', '](delegation/index.mdx)', content)
    
    # Fix overview/phala-network/dstack.mdx
    elif 'overview/phala-network/dstack.mdx' in relative_path:
        content = re.sub(r'phala-cloud\.mdx', 'phala-cloud.mdx', content)
    
    # Fix legacy references
    elif 'references/hackathon-guides/ethglobal-singapore.mdx' in relative_path:
        content = re.sub(r'\.\./\.\./ai-agent-contract-legacy/getting-started/ai-agent-contract-templates\.mdx', '#legacy-content-removed', content)
    
    # Fix references/faq.mdx
    elif 'references/faq.mdx' in relative_path:
        content = re.sub(r'\.\./developers/support/broken-reference/', '', content)
    
    # Fix awesome phat contracts image reference
    elif 'references/advanced-topics/run-local-testnet.mdx' in relative_path:
        content = re.sub(r'\.\./\.\./images/awesome%20phat%20contracts%20\(2\)/', '/images/awesome phat contracts (2)', content)
    
    # Fix phala-cloud design-documents reference
    elif 'phala-cloud/getting-started/explore-templates/start-from-template.mdx' in relative_path:
        content = re.sub(r'\.\./\.\./\.\./design-documents/', '../../../dstack/design-documents/', content)
    
    return content

def process_file(file_path):
    """Process a single MDX file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply specific fixes
        content = fix_specific_links(content, file_path)
        
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
    """Main function."""
    
    # Get repository root
    repo_root = Path.cwd()
    
    print("🔧 Fixing remaining broken links...")
    print("=" * 50)
    
    # Files with known issues based on mint broken-links output
    problem_files = [
        "cloud/getting-started/getting-started.mdx",
        "cloud/getting-started/index.mdx", 
        "cloud/getting-started/start-from-cloud-ui.mdx",
        "cloud/use-cases/tee_with_fhe_and_mpc.mdx",
        "cloud/use-cases/use-cases.mdx",
        "compute-providers/basic-info/budget-balancer.mdx",
        "compute-providers/gatekeeper/index.mdx",
        "overview/pha-token/governance/khala-treasury.mdx",
        "overview/pha-token/governance/setup-account-identity.mdx",
        "overview/pha-token/introduction.mdx",
        "overview/phala-network/dstack.mdx",
        "phala-cloud/getting-started/explore-templates/index.mdx",
        "phala-cloud/getting-started/explore-templates/start-from-template.mdx",
        "references/advanced-topics/run-local-testnet.mdx",
        "references/faq.mdx",
        "references/hackathon-guides/ethglobal-singapore.mdx",
    ]
    
    fixed_count = 0
    
    for file_path_str in problem_files:
        file_path = repo_root / file_path_str
        if file_path.exists():
            if process_file(file_path):
                print(f"✅ Fixed: {file_path_str}")
                fixed_count += 1
            else:
                print(f"⚪ No changes: {file_path_str}")
        else:
            print(f"❌ Not found: {file_path_str}")
    
    print()
    print("=" * 50)
    print(f"📊 SUMMARY: Fixed {fixed_count} additional files")

if __name__ == "__main__":
    main()