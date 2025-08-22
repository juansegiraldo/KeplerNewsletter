#!/usr/bin/env python3
"""
HTML converter for merged Art-Law JSON reports.

This script converts the merged JSON structure into HTML with:
- Proper analytics display
- Cluster sections
- Correct date ranges
- All statistics working
"""

import json
import sys
from pathlib import Path
from collections import Counter
from typing import Dict, List, Any


def load_json_data(json_file: str) -> Dict[str, Any]:
    """Load JSON data from file."""
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        sys.exit(1)


def clean_text(text: str | None) -> str | None:
    """Clean and format text, removing weird symbols and line breaks."""
    if not text:
        return None
    if isinstance(text, str):
        # Remove weird symbols and line breaks
        text = text.replace('\\xa0', ' ')  # Non-breaking space
        text = text.replace('\\n', ' ')    # Line breaks
        text = text.replace('\\r', ' ')    # Carriage returns
        text = text.replace('\\t', ' ')    # Tabs
        
        # Remove reference patterns comprehensively
        import re
        # Remove all content between 【 and 】 brackets
        text = re.sub(r'【.*?】', '', text)
        # Remove numeric references in parentheses
        text = re.sub(r'\([0-9]+[^)]*\)', '', text)
        # Remove any remaining reference patterns
        text = re.sub(r'【[^】]*】', '', text)
        
        # Clean up extra spaces
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    return str(text)


def format_date_for_display(date_str: str) -> str:
    """Format date for display."""
    if not date_str:
        return "Unknown"
    
    # Handle different date formats
    if '-' in date_str:
        parts = date_str.split('-')
        if len(parts) == 3:
            day, month, year = parts
            return f"{day} {get_month_name(month)} {year}"
    
    return date_str


def get_month_name(month: str) -> str:
    """Get month name from number."""
    months = {
        '01': 'Enero', '02': 'Febrero', '03': 'Marzo', '04': 'Abril',
        '05': 'Mayo', '06': 'Junio', '07': 'Julio', '08': 'Agosto',
        '09': 'Septiembre', '10': 'Octubre', '11': 'Noviembre', '12': 'Diciembre'
    }
    return months.get(month, month)


def extract_date_range_from_metadata(data: Dict[str, Any]) -> tuple[str, str]:
    """Extract date range - always use 1 January 2025 to today."""
    # Always use 1 January 2025 as start date
    start_date = "01 Enero 2025"
    
    # Always use "a la fecha" as end date
    end_date = "a la fecha"
    
    return start_date, end_date


def bold_important_entities(text: str) -> str:
    """Add bold formatting to important entities like countries, cities, institutions."""
    if not text:
        return text
    
    # Define important entities to bold
    entities = [
        # Countries
        'España', 'Italia', 'Francia', 'Reino Unido', 'Estados Unidos', 'Australia', 
        'Nueva Zelanda', 'Nigeria', 'Alemania', 'Holanda', 'Bélgica', 'Suiza',
        # Regions
        'Unión Europea', 'UE', 'EU', 'EE.UU.', 'EEUU',
        # Cities
        'Washington D.C.', 'Washington', 'Londres', 'París', 'Roma', 'Madrid', 
        'Berlín', 'Ámsterdam', 'Bruselas', 'Ginebra', 'Nueva York', 'Los Ángeles',
        # Cultural/Historical
        'Holocausto', 'Nazi', 'Benín', 'Mesopotámica', 'Africana',
        # Institutions
        'UNESCO', 'UNIDROIT', 'Congreso estadounidense', 'Casa Blanca', 'Smithsonian',
        'TJUE', 'ICOM', 'Suprema Corte', 'ICG', 'Oficina de Copyright de EE.UU.',
        # Operations/Funds
        'Pandora IX', 'Altarpiece', 'Arts Everywhere Fund',
        # Laws and Regulations
        'HEAR Act', 'Art Market Integrity Act', 'Artist\'s Resale Right', 'ARR',
        # Financial/Compliance Terms
        'KYC', 'AML/KYC', 'AML'
    ]
    
    for entity in entities:
        if entity in text:
            text = text.replace(entity, f'<strong>{entity}</strong>')
    
    return text

def format_json_content(content) -> str:
    """Format JSON content to readable text."""
    if not content:
        return ""
    
    # Fields to exclude from display
    excluded_fields = [
        'objects', 'remedies', 'deadline_days', 'case_refs', 'amount', 
        'items_returned', 'annual_impact', 'works_removed', 'artists_affected',
        'canvas_size', 'safety_zone', 'document_date', 'years_missing', 
        'pages_missing', 'artist', 'title', 'year', 'medium', 'quantity', 'period'
    ]
    
    # If content is already a dict, format it directly
    if isinstance(content, dict):
        formatted_parts = []
        for key, value in content.items():
            if key in excluded_fields:
                continue
                
            if key == 'summary':
                formatted_parts.append(f"{value}")
            elif key == 'laws_invoked' and value:
                if isinstance(value, list) and value:
                    laws_text = ', '.join([bold_important_entities(law) for law in value])
                    formatted_parts.append(f"<strong>Leyes aplicables:</strong> {laws_text}")
            elif key == 'institutions' and value:
                if isinstance(value, list) and value:
                    inst_text = ', '.join([bold_important_entities(inst) for inst in value])
                    formatted_parts.append(f"<strong>Instituciones involucradas:</strong> {inst_text}")
            elif key == 'next_milestones' and value:
                if isinstance(value, list) and value:
                    formatted_parts.append(f"<strong>Próximos hitos:</strong> {', '.join(value)}")
                elif isinstance(value, str) and value:
                    formatted_parts.append(f"<strong>Próximos hitos:</strong> {value}")
        
        return '<br><br>'.join(formatted_parts)
    
    # If content is a string that looks like JSON, try to parse it
    if isinstance(content, str):
        if content.startswith('{') or content.startswith('['):
            try:
                import json
                data = json.loads(content)
                
                # Format as readable text
                if isinstance(data, dict):
                    formatted_parts = []
                    for key, value in data.items():
                        if key in excluded_fields:
                            continue
                            
                        if key == 'summary':
                            formatted_parts.append(f"{value}")
                        elif key == 'laws_invoked' and value:
                            if isinstance(value, list) and value:
                                laws_text = ', '.join([bold_important_entities(law) for law in value])
                                formatted_parts.append(f"<strong>Leyes aplicables:</strong> {laws_text}")
                        elif key == 'institutions' and value:
                            if isinstance(value, list) and value:
                                inst_text = ', '.join([bold_important_entities(inst) for inst in value])
                                formatted_parts.append(f"<strong>Instituciones involucradas:</strong> {inst_text}")
                        elif key == 'next_milestones' and value:
                            if isinstance(value, list) and value:
                                formatted_parts.append(f"<strong>Próximos hitos:</strong> {', '.join(value)}")
                            elif isinstance(value, str) and value:
                                formatted_parts.append(f"<strong>Próximos hitos:</strong> {value}")
                    
                    return '<br><br>'.join(formatted_parts)
                else:
                    return str(data)
            except:
                # If JSON parsing fails, return cleaned content
                return clean_text(content)
    
    return clean_text(content)

def get_human_cluster_title(cluster_name: str) -> str:
    """Convert technical cluster names to human-readable titles."""
    title_mapping = {
        'restitution': 'Restituciones de Patrimonio',
        'copyright': 'Derechos de Autor y Propiedad Intelectual',
        'compliance': 'Cumplimiento y Regulaciones',
        'market_integrity': 'Integridad del Mercado del Arte',
        'cultural_policy': 'Políticas Culturales',
        'museum_operations': 'Operaciones de Museos',
        'legal_developments': 'Desarrollos Legales',
        'international_cooperation': 'Cooperación Internacional',
        'sanctions': 'Sanciones y Embargos',
        'labor_issues': 'Asuntos Laborales en Museos',
        'censorship': 'Censura y Libertad de Expresión',
        'ethical_collections': 'Colecciones Éticas',
        'free_expression': 'Libertad de Expresión',
        'heritage_protection': 'Protección del Patrimonio',
        'art_market': 'Mercado del Arte',
        'cultural_heritage': 'Patrimonio Cultural',
        'legal_framework': 'Marco Legal',
        'international_law': 'Derecho Internacional',
        'museum_ethics': 'Ética Museística',
        'cultural_diplomacy': 'Diplomacia Cultural',
        # Additional mappings for specific cluster names found in data
        'labor employment': 'Asuntos Laborales',
        'ip copyright': 'Propiedad Intelectual',
        'compliance regulatory': 'Cumplimiento Regulatorio',
        'policy politics': 'Políticas y Política',
        'fraud authenticity': 'Fraude y Autenticidad',
        'ethics governance': 'Ética y Gobernanza',
        'public art': 'Arte Público',
        'museum governance': 'Gobernanza de Museos',
        'data privacy': 'Privacidad de Datos',
        'Labor Employment': 'Asuntos Laborales',
        'Ip Copyright': 'Propiedad Intelectual',
        'Compliance Regulatory': 'Cumplimiento Regulatorio',
        'Policy Politics': 'Políticas y Política',
        'Fraud Authenticity': 'Fraude y Autenticidad',
        'Ethics Governance': 'Ética y Gobernanza',
        'Public Art': 'Arte Público',
        'Museum Governance': 'Gobernanza de Museos',
        'Data Privacy': 'Privacidad de Datos'
    }
    
    # Try exact match first
    if cluster_name in title_mapping:
        return title_mapping[cluster_name]
    
    # Try lowercase match
    if cluster_name.lower() in title_mapping:
        return title_mapping[cluster_name.lower()]
    
    # For jurisdiction-based clusters, create a readable title
    if ' — ' in cluster_name:
        parts = cluster_name.split(' — ')
        if len(parts) == 2:
            jurisdiction, institution = parts
            return f"{jurisdiction.upper()} — {institution}"
    
    # Default: clean up the cluster name
    return cluster_name.replace('_', ' ').title()

def generate_cluster_section(cluster_name: str, item_ids: List[str], items_by_id: Dict[str, Any], cluster_index: int, global_item_counter: int) -> tuple[str, int]:
    """Generate HTML for a cluster section."""
    if not item_ids:
        return ""
    
    cluster_items = []
    for item_id in item_ids:
        if item_id in items_by_id:
            item = items_by_id[item_id]
            cluster_items.append(item)
    
    if not cluster_items:
        return "", global_item_counter
    
    # Sort items by date if available
    cluster_items.sort(key=lambda x: x.get('date', ''), reverse=True)
    
    # Get human-readable title
    human_title = get_human_cluster_title(cluster_name)
    
    html = f'''
        <section class="cluster-section" id="cluster-{cluster_index}">
            <h2 class="cluster-title">{human_title}</h2>
            <div class="cluster-items">'''
    
    for i, item in enumerate(cluster_items, 1):
        title = clean_text(item.get('title', ''))
        content = item.get('content', '')
        url = item.get('url', '#')
        date = item.get('date', '')
        jurisdiction = item.get('jurisdiction', '')
        legal_stage = item.get('legal_stage', '')
        
        # Use global counter for sequential numbering
        current_item_number = global_item_counter
        global_item_counter += 1
        
        # Generate title if missing
        if not title or title == 'Sin título':
            # Try to extract title from content
            if isinstance(content, dict) and 'summary' in content:
                summary = content['summary']
                # Clean summary first
                summary = clean_text(summary)
                # Extract first sentence or meaningful phrase
                sentences = summary.split('.')
                if sentences and len(sentences[0]) > 10:
                    title = sentences[0].strip()
                    if len(title) > 80:
                        title = title[:77] + "..."
                else:
                    title = "Desarrollo en " + jurisdiction if jurisdiction else "Actualización Legal"
            elif isinstance(content, str):
                # Clean content first
                clean_content = clean_text(content)
                # Extract first meaningful sentence
                sentences = clean_content.split('.')
                if sentences and len(sentences[0]) > 10:
                    title = sentences[0].strip()
                    if len(title) > 80:
                        title = title[:77] + "..."
                else:
                    title = "Desarrollo en " + jurisdiction if jurisdiction else "Actualización Legal"
            else:
                title = "Desarrollo en " + jurisdiction if jurisdiction else "Actualización Legal"
        
        # Clean title as well
        title = clean_text(title)
        
        # Format content properly
        formatted_content = format_json_content(content)
        # Apply additional cleaning to formatted content
        formatted_content = clean_text(formatted_content)
        formatted_content = bold_important_entities(formatted_content)
        
        # Get compliance labels
        compliance_labels = item.get('compliance_labels', [])
        compliance_chips = ""
        for label in compliance_labels:
            compliance_chips += f'<span class="chip">Cumplimiento: {label}</span>'
        
        html += f'''
                <article class="item">
                    <div class="item-number">{current_item_number}</div>
                    <div class="cluster-flag">{human_title}</div>
                    <h3><a href="{url}" target="_blank">{title}</a></h3>
                    <div class="item-content">{formatted_content}</div>
                    <div class="chips">
                        <span class="chip">Fecha: {date}</span>
                        <span class="chip">Jurisdicción: {jurisdiction}</span>
                        <span class="chip">Etapa: {legal_stage}</span>
                        {compliance_chips}
                    </div>
                    <div class="item-links">
                        <a href="https://www.google.com/search?q={title.replace(' ', '%20')}" target="_blank" class="link-btn google-link">Buscar en Google</a>
                    </div>
                </article>'''
    
    html += '''
            </div>
        </section>'''
    
    return html, global_item_counter


def generate_original_html(data: dict) -> str:
    """Generate the main HTML report."""
    
    metadata = data.get('metadata', {})
    executive_summary = data.get('executive_summary', {})
    items = data.get('items', [])
    clusters = data.get('clusters', {})
    analytics = data.get('analytics', {})
    
    # Get date range
    start_date, end_date = extract_date_range_from_metadata(data)
    
    # Create items lookup
    items_by_id = {item.get('item_id', ''): item for item in items}
    
    # Get analytics data
    totals = analytics.get('totals', {})
    total_items = totals.get('items_combined', 0)
    unique_items = totals.get('unique_item_ids', 0)
    total_sources = len(totals.get('source_items', {}))
    
    # Get executive summary
    bullets = executive_summary.get('bullets', [])
    key_findings = executive_summary.get('key_findings', [])
    overview = executive_summary.get('overview', '')
    
    # Generate bullets HTML with proper formatting
    bullets_html = ""
    for bullet in bullets:
        cleaned_bullet = clean_text(bullet)
        # Remove bullet symbols if present
        if cleaned_bullet.startswith('•'):
            cleaned_bullet = cleaned_bullet[1:].strip()
        formatted_bullet = bold_important_entities(cleaned_bullet)
        bullets_html += f'<li>{formatted_bullet}</li>'
    
    # Generate key findings HTML
    findings_html = ""
    for finding in key_findings:
        cleaned_finding = clean_text(finding)
        formatted_finding = bold_important_entities(cleaned_finding)
        findings_html += f'<li>{formatted_finding}</li>'
    
    # Generate glossary with cross-references
    glossary_html = ""
    cluster_index = 1
    cluster_mapping = {}  # To track cluster names and their indices
    
    # Only use by_normalized_category clusters to avoid duplicates
    if 'by_normalized_category' in clusters:
        cluster_data = clusters['by_normalized_category']
        if isinstance(cluster_data, dict):
            for cluster_name, item_ids in cluster_data.items():
                if isinstance(item_ids, list) and item_ids:
                    human_title = get_human_cluster_title(cluster_name)
                    item_count = len([item_id for item_id in item_ids if item_id in items_by_id])
                    cluster_mapping[cluster_name] = cluster_index
                    glossary_html += f'<li><a href="#cluster-{cluster_index}">{human_title}</a> <span class="glossary-count">({item_count} artículos)</span></li>'
                    cluster_index += 1
    
    # Generate clusters HTML with global sequential numbering
    clusters_html = ""
    cluster_index = 1
    global_item_counter = 1  # Start global counter at 1
    
    # Only use by_normalized_category clusters to avoid duplicates
    if 'by_normalized_category' in clusters:
        cluster_data = clusters['by_normalized_category']
        if isinstance(cluster_data, dict):
            for cluster_name, item_ids in cluster_data.items():
                if isinstance(item_ids, list):
                    cluster_html, global_item_counter = generate_cluster_section(cluster_name, item_ids, items_by_id, cluster_index, global_item_counter)
                    clusters_html += cluster_html
                    cluster_index += 1
    
    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Arte y Derecho — Reporte Consolidado | Kepler Karst</title>
    <meta name="description" content="Reporte consolidado de las novedades más relevantes de Arte y Derecho en 2025.">
    <meta name="keywords" content="arte y derecho, restitución, VARA, ARR, UNESCO, UNIDROIT, cumplimiento, sanciones, museos">
    <meta property="og:title" content="Arte y Derecho — Reporte Consolidado">
    <meta property="og:description" content="Reporte consolidado de Arte y Derecho">
    <meta property="og:type" content="article">
    <meta name="twitter:card" content="summary_large_image">

    <style>
        @font-face {{
            font-family: "Sharp Grotesk";
            src: url("../assets/fonts/SharpGroteskBook16-Regular.ttf") format("truetype");
            font-weight: normal;
            font-style: normal;
        }}
        
        :root {{
            --e-global-color-primary: #000000;
            --e-global-color-secondary: #F1EEA4;
            --e-global-color-text: #000000;
            --e-global-typography-primary-font-family: "Georgia";
            --e-global-typography-primary-font-weight: 700;
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

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

        .container {{ max-width: 1200px; margin: 0 auto; padding: 2rem; }}
        
        .tldr {{ background-color: var(--e-global-color-secondary); padding: 2rem; margin: 2rem 0; }}
        .tldr h2 {{
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            margin-bottom: 1rem; color: var(--e-global-color-primary);
        }}

        .cluster-section {{
            margin: 3rem 0;
            border: 2px solid var(--e-global-color-secondary);
            border-radius: 8px;
            overflow: hidden;
        }}
        
        .cluster-title {{
            background-color: var(--e-global-color-secondary);
            padding: 1rem 2rem;
            font-family: Georgia, serif;
            font-weight: bold;
            font-size: 1.3rem;
            color: var(--e-global-color-primary);
            margin: 0;
        }}
        
        .cluster-items {{
            padding: 2rem;
        }}

        .items {{ margin: 3rem 0; }}
        .item {{ 
            margin-bottom: 2rem; 
            padding: 1.5rem; 
            border: 1px solid #e0e0e0; 
            border-radius: 4px; 
            transition: box-shadow 0.3s ease;
            position: relative;
        }}
        .item:hover {{ box-shadow: 0 4px 12px rgba(0,0,0,0.1); }}
        
        .item-number {{
            position: absolute;
            top: -10px;
            left: 20px;
            background: var(--e-global-color-secondary);
            color: var(--e-global-color-primary);
            font-weight: bold;
            padding: 5px 10px;
            border-radius: 15px;
            font-size: 0.8rem;
            border: 2px solid var(--e-global-color-primary);
        }}
        
        .item h3 {{
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            margin-bottom: 0.5rem;
            margin-top: 0.5rem;
        }}
        .item h3 a {{ color: var(--e-global-color-primary); text-decoration: none; }}
        .item h3 a:hover {{ text-decoration: underline; }}
        .item-meta {{ font-size: 0.9rem; color: #666; margin-bottom: 1rem; }}
        .item-content {{ margin-bottom: 1rem; }}
        
        .toc {{
            background-color: #f8f9fa;
            padding: 2rem;
            margin: 2rem 0;
            border-radius: 8px;
            border-left: 4px solid var(--e-global-color-secondary);
        }}
        
        .toc h3 {{
            font-family: Georgia, serif;
            font-weight: bold;
            margin-bottom: 1rem;
            color: var(--e-global-color-primary);
        }}
        
        .toc ul {{
            list-style: none;
            padding: 0;
        }}
        
        .toc li {{
            margin-bottom: 0.5rem;
            padding: 0.5rem 0;
            border-bottom: 1px solid #e0e0e0;
        }}
        
        .toc li:last-child {{
            border-bottom: none;
        }}
        
        .toc a {{
            color: var(--e-global-color-primary);
            text-decoration: none;
            font-weight: 500;
        }}
        
        .toc a:hover {{
            text-decoration: underline;
        }}
        
        .toc-count {{
            color: #666;
            font-size: 0.9rem;
            font-weight: normal;
        }}
        
        .glossary {{
            background-color: #f8f9fa;
            padding: 2rem;
            margin: 2rem 0;
            border-radius: 8px;
            border-left: 4px solid var(--e-global-color-secondary);
        }}
        
        .glossary h3 {{
            font-family: Georgia, serif;
            font-weight: bold;
            margin-bottom: 1rem;
            color: var(--e-global-color-primary);
        }}
        
        .glossary ul {{
            list-style: none;
            padding: 0;
        }}
        
        .glossary li {{
            margin-bottom: 0.5rem;
            padding: 0.5rem 0;
            border-bottom: 1px solid #e0e0e0;
        }}
        
        .glossary li:last-child {{
            border-bottom: none;
        }}
        
        .glossary a {{
            color: var(--e-global-color-primary);
            text-decoration: none;
            font-weight: 500;
        }}
        
        .glossary a:hover {{
            text-decoration: underline;
        }}
        
        .glossary-count {{
            color: #666;
            font-size: 0.9rem;
            font-weight: normal;
        }}
        
        .cluster-flag {{
            position: absolute;
            top: -10px;
            right: 20px;
            background: #e3f2fd;
            color: #1976d2;
            font-weight: 500;
            padding: 4px 8px;
            border-radius: 12px;
            font-size: 0.7rem;
            border: 1px solid #bbdefb;
            max-width: 200px;
            text-align: center;
        }}

        .chips {{ display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 0.5rem; }}
        .chip {{ font-size: 0.75rem; background: #f3f3f3; border: 1px solid #e2e2e2; border-radius: 999px; padding: 0.2rem 0.6rem; }}

        .item-links {{ margin-top: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap; }}
        .link-btn {{ display: inline-block; padding: 0.5rem 1rem; text-decoration: none; border-radius: 25px; font-size: 0.8rem; font-weight: 500; transition: all 0.3s ease; }}
        .google-link {{ background-color: #E9D95D; color: #333; }}
        .google-link:hover {{ background-color: #d4c552; }}

        .stats-summary {{
            background-color: #f8f9fa;
            padding: 2rem;
            margin: 2rem 0;
            border-radius: 8px;
            border-left: 4px solid var(--e-global-color-secondary);
        }}
        
        .stats-summary h3 {{
            font-family: Georgia, serif;
            font-weight: bold;
            margin-bottom: 1rem;
            color: var(--e-global-color-primary);
        }}
        
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 1rem;
        }}
        
        .stat-item {{
            text-align: center;
        }}
        
        .stat-number {{
            font-size: 1.5rem;
            font-weight: bold;
            color: var(--e-global-color-primary);
        }}
        
        .stat-label {{
            font-size: 0.8rem;
            color: #666;
        }}

        .footer {{ background-color: var(--e-global-color-primary); color: white; text-align: center; padding: 2rem; margin-top: 3rem; }}

        @media (max-width: 768px) {{
            .container {{ padding: 1rem; }}
        }}
    </style>
</head>
<body>
    <header class="header">
        <div class="header-content">
            <img src="../assets/headers/HeaderArt_v2.jpeg" alt="Arte y Derecho Header" class="header-image">
        </div>
    </header>

    <section class="date-range">
        <h2>{start_date} - {end_date}</h2>
    </section>

    <main class="container">
        <section class="stats-summary">
            <h3>Resumen Estadístico</h3>
            <div class="stats-grid">
                <div class="stat-item">
                    <div class="stat-number">{total_sources}</div>
                    <div class="stat-label">Fuentes</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">{total_items}</div>
                    <div class="stat-label">Artículos</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">{unique_items}</div>
                    <div class="stat-label">Únicos</div>
                </div>
            </div>
        </section>

        <section class="tldr">
            <h2>Resumen Ejecutivo</h2>
            <p>{overview}</p>
            
            <h3>Puntos Clave</h3>
            <ul>
{bullets_html}
            </ul>
            
            <h3>Hallazgos Principales</h3>
            <ul>
{findings_html}
            </ul>
        </section>

        {clusters_html}

        <section class="glossary">
            <h3>Glosario de Temas</h3>
            <ul>
{glossary_html}
            </ul>
        </section>
    </main>

    <footer class="footer">
        <p>&copy; 2025 Kepler Karst Law Firm. Todos los derechos reservados.</p>
        <p style="margin-top: 0.5rem; font-size: 0.9rem; opacity: 0.8;">Reporte Consolidado de Arte y Derecho</p>
        <p style="margin-top: 0.5rem; font-size: 0.8rem; opacity: 0.6;">Hecho por Laura Villarraga</p>
    </footer>
</body>
</html>'''
    
    return html


def generate_meta_html(data: dict) -> str:
    """Generate meta HTML with analytics and charts for merged reports."""
    
    # Extract analytics data from merged structure
    analytics = data.get('analytics', {})
    totals = analytics.get('totals', {})
    distributions = analytics.get('distributions', {})
    
    # Get basic stats
    total_items = totals.get('items_combined', 0)
    unique_items = totals.get('unique_item_ids', 0)
    source_items = totals.get('source_items', {})
    total_sources = len(source_items)
    
    # Get distributions
    category_dist = distributions.get('normalized_category', {})
    jurisdiction_dist = distributions.get('jurisdiction', {})
    legal_stage_dist = distributions.get('legal_stage', {})
    compliance_dist = distributions.get('compliance_label', {})
    
    # Sort distributions by count
    category_sorted = sorted(category_dist.items(), key=lambda x: x[1], reverse=True)
    jurisdiction_sorted = sorted(jurisdiction_dist.items(), key=lambda x: x[1], reverse=True)
    legal_stage_sorted = sorted(legal_stage_dist.items(), key=lambda x: x[1], reverse=True)
    compliance_sorted = sorted(compliance_dist.items(), key=lambda x: x[1], reverse=True)
    
    # Generate chart HTML
    category_chart = ""
    for category, count in category_sorted[:10]:  # Top 10
        percentage = (count / total_items * 100) if total_items > 0 else 0
        category_chart += f'''
                    <div class="chart-row">
                        <div class="chart-label">{category}</div>
                        <div class="chart-bar-container">
                            <div class="chart-bar" style="width: {percentage}%"></div>
                        </div>
                        <div class="chart-value">{count}</div>
                    </div>'''
    
    jurisdiction_chart = ""
    for jurisdiction, count in jurisdiction_sorted[:10]:  # Top 10
        percentage = (count / total_items * 100) if total_items > 0 else 0
        jurisdiction_chart += f'''
                    <div class="chart-row">
                        <div class="chart-label">{jurisdiction}</div>
                        <div class="chart-bar-container">
                            <div class="chart-bar" style="width: {percentage}%"></div>
                        </div>
                        <div class="chart-value">{count}</div>
                    </div>'''
    
    legal_stage_chart = ""
    for stage, count in legal_stage_sorted[:10]:  # Top 10
        percentage = (count / total_items * 100) if total_items > 0 else 0
        legal_stage_chart += f'''
                    <div class="chart-row">
                        <div class="chart-label">{stage}</div>
                        <div class="chart-bar-container">
                            <div class="chart-bar" style="width: {percentage}%"></div>
                        </div>
                        <div class="chart-value">{count}</div>
                    </div>'''
    
    compliance_chart = ""
    for label, count in compliance_sorted[:10]:  # Top 10
        percentage = (count / total_items * 100) if total_items > 0 else 0
        compliance_chart += f'''
                    <div class="chart-row">
                        <div class="chart-label">{label}</div>
                        <div class="chart-bar-container">
                            <div class="chart-bar" style="width: {percentage}%"></div>
                        </div>
                        <div class="chart-value">{count}</div>
                    </div>'''
    
    # Generate tag cloud for compliance labels
    compliance_tags = ""
    for label, count in compliance_sorted[:20]:  # Top 20
        max_count = max(compliance_sorted, key=lambda x: x[1])[1] if compliance_sorted else 1
        size_class = f"tag-size-{min(5, max(1, (count * 5) // max_count))}"
        compliance_tags += f'<span class="tag {size_class}">{label} ({count})</span>'
    
    # Get date range from metadata
    start_date, end_date = extract_date_range_from_metadata(data)
    
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard de Analytics - Arte, Derecho y Política Cultural — {start_date} a {end_date} | Kepler Karst</title>
    <meta name="description" content="Dashboard de analytics y métricas para el boletín de Arte y Derecho">
    
    <style>
        @font-face {{
            font-family: "Sharp Grotesk";
            src: url("../assets/fonts/SharpGroteskBook16-Regular.ttf") format("truetype");
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
        <h1>Dashboard de Analytics</h1>
        <div class="subtitle">Arte, Derecho y Política Cultural — {start_date} a {end_date}</div>
        <div class="subtitle">{start_date} - {end_date}</div>
    </header>

    <main class="container">
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number">{total_sources}</div>
                <div class="stat-label">Fuentes Escaneadas</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{total_items}</div>
                <div class="stat-label">Artículos Revisados</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{unique_items}</div>
                <div class="stat-label">Ítems Publicados</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">0.0</div>
                <div class="stat-label">Puntuación Promedio</div>
            </div>
        </div>

        <div class="dashboard-grid">
            <div class="chart-card">
                <h3>Distribución por Categorías</h3>
                <div class="chart-container">
{category_chart}
                </div>
            </div>

            <div class="chart-card">
                <h3>Distribución Geográfica</h3>
                <div class="chart-container">
{jurisdiction_chart}
                </div>
            </div>

            <div class="chart-card">
                <h3>Distribución por Etapas Legales</h3>
                <div class="chart-container">
{legal_stage_chart}
                </div>
            </div>

            <div class="chart-card">
                <h3>Top Etiquetas de Cumplimiento</h3>
                <div class="chart-container">
{compliance_chart}
                </div>
            </div>
        </div>

        <div class="chart-card">
            <h3>Top Tags Secundarios</h3>
            <div class="tag-cloud">
{compliance_tags}
            </div>
        </div>
    </main>

    <footer class="footer">
        <p>&copy; 2025 Kepler Karst Law Firm. Todos los derechos reservados.</p>
        <p style="margin-top: 0.5rem; font-size: 0.9rem; opacity: 0.8;">Dashboard de Analytics para Arte y Derecho</p>
        <p style="margin-top: 0.5rem; font-size: 0.8rem; opacity: 0.6;">Hecho por Laura Villarraga</p>
    </footer>
</body>
</html>"""
    
    return html


def main():
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage: python json_to_html_converter_merged.py <json_file>")
        sys.exit(1)
    
    json_file = sys.argv[1]
    data = load_json_data(json_file)
    
    # Generate output filenames
    base_name = Path(json_file).stem
    output_dir = Path("docs/art-law/issues")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate main HTML
    main_html = generate_original_html(data)
    main_output = output_dir / f"{base_name}.html"
    with open(main_output, 'w', encoding='utf-8') as f:
        f.write(main_html)
    
    # Generate meta HTML
    meta_html = generate_meta_html(data)
    meta_output = output_dir / f"{base_name}_meta.html"
    with open(meta_output, 'w', encoding='utf-8') as f:
        f.write(meta_html)
    
    print(f"Generated: {main_output}")
    print(f"Generated: {meta_output}")


if __name__ == "__main__":
    main()
