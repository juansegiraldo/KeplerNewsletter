#!/usr/bin/env python3
"""
JSON a HTML (Arte y Derecho)
Convierte datos JSON estructurados (según el prompt de Arte y Derecho) a HTML con marca Kepler Karst.

Uso:
  python json_to_html_converter_artlaw.py <archivo.json>
"""

import json
import sys
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

    # Eliminar referencias tipo 【...】
    text = re.sub(r'【[^】]*】', '', text)

    # Eliminar otros artefactos comunes
    text = re.sub(r'†[A-Z]\d+-\d+', '', text)
    text = re.sub(r'【[^】]*†[^】]*】', '', text)

    # Normalizar espacios
    text = re.sub(r'\s+', ' ', text).strip()
    return text


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


def create_google_lucky_url(headline: str, original_url: str) -> str:
    """Crea URL de 'Voy a tener suerte' en Google"""
    base = create_google_search_url(headline, original_url)
    return f"{base}&btnI"


def get_smart_url(headline: str, original_url: str):
    """Devuelve (original|#, url búsqueda, url suerte)"""
    if not original_url or original_url == '#':
        return "#", create_google_search_url(headline, ''), create_google_lucky_url(headline, '')
    return original_url, create_google_search_url(headline, original_url), create_google_lucky_url(headline, original_url)


def render_list(values: list[str] | None) -> str:
    if not values:
        return ""
    safe_values = [clean_text(v) for v in values if v]
    safe_values = [v for v in safe_values if v]
    return ", ".join(safe_values)


def generate_html(data: dict) -> str:
    """Genera HTML en español a partir del JSON de Arte y Derecho"""
    metadata = data.get('metadata', {}) or {}
    executive_summary = data.get('executive_summary', {}) or {}
    items = data.get('items', []) or []
    analytics = data.get('analytics', {}) or {}
    processing_statistics = analytics.get('processing_statistics', {}) or {}
    discarded_items = data.get('discarded_items', []) or []

    title = metadata.get('title', 'Arte y Derecho — Boletín semanal')
    subtitle = metadata.get('subtitle', '#BRAVE ADVOCACY')

    # CSS separado para evitar problemas con llaves en f-strings
    css_styles = """
        :root {
            --e-global-color-primary: #000000;
            --e-global-color-secondary: #F1EEA4;
            --e-global-color-text: #000000;
            --e-global-typography-primary-font-family: "Blacker Pro";
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
            background-color: var(--e-global-color-secondary);
            padding: 1rem 2rem;
            border-bottom: 2px solid var(--e-global-color-primary);
        }
        .header-content {
            max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center;
        }
        .logo {
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            font-size: 1.5rem; color: var(--e-global-color-primary);
        }
        .logo-subtitle { font-size: 0.8rem; font-weight: 400; margin-top: -0.2rem; }

        .hero {
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 600"><rect width="1200" height="600" fill="%23f1eea4"/><text x="600" y="300" text-anchor="middle" font-family="Arial" font-size="48" fill="%23000">#BRAVE ADVOCACY</text></svg>');
            background-size: cover; background-position: center; color: white; text-align: center; padding: 4rem 2rem;
        }
        .hero h1 {
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            font-size: 3rem; margin-bottom: 1rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
        }
        .hero .subtitle { font-size: 1.2rem; opacity: 0.9; }

        .container { max-width: 1200px; margin: 0 auto; padding: 2rem; }
        .tldr { background-color: var(--e-global-color-secondary); padding: 2rem; margin: 2rem 0; border-left: 4px solid var(--e-global-color-primary); }
        .tldr h2 {
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            margin-bottom: 1rem; color: var(--e-global-color-primary);
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
        .link-btn { display: inline-block; padding: 0.5rem 1rem; text-decoration: none; border-radius: 4px; font-size: 0.8rem; font-weight: 500; transition: all 0.3s ease; }
        .original-link { background-color: var(--e-global-color-primary); color: white; }
        .original-link:hover { background-color: #333; }
        .google-link { background-color: #4285f4; color: white; }
        .google-link:hover { background-color: #3367d6; }
        .lucky-link { background-color: #34a853; color: white; }
        .lucky-link:hover { background-color: #2d8e47; }

        .meta-section { background-color: #f8f8f8; padding: 2rem; margin-top: 3rem; border-radius: 4px; }
        .meta-section h2 {
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            margin-bottom: 1rem; color: var(--e-global-color-primary);
        }

        .meta-stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-bottom: 2rem; }
        .stat { background: white; padding: 1rem; border-radius: 4px; border-left: 3px solid var(--e-global-color-primary); }
        .stat-number { font-size: 1.5rem; font-weight: bold; color: var(--e-global-color-primary); }
        .stat-label { font-size: 0.9rem; color: #666; }

        .discarded-items { margin-top: 1rem; }
        .discarded-items h3 {
            font-family: var(--e-global-typography-primary-font-family);
            font-weight: var(--e-global-typography-primary-font-weight);
            margin-bottom: 1rem; color: var(--e-global-color-primary);
        }
        .discarded-item { padding: 0.5rem 0; border-bottom: 1px solid #e0e0e0; font-size: 0.9rem; }

        .footer { background-color: var(--e-global-color-primary); color: white; text-align: center; padding: 2rem; margin-top: 3rem; }

        @media (max-width: 768px) {
            .hero h1 { font-size: 2rem; }
            .container { padding: 1rem; }
            .meta-stats { grid-template-columns: 1fr; }
        }
    """

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Kepler Karst</title>
    <meta name="description" content="Boletín semanal de las novedades más relevantes de Arte y Derecho en los últimos 7 días.">
    <meta name="keywords" content="arte y derecho, restitución, VARA, ARR, UNESCO, UNIDROIT, cumplimiento, sanciones, museos">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="Boletín semanal de Arte y Derecho">
    <meta property="og:type" content="article">
    <meta name="twitter:card" content="summary_large_image">

    <style>
{css_styles}
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
                <span style="font-weight: bold; color: var(--e-global-color-primary);">Arte y Derecho</span>
            </nav>
        </div>
    </header>

    <section class="hero">
        <h1>{subtitle}</h1>
        <p class="subtitle">{title}</p>
    </section>

    <main class="container">
        <section class="tldr">
            <h2>Resumen semanal</h2>
            <p>{clean_text(executive_summary.get('weekly_overview', 'Resumen semanal de novedades en Arte y Derecho.'))}</p>
        </section>

        <section class="items">
            <h2 style="font-family: var(--e-global-typography-primary-font-family); font-weight: var(--e-global-typography-primary-font-weight); margin-bottom: 2rem; color: var(--e-global-color-primary);">Ítems ({len(items)} ítems)</h2>
"""

    # Render de ítems
    for item in items:
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
        objects = content.get('objects', []) or []

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
            items_returned = key_figures.get('items_returned')
            kf_parts = []
            if amount:
                kf_parts.append(f"Importe: {amount}")
            if items_returned is not None:
                kf_parts.append(f"Piezas devueltas: {items_returned}")
            if kf_parts:
                chips_html += f'<span class="chip">Cifras: {"; ".join(kf_parts)}</span>'

        # Objetos (mostramos hasta 2)
        objects_html = ''
        if objects:
            preview = []
            for o in objects[:2]:
                artist = o.get('artist') or ''
                title_o = o.get('title') or ''
                year = o.get('year') or ''
                preview.append(' — '.join([v for v in [artist, title_o, year] if v]))
            if preview:
                objects_html = f"<div class=\"item-content\"><strong>Objetos:</strong> {', '.join(preview)}</div>"

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
                <h3><a href="{original_url_clean}" target="_blank">{headline}</a></h3>
                <div class="item-meta">{meta_line}</div>
                <div class="item-content">{summary}</div>
                {objects_html}
                {milestones_html}
                {case_refs_html}
                <div class="chips">{chips_html}</div>
                <div class="item-links">
                    <a href="{original_url_clean}" target="_blank" class="link-btn original-link">Fuente original</a>
                    <a href="{google_url}" target="_blank" class="link-btn google-link">Buscar en Google</a>
                    <a href="{lucky_url}" target="_blank" class="link-btn lucky-link">Voy a tener suerte</a>
                </div>
            </article>
        """

    # Sección Meta/Analítica
    html += f"""
        </section>

        <section class="meta-section">
            <h2>Meta</h2>
            <div class="meta-stats">
                <div class="stat">
                    <div class="stat-number">{processing_statistics.get('sources_scanned', 0)}</div>
                    <div class="stat-label">Fuentes escaneadas</div>
                </div>
                <div class="stat">
                    <div class="stat-number">{processing_statistics.get('articles_reviewed', 0)}</div>
                    <div class="stat-label">Artículos revisados</div>
                </div>
                <div class="stat">
                    <div class="stat-number">{processing_statistics.get('items_published', 0)}</div>
                    <div class="stat-label">Ítems publicados</div>
                </div>
                <div class="stat">
                    <div class="stat-number">{processing_statistics.get('duplicates_identified', 0)}</div>
                    <div class="stat-label">Duplicados identificados</div>
                </div>
            </div>
    """

    # Ítems descartados (top 5)
    if discarded_items:
        html += """
            <div class="discarded-items">
                <h3>Top 5 titulares descartados:</h3>
        """
        for i, d in enumerate(discarded_items[:5], 1):
            title_d = clean_text(d.get('headline') or d.get('title') or 'Sin título') or 'Sin título'
            original_url = d.get('url', '#')
            original_url_clean, google_url, lucky_url = get_smart_url(title_d, original_url)
            html += f"""
                <div class="discarded-item">{i}. {title_d} — <a href="{original_url_clean}" target="_blank">Original</a> | <a href="{google_url}" target="_blank">Google</a> | <a href="{lucky_url}" target="_blank">Suerte</a></div>
            """
        html += """
            </div>
        """

    html += """
        </section>
    </main>

    <footer class="footer">
        <p>&copy; 2025 Kepler Karst Law Firm. Todos los derechos reservados.</p>
        <p style="margin-top: 0.5rem; font-size: 0.9rem; opacity: 0.8;">Boletín semanal de Arte y Derecho</p>
        <p style="margin-top: 0.5rem; font-size: 0.8rem; opacity: 0.6;">Generado a partir de datos JSON estructurados</p>
    </footer>
</body>
</html>"""

    return html


def main():
    if len(sys.argv) != 2:
        print("Uso: python json_to_html_converter_artlaw.py <archivo_json>")
        print("Ejemplo: python json_to_html_converter_artlaw.py artlaw_digest.json")
        sys.exit(1)

    json_file = sys.argv[1]
    output_file = Path(json_file).stem + '_artlaw.html'

    data = load_json_data(json_file)
    html = generate_html(data)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"HTML generado correctamente: {output_file}")
    print(f"Items procesados: {len(data.get('items', []))}")
    print("Fallback de Google activo para URLs")


if __name__ == "__main__":
    main()


