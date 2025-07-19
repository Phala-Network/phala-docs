#!/usr/bin/env python3
"""
Script to fix remaining MDX parsing errors from the mint dev output.
Targets specific issues found in the error log.
"""

import re
from pathlib import Path

def fix_double_slash_paths(content):
    """Fix double slash paths like ../..//images/"""
    return re.sub(r'(\.\./)*//images/', '/images/', content)

def fix_unclosed_tags(content):
    """Fix unclosed HTML tags and structural issues."""
    
    # Fix <br> tags without closing
    content = re.sub(r'<br>(?!</br>)', '<br />', content)
    
    # Fix unclosed <img> tags followed by paragraph endings
    content = re.sub(r'<img([^>]*?)>(?!</)', r'<img\1 />', content)
    
    # Fix unclosed <code> tags in paragraphs
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        # If line has opening <code> but no closing </code>, add it
        if '<code>' in line and '</code>' not in line and line.strip().endswith('>'):
            line = line.replace('<code>', '`').replace('>', '`')
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_invalid_jsx_expressions(content):
    """Fix invalid JSX expressions that can't be parsed."""
    
    lines = content.split('\n')
    fixed_lines = []
    
    for line_num, line in enumerate(lines, 1):
        original_line = line
        
        # Fix lines starting with { that cause acorn parsing errors
        if re.match(r'^\s*\{[^}]*$', line.strip()):
            line = f'<!-- {line.strip()} -->'
        
        # Fix invalid component names with numbers at start
        if re.search(r'<[0-9]', line):
            line = re.sub(r'<([0-9][^>]*?)>', r'<!-- <\1> -->', line)
        
        # Fix component names with invalid characters like !
        if re.search(r'<[^a-zA-Z/!-]', line):
            line = re.sub(r'<([^a-zA-Z/][^>]*?)>', r'<!-- <\1> -->', line)
        
        # Fix lines with ! at start of component names
        line = re.sub(r'<\s*!\s*([^>]*?)>', r'<!-- <!\1> -->', line)
        
        # Fix unclosed <strong> tags
        if '<strong>' in line and '</strong>' not in line and not line.strip().endswith('</strong>'):
            line = line.replace('<strong>', '**').replace('</strong>', '**')
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_details_figure_mismatch(content):
    """Fix mismatched <details> and </figure> tags."""
    
    # Replace orphaned </figure> tags that should be </details>
    lines = content.split('\n')
    fixed_lines = []
    open_details = False
    
    for line in lines:
        if '<details>' in line:
            open_details = True
        elif '</details>' in line:
            open_details = False
        elif '</figure>' in line and open_details:
            line = line.replace('</figure>', '</details>')
            open_details = False
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_table_br_tags(content):
    """Fix <br> tags in table cells that aren't properly closed."""
    
    # In table contexts, fix <br> followed by </td> or </p>
    content = re.sub(r'<br>\s*(</(?:td|p)>)', r'<br />\1', content)
    
    return content

def process_file(file_path):
    """Process a single MDX file to fix remaining issues."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply all fixes
        content = fix_double_slash_paths(content)
        content = fix_unclosed_tags(content)
        content = fix_invalid_jsx_expressions(content)
        content = fix_details_figure_mismatch(content)
        content = fix_table_br_tags(content)
        
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
    """Main function to process problematic files."""
    
    # Get repository root
    script_dir = Path(__file__).parent.absolute()
    repo_root = script_dir.parent
    
    print("🔧 Fixing remaining MDX parsing issues...")
    print("=" * 60)
    
    # List of specific files with errors from the mint dev output
    problematic_files = [
        "cloud/getting-started/start-from-cloud-ui.mdx",
        "compute-providers/basic-info/staking-mechanism.mdx",
        "compute-providers/run-workers-on-khala/prb-worker-deployment.mdx",
        "compute-providers/run-workers-on-khala/troubleshooting.mdx",
        "compute-providers/run-workers-on-phala/prb-worker-deployment.mdx",
        "compute-providers/run-workers-on-phala/prbv3-deployment.mdx",
        "compute-providers/run-workers-on-phala/solo-worker-deployment.mdx",
        "dstack/design-documents/whitepaper.mdx",
        "overview/pha-token/delegation/index.mdx",
        "overview/pha-token/governance/setup-account-identity.mdx",
        "phala-cloud/getting-started/explore-templates/start-from-template.mdx",
        "phala-cloud/phala-cloud-user-guides/advanced-deployment-options/setup-a-ci-cd-pipeline.mdx",
        "phala-cloud/phala-cloud-user-guides/advanced-deployment-options/start-from-cloud-cli.mdx",
        "phala-cloud/phala-cloud-user-guides/building-with-tee/setting-up-custom-domain.mdx",
        "phala-cloud/phala-cloud-user-guides/create-cvm/debugging-and-analyzing-logs/check-logs.mdx",
        "phala-cloud/phala-cloud-user-guides/create-cvm/set-secure-environment-variables.mdx",
        "references/advanced-topics/run-local-testnet.mdx",
        "references/basic-guidance/get-pha-and-transfer.mdx",
        "references/basic-guidance/index.mdx",
        "references/faq.mdx",
        "references/hackathon-guides/ethglobal-bangkok.mdx",
        "references/hackathon-guides/ethglobal-san-francisco.mdx",
        "references/subbridge/cross-chain-transfer.mdx",
        "references/subbridge/asset-integration-guide.mdx",
        "references/subbridge/technical-details.mdx",
        "references/support/compatibility-matrix.mdx",
        "references/support/endpoints.mdx",
        "references/support/faucet.mdx",
        "references/support/transaction-costs.mdx"
    ]
    
    # Also scan for any files with double slash paths
    all_mdx_files = list(repo_root.glob('**/*.mdx'))
    additional_files = []
    
    for file_path in all_mdx_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if '../..//images/' in content:
                    rel_path = str(file_path.relative_to(repo_root))
                    if rel_path not in problematic_files:
                        additional_files.append(rel_path)
        except:
            continue
    
    all_files_to_fix = problematic_files + additional_files
    fixed_count = 0
    total_count = len(all_files_to_fix)
    
    print(f"Found {total_count} files to fix...")
    print()
    
    for file_rel_path in all_files_to_fix:
        file_path = repo_root / file_rel_path
        
        if not file_path.exists():
            print(f"⚠️  File not found: {file_rel_path}")
            continue
        
        if process_file(file_path):
            print(f"✅ Fixed: {file_rel_path}")
            fixed_count += 1
        else:
            print(f"⚪ No changes: {file_rel_path}")
    
    print()
    print("=" * 60)
    print(f"📊 SUMMARY: Fixed {fixed_count} out of {total_count} files")
    
    if fixed_count > 0:
        print("\n🎉 Additional MDX fixes applied!")
        print("   Test with 'mint dev' to see remaining issues.")
    else:
        print("\n✨ No additional fixes were needed!")

if __name__ == "__main__":
    main()