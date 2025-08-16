#!/usr/bin/env python3
"""
Dynamic Index Builder for Newsletter Issues
Scans issues folders and generates/updates index.html files automatically
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict

def extract_metadata_from_html(html_file):
    """Extract basic metadata from HTML file"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract title
        title_match = re.search(r'<title>(.*?)</title>', content)
        title = title_match.group(1) if title_match else html_file.stem
        
        # Extract date from filename or content
        date_match = re.search(r'(\d{2})(\d{2})(\d{4})', html_file.stem)
        if date_match:
            day, month, year = date_match.groups()
            date_str = f"{day}-{month}-{year}"
            # Create a sortable date object for proper chronological sorting
            sort_date = datetime(int(year), int(month), int(day))
        else:
            date_str = "Unknown"
            sort_date = datetime.min  # Put unknown dates at the end
        
        return {
            'title': title,
            'date': date_str,
            'sort_date': sort_date,  # For proper sorting
            'filename': html_file.name,
            'path': str(html_file.relative_to(html_file.parent.parent))
        }
    except Exception as e:
        print(f"Error reading {html_file}: {e}")
        return {
            'title': html_file.stem,
            'date': 'Unknown',
            'sort_date': datetime.min,  # Put unknown dates at the end
            'filename': html_file.name,
            'path': str(html_file.relative_to(html_file.parent.parent))
        }

def generate_sovereign_debt_index():
    """Generate index.html for sovereign debt newsletter"""
    issues_dir = Path("docs/sovereign-debt/issues")
    index_file = Path("docs/sovereign-debt/index.html")
    
    if not issues_dir.exists():
        print(f"❌ Issues directory not found: {issues_dir}")
        return
    
    # Find all HTML files
    html_files = list(issues_dir.glob("*.html"))
    html_files = [f for f in html_files if not f.name.endswith('_meta.html')]  # Exclude meta files
    
    if not html_files:
        print("❌ No HTML files found in sovereign debt issues")
        return
    
    # Extract metadata
    issues = []
    for html_file in html_files:
        metadata = extract_metadata_from_html(html_file)
        issues.append(metadata)
    
    # Sort by date (newest first)
    issues.sort(key=lambda x: x['sort_date'], reverse=True)
    
    # Generate HTML content
    issues_html = ""
    for issue in issues:
        meta_file = issue['filename'].replace('.html', '_meta.html')
        meta_path = f"issues/{meta_file}"
        
        # Check if meta file exists
        meta_link = ""
        if (issues_dir / meta_file).exists():
            meta_link = f'<a href="{meta_path}" class="link-btn secondary-link">View Analytics</a>'
        
        issues_html += f"""
            <article class="digest-item">
                <h3><a href="issues/{issue['filename']}" target="_blank">{issue['title']}</a></h3>
                <div class="digest-meta">Published: {issue['date']}</div>
                <p>Weekly digest covering sovereign debt developments and international financial markets.</p>
                <div class="issue-links">
                    <a href="issues/{issue['filename']}" class="link-btn primary-link">Read Issue</a>
                    {meta_link}
                </div>
            </article>
        """
    
    # Read the template
    template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sovereign Debt Weekly Digests | Kepler Karst</title>
    <style>
        @font-face {
            font-family: "Sharp Grotesk";
            src: url("assets/fonts/SharpGroteskBook16-Regular.ttf") format("truetype");
            font-weight: normal;
            font-style: normal;
        }
        
        :root {
            --e-global-color-primary: #000000;
            --e-global-color-secondary: #F1EEA4;
            --e-global-color-text: #000000;
            --e-global-typography-primary-font-family: "Blacker Pro";
            --e-global-typography-primary-font-weight: 700;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: "Sharp Grotesk", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            color: var(--e-global-color-text);
            line-height: 1.6;
            background-color: #fff;
        }
        
        .header {
            background-color: var(--e-global-color-secondary);
            padding: 1rem 2rem;
            border-bottom: 2px solid var(--e-global-color-primary);
        }
        
        .header-content {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo {
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            font-size: 1.5rem;
            color: var(--e-global-color-primary);
        }
        
        .logo-subtitle {
            font-size: 0.8rem;
            font-weight: 400;
            margin-top: -0.2rem;
        }
        
        .back-link {
            color: var(--e-global-color-primary);
            text-decoration: none;
            font-weight: 500;
        }
        
        .back-link:hover {
            text-decoration: underline;
        }
        
        .hero {
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 600"><rect width="1200" height="600" fill="%23f1eea4"/><text x="600" y="300" text-anchor="middle" font-family="Arial" font-size="48" fill="%23000">#BRAVE ADVOCACY</text></svg>');
            background-size: cover;
            background-position: center;
            color: white;
            text-align: center;
            padding: 4rem 2rem;
        }
        
        .hero h1 {
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            font-size: 3rem;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
        }
        
        .hero .subtitle {
            font-size: 1.2rem;
            opacity: 0.9;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        .digests {
            margin: 3rem 0;
        }
        
        .digests h2 {
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            margin-bottom: 2rem;
            color: var(--e-global-color-primary);
            font-size: 2rem;
        }
        
        .digest-item {
            margin-bottom: 2rem;
            padding: 1.5rem;
            border: 1px solid #e0e0e0;
            border-radius: 4px;
            transition: box-shadow 0.3s ease;
        }
        
        .digest-item:hover {
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        
        .digest-item h3 {
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            margin-bottom: 0.5rem;
        }
        
        .digest-item h3 a {
            color: var(--e-global-color-primary);
            text-decoration: none;
        }
        
        .digest-item h3 a:hover {
            text-decoration: underline;
        }
        
        .digest-meta {
            font-size: 0.9rem;
            color: #666;
            margin-bottom: 1rem;
        }
        
        .issue-links {
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
            margin-top: 1rem;
        }
        
        .link-btn {
            display: inline-block;
            padding: 0.5rem 1rem;
            text-decoration: none;
            border-radius: 25px;
            font-size: 0.8rem;
            font-weight: 500;
            transition: all 0.3s ease;
        }
        
        .primary-link {
            background-color: var(--e-global-color-primary);
            color: white;
        }
        
        .primary-link:hover {
            background-color: #333;
        }
        
        .secondary-link {
            background-color: var(--e-global-color-secondary);
            color: var(--e-global-color-primary);
        }
        
        .secondary-link:hover {
            background-color: #e8d994;
        }
        
        .footer {
            background-color: var(--e-global-color-primary);
            color: white;
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
        }
        
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2rem;
            }
            
            .container {
                padding: 1rem;
            }
        }
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
                <a href="../index.html" class="back-link">← Back to Home</a>
            </nav>
        </div>
    </header>

    <section class="hero">
        <h1>#BRAVE ADVOCACY</h1>
        <p class="subtitle">Sovereign Debt Weekly Digests</p>
    </section>

    <main class="container">
        <section class="digests">
            <h2>Available Digests</h2>
            {ISSUES_CONTENT}
        </section>
    </main>

    <footer class="footer">
        <p>&copy; 2025 Kepler Karst Law Firm. All rights reserved.</p>
        <p style="margin-top: 0.5rem; font-size: 0.9rem; opacity: 0.8;">Weekly sovereign debt analysis and insights</p>
        <p style="margin-top: 0.5rem; font-size: 0.8rem; opacity: 0.6;">Generated in partnership by: Rodrigo Olivares, Laura Villarraga and Juan Giraldo</p>
    </footer>
</body>
</html>"""
    
    # Replace placeholder with actual content
    final_html = template.replace("{ISSUES_CONTENT}", issues_html)
    
    # Write the file
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print(f"✅ Generated sovereign debt index with {len(issues)} issues")

def generate_art_law_index():
    """Generate index.html for art law newsletter"""
    issues_dir = Path("docs/art-law/issues")
    index_file = Path("docs/art-law/index.html")
    
    if not issues_dir.exists():
        print(f"❌ Issues directory not found: {issues_dir}")
        return
    
    # Find all HTML files
    html_files = list(issues_dir.glob("*.html"))
    html_files = [f for f in html_files if not f.name.endswith('_meta.html')]  # Exclude meta files
    
    if not html_files:
        print("❌ No HTML files found in art law issues")
        return
    
    # Extract metadata
    issues = []
    for html_file in html_files:
        metadata = extract_metadata_from_html(html_file)
        issues.append(metadata)
    
    # Sort by date (newest first)
    issues.sort(key=lambda x: x['sort_date'], reverse=True)
    
    # Generate HTML content
    issues_html = ""
    for issue in issues:
        meta_file = issue['filename'].replace('.html', '_meta.html')
        meta_path = f"issues/{meta_file}"
        
        # Check if meta file exists
        meta_link = ""
        if (issues_dir / meta_file).exists():
            meta_link = f'<a href="{meta_path}" class="link-btn secondary-link">Ver Analytics</a>'
        
        issues_html += f"""
            <article class="issue-item">
                <h3><a href="issues/{issue['filename']}">{issue['title']}</a></h3>
                <div class="issue-meta">Publicado: {issue['date']}</div>
                <p>Análisis de las últimas novedades en derecho cultural, restitución de arte y cumplimiento normativo en el mercado del arte.</p>
                <div class="issue-links">
                    <a href="issues/{issue['filename']}" class="link-btn primary-link">Leer Boletín</a>
                    {meta_link}
                </div>
            </article>
        """
    
    # Read the template
    template = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Arte y Derecho | Kepler Karst</title>
    <style>
        @font-face {
            font-family: "Sharp Grotesk";
            src: url("assets/fonts/SharpGroteskBook16-Regular.ttf") format("truetype");
            font-weight: normal;
            font-style: normal;
        }
        
        :root {
            --e-global-color-primary: #000000;
            --e-global-color-secondary: #F1EEA4;
            --e-global-color-text: #000000;
            --e-global-typography-primary-font-family: "Blacker Pro";
            --e-global-typography-primary-font-weight: 700;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: "Sharp Grotesk", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            color: var(--e-global-color-text);
            line-height: 1.6;
            background-color: #fff;
        }
        
        .header {
            background-color: var(--e-global-color-secondary);
            padding: 1rem 2rem;
            border-bottom: 2px solid var(--e-global-color-primary);
        }
        
        .header-content {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo {
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            font-size: 1.5rem;
            color: var(--e-global-color-primary);
        }
        
        .logo-subtitle {
            font-size: 0.8rem;
            font-weight: 400;
            margin-top: -0.2rem;
        }
        
        .back-link {
            color: var(--e-global-color-primary);
            text-decoration: none;
            font-weight: 500;
        }
        
        .back-link:hover {
            text-decoration: underline;
        }
        
        .hero {
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400"><rect width="1200" height="400" fill="%23f1eea4"/><text x="600" y="200" text-anchor="middle" font-family="Arial" font-size="36" fill="%23000">ARTE Y DERECHO</text></svg>');
            background-size: cover;
            background-position: center;
            color: white;
            text-align: center;
            padding: 4rem 2rem;
        }
        
        .hero h1 {
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            font-size: 3rem;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
        }
        
        .hero .subtitle {
            font-size: 1.2rem;
            opacity: 0.9;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        .issues {
            margin: 3rem 0;
        }
        
        .issues h2 {
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            margin-bottom: 2rem;
            color: var(--e-global-color-primary);
            font-size: 2rem;
        }
        
        .issue-item {
            margin-bottom: 2rem;
            padding: 1.5rem;
            border: 1px solid #e0e0e0;
            border-radius: 4px;
            transition: box-shadow 0.3s ease;
        }
        
        .issue-item:hover {
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        
        .issue-item h3 {
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            margin-bottom: 0.5rem;
        }
        
        .issue-item h3 a {
            color: var(--e-global-color-primary);
            text-decoration: none;
        }
        
        .issue-item h3 a:hover {
            text-decoration: underline;
        }
        
        .issue-meta {
            font-size: 0.9rem;
            color: #666;
            margin-bottom: 1rem;
        }
        
        .issue-links {
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
        }
        
        .link-btn {
            display: inline-block;
            padding: 0.5rem 1rem;
            text-decoration: none;
            border-radius: 25px;
            font-size: 0.8rem;
            font-weight: 500;
            transition: all 0.3s ease;
        }
        
        .primary-link {
            background-color: var(--e-global-color-primary);
            color: white;
        }
        
        .primary-link:hover {
            background-color: #333;
        }
        
        .secondary-link {
            background-color: var(--e-global-color-secondary);
            color: var(--e-global-color-primary);
        }
        
        .secondary-link:hover {
            background-color: #e8d994;
        }
        
        .footer {
            background-color: var(--e-global-color-primary);
            color: white;
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
        }
        
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2rem;
            }
            
            .container {
                padding: 1rem;
            }
            
            .issue-links {
                flex-direction: column;
            }
        }
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
                <a href="../index.html" class="back-link">← Volver al Inicio</a>
            </nav>
        </div>
    </header>

    <section class="hero">
        <h1>ARTE Y DERECHO</h1>
        <p class="subtitle">Boletín Semanal de Derecho Cultural y Restitución de Arte</p>
    </section>

    <main class="container">
        <section class="issues">
            <h2>Boletines Disponibles</h2>
            {ISSUES_CONTENT}
        </section>
    </main>

    <footer class="footer">
        <p>&copy; 2025 Kepler Karst Law Firm. Todos los derechos reservados.</p>
        <p style="margin-top: 0.5rem; font-size: 0.9rem; opacity: 0.8;">Boletín semanal de Arte y Derecho</p>
    </footer>
</body>
</html>"""
    
    # Replace placeholder with actual content
    final_html = template.replace("{ISSUES_CONTENT}", issues_html)
    
    # Write the file
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print(f"✅ Generated art law index with {len(issues)} issues")

def main():
    """Main function"""
    print("🔧 Building dynamic indexes...")
    
    # Generate both indexes
    generate_sovereign_debt_index()
    generate_art_law_index()
    
    print("✅ All indexes generated successfully!")
    print("\n📝 To automatically rebuild indexes after adding new issues:")
    print("   python scripts/build_index.py")

if __name__ == "__main__":
    main()
