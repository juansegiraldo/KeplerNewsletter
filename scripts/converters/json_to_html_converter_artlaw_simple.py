#!/usr/bin/env python3
"""
JSON a HTML (Arte y Derecho) - Versión Simplificada
Convierte datos JSON estructurados a HTML con marca Kepler Karst.
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import quote


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


def create_google_search_url(headline: str, original_url: str) -> str:
    """Crea URL de búsqueda en Google"""
    search_terms = clean_text(headline) or ''
    return f"https://www.google.com/search?q={quote(search_terms)}"


def get_smart_url(headline: str, original_url: str):
    """Devuelve (original|#, url búsqueda)"""
    if not original_url or original_url == '#':
        return "#", create_google_search_url(headline, '')
    return original_url, create_google_search_url(headline, original_url)


def generate_html(data: dict) -> str:
    """Genera el HTML del digest"""
    metadata = data.get('metadata', {}) or {}
    executive_summary = data.get('executive_summary', {}) or {}
    items = data.get('items', []) or []

    title = metadata.get('report_title', 'Arte y Derecho — Boletín semanal')
    
    # Preparar resumen
    key_findings = executive_summary.get('key_findings', [])
    summary_text = key_findings[0] if key_findings else 'Resumen de novedades en Arte y Derecho.'
    annual_bullets = executive_summary.get('annual_bullets', [])

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Kepler Karst</title>
    <meta name="description" content="Boletín semanal de las novedades más relevantes de Arte y Derecho.">
    
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
            font-family: Georgia, serif;
            font-weight: bold;
            margin-bottom: 1rem; color: var(--e-global-color-primary);
        }}

        .items {{ margin: 3rem 0; }}
        .item {{ margin-bottom: 2rem; padding: 1.5rem; border: 1px solid #e0e0e0; border-radius: 4px; transition: box-shadow 0.3s ease; }}
        .item:hover {{ box-shadow: 0 4px 12px rgba(0,0,0,0.1); }}
        .item h3 {{
            font-family: Georgia, serif;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }}
        .item h3 a {{ color: var(--e-global-color-primary); text-decoration: none; }}
        .item h3 a:hover {{ text-decoration: underline; }}
        .item-meta {{ font-size: 0.9rem; color: #666; margin-bottom: 1rem; }}
        .item-content {{ margin-bottom: 1rem; }}

        .chips {{ display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 0.5rem; }}
        .chip {{ font-size: 0.75rem; background: #f3f3f3; border: 1px solid #e2e2e2; border-radius: 999px; padding: 0.2rem 0.6rem; }}

        .item-links {{ margin-top: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap; }}
        .link-btn {{ display: inline-block; padding: 0.5rem 1rem; text-decoration: none; border-radius: 25px; font-size: 0.8rem; font-weight: 500; transition: all 0.3s ease; }}
        .google-link {{ background-color: #E9D95D; color: #333; }}
        .google-link:hover {{ background-color: #d4c552; }}

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
        <h2>{format_date_for_display(metadata.get('coverage_period', {}).get('start_date', 'DD-MM-YYYY'))} - {format_date_for_display(metadata.get('coverage_period', {}).get('end_date', 'DD-MM-YYYY'))}</h2>
    </section>

    <main class="container">
        <section class="tldr">
            <h2>Resumen</h2>
            <p>{clean_text(summary_text)}</p>
            {f"<ul>{''.join(f'<li>{clean_text(str(b or ''))}</li>' for b in annual_bullets if b)}</ul>" if annual_bullets else ""}
        </section>

        <section class="items">
"""

    # Render de ítems
    for i, item in enumerate(items, 1):
        headline = clean_text(item.get('headline', 'Sin título')) or 'Sin título'
        source = item.get('source', {}) or {}
        original_url = source.get('url', '#')
        original_url_clean, google_url = get_smart_url(headline, original_url)

        jurisdiction = item.get('jurisdiction') or ''
        date = item.get('publication_date', 'Fecha desconocida')
        source_name = source.get('name', 'Fuente desconocida')
        legal_stage = item.get('legal_stage') or ''
        content = item.get('content', 'Contenido no disponible.') or 'Contenido no disponible.'
        summary = clean_text(content) if isinstance(content, str) else 'Contenido no disponible.'
        
        # Clasificación
        classification = item.get('classification', {}) or {}
        legal_instruments = classification.get('legal_instruments', []) or []
        compliance_flags = item.get('compliance_flags', []) or []

        # Chips informativas
        chips_html = ''
        if legal_stage:
            chips_html += f'<span class="chip">Etapa: {legal_stage}</span>'
        if legal_instruments:
            chips_html += f'<span class="chip">Leyes: {", ".join(legal_instruments)}</span>'
        if compliance_flags:
            chips_html += f'<span class="chip">Flags: {", ".join(compliance_flags)}</span>'

        html += f"""
            <article class="item">
                <h3><a href="{original_url_clean}" target="_blank">{i}. {headline}</a></h3>
                <div class="item-meta">{jurisdiction} — {date} — {source_name}</div>
                <div class="item-content">{summary}</div>
                <div class="chips">{chips_html}</div>
                <div class="item-links">
                    <a href="{google_url}" target="_blank" class="link-btn google-link">Buscar en Google</a>
                </div>
            </article>
        """

    html += """
        </section>
    </main>

    <footer class="footer">
        <p>&copy; 2025 Kepler Karst Law Firm. Todos los derechos reservados.</p>
        <p style="margin-top: 0.5rem; font-size: 0.9rem; opacity: 0.8;">Boletín semanal de Arte y Derecho</p>
        <p style="margin-top: 0.5rem; font-size: 0.8rem; opacity: 0.6;">Hecho por Laura Villarraga</p>
    </footer>
</body>
</html>"""

    return html


def main():
    if len(sys.argv) != 2:
        print("Uso: python json_to_html_converter_artlaw_simple.py <archivo_json>")
        print("Ejemplo: python json_to_html_converter_artlaw_simple.py arte_derecho_report_2025_08_20_cl.json")
        sys.exit(1)

    json_file = sys.argv[1]
    base_name = Path(json_file).stem
    
    # Cargar datos JSON
    data = load_json_data(json_file)
    
    # Generar HTML
    html = generate_html(data)
    
    # Crear directorio de salida si no existe
    output_dir = Path("docs/art-law/issues")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Escribir archivo HTML
    output_file = output_dir / f"{base_name}.html"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ Archivo HTML generado exitosamente:")
    print(f"   📄 Digest: {output_file}")
    print(f"📈 Procesados {len(data.get('items', []))} ítems")
    print(f"📁 Archivo guardado en: {output_dir}")


if __name__ == "__main__":
    main()
