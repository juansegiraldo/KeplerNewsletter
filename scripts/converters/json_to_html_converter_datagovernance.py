#!/usr/bin/env python3
"""
JSON a HTML (Gobernanza de Datos) v1
Convierte datos JSON estructurados (según el prompt de Gobernanza de Datos) a HTML con marca Kepler Karst.
Genera dos archivos: digest original y dashboard de analytics.

Uso:
  python json_to_html_converter_datagovernance.py <archivo.json>
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import quote
from collections import Counter


def load_json_data(json_file: str):
    """Cargar datos JSON desde archivo"""
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {json_file}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: JSON inválido en {json_file}: {e}")
        sys.exit(1)


def clean_text(text: str | None) -> str | None:
    """Limpia texto removiendo referencias y artefactos frecuentes"""
    import re
    if not text:
        return text
    text = re.sub(r'【[^】]*】', '', text)
    text = re.sub(r'†[A-Z]\d+-\d+', '', text)
    text = re.sub(r'【[^】]*†[^】]*】', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def highlight_countries(text: str | None) -> str | None:
    """Resalta nombres de países, estados americanos y ciudades principales en el texto"""
    import re
    if not text:
        return text
    
    # Países principales para data governance
    countries = [
        'United States', 'United Kingdom', 'European Union', 'Canada', 'Brazil', 'Australia', 'Japan', 'South Korea',
        'India', 'China', 'Singapore', 'Switzerland', 'Norway', 'Iceland', 'Liechtenstein', 'New Zealand',
        'Estados Unidos', 'Reino Unido', 'Unión Europea', 'Canadá', 'Brasil', 'Australia', 'Japón', 'Corea del Sur',
        'India', 'China', 'Singapur', 'Suiza', 'Noruega', 'Islandia', 'Liechtenstein', 'Nueva Zelanda'
    ]
    
    # Estados americanos principales
    us_states = [
        'California', 'New York', 'Texas', 'Florida', 'Illinois', 'Pennsylvania', 'Ohio', 'Georgia',
        'North Carolina', 'Michigan', 'New Jersey', 'Virginia', 'Washington', 'Arizona', 'Massachusetts'
    ]
    
    # Ciudades principales de tech
    major_cities = [
        'San Francisco', 'Silicon Valley', 'Seattle', 'Austin', 'New York', 'Boston', 'Los Angeles',
        'Chicago', 'Washington DC', 'Atlanta', 'Denver', 'Portland', 'Miami', 'Dallas', 'Houston',
        'London', 'Paris', 'Berlin', 'Amsterdam', 'Brussels', 'Dublin', 'Stockholm', 'Copenhagen',
        'Toronto', 'Vancouver', 'Montreal', 'São Paulo', 'Rio de Janeiro', 'Sydney', 'Melbourne',
        'Tokyo', 'Seoul', 'Singapore', 'Hong Kong', 'Mumbai', 'Bangalore', 'New Delhi'
    ]
    
    all_entities = countries + us_states + major_cities
    pattern = r'\b(' + '|'.join(re.escape(entity) for entity in all_entities) + r')\b'
    highlighted_text = re.sub(pattern, r'<strong>\1</strong>', text, flags=re.IGNORECASE)
    
    return highlighted_text


def create_google_search_url(headline: str, original_url: str) -> str:
    """Crea URL de búsqueda en Google usando el slug de la URL si existe"""
    try:
        from urllib.parse import urlparse
        parsed = urlparse(original_url or '')
        path_parts = (parsed.path or '').strip('/').split('/')
        slug = path_parts[-1] if path_parts and path_parts[-1] else ''
    except Exception:
        slug = ''

    search_terms = slug if slug else (clean_text(headline) or '')
    return f"https://www.google.com/search?q={quote(search_terms)}"


def get_smart_url(headline: str, original_url: str):
    """Devuelve (original|#, url búsqueda, url suerte)"""
    if not original_url or original_url == '#':
        return "#", create_google_search_url(headline, ''), f"{create_google_search_url(headline, '')}&btnI"
    return original_url, create_google_search_url(headline, original_url), f"{create_google_search_url(headline, original_url)}&btnI"


def format_date_for_display(date_str: str) -> str:
    """Convierte fecha de formato DD-MM-YYYY a DD Month YYYY"""
    if not date_str or date_str == 'DD-MM-YYYY':
        return 'DD Month YYYY'
    
    try:
        day, month, year = date_str.split('-')
        months = {
            '01': 'Enero', '02': 'Febrero', '03': 'Marzo', '04': 'Abril',
            '05': 'Mayo', '06': 'Junio', '07': 'Julio', '08': 'Agosto',
            '09': 'Septiembre', '10': 'Octubre', '11': 'Noviembre', '12': 'Diciembre'
        }
        month_name = months.get(month, month)
        return f"{day} {month_name} {year}"
    except:
        return date_str


def render_list(values: list[str] | None) -> str:
    if not values:
        return ""
    safe_values = [clean_text(v) for v in values if v]
    safe_values = [v for v in safe_values if v]
    return ", ".join(safe_values)


def generate_jurisdiction_chart(data: dict) -> str:
    """Genera un gráfico simple HTML/CSS mostrando la distribución por jurisdicción"""
    analytics = data.get('analytics', {})
    coverage_analysis = analytics.get('coverage_analysis', {})
    jurisdiction_distribution = coverage_analysis.get('jurisdiction_distribution', {})
    
    if not jurisdiction_distribution:
        return ""
    
    region_mapping = {
        'US': 'Estados Unidos',
        'UK': 'Reino Unido', 
        'EU': 'Unión Europea',
        'CA': 'Canadá',
        'BR': 'Brasil',
        'Global': 'Global'
    }
    
    jurisdiction_items = []
    for region, count in jurisdiction_distribution.items():
        region_name = region_mapping.get(region, region)
        jurisdiction_items.append((region_name, count))
    
    jurisdiction_items.sort(key=lambda x: x[1], reverse=True)
    top_jurisdictions = jurisdiction_items[:8]
    
    if not top_jurisdictions:
        return ""
    
    max_count = max(count for _, count in top_jurisdictions)
    
    chart_html = """
            <div class="jurisdiction-chart">
                <h3>Distribución Geográfica</h3>
                <div class="chart-container">
"""
    
    for jurisdiction, count in top_jurisdictions:
        percentage = (count / max_count) * 100
        chart_html += f"""
                    <div class="chart-row">
                        <div class="chart-label">{jurisdiction}</div>
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


def generate_meta_html(data: dict) -> str:
    """Genera HTML de analytics con gráficos y métricas"""
    
    metadata = data.get('metadata', {})
    analytics = data.get('analytics', {})
    items = data.get('items', [])
    coverage_analysis = analytics.get('coverage_analysis', {})
    content_metrics = analytics.get('content_metrics', {})
    processing_statistics = analytics.get('processing_statistics', {})
    
    category_distribution = coverage_analysis.get('category_distribution', {})
    jurisdiction_distribution = coverage_analysis.get('jurisdiction_distribution', {})
    score_distribution = content_metrics.get('score_distribution', {})
    
    all_secondary_tags = []
    for item in items:
        secondary_tags = item.get('classification', {}).get('secondary_tags', [])
        all_secondary_tags.extend(secondary_tags)
    
    tag_counts = Counter(all_secondary_tags)
    top_tags = tag_counts.most_common(10)
    
    all_instruments = []
    for item in items:
        instruments = item.get('classification', {}).get('instruments', [])
        all_instruments.extend(instruments)
    
    instrument_counts = Counter(all_instruments)
    top_instruments = instrument_counts.most_common(8)
    
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard de Analytics - {metadata.get('title', 'Gobernanza de Datos')} | Kepler Karst</title>
    <meta name="description" content="Dashboard de analytics y métricas para el boletín de Gobernanza de Datos">
    
    <style>
        @font-face {{
            font-family: "Sharp Grotesk";
            src: url("../assets/fonts/SharpGroteskBook16-Regular.ttf") format("truetype");
            font-weight: normal;
            font-style: normal;
        }}
        
        :root {{
            --e-global-color-primary: #000000;
            --e-global-color-secondary: #4A90E2;
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
            background: linear-gradient(90deg, var(--e-global-color-secondary), #357ABD);
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
            color: white;
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
        <h1>Dashboard de Analytics</h1>
        <div class="subtitle">{metadata.get('title', 'Gobernanza de Datos')}</div>
        <div class="subtitle">{format_date_for_display(metadata.get('period', {}).get('start_date', ''))} - {format_date_for_display(metadata.get('period', {}).get('end_date', ''))}</div>
    </header>

    <main class="container">
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number">{processing_statistics.get('sources_scanned', 0)}</div>
                <div class="stat-label">Fuentes Escaneadas</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{processing_statistics.get('articles_reviewed', 0)}</div>
                <div class="stat-label">Artículos Revisados</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{processing_statistics.get('items_published', 0)}</div>
                <div class="stat-label">Ítems Publicados</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{content_metrics.get('average_score', 0):.1f}</div>
                <div class="stat-label">Puntuación Promedio</div>
            </div>
        </div>

        <div class="dashboard-grid">
            <div class="chart-card">
                <h3>Distribución por Categorías</h3>
                <div class="chart-container">
"""
    
    if category_distribution:
        max_count = max(category_distribution.values())
        for category, count in sorted(category_distribution.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / max_count) * 100
            category_name = category.replace('_', ' ').title()
            html += f"""
                    <div class="chart-row">
                        <div class="chart-label">{category_name}</div>
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
                <h3>Distribución Geográfica</h3>
                <div class="chart-container">
"""
    
    if jurisdiction_distribution:
        max_count = max(jurisdiction_distribution.values())
        for region, count in sorted(jurisdiction_distribution.items(), key=lambda x: x[1], reverse=True):
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
                <h3>Distribución de Puntuaciones</h3>
                <div class="chart-container">
"""
    
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
                <h3>Top Instrumentos Legales</h3>
                <div class="chart-container">
"""
    
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
            <h3>Top Tags Secundarios</h3>
            <div class="tag-cloud">
"""
    
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
        <p>&copy; 2025 Kepler Karst Law Firm. Todos los derechos reservados.</p>
        <p style="margin-top: 0.5rem; font-size: 0.9rem; opacity: 0.8;">Dashboard de Analytics para Gobernanza de Datos</p>
    </footer>
</body>
</html>"""

    return html


def generate_original_html(data: dict) -> str:
    """Genera el HTML del digest original"""
    metadata = data.get('metadata', {}) or {}
    executive_summary = data.get('executive_summary', {}) or {}
    items = data.get('items', []) or []
    analytics = data.get('analytics', {}) or {}
    processing_statistics = analytics.get('processing_statistics', {}) or {}
    discarded_items = data.get('discarded_items', []) or []

    title = metadata.get('title', 'Gobernanza de Datos — Boletín semanal')
    subtitle = metadata.get('subtitle', '#DATA GOVERNANCE INSIGHTS')

    css_styles = """
        @font-face {
            font-family: "Sharp Grotesk";
            src: url("../assets/fonts/SharpGroteskBook16-Regular.ttf") format("truetype");
            font-weight: normal;
            font-style: normal;
        }
        
        :root {
            --e-global-color-primary: #000000;
            --e-global-color-secondary: #4A90E2;
            --e-global-color-text: #000000;
            --e-global-typography-primary-font-family: "Georgia";
            --e-global-typography-primary-font-weight: 700;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: "Sharp Grotesk", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            color: var(--e-global-color-text);
            line-height: 1.6;
            background-color: #fff;
        }

        .header {
            background-color: white;
            padding: 1rem 2rem;
        }
        
        .header-content {
            max-width: 1200px;
            margin: 0 auto;
            display: block;
        }
        
        .header-image {
            width: 100%;
            height: auto;
            display: block;
        }

        .date-range {
            background-color: white;
            text-align: center;
            padding: 1rem 2rem;
        }
        
        .date-range h2 {
            font-family: Georgia, serif;
            font-weight: bold;
            font-size: 0.9rem;
            color: var(--e-global-color-primary);
            margin: 0;
        }

        .container { max-width: 1200px; margin: 0 auto; padding: 2rem; }
        .tldr { background-color: var(--e-global-color-secondary); color: white; padding: 2rem; margin: 2rem 0; }
        .tldr h2 {
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            margin-bottom: 1rem; color: white;
        }

        .items { margin: 3rem 0; }
        .item { margin-bottom: 2rem; padding: 1.5rem; border: 1px solid #e0e0e0; border-radius: 4px; transition: box-shadow 0.3s ease; }
        .item:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
        .item h3 {
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            margin-bottom: 0.5rem;
        }
        .item h3 a { color: var(--e-global-color-primary); text-decoration: none; }
        .item h3 a:hover { text-decoration: underline; }
        .item-meta { font-size: 0.9rem; color: #666; margin-bottom: 1rem; }
        .item-content { margin-bottom: 1rem; }

        .chips { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 0.5rem; }
        .chip { font-size: 0.75rem; background: #f3f3f3; border: 1px solid #e2e2e2; border-radius: 999px; padding: 0.2rem 0.6rem; }

        .item-links { margin-top: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap; }
        .link-btn { display: inline-block; padding: 0.5rem 1rem; text-decoration: none; border-radius: 25px; font-size: 0.8rem; font-weight: 500; transition: all 0.3s ease; }
        .google-link { background-color: var(--e-global-color-secondary); color: white; }
        .google-link:hover { background-color: #357ABD; }

        .jurisdiction-chart {
            background-color: white;
            padding: 2rem;
            margin: 2rem 0;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .jurisdiction-chart h3 {
            font-family: Georgia, serif;
            font-weight: bold;
            margin-bottom: 1.5rem;
            color: var(--e-global-color-primary);
            font-size: 1.2rem;
        }
        
        .chart-container {
            margin-top: 1rem;
        }
        
        .chart-row {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 0.8rem;
        }
        
        .chart-label {
            min-width: 120px;
            font-weight: 500;
            font-size: 0.9rem;
        }
        
        .chart-bar-container {
            flex: 1;
            height: 20px;
            background-color: #f0f0f0;
            border-radius: 10px;
            overflow: hidden;
            position: relative;
            border: 1px solid #e0e0e0;
        }
        
        .chart-bar {
            height: 100%;
            background: linear-gradient(90deg, var(--e-global-color-secondary), #357ABD);
            border-radius: 10px;
            transition: width 0.3s ease;
            display: block;
            min-width: 4px;
            position: relative;
        }
        
        .chart-value {
            min-width: 30px;
            text-align: right;
            font-weight: bold;
            color: var(--e-global-color-primary);
        }

        .discarded-section {
            background-color: #f8f9fa;
            padding: 2rem;
            margin: 2rem 0;
            border-radius: 8px;
        }
        
        .discarded-section h2 {
            font-family: Georgia, serif;
            font-weight: bold;
            margin-bottom: 1.5rem;
            color: var(--e-global-color-primary);
            font-size: 1.2rem;
        }
        
        .discarded-item {
            margin-bottom: 1rem;
            padding: 1rem;
            background-color: white;
            border-radius: 4px;
            border: 1px solid #e0e0e0;
        }
        
        .discarded-item h4 {
            font-family: Georgia, serif;
            font-weight: bold;
            margin-bottom: 0.5rem;
            color: var(--e-global-color-primary);
        }
        
        .discarded-meta {
            font-size: 0.8rem;
            color: #666;
            margin-bottom: 0.5rem;
        }

        .footer { background-color: var(--e-global-color-primary); color: white; text-align: center; padding: 2rem; margin-top: 3rem; }

        @media (max-width: 768px) {
            .container { padding: 1rem; }
        }
    """

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Kepler Karst</title>
    <meta name="description" content="Boletín semanal de las novedades más relevantes de Gobernanza de Datos en los últimos 7 días.">
    <meta name="keywords" content="gobernanza de datos, GDPR, CCPA, LGPD, privacidad, seguridad, IA, cumplimiento">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="Boletín semanal de Gobernanza de Datos">
    <meta property="og:type" content="article">
    <meta name="twitter:card" content="summary_large_image">

    <style>
{css_styles}
    </style>
</head>
<body>
    <header class="header">
        <div class="header-content">
            <img src="../assets/headers/HeaderDataGovernance.jpeg" alt="Gobernanza de Datos Header" class="header-image">
        </div>
    </header>

    <section class="date-range">
        <h2>{format_date_for_display(metadata.get('period', {}).get('start_date', 'DD-MM-YYYY'))} - {format_date_for_display(metadata.get('period', {}).get('end_date', 'DD-MM-YYYY'))}</h2>
    </section>

    <main class="container">
        <section class="tldr">
            <h2>Resumen</h2>
            { (lambda bullets: ("<ul>" + ''.join(f"<li>{highlight_countries(clean_text(str(b or '')))}</li>" for b in bullets if b) + "</ul>") if bullets else f"<p>{highlight_countries(clean_text(executive_summary.get('weekly_overview', 'Resumen de novedades en Gobernanza de Datos.')))}</p>" ) (executive_summary.get('weekly_bullets', []) or []) }
        </section>

        {generate_jurisdiction_chart(data)}

        <section class="items">
"""

    # Render de ítems
    for i, item in enumerate(items, 1):
        headline = clean_text(item.get('headline', 'Sin título')) or 'Sin título'
        source = item.get('source', {}) or {}
        original_url = source.get('original_url', '#')
        original_url_clean, google_url, lucky_url = get_smart_url(headline, original_url)

        jurisdiction = item.get('jurisdiction') or ''
        date = item.get('publication_date', 'Fecha desconocida')
        source_name = source.get('name', 'Fuente desconocida')
        legal_stage = item.get('legal_stage') or ''

        content = item.get('content', {}) or {}
        summary = clean_text(content.get('summary', 'Contenido no disponible.')) or 'Contenido no disponible.'
        laws_invoked = content.get('laws_invoked', []) or []
        institutions = content.get('institutions', []) or []
        remedies = content.get('remedies', []) or []
        key_figures = content.get('key_figures', {}) or {}
        next_milestones = content.get('next_milestones', []) or []
        case_refs = content.get('case_refs', []) or []
        entities = content.get('entities', []) or []

        # Componer metadatos
        meta_parts = []
        if jurisdiction:
            meta_parts.append(jurisdiction)
        if date:
            meta_parts.append(date)
        if source_name:
            meta_parts.append(source_name)
        meta_line = ' — '.join(meta_parts) if meta_parts else ''

        # Chips informativas
        chips_html = ''
        if legal_stage:
            chips_html += f'<span class="chip">Etapa: {legal_stage}</span>'
        if laws_invoked:
            chips_html += f'<span class="chip">Leyes: {render_list(laws_invoked)}</span>'
        if institutions:
            chips_html += f'<span class="chip">Instituciones: {render_list(institutions)}</span>'
        if remedies:
            chips_html += f'<span class="chip">Remedios: {render_list(remedies)}</span>'
        if key_figures:
            amount = key_figures.get('amount')
            records_affected = key_figures.get('records_affected')
            kf_parts = []
            if amount:
                kf_parts.append(f"Importe: {amount}")
            if records_affected is not None:
                kf_parts.append(f"Registros afectados: {records_affected}")
            if kf_parts:
                chips_html += f'<span class="chip">Cifras: {"; ".join(kf_parts)}</span>'

        # Entidades (mostramos hasta 2)
        entities_html = ''
        if entities:
            preview = []
            for e in entities[:2]:
                name = e.get('name') or ''
                entity_type = e.get('type') or ''
                sector = e.get('sector') or ''
                preview.append(' — '.join([v for v in [name, entity_type, sector] if v]))
            if preview:
                entities_html = f"<div class=\"item-content\"><strong>Entidades:</strong> {', '.join(preview)}</div>"

        # Próximos hitos
        milestones_html = ''
        if next_milestones:
            milestones_html = f"<div class=\"item-content\"><strong>Próximos hitos:</strong> {render_list(next_milestones)}</div>"

        # Referencias de caso
        case_refs_html = ''
        if case_refs:
            links = ' | '.join([f'<a href="{ref}" target="_blank">Ref</a>' for ref in case_refs if ref])
            case_refs_html = f"<div class=\"item-content\"><strong>Referencias de caso:</strong> {links}</div>"

        html += f"""
            <article class="item">
                <h3><a href="{original_url_clean}" target="_blank">{i}. {headline}</a></h3>
                <div class="item-content">{summary}</div>
                {entities_html}
                {milestones_html}
                {case_refs_html}
                <div class="chips">{chips_html}</div>
                <div class="item-links">
                    <a href="{google_url}" target="_blank" class="link-btn google-link">Buscar en Google</a>
                </div>
            </article>
        """

    # Sección de ítems descartados
    if discarded_items:
        html += """
        </section>

        <section class="discarded-section">
            <h2>Top Titulares Descartados</h2>
"""
        
        for i, d in enumerate(discarded_items[:5], 1):
            title_d = clean_text(d.get('headline') or d.get('title') or 'Sin título') or 'Sin título'
            original_url = d.get('url', '#')
            original_url_clean, google_url, lucky_url = get_smart_url(title_d, original_url)
            html += f"""
            <div class="discarded-item">
                <h4>{i}. {title_d}</h4>
                <div class="item-links">
                    <a href="{google_url}" target="_blank" class="link-btn google-link">Buscar en Google</a>
                </div>
            </div>
"""
        
        html += """
        </section>
"""
    else:
        html += """
        </section>
"""

    html += """
    </main>

    <footer class="footer">
        <p>&copy; 2025 Kepler Karst Law Firm. Todos los derechos reservados.</p>
        <p style="margin-top: 0.5rem; font-size: 0.9rem; opacity: 0.8;">Boletín semanal de Gobernanza de Datos</p>
        <p style="margin-top: 0.5rem; font-size: 0.8rem; opacity: 0.6;">Generado a partir de datos JSON estructurados</p>
    </footer>
</body>
</html>"""

    return html


def main():
    if len(sys.argv) != 2:
        print("Uso: python json_to_html_converter_datagovernance.py <archivo_json>")
        print("Ejemplo: python json_to_html_converter_datagovernance.py datagovernance_digest.json")
        sys.exit(1)

    json_file = sys.argv[1]
    base_name = Path(json_file).stem
    
    # Cargar datos JSON
    data = load_json_data(json_file)
    
    # Generar ambos archivos HTML
    original_html = generate_original_html(data)
    meta_html = generate_meta_html(data)
    
    # Crear directorio de salida si no existe
    output_dir = Path("docs/data-governance/issues")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Escribir archivos HTML en la carpeta correcta
    original_output = output_dir / f"{base_name}.html"
    meta_output = output_dir / f"{base_name}_meta.html"
    
    with open(original_output, 'w', encoding='utf-8') as f:
        f.write(original_html)
    
    with open(meta_output, 'w', encoding='utf-8') as f:
        f.write(meta_html)
    
    print(f"✅ Archivos HTML generados exitosamente:")
    print(f"   📄 Digest original: {original_output}")
    print(f"   📊 Dashboard de analytics: {meta_output}")
    print(f"📈 Procesados {len(data.get('items', []))} ítems")
    print(f"🔍 Usando fallback de Google para URLs")
    print(f"📁 Archivos guardados en: {output_dir}")


if __name__ == "__main__":
    main()
