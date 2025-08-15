#!/usr/bin/env python3
"""
JSON to HTML Converter v2 for Sovereign Debt Weekly Digest
Converts structured JSON data to Kepler Karst branded HTML
Generates two files: original digest and meta analytics
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import quote
from collections import Counter

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
    text = re.sub(r'†[A-Z]\d+-\d+', '', text)
    text = re.sub(r'【[^】]*†[^】]*】', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    
    return text

def highlight_countries(text):
    """Highlight country names in text by making them bold"""
    import re
    if not text:
        return text
    
    countries = [
        'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan',
        'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi',
        'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic',
        'Democratic Republic of the Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic',
        'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia',
        'Fiji', 'Finland', 'France',
        'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana',
        'Haiti', 'Honduras', 'Hungary',
        'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Ivory Coast',
        'Jamaica', 'Japan', 'Jordan',
        'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan',
        'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg',
        'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar',
        'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'North Macedonia', 'Norway',
        'Oman',
        'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal',
        'Qatar',
        'Romania', 'Russia', 'Rwanda',
        'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria',
        'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu',
        'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan',
        'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam',
        'Yemen',
        'Zambia', 'Zimbabwe'
    ]
    
    pattern = r'\b(' + '|'.join(re.escape(country) for country in countries) + r')\b'
    highlighted_text = re.sub(pattern, r'<strong>\1</strong>', text, flags=re.IGNORECASE)
    
    return highlighted_text

def get_smart_url(headline, original_url):
    """Get original URL, Google search URL, and Google Lucky URL"""
    if not original_url or original_url == '#':
        return "#", create_google_search_url(headline, ""), create_google_lucky_url(headline, "")
    
    return original_url, create_google_search_url(headline, original_url), create_google_lucky_url(headline, original_url)

def create_google_search_url(headline, original_url):
    """Create a Google search URL using the URL slug instead of full headline"""
    import re
    
    domain = ""
    slug = ""
    try:
        from urllib.parse import urlparse
        parsed = urlparse(original_url)
        domain = parsed.netloc
        path_parts = parsed.path.strip('/').split('/')
        if path_parts:
            slug = path_parts[-1]
    except:
        pass
    
    search_terms = slug if slug else clean_text(headline)
    encoded_search = quote(search_terms)
    
    return f"https://www.google.com/search?q={encoded_search}"

def create_google_lucky_url(headline, original_url):
    """Create a Google 'I'm Feeling Lucky' URL that goes directly to the first result"""
    import re
    
    domain = ""
    slug = ""
    try:
        from urllib.parse import urlparse
        parsed = urlparse(original_url)
        domain = parsed.netloc
        path_parts = parsed.path.strip('/').split('/')
        if path_parts:
            slug = path_parts[-1]
    except:
        pass
    
    search_terms = slug if slug else clean_text(headline)
    encoded_search = quote(search_terms)
    
    return f"https://www.google.com/search?q={encoded_search}&btnI"

def format_date_for_display(date_str):
    """Convert date from DD-MM-YYYY format to DD Month YYYY format"""
    if not date_str or date_str == 'DD-MM-YYYY':
        return 'DD Month YYYY'
    
    try:
        day, month, year = date_str.split('-')
        months = {
            '01': 'January', '02': 'February', '03': 'March', '04': 'April',
            '05': 'May', '06': 'June', '07': 'July', '08': 'August',
            '09': 'September', '10': 'October', '11': 'November', '12': 'December'
        }
        month_name = months.get(month, month)
        return f"{day} {month_name} {year}"
    except:
        return date_str

def generate_country_chart(items):
    """Generate a simple HTML/CSS chart showing country distribution"""
    country_counts = Counter()
    for item in items:
        countries = item.get('countries', [])
        if len(countries) > 1:
            country_name = countries[1]
        elif countries:
            country_name = countries[0]
        else:
            continue
        
        if len(country_name) <= 3 or country_name == 'GLOBAL':
            continue
            
        country_counts[country_name] += 1
    
    top_countries = country_counts.most_common(8)
    
    if not top_countries:
        return ""
    
    max_count = max(count for _, count in top_countries)
    
    chart_html = """
            <div class="country-chart">
                <h3>Geographic Distribution</h3>
                <div class="chart-container">
"""
    
    for country, count in top_countries:
        percentage = (count / max_count) * 100
        chart_html += f"""
                    <div class="chart-row">
                        <div class="chart-label">{country}</div>
                        <div class="chart-bar-container">
                            <div class="chart-bar" style="width: {percentage}%"></div>
                        </div>
                        <div class="chart-value">{count}</div>
                    </div>
"""
    
    chart_html += """
                </div>
            </div>
"""
    
    return chart_html

def generate_meta_html(data):
    """Generate meta analytics HTML with charts and metrics"""
    
    metadata = data.get('metadata', {})
    analytics = data.get('analytics', {})
    items = data.get('items', [])
    coverage_analysis = analytics.get('coverage_analysis', {})
    content_metrics = analytics.get('content_metrics', {})
    processing_statistics = analytics.get('processing_statistics', {})
    
    # Extract data for charts
    category_distribution = coverage_analysis.get('category_distribution', {})
    geographical_distribution = coverage_analysis.get('geographical_distribution', {})
    score_distribution = content_metrics.get('score_distribution', {})
    
    # Collect secondary tags
    all_secondary_tags = []
    for item in items:
        secondary_tags = item.get('classification', {}).get('secondary_tags', [])
        all_secondary_tags.extend(secondary_tags)
    
    tag_counts = Counter(all_secondary_tags)
    top_tags = tag_counts.most_common(10)
    
    # Collect instruments
    all_instruments = []
    for item in items:
        instruments = item.get('classification', {}).get('instruments', [])
        all_instruments.extend(instruments)
    
    instrument_counts = Counter(all_instruments)
    top_instruments = instrument_counts.most_common(8)
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Analytics Dashboard - {metadata.get('title', 'Sovereign Debt Weekly')} | Kepler Karst</title>
    <meta name="description" content="Analytics and metrics dashboard for sovereign debt weekly digest">
    
    <style>
        @font-face {{
            font-family: "Sharp Grotesk";
            src: url("Fonts/SharpGroteskBook16-Regular.ttf") format("truetype");
            font-weight: normal;
            font-style: normal;
        }}
        
        :root {{
            --e-global-color-primary: #000000;
            --e-global-color-secondary: #F1EEA4;
            --e-global-color-text: #000000;
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
            background-color: #f8f9fa;
        }}
        
        .header {{
            background-color: white;
            padding: 2rem;
            text-align: center;
            border-bottom: 1px solid #e0e0e0;
        }}
        
        .header h1 {{
            font-family: Georgia, serif;
            font-weight: bold;
            font-size: 2.5rem;
            color: var(--e-global-color-primary);
            margin-bottom: 0.5rem;
        }}
        
        .header .subtitle {{
            font-size: 1.1rem;
            color: #666;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
        }}
        
        .dashboard-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }}
        
        .chart-card {{
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        .chart-card h3 {{
            font-family: Georgia, serif;
            font-weight: bold;
            margin-bottom: 1rem;
            color: var(--e-global-color-primary);
            font-size: 1.2rem;
        }}
        
        .chart-container {{
            margin-top: 1rem;
        }}
        
        .chart-row {{
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 0.5rem;
        }}
        
        .chart-label {{
            min-width: 120px;
            font-weight: 500;
            font-size: 0.9rem;
        }}
        
        .chart-bar-container {{
            flex: 1;
            height: 20px;
            background-color: #f0f0f0;
            border-radius: 10px;
            overflow: hidden;
            position: relative;
            border: 1px solid #e0e0e0;
        }}
        
        .chart-bar {{
            height: 100%;
            background: linear-gradient(90deg, var(--e-global-color-secondary), #d4d1a0);
            background-color: var(--e-global-color-secondary);
            border-radius: 10px;
            transition: width 0.3s ease;
            display: block;
            min-width: 4px;
            position: relative;
        }}
        
        .chart-value {{
            min-width: 30px;
            text-align: right;
            font-weight: bold;
            color: var(--e-global-color-primary);
        }}
        
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-bottom: 2rem;
        }}
        
        .stat-card {{
            background: white;
            padding: 1.5rem;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        .stat-number {{
            font-size: 2rem;
            font-weight: bold;
            color: var(--e-global-color-primary);
            margin-bottom: 0.5rem;
        }}
        
        .stat-label {{
            font-size: 0.9rem;
            color: #666;
        }}
        
        .tag-cloud {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-top: 1rem;
        }}
        
        .tag {{
            background: var(--e-global-color-secondary);
            padding: 0.3rem 0.8rem;
            border-radius: 15px;
            font-size: 0.8rem;
            font-weight: 500;
        }}
        
        .tag-size-1 {{ font-size: 0.7rem; opacity: 0.6; }}
        .tag-size-2 {{ font-size: 0.8rem; opacity: 0.8; }}
        .tag-size-3 {{ font-size: 0.9rem; opacity: 1; }}
        .tag-size-4 {{ font-size: 1rem; opacity: 1; }}
        .tag-size-5 {{ font-size: 1.1rem; opacity: 1; }}
        
        .footer {{
            background-color: var(--e-global-color-primary);
            color: white;
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
        }}
        
        @media (max-width: 768px) {{
            .dashboard-grid {{
                grid-template-columns: 1fr;
            }}
            
            .stats-grid {{
                grid-template-columns: repeat(2, 1fr);
            }}
        }}
    </style>
</head>
<body>
    <header class="header">
        <h1>Analytics Dashboard</h1>
        <div class="subtitle">{metadata.get('title', 'Sovereign Debt Weekly')}</div>
        <div class="subtitle">{format_date_for_display(metadata.get('period', {}).get('start_date', ''))} - {format_date_for_display(metadata.get('period', {}).get('end_date', ''))}</div>
    </header>

    <main class="container">
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number">{processing_statistics.get('sources_scanned', 0)}</div>
                <div class="stat-label">Sources Scanned</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{processing_statistics.get('articles_reviewed', 0)}</div>
                <div class="stat-label">Articles Reviewed</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{processing_statistics.get('items_published', 0)}</div>
                <div class="stat-label">Items Published</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{content_metrics.get('average_score', 0):.1f}</div>
                <div class="stat-label">Average Score</div>
            </div>
        </div>

        <div class="dashboard-grid">
            <div class="chart-card">
                <h3>Category Distribution</h3>
                <div class="chart-container">
"""
    
    # Category distribution chart
    if category_distribution:
        max_count = max(category_distribution.values())
        for category, count in sorted(category_distribution.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / max_count) * 100
            html += f"""
                    <div class="chart-row">
                        <div class="chart-label">{category.replace('_', ' ').title()}</div>
                        <div class="chart-bar-container">
                            <div class="chart-bar" style="width: {percentage}%"></div>
                        </div>
                        <div class="chart-value">{count}</div>
                    </div>
"""
    
    html += """
                </div>
            </div>

            <div class="chart-card">
                <h3>Geographical Distribution</h3>
                <div class="chart-container">
"""
    
    # Geographical distribution chart
    if geographical_distribution:
        max_count = max(geographical_distribution.values())
        for region, count in sorted(geographical_distribution.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / max_count) * 100
            html += f"""
                    <div class="chart-row">
                        <div class="chart-label">{region}</div>
                        <div class="chart-bar-container">
                            <div class="chart-bar" style="width: {percentage}%"></div>
                        </div>
                        <div class="chart-value">{count}</div>
                    </div>
"""
    
    html += """
                </div>
            </div>

            <div class="chart-card">
                <h3>Score Distribution</h3>
                <div class="chart-container">
"""
    
    # Score distribution chart
    if score_distribution:
        max_count = max(score_distribution.values())
        for score_range, count in sorted(score_distribution.items(), key=lambda x: int(x[0].split('-')[0])):
            percentage = (count / max_count) * 100
            html += f"""
                    <div class="chart-row">
                        <div class="chart-label">{score_range}</div>
                        <div class="chart-bar-container">
                            <div class="chart-bar" style="width: {percentage}%"></div>
                        </div>
                        <div class="chart-value">{count}</div>
                    </div>
"""
    
    html += """
                </div>
            </div>

            <div class="chart-card">
                <h3>Top Financial Instruments</h3>
                <div class="chart-container">
"""
    
    # Instruments chart
    if top_instruments:
        max_count = max(count for _, count in top_instruments)
        for instrument, count in top_instruments:
            percentage = (count / max_count) * 100
            html += f"""
                    <div class="chart-row">
                        <div class="chart-label">{instrument.replace('_', ' ').title()}</div>
                        <div class="chart-bar-container">
                            <div class="chart-bar" style="width: {percentage}%"></div>
                        </div>
                        <div class="chart-value">{count}</div>
                    </div>
"""
    
    html += """
                </div>
            </div>
        </div>

        <div class="chart-card">
            <h3>Top Secondary Tags</h3>
            <div class="tag-cloud">
"""
    
    # Tag cloud
    if top_tags:
        max_count = max(count for _, count in top_tags)
        for tag, count in top_tags:
            size_class = f"tag-size-{min(5, max(1, int((count / max_count) * 5)))}"
            html += f'<span class="tag {size_class}">{tag.replace("_", " ").title()} ({count})</span>'
    
    html += """
            </div>
        </div>
    </main>

    <footer class="footer">
        <p>&copy; 2025 Kepler Karst Law Firm. All rights reserved.</p>
        <p style="margin-top: 0.5rem; font-size: 0.9rem; opacity: 0.8;">Analytics Dashboard for Sovereign Debt Weekly</p>
    </footer>
</body>
</html>"""

    return html

def generate_original_html(data):
    """Generate the original HTML digest (simplified version of the original function)"""
    
    metadata = data.get('metadata', {})
    executive_summary = data.get('executive_summary', {})
    items = data.get('items', [])
    analytics = data.get('analytics', {})
    processing_statistics = analytics.get('processing_statistics', {})
    discarded_items = data.get('discarded_items', [])
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{metadata.get('title', 'Sovereign Debt Weekly')} | Kepler Karst</title>
    <meta name="description" content="Weekly digest of the most relevant sovereign debt news and analysis from the past 7 days.">
    
    <style>
        @font-face {{
            font-family: "Sharp Grotesk";
            src: url("Fonts/SharpGroteskBook16-Regular.ttf") format("truetype");
            font-weight: normal;
            font-style: normal;
        }}
        
        :root {{
            --e-global-color-primary: #000000;
            --e-global-color-secondary: #F1EEA4;
            --e-global-color-text: #000000;
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
            background-color: white;
            padding: 1rem 2rem;
        }}
        
        .header-content {{
            max-width: 1200px;
            margin: 0 auto;
            display: block;
        }}
        
        .header-image {{
            width: 100%;
            height: auto;
            display: block;
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
            font-family: Georgia, serif;
            font-weight: bold;
            font-size: 3rem;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
        }}
        
        .hero .subtitle {{
            font-size: 0.8rem;
            opacity: 0.9;
        }}
        
        .date-range {{
            background-color: white;
            text-align: center;
            padding: 1rem 2rem;
        }}
        
        .date-range h2 {{
            font-family: Georgia, serif;
            font-weight: bold;
            font-size: 0.9rem;
            color: var(--e-global-color-primary);
            margin: 0;
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
        }}
        
        .tldr h2 {{
            font-family: Georgia, serif;
            font-weight: bold;
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
            font-family: Georgia, serif;
            font-weight: bold;
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
            border-radius: 25px;
            font-size: 0.8rem;
            font-weight: 500;
            transition: all 0.3s ease;
        }}
        
        .original-link {{
            background-color: #F3EAA4;
            color: #333;
        }}
        
        .original-link:hover {{
            background-color: #e8d994;
        }}
        
        .google-link {{
            background-color: #E9D95D;
            color: #333;
        }}
        
        .google-link:hover {{
            background-color: #d4c552;
        }}
        
        .lucky-link {{
            background-color: #908114;
            color: white;
        }}
        
        .lucky-link:hover {{
            background-color: #7a6d10;
        }}
        
        .country-chart {{
            background-color: white;
            padding: 2rem;
            margin: 2rem 0;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        .country-chart h3 {{
            font-family: Georgia, serif;
            font-weight: bold;
            margin-bottom: 1.5rem;
            color: var(--e-global-color-primary);
            font-size: 1.2rem;
        }}
        
        .chart-container {{
            margin-top: 1rem;
        }}
        
        .chart-row {{
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 0.8rem;
        }}
        
        .chart-label {{
            min-width: 120px;
            font-weight: 500;
            font-size: 0.9rem;
        }}
        
        .chart-bar-container {{
            flex: 1;
            height: 20px;
            background-color: #f0f0f0;
            border-radius: 10px;
            overflow: hidden;
            position: relative;
            border: 1px solid #e0e0e0;
        }}
        
        .chart-bar {{
            height: 100%;
            background: linear-gradient(90deg, var(--e-global-color-secondary), #d4d1a0);
            background-color: var(--e-global-color-secondary);
            border-radius: 10px;
            transition: width 0.3s ease;
            display: block;
            min-width: 4px;
            position: relative;
        }}
        
        .chart-value {{
            min-width: 30px;
            text-align: right;
            font-weight: bold;
            color: var(--e-global-color-primary);
        }}
        
        .discarded-section {{
            background-color: #f8f9fa;
            padding: 2rem;
            margin: 2rem 0;
            border-radius: 8px;
        }}
        
        .discarded-section h2 {{
            font-family: Georgia, serif;
            font-weight: bold;
            margin-bottom: 1.5rem;
            color: var(--e-global-color-primary);
            font-size: 1.2rem;
        }}
        
        .discarded-item {{
            margin-bottom: 1rem;
            padding: 1rem;
            background-color: white;
            border-radius: 4px;
            border: 1px solid #e0e0e0;
        }}
        
        .discarded-item h4 {{
            font-family: Georgia, serif;
            font-weight: bold;
            margin-bottom: 0.5rem;
            color: var(--e-global-color-primary);
        }}
        
        .discarded-meta {{
            font-size: 0.8rem;
            color: #666;
            margin-bottom: 0.5rem;
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
        }}
    </style>
</head>
<body>
    <header class="header">
        <div class="header-content">
            <img src="Headers/HeaderV2.jpeg" alt="Sovereign Debt Weekly Header" class="header-image">
        </div>
    </header>

    <section class="date-range">
        <h2>{format_date_for_display(metadata.get('period', {}).get('start_date', 'DD-MM-YYYY'))} - {format_date_for_display(metadata.get('period', {}).get('end_date', 'DD-MM-YYYY'))}</h2>
    </section>

    <main class="container">
        <section class="tldr">
            <h2>Weekly Summary</h2>
            <p>{highlight_countries(clean_text(executive_summary.get('weekly_overview', 'Weekly summary of sovereign debt developments.')))}</p>
        </section>

        {generate_country_chart(items)}

        <section class="items">
"""

    # Generate items
    for i, item in enumerate(items, 1):
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
                <h3><a href="{original_url_clean}" target="_blank">{i}. {headline}</a></h3>
                <div class="item-content">
                    {content_summary}
                </div>
                <div class="item-links">
                    <a href="{google_url}" target="_blank" class="link-btn google-link">Search on Google</a>
                </div>
            </article>
"""

    html += """
        </section>

        <section class="discarded-section">
            <h2>Top Discarded Headlines</h2>
"""
    
    # Generate discarded items
    for i, item in enumerate(discarded_items, 1):
        headline = clean_text(item.get('headline', 'No title'))
        original_url = item.get('url', '#')
        original_url_clean, google_url, lucky_url = get_smart_url(headline, original_url)
        date = item.get('publication_date', 'Unknown date')
        source_name = item.get('source', 'Unknown source')
        discard_reason = item.get('discard_reason', 'Below threshold')
        score = item.get('score', 0)
        
        html += f"""
            <div class="discarded-item">
                <h4>{i}. {headline}</h4>
                <div class="item-links">
                    <a href="{google_url}" target="_blank" class="link-btn google-link">Search on Google</a>
                </div>
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
        print("Usage: python json_to_html_converter_v2.py <json_file>")
        print("Example: python json_to_html_converter_v2.py weekly_digest.json")
        sys.exit(1)
    
    json_file = sys.argv[1]
    base_name = Path(json_file).stem
    
    # Load JSON data
    data = load_json_data(json_file)
    
    # Generate both HTML files
    original_html = generate_original_html(data)
    meta_html = generate_meta_html(data)
    
    # Write HTML files
    original_output = f"{base_name}.html"
    meta_output = f"{base_name}_meta.html"
    
    with open(original_output, 'w', encoding='utf-8') as f:
        f.write(original_html)
    
    with open(meta_output, 'w', encoding='utf-8') as f:
        f.write(meta_html)
    
    print(f"✅ HTML files generated successfully:")
    print(f"   📄 Original digest: {original_output}")
    print(f"   📊 Analytics dashboard: {meta_output}")
    print(f"📈 Processed {len(data.get('items', []))} items")
    print(f"🔍 Using Google search fallback for URLs")

if __name__ == "__main__":
    main()
