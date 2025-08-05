#!/usr/bin/env python3
"""
URL Validator for Sovereign Debt Weekly Digest
Validates all URLs in the JSON file to ensure they are accessible
"""

import json
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse
import time

def load_json_data(json_file):
    """Load JSON data from file"""
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File {json_file} not found")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {json_file}: {e}")
        sys.exit(1)

def validate_url(url, timeout=10):
    """Validate if a URL is accessible"""
    try:
        # Add user agent to avoid being blocked
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
        
        if response.status_code == 200:
            return True, response.status_code, "OK"
        else:
            return False, response.status_code, f"HTTP {response.status_code}"
            
    except requests.exceptions.Timeout:
        return False, 0, "Timeout"
    except requests.exceptions.ConnectionError:
        return False, 0, "Connection Error"
    except requests.exceptions.RequestException as e:
        return False, 0, f"Request Error: {str(e)}"
    except Exception as e:
        return False, 0, f"Unexpected Error: {str(e)}"

def extract_urls_from_json(data):
    """Extract all URLs from JSON data"""
    urls = []
    
    # Extract URLs from items
    for item in data.get('items', []):
        if 'url' in item and item['url']:
            urls.append({
                'url': item['url'],
                'title': item.get('title', 'No title'),
                'type': 'published_item',
                'source': item.get('source', 'Unknown')
            })
    
    # Extract URLs from discarded items
    for item in data.get('discarded_items', []):
        if 'url' in item and item['url']:
            urls.append({
                'url': item['url'],
                'title': item.get('title', 'No title'),
                'type': 'discarded_item',
                'source': item.get('source', 'Unknown')
            })
    
    return urls

def validate_urls(urls, delay=1):
    """Validate a list of URLs"""
    results = []
    total = len(urls)
    
    print(f"🔍 Validating {total} URLs...")
    print("=" * 60)
    
    for i, url_info in enumerate(urls, 1):
        url = url_info['url']
        title = url_info['title']
        url_type = url_info['type']
        source = url_info['source']
        
        print(f"[{i}/{total}] Checking: {title[:50]}...")
        
        is_valid, status_code, message = validate_url(url)
        
        result = {
            'url': url,
            'title': title,
            'type': url_type,
            'source': source,
            'is_valid': is_valid,
            'status_code': status_code,
            'message': message
        }
        
        results.append(result)
        
        # Status indicator
        if is_valid:
            print(f"   ✅ {message}")
        else:
            print(f"   ❌ {message}")
        
        # Add delay to be respectful to servers
        if i < total:
            time.sleep(delay)
    
    return results

def generate_report(results):
    """Generate a validation report"""
    total_urls = len(results)
    valid_urls = sum(1 for r in results if r['is_valid'])
    invalid_urls = total_urls - valid_urls
    
    print("\n" + "=" * 60)
    print("📊 VALIDATION REPORT")
    print("=" * 60)
    print(f"Total URLs checked: {total_urls}")
    print(f"✅ Valid URLs: {valid_urls}")
    print(f"❌ Invalid URLs: {invalid_urls}")
    print(f"Success rate: {(valid_urls/total_urls)*100:.1f}%")
    
    if invalid_urls > 0:
        print("\n❌ INVALID URLS:")
        print("-" * 40)
        for result in results:
            if not result['is_valid']:
                print(f"• {result['title']}")
                print(f"  URL: {result['url']}")
                print(f"  Error: {result['message']}")
                print(f"  Source: {result['source']}")
                print()
    
    # Group by type
    published_items = [r for r in results if r['type'] == 'published_item']
    discarded_items = [r for r in results if r['type'] == 'discarded_item']
    
    print("📈 BREAKDOWN BY TYPE:")
    print("-" * 40)
    print(f"Published items: {len(published_items)} total, {sum(1 for r in published_items if r['is_valid'])} valid")
    print(f"Discarded items: {len(discarded_items)} total, {sum(1 for r in discarded_items if r['is_valid'])} valid")
    
    return {
        'total': total_urls,
        'valid': valid_urls,
        'invalid': invalid_urls,
        'success_rate': (valid_urls/total_urls)*100,
        'results': results
    }

def save_report(report, output_file):
    """Save validation report to JSON file"""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\n💾 Report saved to: {output_file}")

def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: python url_validator.py <json_file>")
        print("Example: python url_validator.py example_weekly_digest.json")
        sys.exit(1)
    
    json_file = sys.argv[1]
    report_file = Path(json_file).stem + '_url_validation.json'
    
    # Load JSON data
    print(f"📂 Loading JSON file: {json_file}")
    data = load_json_data(json_file)
    
    # Extract URLs
    urls = extract_urls_from_json(data)
    
    if not urls:
        print("❌ No URLs found in the JSON file")
        sys.exit(1)
    
    # Validate URLs
    results = validate_urls(urls)
    
    # Generate and display report
    report = generate_report(results)
    
    # Save report
    save_report(report, report_file)
    
    # Summary
    if report['invalid'] == 0:
        print("🎉 All URLs are valid!")
    else:
        print(f"⚠️  {report['invalid']} URLs need attention")

if __name__ == "__main__":
    main() 