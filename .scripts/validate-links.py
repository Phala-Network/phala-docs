#!/usr/bin/env python3
"""
Script to validate that all files referenced in gitbook-redirects.csv actually exist
and that their corresponding URLs are accessible on the production GitBook domain.
This helps identify potential 404 links before setting up redirects.
"""

import csv
import os
import sys
import requests
import time
from pathlib import Path
from urllib.parse import urljoin

def check_url_accessibility(url, timeout=10):
    """
    Check if a URL is accessible and returns 200 status using HEAD request.
    HEAD requests are faster and less disruptive than GET requests.
    
    Args:
        url: URL to check
        timeout: Request timeout in seconds
    
    Returns:
        tuple: (is_accessible, status_code, error_message)
    """
    try:
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        return response.status_code == 200, response.status_code, None
    except requests.exceptions.Timeout:
        return False, None, "Timeout"
    except requests.exceptions.ConnectionError:
        return False, None, "Connection Error"
    except requests.exceptions.RequestException as e:
        return False, None, str(e)

def validate_redirects(csv_file_path, repo_root, check_production=False, production_domain="https://docs.phala.network"):
    """
    Validate that all source files in the CSV exist in the repository.
    Optionally check if URLs are accessible on production domain.
    
    Args:
        csv_file_path: Path to the gitbook-redirects.csv file
        repo_root: Root directory of the repository
        check_production: Whether to check URLs against production domain
        production_domain: Base URL of the production GitBook site
    
    Returns:
        tuple: (missing_files, broken_urls, total_files)
    """
    missing_files = []
    broken_urls = []
    total_files = 0
    
    print(f"🔍 Validating files from: {csv_file_path}")
    print(f"📁 Repository root: {repo_root}")
    if check_production:
        print(f"🌐 Production domain: {production_domain}")
    print("-" * 60)
    
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                source_file = row['Source File']
                gitbook_url = row['GitBook URL']
                section = row['Section']
                
                # Construct full file path
                full_path = os.path.join(repo_root, source_file)
                total_files += 1
                
                # Check if file exists locally
                file_exists = os.path.exists(full_path)
                if not file_exists:
                    missing_files.append({
                        'source_file': source_file,
                        'gitbook_url': gitbook_url,
                        'section': section,
                        'full_path': full_path
                    })
                
                # Check production URL if requested and file exists locally
                url_accessible = None
                url_status = None
                url_error = None
                
                if check_production and file_exists:
                    # Construct full production URL
                    full_url = urljoin(production_domain, gitbook_url)
                    url_accessible, url_status, url_error = check_url_accessibility(full_url)
                    
                    if not url_accessible:
                        broken_urls.append({
                            'source_file': source_file,
                            'gitbook_url': gitbook_url,
                            'full_url': full_url,
                            'section': section,
                            'status_code': url_status,
                            'error': url_error
                        })
                    
                    # Add small delay to be respectful to the server
                    time.sleep(0.1)
                
                # Print status
                if check_production and file_exists:
                    if url_accessible:
                        print(f"✅ EXISTS & LIVE: {source_file} → {gitbook_url}")
                    else:
                        status_info = f"({url_status})" if url_status else f"({url_error})"
                        print(f"⚠️  EXISTS & DEAD: {source_file} → {gitbook_url} {status_info}")
                elif file_exists:
                    print(f"✅ EXISTS: {source_file}")
                else:
                    print(f"❌ MISSING: {source_file}")
                    
    except FileNotFoundError:
        print(f"❌ ERROR: CSV file not found: {csv_file_path}")
        return [], [], 0
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        return [], [], 0
    
    return missing_files, broken_urls, total_files

def main():
    import argparse
    
    # Set up command line arguments
    parser = argparse.ArgumentParser(description='Validate GitBook redirect links')
    parser.add_argument('--check-production', '-p', action='store_true',
                        help='Check URLs against production GitBook domain')
    parser.add_argument('--domain', '-d', default='https://docs.phala.network',
                        help='Production domain to check against (default: https://docs.phala.network)')
    parser.add_argument('--timeout', '-t', type=int, default=10,
                        help='HTTP request timeout in seconds (default: 10)')
    
    args = parser.parse_args()
    
    # Get repository root (parent of .scripts directory)
    script_dir = Path(__file__).parent.absolute()
    repo_root = script_dir.parent
    
    # Paths
    csv_file = repo_root / "gitbook-redirects.csv"
    
    print("🚀 GitBook Links Validator")
    print("=" * 60)
    
    if args.check_production:
        print(f"🌐 Production mode: Checking URLs against {args.domain}")
        print(f"⏱️  Request timeout: {args.timeout}s")
        print("=" * 60)
    
    # Validate files
    missing_files, broken_urls, total_files = validate_redirects(
        csv_file, repo_root, args.check_production, args.domain
    )
    
    # Print summary
    print("\n" + "=" * 60)
    print("📊 VALIDATION SUMMARY")
    print("=" * 60)
    
    has_errors = bool(missing_files or broken_urls)
    
    # Report missing files
    if missing_files:
        print(f"❌ Found {len(missing_files)} missing files out of {total_files} total files")
        print("\n🔍 MISSING FILES DETAILS:")
        print("-" * 40)
        
        for file_info in missing_files:
            print(f"File: {file_info['source_file']}")
            print(f"  ↳ URL: {file_info['gitbook_url']}")
            print(f"  ↳ Section: {file_info['section']}")
            print(f"  ↳ Full path: {file_info['full_path']}")
            print()
    
    # Report broken URLs
    if broken_urls:
        print(f"❌ Found {len(broken_urls)} broken URLs out of {total_files - len(missing_files)} checked URLs")
        print("\n🔗 BROKEN URLS DETAILS:")
        print("-" * 40)
        
        for url_info in broken_urls:
            print(f"URL: {url_info['full_url']}")
            print(f"  ↳ Source: {url_info['source_file']}")
            print(f"  ↳ Section: {url_info['section']}")
            if url_info['status_code']:
                print(f"  ↳ Status: {url_info['status_code']}")
            if url_info['error']:
                print(f"  ↳ Error: {url_info['error']}")
            print()
    
    # Print recommendations and final status
    if has_errors:
        print("⚠️  RECOMMENDATIONS:")
        if missing_files:
            print("   - Remove missing files from gitbook-redirects.csv, OR")
            print("   - Create the missing files if they should exist")
        if broken_urls:
            print("   - Check if broken URLs have different paths on GitBook")
            print("   - Verify the production domain is correct")
            print("   - Some URLs might be redirected or require authentication")
        
        # Exit with error code
        sys.exit(1)
    else:
        if args.check_production:
            print(f"✅ All {total_files} files exist and all URLs are accessible!")
            print("🎉 No missing files or broken links detected - ready for redirect setup!")
        else:
            print(f"✅ All {total_files} files exist and are valid!")
            print("🎉 No missing files detected - ready for redirect setup!")
            print("💡 Run with --check-production to also validate URLs against production domain")
        
        # Exit successfully
        sys.exit(0)

if __name__ == "__main__":
    main()