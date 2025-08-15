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

def highlight_countries(text):
    """Highlight country names in text by making them bold"""
    import re
    if not text:
        return text
    
    # Lista de países comunes en inglés y español
    countries = [
        # English country names
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
        'Zambia', 'Zimbabwe',
        # Spanish country names
        'Afganistán', 'Albania', 'Alemania', 'Andorra', 'Angola', 'Antigua y Barbuda', 'Arabia Saudita', 'Argelia', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaiyán',
        'Bahamas', 'Bahrein', 'Bangladés', 'Barbados', 'Bélgica', 'Belice', 'Benín', 'Bielorrusia', 'Birmania', 'Bolivia', 'Bosnia y Herzegovina', 'Botsuana', 'Brasil', 'Brunéi', 'Bulgaria', 'Burkina Faso', 'Burundi',
        'Camboya', 'Camerún', 'Canadá', 'Chad', 'Chile', 'China', 'Chipre', 'Colombia', 'Comoras', 'Congo', 'Corea del Norte', 'Corea del Sur', 'Costa Rica', 'Costa de Marfil', 'Croacia', 'Cuba', 'República Checa',
        'Dinamarca', 'Dominica', 'República Dominicana',
        'Ecuador', 'Egipto', 'El Salvador', 'Emiratos Árabes Unidos', 'Eritrea', 'Eslovaquia', 'Eslovenia', 'España', 'Estados Unidos', 'Estonia', 'Etiopía',
        'Filipinas', 'Finlandia', 'Fiyi', 'Francia',
        'Gabón', 'Gambia', 'Georgia', 'Ghana', 'Granada', 'Grecia', 'Guatemala', 'Guinea', 'Guinea-Bisáu', 'Guinea Ecuatorial', 'Guyana',
        'Haití', 'Honduras', 'Hungría',
        'India', 'Indonesia', 'Irán', 'Irak', 'Irlanda', 'Islandia', 'Islas Marshall', 'Islas Salomón', 'Israel', 'Italia',
        'Jamaica', 'Japón', 'Jordania',
        'Kazajistán', 'Kenia', 'Kirguistán', 'Kuwait',
        'Laos', 'Lesoto', 'Letonia', 'Líbano', 'Liberia', 'Libia', 'Liechtenstein', 'Lituania', 'Luxemburgo',
        'Macedonia del Norte', 'Madagascar', 'Malasia', 'Malaui', 'Maldivas', 'Malí', 'Malta', 'Marruecos', 'Mauricio', 'Mauritania', 'México', 'Micronesia', 'Moldavia', 'Mónaco', 'Mongolia', 'Montenegro', 'Mozambique',
        'Namibia', 'Nauru', 'Nepal', 'Nicaragua', 'Níger', 'Nigeria', 'Noruega', 'Nueva Zelanda',
        'Omán',
        'Países Bajos', 'Pakistán', 'Palaos', 'Panamá', 'Papúa Nueva Guinea', 'Paraguay', 'Perú', 'Polonia', 'Portugal',
        'Qatar',
        'Reino Unido', 'República Centroafricana', 'República Democrática del Congo', 'República del Congo', 'Rumania', 'Rusia', 'Ruanda',
        'Samoa', 'San Marino', 'Santa Lucía', 'San Vicente y las Granadinas', 'San Cristóbal y Nieves', 'Santo Tomé y Príncipe', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leona', 'Singapur', 'Siria', 'Somalia', 'Sudáfrica', 'Sudán', 'Sudán del Sur', 'Suecia', 'Suiza', 'Surinam',
        'Tailandia', 'Tanzania', 'Tayikistán', 'Timor Oriental', 'Togo', 'Tonga', 'Trinidad y Tobago', 'Túnez', 'Turkmenistán', 'Turquía', 'Tuvalu',
        'Ucrania', 'Uganda', 'Uruguay', 'Uzbekistán',
        'Vanuatu', 'Vaticano', 'Venezuela', 'Vietnam',
        'Yemen',
        'Zambia', 'Zimbabue'
    ]
    
    # Crear patrón regex para buscar países (case insensitive)
    pattern = r'\b(' + '|'.join(re.escape(country) for country in countries) + r')\b'
    
    # Reemplazar países encontrados con versión en negrita
    highlighted_text = re.sub(pattern, r'<strong>\1</strong>', text, flags=re.IGNORECASE)
    
    return highlighted_text

def get_country_code(country_name):
    """Get country code based on country name"""
    code_map = {
        # Africa
        'Malawi': 'MW', 'Zambia': 'ZM', 'Ghana': 'GH', 'Angola': 'AO', 'Ethiopia': 'ET', 'Kenya': 'KE', 'Nigeria': 'NG', 'South Africa': 'ZA', 'Egypt': 'EG', 'Morocco': 'MA', 'Tunisia': 'TN', 'Algeria': 'DZ', 'Sudan': 'SD', 'South Sudan': 'SS', 'Somalia': 'SO', 'Eritrea': 'ER', 'Djibouti': 'DJ', 'Chad': 'TD', 'Niger': 'NE', 'Mali': 'ML', 'Burkina Faso': 'BF', 'Senegal': 'SN', 'Gambia': 'GM', 'Guinea-Bissau': 'GW', 'Guinea': 'GN', 'Sierra Leone': 'SL', 'Liberia': 'LR', 'Ivory Coast': 'CI', 'Togo': 'TG', 'Benin': 'BJ', 'Cameroon': 'CM', 'Central African Republic': 'CF', 'Congo': 'CG', 'Democratic Republic of the Congo': 'CD', 'Gabon': 'GA', 'Equatorial Guinea': 'GQ', 'Sao Tome and Principe': 'ST', 'Mauritania': 'MR', 'Mauritius': 'MU', 'Seychelles': 'SC', 'Comoros': 'KM', 'Madagascar': 'MG', 'Mozambique': 'MZ', 'Zimbabwe': 'ZW', 'Botswana': 'BW', 'Namibia': 'NA', 'Lesotho': 'LS', 'Eswatini': 'SZ', 'Burundi': 'BI', 'Rwanda': 'RW', 'Uganda': 'UG', 'Tanzania': 'TZ',
        
        # Asia
        'India': 'IN', 'Pakistan': 'PK', 'Sri Lanka': 'LK', 'Bangladesh': 'BD', 'Nepal': 'NP', 'Bhutan': 'BT', 'Maldives': 'MV', 'China': 'CN', 'Japan': 'JP', 'South Korea': 'KR', 'North Korea': 'KP', 'Mongolia': 'MN', 'Taiwan': 'TW', 'Vietnam': 'VN', 'Laos': 'LA', 'Cambodia': 'KH', 'Thailand': 'TH', 'Myanmar': 'MM', 'Malaysia': 'MY', 'Singapore': 'SG', 'Indonesia': 'ID', 'Philippines': 'PH', 'Brunei': 'BN', 'East Timor': 'TL', 'Kazakhstan': 'KZ', 'Kyrgyzstan': 'KG', 'Tajikistan': 'TJ', 'Uzbekistan': 'UZ', 'Turkmenistan': 'TM', 'Afghanistan': 'AF', 'Iran': 'IR', 'Iraq': 'IQ', 'Syria': 'SY', 'Lebanon': 'LB', 'Jordan': 'JO', 'Israel': 'IL', 'Palestine': 'PS', 'Saudi Arabia': 'SA', 'Yemen': 'YE', 'Oman': 'OM', 'United Arab Emirates': 'AE', 'Qatar': 'QA', 'Kuwait': 'KW', 'Bahrain': 'BH', 'Armenia': 'AM', 'Azerbaijan': 'AZ', 'Georgia': 'GE', 'Turkey': 'TR', 'Cyprus': 'CY',
        
        # Europe
        'Ukraine': 'UA', 'Russia': 'RU', 'Belarus': 'BY', 'Poland': 'PL', 'Lithuania': 'LT', 'Latvia': 'LV', 'Estonia': 'EE', 'Finland': 'FI', 'Sweden': 'SE', 'Norway': 'NO', 'Denmark': 'DK', 'Iceland': 'IS', 'Germany': 'DE', 'France': 'FR', 'Spain': 'ES', 'Portugal': 'PT', 'Italy': 'IT', 'Greece': 'GR', 'Albania': 'AL', 'North Macedonia': 'MK', 'Kosovo': 'XK', 'Serbia': 'RS', 'Montenegro': 'ME', 'Bosnia and Herzegovina': 'BA', 'Croatia': 'HR', 'Slovenia': 'SI', 'Hungary': 'HU', 'Slovakia': 'SK', 'Czech Republic': 'CZ', 'Austria': 'AT', 'Switzerland': 'CH', 'Liechtenstein': 'LI', 'Netherlands': 'NL', 'Belgium': 'BE', 'Luxembourg': 'LU', 'Ireland': 'IE', 'United Kingdom': 'GB', 'Malta': 'MT', 'Bulgaria': 'BG', 'Romania': 'RO', 'Moldova': 'MD',
        
        # Americas
        'United States': 'US', 'Canada': 'CA', 'Mexico': 'MX', 'Guatemala': 'GT', 'Belize': 'BZ', 'El Salvador': 'SV', 'Honduras': 'HN', 'Nicaragua': 'NI', 'Costa Rica': 'CR', 'Panama': 'PA', 'Colombia': 'CO', 'Venezuela': 'VE', 'Guyana': 'GY', 'Suriname': 'SR', 'Brazil': 'BR', 'Ecuador': 'EC', 'Peru': 'PE', 'Bolivia': 'BO', 'Paraguay': 'PY', 'Uruguay': 'UY', 'Argentina': 'AR', 'Chile': 'CL', 'Cuba': 'CU', 'Jamaica': 'JM', 'Haiti': 'HT', 'Dominican Republic': 'DO', 'Puerto Rico': 'PR', 'Bahamas': 'BS', 'Barbados': 'BB', 'Trinidad and Tobago': 'TT', 'Grenada': 'GD', 'Saint Vincent and the Grenadines': 'VC', 'Saint Lucia': 'LC', 'Saint Kitts and Nevis': 'KN', 'Antigua and Barbuda': 'AG', 'Dominica': 'DM',
        
        # Oceania
        'Australia': 'AU', 'New Zealand': 'NZ', 'Papua New Guinea': 'PG', 'Fiji': 'FJ', 'Solomon Islands': 'SB', 'Vanuatu': 'VU', 'New Caledonia': 'NC', 'Samoa': 'WS', 'Tonga': 'TO', 'Tuvalu': 'TV', 'Kiribati': 'KI', 'Nauru': 'NR', 'Palau': 'PW', 'Micronesia': 'FM', 'Marshall Islands': 'MH',
        
        # Global/International
        'GLOBAL': 'GL', 'Global': 'GL'
    }
    
    return code_map.get(country_name, 'XX')

def generate_country_chart(items):
    """Generate a simple HTML/CSS chart showing country distribution"""
    from collections import Counter
    
    # Extract countries from items
    country_counts = Counter()
    for item in items:
        countries = item.get('countries', [])
        # Get the full country name (second element if available, otherwise first)
        if len(countries) > 1:
            country_name = countries[1]  # Full name
        elif countries:
            country_name = countries[0]  # Code or name
        else:
            continue
        
        # Skip if it's a code (2-3 letters) or GLOBAL
        if len(country_name) <= 3 or country_name == 'GLOBAL':
            continue
            
        country_counts[country_name] += 1
    
    # Get top 8 countries
    top_countries = country_counts.most_common(8)
    
    if not top_countries:
        return ""
    
    # Calculate max count for scaling
    max_count = max(count for _, count in top_countries)
    
    # Generate chart HTML
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
        
        .lion-header {{
            background-color: white;
            text-align: center;
            padding: 1rem 0;
            border-bottom: 1px solid #e0e0e0;
        }}
        
        .lion-image {{
            max-width: 400px;
            height: auto;
            display: block;
            margin: 0 auto;
        }}
        
        .header {{
            background-color: white;
            padding: 1rem 2rem;
            border-bottom: 2px solid var(--e-global-color-primary);
        }}
        
        .header-content {{
            max-width: 1200px;
            margin: 0 auto;
            display: block;
        }}
        
        .logo {{
            font-family: Georgia, serif;
            font-weight: bold;
            font-size: 1.5rem;
            color: var(--e-global-color-primary);
        }}
        
        .logo-subtitle {{
            font-size: 0.8rem;
            font-weight: 400;
            margin-top: -0.2rem;
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
        
        .meta-section {{
            background-color: #f8f8f8;
            padding: 2rem;
            margin-top: 3rem;
            border-radius: 4px;
        }}
        
        .meta-section h2 {{
            font-family: Georgia, serif;
            font-weight: bold;
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
            font-family: Georgia, serif;
            font-weight: bold;
            margin-bottom: 1rem;
            color: var(--e-global-color-primary);
        }}
        
        .discarded-item {{
            padding: 0.5rem 0;
            border-bottom: 1px solid #e0e0e0;
            font-size: 0.9rem;
        }}
        
        .country-chart {{
            margin-top: 2rem;
            padding: 1.5rem;
            background: white;
            border-radius: 4px;
        }}
        
        .country-chart h3 {{
            font-family: Georgia, serif;
            font-weight: bold;
            margin-bottom: 1rem;
            color: var(--e-global-color-primary);
        }}
        
        .chart-container {{
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }}
        
        .chart-row {{
            display: flex;
            align-items: center;
            gap: 1rem;
        }}
        
        .chart-label {{
            min-width: 120px;
            font-weight: 500;
            font-size: 0.9rem;
            text-align: left;
        }}
        
        .chart-bar-container {{
            flex: 1;
            height: 20px;
            background-color: #f0f0f0;
            border-radius: 10px;
            overflow: hidden;
        }}
        
        .chart-bar {{
            height: 100%;
            background: linear-gradient(90deg, var(--e-global-color-secondary), #d4d1a0);
            border-radius: 10px;
            transition: width 0.3s ease;
        }}
        
        .chart-value {{
            min-width: 30px;
            text-align: right;
            font-weight: bold;
            color: var(--e-global-color-primary);
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
    <div class="lion-header">
        <img src="Headers/Lion.jpeg" alt="Majestic Lion" class="lion-image">
    </div>
    
    <header class="header">
        <div class="header-content">
            <img src="Headers/SovereignDebtWeeklyHeaderV1.jpeg" alt="Sovereign Debt Weekly Header" class="header-image">
        </div>
    </header>

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
        # Determine how many discarded items to show (up to 10, but show actual count if less)
        items_to_show = min(len(discarded_items), 10)
        html += f"""
            <div class="discarded-items">
                <h3>Top Discarded Headlines</h3>
"""
        for i, item in enumerate(discarded_items[:items_to_show], 1):
            headline = clean_text(item.get('headline', 'No title'))
            original_url = item.get('url', '#')
            original_url_clean, google_url, lucky_url = get_smart_url(headline, original_url)
            
            html += f"""
                <div class="discarded-item">{i}. {headline} — <a href="{original_url_clean}" target="_blank">Original</a> | <a href="{google_url}" target="_blank">Google Search</a> | <a href="{lucky_url}" target="_blank">Lucky</a></div>
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