#!/usr/bin/env python3
"""
Merge all Art-Law JSON reports in the data/art-law directory into a single, well-structured, clustered report.

Inputs (defaults):
  - All *.json files in data/art-law/ directory (auto-discovered)

Output (default):
  - data/art-law/arte_derecho_report_2025_08_20_all_merged.json

Usage:
  python scripts/converters/merge_artlaw_reports.py
  python scripts/converters/merge_artlaw_reports.py <input1> <input2> ... [output]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict, Counter
from typing import Any, Dict, List, Tuple


def load_json(path: Path) -> Dict[str, Any]:
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)


def parse_date(date_str: str | None) -> datetime | None:
    if not date_str:
        return None
    # Try common formats found in the sources
    for fmt in ('%d-%m-%Y', '%Y-%m-%d', '%d/%m/%Y', '%m-%d-%Y'):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None


SPANISH_TO_NORMALIZED_CATEGORY = {
    'Patrimonio y restitución': 'restitution',
    'Propiedad intelectual': 'ip_copyright',
    'Cumplimiento regulatorio': 'compliance_regulatory',
    'Fraude y autenticidad': 'fraud_authenticity',
    'Política cultural': 'policy_politics',
    'Gobernanza museística': 'museum_governance',
}


def normalize_category(item: Dict[str, Any]) -> str:
    # Prefer explicit primary_category when present
    classification = item.get('classification') or {}
    primary = classification.get('primary_category')
    if isinstance(primary, str) and primary.strip():
        p = primary.strip()
        # Already normalized in EN?
        if p in {
            'restitution', 'ip_copyright', 'aml_sanctions', 'fraud_authenticity',
            'free_expression', 'policy_politics', 'labor_employment', 'data_privacy',
            'market_auction', 'ethics_governance', 'platform_governance'
        }:
            # Map aml_sanctions to compliance_regulatory for consolidation
            return 'compliance_regulatory' if p == 'aml_sanctions' else p
        # Spanish → normalized
        return SPANISH_TO_NORMALIZED_CATEGORY.get(p, p)
    # Fallbacks using compliance flags
    flags = item.get('compliance_flags')
    if isinstance(flags, dict):
        if flags.get('aml') or flags.get('sanctions'):
            return 'compliance_regulatory'
        if flags.get('data_privacy'):
            return 'data_privacy'
    if isinstance(flags, list):
        lower = {str(x).strip().lower() for x in flags}
        if any(k in lower for k in ('aml', 'kyc', 'sanciones', 'financial sanctions')):
            return 'compliance_regulatory'
        if any(k in lower for k in ('data privacy', 'gdpr', 'protección de datos')):
            return 'data_privacy'
    return 'uncategorized'


def collect_compliance_labels(item: Dict[str, Any]) -> List[str]:
    labels: set[str] = set()
    flags = item.get('compliance_flags')
    if isinstance(flags, dict):
        for k, v in flags.items():
            if v:
                labels.add(k)
    elif isinstance(flags, list):
        for v in flags:
            labels.add(str(v))
    return sorted(labels)


def merge_items(sources: List[Tuple[str, Dict[str, Any]]]) -> Tuple[List[Dict[str, Any]], Dict[str, Dict[str, Any]]]:
    """
    Merge items across sources by item_id, preserving per-source payloads.
    Returns (items_sorted, items_by_id)
    """
    items_by_id: Dict[str, Dict[str, Any]] = {}

    for source_name, data in sources:
        for item in data.get('items', []):
            item_id = item.get('item_id')
            if not item_id:
                # Create synthetic id if missing (should not happen in given inputs)
                item_id = f"SYN-{source_name}-{len(items_by_id) + 1}"
                item['item_id'] = item_id

            if item_id not in items_by_id:
                merged = dict(item)
                merged['origin_sources'] = [source_name]
                merged['origin_payloads'] = {source_name: item}
                merged['normalized_category'] = normalize_category(item)
                merged['compliance_labels'] = collect_compliance_labels(item)
                items_by_id[item_id] = merged
            else:
                existing = items_by_id[item_id]
                if source_name not in existing['origin_sources']:
                    existing['origin_sources'].append(source_name)
                existing['origin_payloads'][source_name] = item
                # Enrich merged fields conservatively (don't overwrite existing when present)
                for k, v in item.items():
                    if k in ('origin_sources', 'origin_payloads'):
                        continue
                    if existing.get(k) in (None, '', [], {}):
                        existing[k] = v
                # Union compliance labels
                existing_labels = set(existing.get('compliance_labels', []))
                existing_labels.update(collect_compliance_labels(item))
                existing['compliance_labels'] = sorted(existing_labels)
                # Normalize category if previously uncategorized
                if existing.get('normalized_category') in (None, '', 'uncategorized'):
                    existing['normalized_category'] = normalize_category(item)

    # Order: rank asc (if present), then publication_date desc, then headline asc
    def sort_key(it: Dict[str, Any]):
        rank = it.get('rank')
        try:
            rank_val = int(rank) if rank is not None else 10_000
        except Exception:
            rank_val = 10_000
        pub = parse_date(it.get('publication_date')) or datetime.min
        head = it.get('headline') or ''
        # Negative date for descending within tuple by invert later using sort params
        return (rank_val, -int(pub.timestamp()) if pub != datetime.min else 0, head)

    items_sorted = sorted(items_by_id.values(), key=sort_key)
    return items_sorted, items_by_id


def build_clusters(items_sorted: List[Dict[str, Any]]) -> Dict[str, Any]:
    clusters: Dict[str, Any] = {
        'by_normalized_category': defaultdict(list),
        'by_jurisdiction': defaultdict(list),
        'by_legal_stage': defaultdict(list),
        'by_compliance_label': defaultdict(list),
    }
    for it in items_sorted:
        item_id = it.get('item_id')
        clusters['by_normalized_category'][it.get('normalized_category', 'uncategorized')].append(item_id)
        jur = it.get('jurisdiction') or 'Unspecified'
        clusters['by_jurisdiction'][jur].append(item_id)
        stage = it.get('legal_stage') or 'Unspecified'
        clusters['by_legal_stage'][stage].append(item_id)
        for lbl in it.get('compliance_labels', []):
            clusters['by_compliance_label'][lbl].append(item_id)
    # Convert defaultdicts to dicts
    for k in list(clusters.keys()):
        if isinstance(clusters[k], defaultdict):
            clusters[k] = dict(clusters[k])
    return clusters


def merge_metadata(source_payloads: List[Tuple[str, Dict[str, Any]]]) -> Dict[str, Any]:
    meta: Dict[str, Any] = {
        'title': None,
        'subtitle': None,
        'period': None,
        'parameters': None,
        'processing': None,
        'validation': None,
        'language': None,
        'generation_date': None,
        'lookback_days': None,
        'selection_days': None,
        'source_files': [],
    }

    for name, data in source_payloads:
        meta['source_files'].append(name)
        m = data.get('metadata', {})
        # Prefer cg/standard keys when present
        meta['title'] = meta['title'] or m.get('title') or m.get('report_title')
        meta['subtitle'] = meta['subtitle'] or m.get('subtitle')
        meta['period'] = meta['period'] or m.get('period') or m.get('coverage_period')
        meta['parameters'] = meta['parameters'] or m.get('parameters')
        meta['processing'] = meta['processing'] or m.get('processing')
        meta['validation'] = meta['validation'] or m.get('validation')
        meta['language'] = meta['language'] or m.get('language')
        meta['generation_date'] = meta['generation_date'] or m.get('generation_date')
        meta['lookback_days'] = meta['lookback_days'] or m.get('lookback_days')
        meta['selection_days'] = meta['selection_days'] or m.get('selection_days')
    return meta


def merge_executive_summary(source_payloads: List[Tuple[str, Dict[str, Any]]]) -> Dict[str, Any]:
    bullets = []
    key_findings = []
    overview = None
    key_themes = []
    geographical_focus = []
    trend_analysis = None

    def extend_unique(target: List[str], values: List[str] | None):
        if not values:
            return
        seen = set(target)
        for v in values:
            if v not in seen:
                target.append(v)
                seen.add(v)

    for _, data in source_payloads:
        es = data.get('executive_summary') or {}
        # Combine annual bullets and key findings
        extend_unique(bullets, es.get('annual_bullets'))
        extend_unique(key_findings, es.get('key_findings'))
        overview = overview or es.get('annual_overview') or es.get('overview')
        extend_unique(key_themes, es.get('key_themes'))
        extend_unique(geographical_focus, es.get('geographical_focus'))
        trend_analysis = trend_analysis or es.get('trend_analysis')

    return {
        'bullets': bullets,
        'key_findings': key_findings,
        'overview': overview,
        'key_themes': key_themes,
        'geographical_focus': geographical_focus,
        'trend_analysis': trend_analysis,
    }


def build_analytics(items_sorted: List[Dict[str, Any]], items_by_id: Dict[str, Dict[str, Any]], source_payloads: List[Tuple[str, Dict[str, Any]]]) -> Dict[str, Any]:
    categories = Counter(it.get('normalized_category', 'uncategorized') for it in items_sorted)
    jurisdictions = Counter((it.get('jurisdiction') or 'Unspecified') for it in items_sorted)
    stages = Counter((it.get('legal_stage') or 'Unspecified') for it in items_sorted)

    source_items = {name: len(data.get('items', [])) for name, data in source_payloads}

    source_analytics = {name: data.get('analytics') for name, data in source_payloads if data.get('analytics')}

    return {
        'totals': {
            'items_combined': len(items_sorted),
            'unique_item_ids': len(items_by_id),
            'source_items': source_items,
        },
        'distributions': {
            'normalized_category': dict(categories),
            'jurisdiction': dict(jurisdictions),
            'legal_stage': dict(stages),
        },
        'source_analytics': source_analytics,
    }


def build_sources_block(source_payloads: List[Tuple[str, Dict[str, Any]]]) -> Dict[str, Any]:
    sources: Dict[str, Any] = {}
    for name, data in source_payloads:
        sources[name] = {
            'metadata': data.get('metadata'),
            'analytics': data.get('analytics'),
            'discarded_items': data.get('discarded_items'),
            'quality_assurance': data.get('quality_assurance'),
        }
    return sources


def main(argv: List[str]) -> int:
    root = Path('.')
    art_law_dir = root / 'data' / 'art-law'
    default_output = art_law_dir / 'arte_derecho_report_2025_08_20_all_merged.json'

    inputs: List[Path]
    output: Path
    
    if len(argv) in (0, 1):
        # Auto-discover all JSON files in art-law directory
        inputs = list(art_law_dir.glob('*.json'))
        # Exclude the output file if it already exists
        inputs = [p for p in inputs if not p.name.startswith('arte_derecho_report_2025_08_20_all_merged')]
        if not inputs:
            print('Error: No JSON files found in data/art-law directory.')
            return 2
        output = default_output
    else:
        args = [Path(a) for a in argv[1:]]
        if len(args) < 1:
            print('Error: provide at least one input file and optionally an output path.')
            return 2
        inputs = args[:-1] if len(args) > 1 and not args[-1].suffix == '.json' else args
        output = args[-1] if len(args) > 1 and not args[-1].suffix == '.json' else default_output

    # Load sources
    source_payloads: List[Tuple[str, Dict[str, Any]]] = []
    for p in inputs:
        if not p.exists():
            print(f'Error: input not found: {p}')
            return 2
        source_payloads.append((str(p).replace('\\', '/'), load_json(p)))

    # Merge items
    items_sorted, items_by_id = merge_items(source_payloads)
    # Build clusters
    clusters = build_clusters(items_sorted)
    # Merge metadata and executive summary
    metadata = merge_metadata(source_payloads)
    executive_summary = merge_executive_summary(source_payloads)
    # Build analytics
    analytics = build_analytics(items_sorted, items_by_id, source_payloads)
    # Sources block
    sources_block = build_sources_block(source_payloads)

    merged: Dict[str, Any] = {
        'metadata': metadata,
        'executive_summary': executive_summary,
        'items': items_sorted,
        'clusters': clusters,
        'analytics': analytics,
        'sources': sources_block,
        'generated_at': datetime.utcnow().isoformat() + 'Z',
        'generator': 'merge_artlaw_reports.py',
        'version': '1.0',
    }

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('w', encoding='utf-8') as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
    print(f'Wrote merged report: {output}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))


