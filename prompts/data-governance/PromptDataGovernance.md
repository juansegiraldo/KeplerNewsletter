## OBJETIVO PRINCIPAL
Generar un **archivo JSON estructurado** con **hasta 50 noticias de Gobernanza de Datos Empresarial más relevantes de los últimos 30 días**, **alineado a DMBoK2** (DAMA-DMBOK v2). El alcance incluye **señales regulatorias** (consultas públicas, anteproyectos, políticas corporativas, decisiones de cumplimiento) con alta probabilidad de traducirse en efectos **normativos, de cumplimiento o contenciosos**. Cada ítem debe incluir un párrafo analítico conciso (100–140 palabras) con **URLs de fuente validadas** y un **mapeo DMBoK2** mínimo: áreas de conocimiento afectadas, dimensiones de calidad de datos, nivel de gobernanza (política/estándar/procedimiento/guía), dominios de datos y controles asociados. La salida debe estar en **español** y lista para conversión a marca Kepler Karst.

---

## PARÁMETROS RÁPIDOS (editar fácilmente)

- LOOKBACK_DAYS: 30    ← ventana de búsqueda inicial hacia atrás
- SELECTION_DAYS: 30    ← ítems publicados dentro de los últimos N días

Usa estos parámetros en todo el proceso. Cambia SELECTION_DAYS a 30 si quieres cubrir 30 días; ajusta LOOKBACK_DAYS para ampliar la exploración.

---

## MARCO DE EJECUCIÓN

### 1) ALCANCE TEMPORAL
- **Búsqueda ampliada**: LOOKBACK_DAYS días naturales hacia atrás desde la fecha actual
- **Selección final**: ítems publicados en los últimos SELECTION_DAYS
- **Formato de fecha**: DD-MM-YYYY en todas las salidas  
- **Zona horaria**: usar UTC para consistencia

### 1.b) ORDEN DE TRABAJO (obligatorio)
- Recopilar candidatos dentro de LOOKBACK_DAYS.
- Filtrar por dominio (ver sección de Filtros).
- Atribuir mapeo **DMBoK2** por ítem (ver sección 2.b).
- Evaluar y puntuar cada candidato.
- Seleccionar top 50 dentro de SELECTION_DAYS, equilibrando categorías y cobertura DMBoK2.
- Generar el Resumen semanal AL FINAL, en formato de viñetas, a partir de los ítems seleccionados.

### 2) FILTRO DE CONTENIDO: DOMINIO GOBERNANZA DE DATOS EMPRESARIAL
**Principio rector**: priorizar piezas donde la intersección principal sea **Derecho + Datos + Empresa**. Se admite expansión a Tecnología/Compliance/Política si existe un ángulo jurídico/regulatorio claro. Incorporar criterios **DMBoK2**: impacto en políticas, roles y responsabilidades, procesos de gestión de datos, controles, métricas y calidad.

**Ámbitos núcleo (con vínculo jurídico explícito)**
- Privacidad y protección de datos: GDPR, CCPA, LGPD, PIPEDA, reglamentos sectoriales, decisiones de autoridades de protección de datos, multas y sanciones.
- Seguridad de datos y ciberseguridad: incidentes de seguridad, violaciones de datos, regulaciones de seguridad (NIS2, CISA, etc.), cumplimiento SOC2/ISO27001, litigios por brechas.
- Gobernanza de datos corporativa: políticas de datos, frameworks de gobernanza, roles y responsabilidades (DPO, CDO), auditorías de cumplimiento, mejores prácticas.
- Inteligencia artificial y datos: regulaciones de IA (AI Act, etc.), sesgos algorítmicos, transparencia, responsabilidad por decisiones automatizadas, ética de datos.
- Comercio y transferencias internacionales: cláusulas contractuales estándar, decisiones de adecuación, mecanismos de transferencia, restricciones geográficas.
- Cumplimiento sectorial: regulaciones financieras (BCBS, Solvency II), salud (HIPAA), telecomunicaciones, retail, manufactura.

### 2.b) COBERTURA DMBoK2 (añadido)
Mapear cada ítem a las áreas de conocimiento **DMBoK2** relevantes. Elegir 1–3 por ítem:
- Gobernanza de Datos (política, RACI, principios, métricas)
- Gestión de Calidad de Datos (exactitud, completitud, consistencia, puntualidad, unicidad, validez)
- Gestión de Metadatos y Glosario de Negocio
- Modelado y Diseño de Datos (conceptual/lógico/físico)
- Arquitectura de Datos (principios, dominios, integración)
- Almacenamiento y Operaciones de Datos (retención, archivado, borrado seguro)
- Integración e Interoperabilidad de Datos (ETL/ELT, APIs, streaming)
- Gestión de Referencia y Maestro (MDM/RDM)
- Seguridad de Datos (controles administrativos/técnicos/físicos)
- Analítica, BI y Almacenamiento (lineaje, calidad para reporting)

Adicionalmente, mapear:
- Nivel de gobernanza: principle|policy|standard|procedure|guideline
- Dominio(s) de datos: customer|employee|financial|product|operations|vendor|health|research|other
- Clasificación de datos: public|internal|confidential|restricted
- Ciclo de vida de datos: create|store|use|share|archive|delete
- Tipo de control: preventive|detective|corrective; categoría: administrative|technical|physical
- Roles implicados: data_owner|data_steward|data_custodian|DPO|CISO|CDO

**Expansión (siempre con impacto jurídico/regulatorio)**
- Política tecnológica y regulación: consultas públicas sobre regulación digital, estrategias nacionales de datos, marcos regulatorios emergentes.
- Libertad de expresión y moderación de contenidos: regulaciones de plataformas, responsabilidad de intermediarios, transparencia algorítmica.
- Trabajo y empleo: monitoreo de empleados, datos de recursos humanos, sindicatos y privacidad laboral.
- Espacio público y smart cities: datos de ciudades inteligentes, vigilancia pública, transparencia gubernamental.
- Fiscalidad y auditoría: impuestos digitales, auditorías de datos, cumplimiento fiscal basado en datos.
- Datos y competencia: fusiones de datos, poder de mercado, regulación antimonopolio aplicada a datos.
- Movilidad internacional: flujos de datos transfronterizos, jurisdicciones conflictivas, extraterritorialidad.

**INCLUIR (aclaraciones)**
- Incidentes y violaciones: incluir cuando exista ángulo legal/regulatorio (p. ej., investigaciones regulatorias, litigios, multas, cambios de políticas).
- Innovación tecnológica: incluir cuando afecte marcos regulatorios existentes o genere nuevos requisitos legales.

**EXCLUIR**
- Opinión/comentario sin documento/acto oficial o hechos verificables.
- Temas de TI no relacionados con gobernanza de datos.
- Anécdotas empresariales sin trayecto plausible de big data.

### 3) PRIORIZACIÓN DE FUENTES (con ejemplos)
Esta lista es orientativa, no exhaustiva. Cualquier fuente válida con documentos/actos oficiales es elegible.

**Nivel 1 — Primarias/Autoritativas (preferidas)**
- Autoridades de protección de datos: ICO (UK), CNIL (Francia), AEPD (España), FTC (US), OPC (Canadá), ANPD (Brasil).
- Organismos regulatorios: EDPB, Comisión Europea, Parlamento Europeo, reguladores sectoriales (BCBS, FCA, SEC).
- Tribunales y decisiones judiciales: CJEU, tribunales nacionales, decisiones de autoridades administrativas.

**Nivel 2 — Sector/Profesional**
- Organizaciones profesionales: IAPP, ISACA, DAMA, IEEE, ACM.
- Consultoras especializadas: Gartner, Forrester, IDC (reportes regulatorios).
- Plataformas: blogs/políticas oficiales (Google, Microsoft, AWS, Meta).

**Nivel 3 — Prensa especializada legal/tecnológica**
- Law.com, TechCrunch (legal), The Verge (policy), Ars Technica (legal).

**Nivel 4 — Prensa general (cuando aporta docs/actos oficiales o grandes desarrollos)**
- FT/Reuters/AP/WSJ, The Guardian, prensa nacional con documentos primarios.

**Reglas**
- Preferir documentos/decisiones oficiales; usar la fecha más temprana y autorizada; validar URLs; fusionar duplicados útiles.
- Asegurar diversidad temática/geográfica y **cobertura balanceada de áreas DMBoK2**; evitar sobreconcentración en un solo tema, jurisdicción o área.

### 4) SISTEMA DE PUNTUACIÓN (simplificado y balanceado, con factores DMBoK2)

Puntuación total sobre 100. Seleccionar top 50, asegurando al menos 4 categorías representadas, ≤40% en una sola categoría y cobertura mínima de 4 áreas DMBoK2 a lo largo del set.

1) Impacto jurídico/regulatorio (0–30)
- 26–30: acto oficial ejecutable (sentencia, norma vigente, guía vinculante, multa aplicada)
- 18–25: señal regulatoria robusta (consulta formal, anteproyecto, presupuesto aprobado, anuncio con calendario)
- 10–17: reporte sólido con implicaciones legales claras

2) Autoridad de la fuente (0–15)
- 12–15: tribunal/autoridad regulatoria/boletín oficial
- 8–11: ministerio/regulador sectorial/políticas de plataformas
- 4–7: sector profesional (IAPP, ISACA, DAMA)
- 1–3: prensa especializada con reportaje original

3) Proximidad a enforcement (0–15)
- 12–15: sentencia/multa/implementación/sanción ejecutada
- 8–11: aprobación/entrada en vigor/ratificación
- 4–7: presentación/consulta/orden administrativa
- 1–3: anuncio de intención

4) Claridad cuantitativa y trazabilidad (0–10)
- Métricas (importes, nº de registros afectados, plazos), enlaces a docs oficiales, fechas/casos referenciados

5) Cobertura DMBoK2 (0–15)
- 12–15: afecta ≥2 áreas DMBoK2 + define nivel de gobernanza + roles RACI + controles
- 8–11: mapea ≥2 áreas DMBoK2 + una dimensión de calidad de datos
- 4–7: mapea 1 área DMBoK2
- 1–3: mapeo superficial

6) Riesgo y criticidad de datos (0–15)
- 12–15: datos altamente sensibles (confidential/restricted), gran escala, dominios core
- 8–11: sensibilidad media, alcance regional/sectorial
- 4–7: sensibilidad baja, alcance limitado
- 1–3: impacto marginal

Penalizaciones
- −25: duplicado evidente
- −15: especulación sin respaldo documental
- −10: fuera de SELECTION_DAYS
- −5: paywall duro sin alternativa

### 5) REQUISITOS DE CONTENIDO

**Estándares de redacción**
- 100–140 palabras por ítem; español; analítico y conciso  
- Estructura: *Qué ocurrió → Etapa procesal → Leyes invocadas/entidades/cifras → Próximos pasos*
 - Añadir: *Mapeo DMBoK2 → áreas, nivel de gobernanza, dominios y controles → dimensiones de calidad de datos afectadas*

**Elementos obligatorios por ítem**
- **Jurisdicción y órgano** (tribunal/autoridad regulatoria)  
- **Etapa procesal** (investigación, presentación, audiencia, sentencia, apelación, acuerdo, ejecución, consulta, anteproyecto, anuncio_político, actualización_política_plataforma, presupuesto, guidance_published, proposed_rule, fine_imposed)  
- **Leyes invocadas** (p. ej., "GDPR Art. 32"; "CCPA §1798.100"; "LGPD Art. 37"; "AI Act Art. 6")  
- **Entidades** (empresa, autoridad, organización) cuando esté disponible  
- **Instituciones** (autoridades de protección de datos, reguladores sectoriales, tribunales)  
- **Cifras** (multas/daños/número de registros afectados; plazos de cumplimiento)  
- **Cronograma** (próxima audiencia/consulta/fecha de implementación)  
- **Fuente** (nombre, fecha, URL validada)
 - **Mapeo DMBoK2**: áreas de conocimiento, nivel de gobernanza (principle/policy/standard/procedure/guideline), dominios de datos, roles (data_owner/steward/custodian/DPO/CDO/CISO), tipo de control (preventive/detective/corrective; administrative/technical/physical), ciclo de vida (create/store/use/share/archive/delete)
 - **Calidad de datos**: dimensiones impactadas (exactitud, completitud, consistencia, puntualidad, unicidad, validez) y KPI sugeridos

**Elementos recomendados para política/plataformas**
- **Entidades políticas** (ministerio, regulador, partido, funcionario)
- **Plataformas afectadas** (Google, Microsoft, AWS, Meta, Apple)
- **Señal de política** (consulta|anteproyecto|anuncio|presupuesto|actualización_plataforma)

**Validación**
- Cada hecho debe ser trazable a la(s) fuente(s) citada(s); URLs accesibles; fechas dentro de SELECTION_DAYS; sin extrapolaciones no sustentadas; reconciliar informes conflictivos mediante contraste cruzado. Verificar que el **mapeo DMBoK2** y **dimensiones de calidad** estén presentes y consistentes con el contenido.

### 6) ESPECIFICACIÓN DE ESTRUCTURA JSON (Gobernanza de Datos Empresarial, extendida con DMBoK2)

**Reglas de integridad**
- Todas las fechas en DD-MM-YYYY; todos los números en sus unidades originales; países en ISO-3166-1 alfa-2.

**Campos adicionales**
- `jurisdiction`: p. ej., "UK — ICO", "EU — EDPB", "US — FTC", "CA — OPC"  
- `legal_stage`: investigation|filing|hearing|judgment|appeal|settlement|implementation|consultation|draft_bill|policy_announcement|platform_policy_update|budget|guidance_published|proposed_rule|fine_imposed  
- `laws_invoked`: p. ej., ["GDPR Art. 32","CCPA §1798.100","LGPD Art. 37","AI Act Art. 6"]  
- `entities`: [{name, type, sector, jurisdiction}]  
- `institutions`: [authority/regulator/court]  
- `remedies`: [fine|injunction|damages|corrective_measures|ban|restriction]  
- `case_refs`: enlaces a sentencias/expedientes (EUR-Lex, BAILII, etc.)  
- `compliance_flags`: {privacy: true|false, security: true|false, ai_governance: true|false, cross_border: true|false, sector_specific: true|false, employee_data: true|false, consumer_rights: true|false}  
- Opcional: `media_assets` (URLs a documentos oficiales o imágenes)
- `policy_signal`: consultation|draft_bill|policy_announcement|platform_policy_update|budget|enforcement  
- `political_entities`: [{name, role, affiliation}]  
- `platforms`: ["Google","Microsoft","AWS","Meta","Apple"]

**Campos DMBoK2 (nuevos; opcionales pero recomendados)**
- `dmbok_mapping`: {
  `knowledge_areas`: ["data_governance","data_quality","metadata","data_architecture","data_modeling","data_storage_operations","data_integration","mdm_rdm","data_security","analytics_bi"],
  `governance_level`: "principle|policy|standard|procedure|guideline",
  `operating_model`: "centralized|federated|hybrid",
  `roles`: ["data_owner","data_steward","data_custodian","DPO","CISO","CDO"],
  `controls`: {"type": "preventive|detective|corrective", "category": "administrative|technical|physical", "frameworks": ["ISO27001","NIST_CSf","SOC2","COBIT"]},
  `data_domains`: ["customer","employee","financial","product","operations","vendor","health","research","other"],
  `data_classification": "public|internal|confidential|restricted",
  `data_lifecycle`: ["create","store","use","share","archive","delete"]
}
- `data_quality`: {`dimensions`: ["accuracy","completeness","consistency","timeliness","uniqueness","validity"], `kpi_suggestions`: ["% registros completos","% coincidencias maestras","SLA resolución incidentes de datos"], `severity`: "low|medium|high"}
- `lineage`: {`sources`: ["sistema_origen"], `targets`: ["sistema_destino"], `integration_type`: "ETL|ELT|API|stream|manual"}
- `business_glossary_terms`: ["término_1","término_2"]
- `risk_rating`: {`level`: "low|medium|high", `rationale`: "texto breve"}

### 7) MANEJO DE ERRORES Y VALIDACIÓN
Prechequeos: accesibilidad de URLs; ventana temporal; coincidencia de palabras clave legales; detección de duplicados; equilibrio temático (<40% en una sola categoría).  
QA: conteo de palabras; verificaciones estructurales; cifras inconsistentes; marcar afirmaciones no verificadas; presencia de `dmbok_mapping` y `data_quality` en cada ítem.  
Validación de salida: sintaxis JSON; cumplimiento de esquema; pruebas de URLs; auditoría de puntuación y cobertura DMBoK2 (al menos 4 áreas cubiertas en conjunto; ≤40% en una sola área o categoría).

---

## PLANTILLA DE SALIDA (Gobernanza de Datos Empresarial, extendida DMBoK2)

```json
{
  "metadata": {
    "title": "Gobernanza de Datos Empresarial — [DD-MM-YYYY] a [DD-MM-YYYY]",
    "subtitle": "#DATA GOVERNANCE INSIGHTS",
    "period": {"start_date":"[DD-MM-YYYY]","end_date":"[DD-MM-YYYY]","days_covered":7},
    "parameters": {"lookback_days": "LOOKBACK_DAYS", "selection_days": "SELECTION_DAYS"},
    "processing": {
      "generated_at": "[ISO 8601 timestamp]",
      "version": "1.0",
      "brand": "Kepler Karst",
      "ai_model": "[model_identifier]",
      "processing_time_seconds": "[duration]"
    },
    "validation": {
      "urls_verified": true,
      "dates_validated": true,
      "content_reviewed": true,
      "schema_compliant": true
    },
    "governance_principles": ["accountability","transparency","integrity","protection","compliance","standardization"],
    "dmbok_alignment": {"coverage_areas": ["data_governance","data_quality","metadata"], "notes": "Cobertura resumida de áreas DMBoK2 en el periodo"}
  },
  "executive_summary": {
    "weekly_bullets": [
      "[5–8 viñetas] Regulaciones clave / multas / cumplimiento (GDPR, CCPA, LGPD) / IA y datos / política tecnológica / plataformas / próximos hitos",
      "Sentencias y sanciones ejecutadas (nº, jurisdicciones)",
      "Consultas y anteproyectos abiertos (fechas límite)",
      "Cambios en políticas de plataformas que afecten a empresas"
    ],
    "weekly_overview": "Resumen generado AL FINAL a partir de viñetas (unir con •).",
    "key_themes": ["Privacidad y GDPR/CCPA/LGPD","Seguridad y ciberseguridad","IA y gobernanza de datos","Cumplimiento sectorial","Transferencias internacionales"],
    "geographical_focus": ["UE/Reino Unido","EE. UU.","América Latina","Asia-Pacífico"],
    "trend_analysis": "Breve evaluación de patrones e implicaciones"
  },
  "items": [
    {
      "item_id": "DG2025W33-001",
      "rank": 1,
      "headline": "Titular claro y factual",
      "jurisdiction": "UK — ICO",
      "legal_stage": "fine_imposed",
      "policy_signal": "enforcement",
      "publication_date": "DD-MM-YYYY",
      "source": {
        "name": "Source Name",
        "tier": "1|2|3|4",
        "original_url": "https://validated.source.url",
        "paywall": false,
        "author": "If available"
      },
      "scoring": {
        "total_score": 86,
        "breakdown": {
          "content_relevance": 40,
          "source_authority": 25,
          "development_significance": 15,
          "innovation_factor": 0,
          "quantitative_content": 6
        }
      },
      "content": {
        "summary": "100–140 palabras en español que cubran qué ocurrió, etapa, normas/políticas aplicables, entidades/afectados, métricas y próximos pasos.",
        "laws_invoked": ["GDPR Art. 32","Data Protection Act 2018"],
        "entities": [
          {"name":"[Nombre empresa]","type":"[Tipo]","sector":"[Sector]","jurisdiction":"[Jurisdicción]"}
        ],
        "institutions": ["[Autoridad de protección de datos]","[Regulador/Fuerzas del orden]"],
        "remedies": ["fine","corrective_measures"],
        "key_figures": {"amount":"[valor]","records_affected":"[n]"},
        "next_milestones": ["[Fecha de audiencia]","[Paso de implementación]"],
        "case_refs": ["https://ico.org.uk/...","https://eur-lex.europa.eu/..."],
        "dmbok_mapping": {
          "knowledge_areas": ["data_governance","data_quality"],
          "governance_level": "policy",
          "operating_model": "federated",
          "roles": ["data_owner","data_steward","DPO"],
          "controls": {"type":"preventive","category":"administrative","frameworks":["ISO27001"]},
          "data_domains": ["customer","employee"],
          "data_classification": "confidential",
          "data_lifecycle": ["use","share","archive"]
        },
        "data_quality": {"dimensions": ["accuracy","completeness"], "kpi_suggestions": ["% registros completos"], "severity": "medium"},
        "lineage": {"sources": ["CRM"], "targets": ["Data Warehouse"], "integration_type": "ETL"},
        "business_glossary_terms": ["dato_personal","transferencia_internacional"],
        "risk_rating": {"level": "high", "rationale": "Datos sensibles y alcance multinacional"}
      },
      "political_entities": [
        {"name":"[Ministerio/Autoridad]","role":"[ministro/regulador]","affiliation":"[partido]"}
      ],
      "platforms": ["Google","Microsoft"],
      "classification": {
        "primary_category": "privacy_gdpr|security_cybersecurity|ai_governance|cross_border_transfers|sector_compliance|employee_data|consumer_rights|data_ethics",
        "secondary_tags": ["GDPR","CCPA","LGPD","AI_Act","NIS2","SOC2","ISO27001","DMBoK2"],
        "instruments": ["EDPB_Guidelines","ICO_Guidance","FTC_Orders"],
        "institutions": ["EDPB","ICO","FTC","CNIL","AEPD"],
        "dmbok_knowledge_areas": ["data_governance","data_quality","metadata"]
      },
      "compliance_flags": {"privacy": true, "security": false, "ai_governance": false, "cross_border": false, "sector_specific": false, "employee_data": false, "consumer_rights": true}
    }
  ],
  "analytics": {
    "processing_statistics": {
      "sources_scanned": 0,
      "articles_reviewed": 0,
      "items_scoring_above_threshold": 0,
      "items_published": 0,
      "duplicates_identified": 0,
      "urls_validated": 0,
      "validation_failures": 0
    },
    "content_metrics": {
      "average_score": 0,
      "score_distribution": {"90-100":0,"80-89":0,"70-79":0,"60-69":0},
      "word_count_statistics": {"average_words": 0, "min_words": 0, "max_words": 0}
    },
    "coverage_analysis": {
      "jurisdiction_distribution": {"EU":0,"UK":0,"US":0,"CA":0,"BR":0,"Global":0},
      "category_distribution": {
        "privacy_gdpr": 0,
        "security_cybersecurity": 0,
        "ai_governance": 0,
        "cross_border_transfers": 0,
        "sector_compliance": 0,
        "employee_data": 0,
        "consumer_rights": 0,
        "data_ethics": 0,
        "platform_governance": 0,
        "policy_regulation": 0,
        "incidents_breaches": 0,
        "compliance_frameworks": 0
      },
      "dmbok_distribution": {
        "data_governance": 0,
        "data_quality": 0,
        "metadata": 0,
        "data_architecture": 0,
        "data_modeling": 0,
        "data_storage_operations": 0,
        "data_integration": 0,
        "mdm_rdm": 0,
        "data_security": 0,
        "analytics_bi": 0
      }
    }
  },
  "discarded_items": [
    {
      "rank": 21,
      "headline": "Titular descartado",
      "source": "Source Name",
      "url": "https://source.url",
      "publication_date": "DD-MM-YYYY",
      "score": 58,
      "discard_reason": "Por debajo del umbral de 60 puntos o fuera del alcance legal",
      "score_breakdown": {
        "content_relevance": 30,
        "source_authority": 15,
        "development_significance": 10,
        "innovation_factor": 0,
        "quantitative_content": 3
      }
    }
  ],
  "forward_looking": {
    "next_week_calendar": [
      {"date":"DD-MM-YYYY","event":"[Audiencia/Publicación de guía]","significance":"high|medium|low"}
    ],
    "monitoring_priorities": ["Caso clave a seguir","Regulación pendiente"],
    "emerging_trends": ["Patrón","Observación"],
    "data_gaps": ["Documentos faltantes","Métricas no disponibles"],
    "governance_actions": ["Actualizar política de retención","Definir KPIs de calidad para transferencias"]
  },
  "quality_assurance": {
    "editorial_notes": ["Nota sobre cifras conflictivas entre fuentes A/B"],
    "source_reliability": {"tier_1_percentage": 50, "tier_2_percentage": 30, "tier_3_percentage": 15, "tier_4_percentage": 5},
    "fact_checking": {"claims_verified": 0, "cross_references": 0, "potential_discrepancies": 0},
    "dmbok_checks": {"mapping_present": true, "dq_dimensions_present": true}
  }
}
```
