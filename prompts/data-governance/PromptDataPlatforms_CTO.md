## OBJETIVO PRINCIPAL — Edición CTO / Big Data
Generar un **archivo JSON estructurado** con **hasta 50 novedades y decisiones clave en implementaciones empresariales de Data Governance** publicadas en los **últimos 30 días**, orientado a **CPOs, DPOs, CTOs, C‑levels, consultores de tecnología y profesionales de Big Data**. Priorizar **casos de implementación reales, problemas operativos, incidentes de datos, proyectos de transformación digital** y **decisiones estratégicas de gobernanza** con impacto tangible. Cada ítem debe incluir un párrafo analítico (100–140 palabras), **URLs verificadas** y un **mapeo DMBoK2** mínimo: áreas de conocimiento, nivel de gobernanza, dominios y controles; además, **stack tecnológico**, **patrón arquitectónico**, **workloads**, **impacto en rendimiento/costo** y **recomendaciones accionables**. Salida en **español**, lista para marca Stratesys.

---

## PARÁMETROS RÁPIDOS (editar fácilmente)

- LOOKBACK_DAYS: 30
- SELECTION_DAYS: 30

Usa estos parámetros en todo el proceso; ajusta LOOKBACK_DAYS para ampliar exploración.

---

## MARCO DE EJECUCIÓN

### 1) ALCANCE TEMPORAL
- Búsqueda ampliada: LOOKBACK_DAYS días naturales hacia atrás
- Selección final: ítems publicados en los últimos SELECTION_DAYS
- Formato de fecha: DD-MM-YYYY (usar UTC)

### 1.b) ORDEN DE TRABAJO (obligatorio)
- Recopilar candidatos dentro de LOOKBACK_DAYS
- Filtrar por dominio (ver sección de Filtros)
- Atribuir mapeo **DMBoK2** y **atributos técnicos** por ítem
- Evaluar y puntuar cada candidato
- Seleccionar top 50 equilibrando categorías y cobertura DMBoK2
- Generar el resumen AL FINAL (viñetas) a partir de los ítems seleccionados

---

## 2) FILTRO DE CONTENIDO: IMPLEMENTACIONES EMPRESARIALES + PROBLEMAS REALES
**Principio rector**: priorizar **noticias de implementaciones reales, incidentes, proyectos de transformación y decisiones estratégicas** de empresas que implementan o tienen problemas con Data Governance, con impacto tangible para toma de decisiones de CTO/CDO/C‑suite.

**Ámbitos núcleo (con enfoque en casos reales)**
- **Implementaciones y proyectos reales**: casos de éxito, fracasos, migraciones, transformaciones digitales con métricas y lecciones aprendidas.
- **Incidentes y problemas operativos**: brechas de datos, fallos de calidad, problemas de compliance, incidentes de SLO/SLA con impacto real.
- **Decisiones estratégicas**: cambios de arquitectura, adopción de nuevas tecnologías, reorganizaciones de equipos, inversiones en gobernanza.
- **Casos de uso específicos**: implementaciones de data mesh, lakehouse, MDM, data contracts, observabilidad, con resultados medibles.
- **Problemas de compliance y regulatorios**: multas, sanciones, auditorías, cambios regulatorios que afectan implementaciones.
- **Fusiones, adquisiciones y reorganizaciones**: impacto en arquitecturas de datos, consolidación de plataformas, migraciones post-M&A.

**Vendors/tecnologías (limitado a herramientas de gobernanza pura)**
- **Gobernanza pura**: Collibra, Informatica, Talend, OpenMetadata, Purview, DataPlex, OpenHub, Unity Catalog, Alation, Atlan, Data.World, Amundsen, Marquez.
- **Arquitecturas mencionadas en contexto**: Microsoft Fabric, Snowflake, Databricks, BigQuery, GCP, AWS, Azure (solo cuando expliquen arquitecturas de casos reales).

**Incluir**
- Casos de implementación con métricas reales (ROI, tiempo de implementación, problemas resueltos).
- Incidentes con impacto cuantificable (costos, tiempo de resolución, alcance).
- Decisiones estratégicas con justificación técnica y de negocio.
- Proyectos de transformación con timeline y resultados.

**Excluir**
- Actualizaciones de productos de vendors de plataforma (Fabric, Snowflake, Databricks, etc.) a menos que sean herramientas de gobernanza pura.
- Marketing sin casos reales o métricas verificables.
- Opiniones sin documentación de implementaciones concretas.

### 2.b) COBERTURA DMBoK2 (añadido)
Elegir 1–3 áreas por ítem (mínimo 1):
- Gobernanza de Datos; Gestión de Calidad de Datos; Metadatos/Glosario; Modelado/Diseño; Arquitectura de Datos; Almacenamiento/Operaciones; Integración e Interoperabilidad; Gestión de Referencia y Maestro; Seguridad de Datos; Analítica/BI.

Mapear además:
- Nivel de gobernanza: principle|policy|standard|procedure|guideline
- Dominios de datos: customer|employee|financial|product|operations|vendor|health|research|other
- Clasificación: public|internal|confidential|restricted
- Ciclo de vida: create|store|use|share|archive|delete
- Controles: preventive|detective|corrective; categoría: administrative|technical|physical
- Roles: data_owner|data_steward|data_custodian|DPO|CISO|CDO

---

## 3) PRIORIZACIÓN DE FUENTES (con ejemplos)

**Nivel 1 — Casos reales documentados**
- Reportes de incidentes oficiales, comunicados de empresas, resultados de auditorías, casos de estudio con métricas.
- Documentación de proyectos de implementación, whitepapers con casos reales, presentaciones de conferencias con resultados.

**Nivel 2 — Prensa especializada con casos**
- Prensa técnica y de negocio que reporte implementaciones reales, incidentes, decisiones estratégicas con detalles técnicos.

**Nivel 3 — Blogs de empresas y consultores**
- Blogs de empresas que documenten sus propias implementaciones, consultores que compartan casos reales.

**Nivel 4 — Redes sociales y foros (cuando documenten casos verificables)**
- LinkedIn posts de profesionales, foros técnicos con casos reales documentados.

Reglas: preferir casos con métricas, usar la fecha más temprana autorizada, validar URLs, reconciliar duplicados.

---

## 4) SISTEMA DE PUNTUACIÓN (orientado a casos reales)

Puntuación total sobre 100. Seleccionar top 50 con diversidad temática y cobertura DMBoK2.

1) Impacto de caso real (0–35)
- 30–35: incidente mayor o implementación estratégica con impacto significativo en múltiples empresas
- 20–29: caso de implementación con métricas claras y lecciones aprendidas
- 10–19: proyecto o decisión con implicaciones operativas medibles

2) Documentación del caso (0–20)
- 16–20: documentación oficial con métricas detalladas y timeline
- 10–15: reporte con métricas parciales y contexto técnico
- 5–9: mención con algunos detalles verificables

3) Relevancia para implementación (0–15)
- 12–15: patrón replicable, lecciones claras, roadmap de implementación
- 8–11: insights útiles para planificación
- 4–7: información general de contexto

4) Claridad cuantitativa (0–10)
- Métricas de impacto, costos, tiempo, escala, resultados

5) Cobertura DMBoK2 (0–10)
- 8–10: ≥2 áreas + nivel de gobernanza + roles + controles
- 5–7: ≥2 áreas + dimensión de calidad
- 2–4: 1 área

6) Riesgo y criticidad (0–10)
- 8–10: datos sensibles/alto volumen/elevada concurrencia/blast radius amplio
- 5–7: sensibilidad media, alcance regional/por dominio
- 2–4: impacto limitado

Penalizaciones: duplicado, fuera de ventana, marketing sin casos, paywall duro sin alternativa.

---

## 5) REQUISITOS DE CONTENIDO

**Estándares de redacción**
- 100–140 palabras; español; analítico y accionable (qué aprendería un CTO/Head of Data)
- Estructura: Qué empresa/proyecto → Qué ocurrió/implementó → Stack/Arquitectura/Workloads → Métricas (impacto/resultados) → Lecciones aprendidas → Próximos pasos/recomendaciones

**Elementos obligatorios por ítem**
- **case_type**: implementation|incident|strategic_decision|transformation|compliance_issue
- **company_industry**: sector de la empresa (fintech, retail, healthcare, etc.)
- **company_size**: startup|midmarket|enterprise|fortune500
- **vendors/stack**: tecnologías principales (p. ej., Collibra, Snowflake, dbt, Airflow)
- **cloud_environment**: AWS|Azure|GCP|Hybrid|On‑prem|Multi‑cloud
- **workloads**: batch|streaming|ml|serving
- **architecture_patterns**: lakehouse|data_mesh|dwh|data_lake|event_driven
- **scale_summary**: volumen/velocidad/concurrencia/almacenamiento
- **business_impact**: métricas de negocio, ROI, tiempo de resolución
- **technical_impact**: métricas de performance, costo, confiabilidad
- **lessons_learned**: insights clave para otras implementaciones
- **source**: nombre, tier, URL validada
- **dmbok_mapping** y **data_quality** (dimensiones/KPIs)

**Recomendados**
- Timeline de implementación, presupuesto, equipo involucrado, dependencias, riesgos identificados.

**Validación**
- Trazabilidad a fuentes, fechas, métricas consistentes, presencia de mapeo DMBoK2 y DQ, diversidad temática.

---

## 6) ESPECIFICACIÓN DE ESTRUCTURA JSON (Casos Reales)

**Reglas de integridad**
- Fechas en DD-MM-YYYY; cantidades en unidades originales; vendors/tecnologías normalizados.

**Plantilla**

```json
{
  "metadata": {
    "title": "Data Governance Implementation Cases — [DD-MM-YYYY] a [DD-MM-YYYY]",
    "subtitle": "#DATA GOVERNANCE INSIGHTS",
    "period": {"start_date":"[DD-MM-YYYY]","end_date":"[DD-MM-YYYY]","days_covered":7},
    "parameters": {"lookback_days": "LOOKBACK_DAYS", "selection_days": "SELECTION_DAYS"},
    "processing": {"generated_at": "[ISO 8601]","version": "1.0","brand": "Kepler Karst","ai_model": "[model]","processing_time_seconds": "[duration]"},
    "validation": {"urls_verified": true, "dates_validated": true, "content_reviewed": true, "schema_compliant": true},
    "governance_principles": ["accountability","observability","reliability","protection","compliance","cost_efficiency"],
    "dmbok_alignment": {"coverage_areas": ["data_governance","data_quality","data_architecture"], "notes": "Cobertura DMBoK2 técnica"}
  },
  "executive_summary": {
    "weekly_bullets": [
      "[5–8 viñetas] Implementaciones exitosas, incidentes importantes, decisiones estratégicas y lecciones aprendidas",
      "Patrones de implementación (lakehouse/mesh), problemas comunes y soluciones innovadoras",
      "Impacto en métricas de negocio (ROI, tiempo de resolución, compliance) y operaciones",
      "Tendencias en arquitecturas, herramientas de gobernanza y prácticas emergentes",
      "Casos de transformación digital y reorganizaciones con impacto en datos"
    ],
    "weekly_overview": "Resumen generado AL FINAL (unir con •).",
    "key_themes": ["Implementaciones reales","Incidentes y problemas","Decisiones estratégicas","Transformación digital","Compliance y auditorías","Arquitecturas emergentes"],
    "geographical_focus": ["Global"],
    "trend_analysis": "Patrones e implicaciones para implementaciones futuras"
  },
  "items": [
    {
      "item_id": "DG2025W33-001",
      "rank": 1,
      "headline": "Titular claro del caso real",
      "case_type": "implementation|incident|strategic_decision|transformation|compliance_issue",
      "publication_date": "DD-MM-YYYY",
      "company": {"name": "Company Name", "industry": "fintech|retail|healthcare|etc", "size": "startup|midmarket|enterprise|fortune500"},
      "source": {"name": "Source Name","tier": "1|2|3|4","original_url": "https://validated.source.url","paywall": false,"author": "If available"},
      "stack": ["Collibra","Snowflake","dbt","Airflow"],
      "vendors": ["Collibra","Snowflake"],
      "cloud_environment": "AWS|Azure|GCP|Hybrid|On-prem|Multi-cloud",
      "workloads": ["batch","streaming"],
      "architecture_patterns": ["lakehouse","data_mesh"],
      "environment": "production|staging|pilot|poc",
      "scale_summary": {"storage_tb": 0, "daily_rows": 0, "throughput_msgs_sec": 0, "concurrency": 0},
      "business_impact": {"roi_pct": 0, "time_to_resolution_days": 0, "cost_savings_usd": 0, "notes": ""},
      "technical_impact": {"performance_improvement_pct": 0, "cost_reduction_pct": 0, "reliability_improvement_pct": 0, "notes": ""},
      "lessons_learned": ["lección clave 1", "lección clave 2"],
      "timeline": {"start_date": "DD-MM-YYYY", "end_date": "DD-MM-YYYY", "duration_months": 0},
      "content": {
        "summary": "100–140 palabras en español que cubran qué empresa/proyecto, qué ocurrió/implementó, stack/arquitectura/workloads, métricas de impacto/resultados, lecciones aprendidas y próximos pasos.",
        "dmbok_mapping": {
          "knowledge_areas": ["data_governance","data_quality"],
          "governance_level": "policy",
          "operating_model": "federated",
          "roles": ["data_owner","data_steward","CISO"],
          "controls": {"type":"preventive","category":"technical","frameworks":["ISO27001"]},
          "data_domains": ["customer","operations"],
          "data_classification": "confidential",
          "data_lifecycle": ["use","share","archive"]
        },
        "data_quality": {"dimensions": ["accuracy","timeliness"], "kpi_suggestions": ["% tablas con tests verdes","SLA pipelines"], "severity": "medium"},
        "lineage": {"sources": ["CRM"], "targets": ["Data Warehouse"], "integration_type": "ETL"},
        "business_glossary_terms": ["dato_clientes","latencia_pipeline"],
        "risk_rating": {"level": "high", "rationale": "Datos sensibles y alcance multinube"}
      },
      "recommended_actions": ["evaluar patrón para implementación similar","documentar lecciones aprendidas","planificar roadmap de adopción"],
      "classification": {
        "primary_category": "implementation_success|incident_response|strategic_decision|digital_transformation|compliance_audit|architecture_migration|team_reorganization|vendor_selection",
        "secondary_tags": ["lakehouse","mesh","collibra","incident","transformation"],
        "vendors": ["Collibra","Informatica","Talend","OpenMetadata","Snowflake","Databricks"]
      }
    }
  ],
  "analytics": {
    "processing_statistics": {"sources_scanned": 0, "articles_reviewed": 0, "items_scoring_above_threshold": 0, "items_published": 0, "duplicates_identified": 0, "urls_validated": 0, "validation_failures": 0},
    "content_metrics": {"average_score": 0, "score_distribution": {"90-100":0,"80-89":0,"70-79":0,"60-69":0}, "word_count_statistics": {"average_words": 0, "min_words": 0, "max_words": 0}},
    "coverage_analysis": {
      "category_distribution": {"implementation_success": 0, "incident_response": 0, "strategic_decision": 0, "digital_transformation": 0, "compliance_audit": 0, "architecture_migration": 0, "team_reorganization": 0, "vendor_selection": 0},
      "industry_distribution": {"fintech":0,"retail":0,"healthcare":0,"manufacturing":0,"consulting":0},
      "company_size_distribution": {"startup":0,"midmarket":0,"enterprise":0,"fortune500":0}
    }
  },
  "discarded_items": [
    {"rank": 21, "headline": "Titular descartado", "source": "Source Name", "url": "https://source.url", "publication_date": "DD-MM-YYYY", "score": 58, "discard_reason": "Por debajo de umbral o sin casos reales/ métricas"}
  ],
  "forward_looking": {
    "next_week_calendar": [{"date":"DD-MM-YYYY","event":"[Implementación/Incidente/Decisión esperada]","significance":"high|medium|low"}],
    "monitoring_priorities": ["Implementación crítica en curso","Incidente con impacto amplio"],
    "emerging_trends": ["Patrones de implementación exitosa","Problemas comunes y soluciones"],
    "data_gaps": ["Métricas de ROI de gobernanza","Benchmarks de implementación"],
    "governance_actions": ["Documentar patrones exitosos","Identificar anti-patrones comunes"]
  },
  "quality_assurance": {
    "editorial_notes": ["Validar métricas vs documentación oficial"],
    "source_reliability": {"tier_1_percentage": 50, "tier_2_percentage": 30, "tier_3_percentage": 15, "tier_4_percentage": 5},
    "fact_checking": {"claims_verified": 0, "cross_references": 0, "potential_discrepancies": 0},
    "dmbok_checks": {"mapping_present": true, "dq_dimensions_present": true}
  }
}
```

---

## 7) MANEJO DE ERRORES Y VALIDACIÓN
- Verificar accesibilidad de URLs y que las fechas estén dentro de la ventana
- Detección de duplicados; equilibrio temático (<40% en una sola categoría)
- QA: conteo de palabras, presencia de métricas (impacto/resultados), mapeo DMBoK2 y DQ en cada ítem
- Validación de salida: sintaxis JSON, cumplimiento de esquema, cobertura de áreas DMBoK2 técnico‑operativas


