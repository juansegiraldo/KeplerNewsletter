#!/usr/bin/env python3
"""
JSON to HTML Converter for Sovereign Debt Weekly Digest
Converts structured JSON data to Kepler Karst branded HTML
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

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

def clean_text(text):
    """Clean text by removing citation references and other artifacts"""
    import re
    if not text:
        return text
    
    # Remove citation references like 【868222379580860†L154-L186】
    text = re.sub(r'【[^】]*】', '', text)
    
    # Remove other common artifacts
    text = re.sub(r'†[A-Z]\d+-\d+', '', text)
    text = re.sub(r'【[^】]*†[^】]*】', '', text)
    
    # Clean up extra spaces that might be left
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    
    return text

def create_google_search_url(headline, original_url):
    """Create a Google search URL using the URL slug instead of full headline"""
    import re
    
    # Extract domain and slug from original URL
    domain = ""
    slug = ""
    try:
        from urllib.parse import urlparse
        parsed = urlparse(original_url)
        domain = parsed.netloc
        
        # Extract the slug (last part of the path)
        path_parts = parsed.path.strip('/').split('/')
        if path_parts:
            slug = path_parts[-1]  # Get the last part of the path
    except:
        pass
    
    # Use slug if available, otherwise fall back to headline
    search_terms = slug if slug else clean_text(headline)
    
    # URL encode the search terms
    encoded_search = quote(search_terms)
    
    return f"https://www.google.com/search?q={encoded_search}"

def create_google_lucky_url(headline, original_url):
    """Create a Google 'I'm Feeling Lucky' URL that goes directly to the first result"""
    import re
    
    # Extract domain and slug from original URL
    domain = ""
    slug = ""
    try:
        from urllib.parse import urlparse
        parsed = urlparse(original_url)
        domain = parsed.netloc
        
        # Extract the slug (last part of the path)
        path_parts = parsed.path.strip('/').split('/')
        if path_parts:
            slug = path_parts[-1]  # Get the last part of the path
    except:
        pass
    
    # Use slug if available, otherwise fall back to headline
    search_terms = slug if slug else clean_text(headline)
    
    # URL encode the search terms
    encoded_search = quote(search_terms)
    
    return f"https://www.google.com/search?q={encoded_search}&btnI"

def get_smart_url(headline, original_url):
    """Get original URL, Google search URL, and Google Lucky URL"""
    if not original_url or original_url == '#':
        return "#", create_google_search_url(headline, ""), create_google_lucky_url(headline, "")
    
    return original_url, create_google_search_url(headline, original_url), create_google_lucky_url(headline, original_url)

def generate_html(data):
    """Generate HTML from JSON data"""
    
    # Extract metadata
    metadata = data.get('metadata', {})
    executive_summary = data.get('executive_summary', {})
    items = data.get('items', [])
    analytics = data.get('analytics', {})
    processing_statistics = analytics.get('processing_statistics', {})
    discarded_items = data.get('discarded_items', [])
    processing_notes = data.get('processing_notes', {})
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{metadata.get('title', 'Sovereign Debt Weekly')} | Kepler Karst</title>
    <meta name="description" content="Weekly digest of the most relevant sovereign debt news and analysis from the past 7 days.">
    <meta name="keywords" content="sovereign debt, restructuring, IMF, World Bank, Paris Club, debt sustainability">
    <meta property="og:title" content="{metadata.get('title', 'Sovereign Debt Weekly')}">
    <meta property="og:description" content="Weekly digest of sovereign debt developments">
    <meta property="og:type" content="article">
    <meta name="twitter:card" content="summary_large_image">
    
    <style>
        :root {{
            --e-global-color-primary: #000000;
            --e-global-color-secondary: #F1EEA4;
            --e-global-color-text: #000000;
            --e-global-typography-primary-font-family: "Blacker Pro";
            --e-global-typography-primary-font-weight: 700;
        }}
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: "Sharp Grotesk", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            color: var(--e-global-color-text);
            line-height: 1.6;
            background-color: #fff;
        }}
        
        .header {{
            background-color: var(--e-global-color-secondary);
            padding: 1rem 2rem;
            border-bottom: 2px solid var(--e-global-color-primary);
        }}
        
        .header-content {{
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .logo {{
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            font-size: 1.5rem;
            color: var(--e-global-color-primary);
        }}
        
        .logo-subtitle {{
            font-size: 0.8rem;
            font-weight: 400;
            margin-top: -0.2rem;
        }}
        
        .hero {{
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 600"><rect width="1200" height="600" fill="%23f1eea4"/><text x="600" y="300" text-anchor="middle" font-family="Arial" font-size="48" fill="%23000">#BRAVE ADVOCACY</text></svg>');
            background-size: cover;
            background-position: center;
            color: white;
            text-align: center;
            padding: 4rem 2rem;
        }}
        
        .hero h1 {{
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            font-size: 3rem;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
        }}
        
        .hero .subtitle {{
            font-size: 1.2rem;
            opacity: 0.9;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }}
        
        .tldr {{
            background-color: var(--e-global-color-secondary);
            padding: 2rem;
            margin: 2rem 0;
            border-left: 4px solid var(--e-global-color-primary);
        }}
        
        .tldr h2 {{
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            margin-bottom: 1rem;
            color: var(--e-global-color-primary);
        }}
        
        .items {{
            margin: 3rem 0;
        }}
        
        .item {{
            margin-bottom: 2rem;
            padding: 1.5rem;
            border: 1px solid #e0e0e0;
            border-radius: 4px;
            transition: box-shadow 0.3s ease;
        }}
        
        .item:hover {{
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }}
        
        .item h3 {{
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            margin-bottom: 0.5rem;
        }}
        
        .item h3 a {{
            color: var(--e-global-color-primary);
            text-decoration: none;
        }}
        
        .item h3 a:hover {{
            text-decoration: underline;
        }}
        
        .item-meta {{
            font-size: 0.9rem;
            color: #666;
            margin-bottom: 1rem;
        }}
        
        .item-content {{
            margin-bottom: 1rem;
        }}
        
        .item-links {{
            margin-top: 1rem;
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
        }}
        
        .link-btn {{
            display: inline-block;
            padding: 0.5rem 1rem;
            text-decoration: none;
            border-radius: 4px;
            font-size: 0.8rem;
            font-weight: 500;
            transition: all 0.3s ease;
        }}
        
        .original-link {{
            background-color: var(--e-global-color-primary);
            color: white;
        }}
        
        .original-link:hover {{
            background-color: #333;
        }}
        
        .google-link {{
            background-color: #4285f4;
            color: white;
        }}
        
        .google-link:hover {{
            background-color: #3367d6;
        }}
        
        .lucky-link {{
            background-color: #34a853;
            color: white;
        }}
        
        .lucky-link:hover {{
            background-color: #2d8e47;
        }}
        
        .meta-section {{
            background-color: #f8f8f8;
            padding: 2rem;
            margin-top: 3rem;
            border-radius: 4px;
        }}
        
        .meta-section h2 {{
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            margin-bottom: 1rem;
            color: var(--e-global-color-primary);
        }}
        
        .meta-stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-bottom: 2rem;
        }}
        
        .stat {{
            background: white;
            padding: 1rem;
            border-radius: 4px;
            border-left: 3px solid var(--e-global-color-primary);
        }}
        
        .stat-number {{
            font-size: 1.5rem;
            font-weight: bold;
            color: var(--e-global-color-primary);
        }}
        
        .stat-label {{
            font-size: 0.9rem;
            color: #666;
        }}
        
        .discarded-items {{
            margin-top: 1rem;
        }}
        
        .discarded-items h3 {{
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            margin-bottom: 1rem;
            color: var(--e-global-color-primary);
        }}
        
        .discarded-item {{
            padding: 0.5rem 0;
            border-bottom: 1px solid #e0e0e0;
            font-size: 0.9rem;
        }}
        
        .footer {{
            background-color: var(--e-global-color-primary);
            color: white;
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
        }}
        
        @media (max-width: 768px) {{
            .hero h1 {{
                font-size: 2rem;
            }}
            
            .container {{
                padding: 1rem;
            }}
            
            .meta-stats {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <header class="header">
        <div class="header-content">
            <div class="logo">
                KEPLER—KARST<br>
                <span class="logo-subtitle">LAW FIRM</span>
            </div>
            <nav>
                <span style="font-weight: bold; color: var(--e-global-color-primary);">Sovereign Debt Weekly</span>
            </nav>
        </div>
    </header>

    <section class="hero">
        <h1>{metadata.get('subtitle', '#BRAVE ADVOCACY')}</h1>
        <p class="subtitle">{metadata.get('title', 'Sovereign Debt Weekly')}</p>
    </section>

    <main class="container">
        <section class="tldr">
            <h2>Weekly Summary</h2>
            <p>{clean_text(executive_summary.get('weekly_overview', 'Weekly summary of sovereign debt developments.'))}</p>
        </section>

        <section class="items">
            <h2 style="font-family: var(--e-global-typography-primary-font-family); font-weight: var(--e-global-typography-primary-font-weight); margin-bottom: 2rem; color: var(--e-global-color-primary);">Items ({len(items)} items)</h2>
"""

    # Generate items
    for item in items:
        headline = clean_text(item.get('headline', 'No title'))
        original_url = item.get('source', {}).get('original_url', '#')
        original_url_clean, google_url, lucky_url = get_smart_url(headline, original_url)
        countries = item.get('countries', [])
        country = countries[1] if len(countries) > 1 else countries[0] if countries else 'Unknown'
        date = item.get('publication_date', 'Unknown date')
        source_name = item.get('source', {}).get('name', 'Unknown source')
        content_summary = clean_text(item.get('content', {}).get('summary', 'No content available.'))
        
        html += f"""
            <article class="item">
                <h3><a href="{original_url_clean}" target="_blank">{headline}</a></h3>
                <div class="item-meta">{country} — {date} — {source_name}</div>
                <div class="item-content">
                    {content_summary}
                </div>
                <div class="item-links">
                    <a href="{original_url_clean}" target="_blank" class="link-btn original-link">Original Source</a>
                    <a href="{google_url}" target="_blank" class="link-btn google-link">Search on Google</a>
                    <a href="{lucky_url}" target="_blank" class="link-btn lucky-link">I'm Feeling Lucky</a>
                </div>
            </article>
"""

    # Generate statistics and meta section
    html += f"""
        </section>

        <section class="meta-section">
            <h2>Meta</h2>
            <div class="meta-stats">
                <div class="stat">
                    <div class="stat-number">{processing_statistics.get('sources_scanned', 0)}</div>
                    <div class="stat-label">Sources scanned</div>
                </div>
                <div class="stat">
                    <div class="stat-number">{processing_statistics.get('articles_reviewed', 0)}</div>
                    <div class="stat-label">Articles reviewed</div>
                </div>
                <div class="stat">
                    <div class="stat-number">{processing_statistics.get('items_published', 0)}</div>
                    <div class="stat-label">Items published</div>
                </div>
                <div class="stat">
                    <div class="stat-number">{processing_statistics.get('duplicates_identified', 0)}</div>
                    <div class="stat-label">Duplicates identified</div>
                </div>
            </div>
"""

    # Add discarded items
    if discarded_items:
        html += """
            <div class="discarded-items">
                <h3>Top 5 discarded headlines:</h3>
"""
        for i, item in enumerate(discarded_items[:5], 1):
            title = clean_text(item.get('title', 'No title'))
            original_url = item.get('url', '#')
            original_url_clean, google_url, lucky_url = get_smart_url(title, original_url)
            
            html += f"""
                <div class="discarded-item">{i}. {title} — <a href="{original_url_clean}" target="_blank">Original</a> | <a href="{google_url}" target="_blank">Google Search</a> | <a href="{lucky_url}" target="_blank">Lucky</a></div>
"""
        html += """
            </div>
"""

    # Add processing notes
    if processing_notes:
        html += """
            <div class="processing-notes" style="margin-top: 2rem;">
                <h3>Processing Notes</h3>
                <p><strong>Topics covered:</strong> """ + ", ".join(processing_notes.get('topics_covered', [])) + """</p>
                <p><strong>Geographic focus:</strong> """ + ", ".join(processing_notes.get('geographic_focus', [])) + """</p>
                <p><strong>Key developments:</strong> """ + ", ".join(processing_notes.get('key_developments', [])) + """</p>
                <p><strong>Next week watch:</strong> """ + ", ".join(processing_notes.get('next_week_watch', [])) + """</p>
            </div>
"""

    html += """
        </section>
    </main>

    <footer class="footer">
        <p>&copy; 2025 Kepler Karst Law Firm. All rights reserved.</p>
        <p style="margin-top: 0.5rem; font-size: 0.9rem; opacity: 0.8;">Weekly sovereign debt analysis and insights</p>
        <p style="margin-top: 0.5rem; font-size: 0.8rem; opacity: 0.6;">Generated in partnership by: Rodrigo Olivares, Laura Villarraga and Juan Giraldo</p>
    </footer>
</body>
</html>"""

    return html

def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: python json_to_html_converter.py <json_file>")
        print("Example: python json_to_html_converter.py weekly_digest.json")
        sys.exit(1)
    
    json_file = sys.argv[1]
    output_file = Path(json_file).stem + '.html'
    
    # Load JSON data
    data = load_json_data(json_file)
    
    # Generate HTML
    html = generate_html(data)
    
    # Write HTML file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ HTML generated successfully: {output_file}")
    print(f"📊 Processed {len(data.get('items', []))} items")
    print(f"🔍 Using Google search fallback for URLs")

if __name__ == "__main__":
    main() 