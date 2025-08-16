## OBJETIVO PRINCIPAL
Generar un **archivo JSON estructurado** con **hasta 50 noticias de Arte, Derecho y Política Cultural más relevantes de los últimos 30 días**. El alcance incluye **señales prejurídicas** (consultas públicas, anteproyectos, políticas de plataformas, decisiones de financiación) con alta probabilidad de traducirse en efectos **normativos, de cumplimiento o contenciosos**. Cada ítem debe incluir un párrafo analítico conciso (100–140 palabras) con **URLs de fuente validadas**. La salida debe estar en **español** y lista para conversión a marca Kepler Karst.

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
- Evaluar y puntuar cada candidato.
- Seleccionar top 50 dentro de SELECTION_DAYS, equilibrando categorías.
- Generar el Resumen semanal AL FINAL, en formato de viñetas, a partir de los ítems seleccionados.

### 2) FILTRO DE CONTENIDO: DOMINIO ARTE, DERECHO Y POLÍTICA CULTURAL
**Principio rector**: priorizar piezas donde la intersección principal sea **Derecho + Arte**. Se admite expansión a Negocios/Cultura/Política si existe un ángulo jurídico/regulatorio claro.

**Ámbitos núcleo (con vínculo jurídico explícito)**
- Patrimonio y restitución: UNESCO 1970; UNIDROIT 1995; ICPRCP; La Haya 1954; importación/exportación; devoluciones; decomisos.
- Propiedad intelectual y derechos morales: VARA (17 USC §106A), ARR, jurisprudencia TJUE/TEDH relevante para artes visuales, IA generativa afectando a artistas/colecciones.
- Cumplimiento y mercado del arte: AML/KYC para AMPs (UK/UE), sanciones (OFSI/UE/US), aduanas (Reg (UE) 2019/880), registros/supervisión.
- Fraude, autenticidad y enforcement: litigios por procedencia/autenticidad, delitos contra patrimonio, incautaciones, ADR (p. ej., CAfA).
- Gobernanza y ética en museos: códigos (ICOM/Museums Association), guías (Arts Council), conflictos de interés, compliance operativo.

**Expansión (siempre con impacto jurídico/regulatorio)**
- Política cultural y financiación: presupuestos, subvenciones condicionadas, reformas normativas, contratación pública.
- Libertad de expresión/orden público: retiradas de obras, restricciones en museos, periodo electoral, seguridad nacional aplicada al arte.
- Plataformas y gobernanza de contenidos: cambios de políticas, licencias, DMCA/notice-and-takedown, transparencia/publicidad.
- Trabajo y empleo: huelgas, litigios laborales, salud y seguridad, estatus de artistas.
- Espacio público y urbanismo: permisos, ordenanzas, remociones.
- Fiscalidad y mecenazgo/charities: IVA, exenciones, obligaciones de fundaciones.
- Datos y ciberseguridad: GDPR/CCPA, brechas/scraping/biometría en museos.
- Movilidad internacional: visados y controles fronterizos que afecten a exposiciones o artistas.

**INCLUIR (aclaraciones)**
- Subastas y mercado: incluir cuando exista ángulo legal/regulatorio (p. ej., ARR, sanciones/embargos, AML/KYC, disputas por procedencia, medidas cautelares, licencias).

**EXCLUIR**
- Cobertura cultural o de mercado sin ángulo jurídico (p. ej., precios récord, previews curatoriales, reseñas) salvo que se vincule a obligaciones legales.
- Opinión/comentario sin documento/acto oficial o hechos verificables.
- Temas de PI no relacionados con artes visuales, salvo impacto directo en artistas/obras/instituciones.
- Anécdotas políticas sin trayecto plausible a efectos regulatorios.

### 3) PRIORIZACIÓN DE FUENTES (con ejemplos)
Esta lista es orientativa, no exhaustiva. Cualquier fuente válida con documentos/actos oficiales es elegible.

**Nivel 1 — Primarias/Autoritativas (preferidas)**
- Tratados/organismos y boletines oficiales: UNESCO (1970; 1954 La Haya; ICPRCP), UNIDROIT 1995, EUR-Lex (ARR; Reg (UE) 2019/880), HUDOC (TEDH), CURIA (TJUE), BAILII, diarios/gacetas oficiales, consultas públicas.
- Autoridades PI y fuerzas del orden: WIPO/WIPO-Lex, US Copyright Office, OFSI/UE/US sanciones, INTERPOL/FBI.

**Nivel 2 — Sector/Profesional**
- ICOM (incl. Red Lists), Arts Council/Museums Association, Center for Art Law, CAfA.
- Plataformas: blogs/políticas oficiales (Meta/Instagram, YouTube, X, TikTok).

**Nivel 3 — Prensa especializada legal**
- The Art Newspaper (Law), Artnet (legal/IP), Hyperallergic (Art Law), etc.

**Nivel 4 — Prensa general (cuando aporta docs/actos oficiales o grandes desarrollos)**
- FT/Reuters/AP/WSJ, The Guardian, prensa nacional con documentos primarios.

**Reglas**
- Preferir documentos/decisiones oficiales; usar la fecha más temprana y autorizada; validar URLs; fusionar duplicados útiles.
- Asegurar diversidad temática/geográfica; evitar sobreconcentración en restituciones si hay desarrollos en política cultural o plataformas.

### 4) SISTEMA DE PUNTUACIÓN (simplificado y balanceado)

Puntuación total sobre 100. Seleccionar top 50, asegurando al menos 4 categorías representadas y ≤40% en «restitución».

1) Impacto jurídico/regulatorio (0–40)
- 35–40: acto oficial ejecutable (sentencia, norma vigente, guía vinculante, política de plataforma aplicada)
- 25–34: señal prejurídica robusta (consulta formal, anteproyecto, presupuesto aprobado, anuncio con calendario)
- 10–24: reporte sólido con implicaciones legales claras

2) Autoridad de la fuente (0–25)
- 20–25: tribunal/boletín/tratado/autoridad competente
- 12–19: ministerio/regulador/museo/fuerzas del orden; políticas de plataformas
- 6–11: sector profesional (ICOM, CAfA, Center for Art Law)
- 1–5: prensa especializada con reportaje original

3) Etapa/proximidad a enforcement (0–20)
- 16–20: sentencia/acuerdo/implementación/sanción ejecutada
- 11–15: aprobación/entrada en vigor/ratificación
- 6–10: presentación/consulta/orden administrativa
- 1–5: anuncio de intención

4) Claridad cuantitativa y trazabilidad (0–10)
- Métricas (importes, nº de piezas, regalías), enlaces a docs oficiales, fechas/casos referenciados

5) Diversidad temática/geográfica (0–5)
- Mejora el equilibrio del conjunto semanal

Penalizaciones
- −25: duplicado evidente
- −15: especulación sin respaldo documental
- −10: fuera de SELECTION_DAYS
- −5: paywall duro sin alternativa

### 5) REQUISITOS DE CONTENIDO

**Estándares de redacción**
- 100–140 palabras por ítem; español; analítico y conciso  
- Estructura: *Qué ocurrió → Etapa procesal → Leyes invocadas/objetos/cifras → Próximos pasos*

**Elementos obligatorios por ítem**
- **Jurisdicción y órgano** (tribunal/autoridad)  
- **Etapa procesal** (investigación, presentación, audiencia, sentencia, apelación, acuerdo, ejecución, consulta, anteproyecto, anuncio_político, actualización_política_plataforma, presupuesto)  
- **Leyes invocadas** (p. ej., “UNESCO 1970”; “UNIDROIT 1995”; “Directiva 2001/84/CE”; “17 USC §106A”; “Reg (UE) 2019/880”)  
- **Objetos** (artista, título, año, medio, cantidad) cuando esté disponible  
- **Instituciones** (museos/galerías/casas de subastas/aduanas/fuerzas del orden)  
- **Cifras** (daños/regalías/multas; número de piezas)  
- **Cronograma** (próxima audiencia/consulta/fecha de implementación)  
- **Fuente** (nombre, fecha, URL validada)

**Elementos recomendados para política/plataformas**
- **Entidades políticas** (ministerio, regulador, partido, funcionario)
- **Plataformas afectadas** (Meta/Instagram, YouTube, X, TikTok)
- **Señal de política** (consulta|anteproyecto|anuncio|presupuesto|actualización_plataforma)

**Validación**
- Cada hecho debe ser trazable a la(s) fuente(s) citada(s); URLs accesibles; fechas dentro de SELECTION_DAYS; sin extrapolaciones no sustentadas; reconciliar informes conflictivos mediante contraste cruzado.

### 6) ESPECIFICACIÓN DE ESTRUCTURA JSON (Arte, Derecho y Política Cultural)

**Reglas de integridad**
- Todas las fechas en DD-MM-YYYY; todos los números en sus unidades originales; países en ISO-3166-1 alfa-2.

**Campos adicionales**
- `jurisdiction`: p. ej., “UK — High Court”, “EU — CJEU”, “US — S.D.N.Y.”  
- `legal_stage`: investigation|filing|hearing|judgment|appeal|settlement|implementation|consultation|draft_bill|policy_announcement|platform_policy_update|budget  
- `laws_invoked`: p. ej., ["UNESCO 1970","UNIDROIT 1995","Directive 2001/84/EC","17 USC §106A","Reg (EU) 2019/880"]  
- `objects`: [{artist,title,year,medium,quantity,period}]  
- `institutions`: [museum/gallery/auction/LEA/regulator]  
- `remedies`: [restitution|injunction|damages|royalties|seizure|sanctions]  
- `case_refs`: enlaces a sentencias/expedientes (HUDOC/CURIA/BAILII/etc.)  
- `compliance_flags`: {aml: true|false, sanctions: true|false, ethics_guidance: true|false, platform_policy: true|false, speech_censorship: true|false, charity_compliance: true|false, data_privacy: true|false}  
- Opcional: `media_assets` (URLs a documentos oficiales o imágenes)
- `policy_signal`: consultation|draft_bill|policy_announcement|platform_policy_update|budget  
- `political_entities`: [{name, role, affiliation}]  
- `platforms`: ["Instagram","YouTube","X","TikTok"]

### 7) MANEJO DE ERRORES Y VALIDACIÓN
Prechequeos: accesibilidad de URLs; ventana temporal; coincidencia de palabras clave legales; detección de duplicados; equilibrio temático (<40% en una sola categoría).  
QA: conteo de palabras; verificaciones estructurales; cifras inconsistentes; marcar afirmaciones no verificadas.  
Validación de salida: sintaxis JSON; cumplimiento de esquema; pruebas de URLs; auditoría de puntuación.

---

## PLANTILLA DE SALIDA (Arte, Derecho y Política Cultural)

```json
{
  "metadata": {
    "title": "Arte, Derecho y Política Cultural — [DD-MM-YYYY] a [DD-MM-YYYY]",
    "subtitle": "#BRAVE A(rt)DVOCACY",
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
    }
  },
  "executive_summary": {
    "weekly_bullets": [
      "[5–8 viñetas] Fallos clave / restituciones / cumplimiento (AML, sanciones) / PI (VARA, ARR, IA) / política cultural / plataformas / próximos hitos",
      "Sentencias y medidas ejecutadas (nº, jurisdicciones)",
      "Consultas y anteproyectos abiertos (fechas límite)",
      "Cambios en políticas de plataformas que afecten a museos/artistas"
    ],
    "weekly_overview": "Resumen generado AL FINAL a partir de viñetas (unir con •).",
    "key_themes": ["Restitución y UNESCO/UNIDROIT","Derechos de autor y morales","Cumplimiento AML/Sanciones","Política cultural","Plataformas y moderación"],
    "geographical_focus": ["UE/Reino Unido","EE. UU.","Sur Global"],
    "trend_analysis": "Breve evaluación de patrones e implicaciones"
  },
  "items": [
    {
      "item_id": "AL2025W33-001",
      "rank": 1,
      "headline": "Titular claro y factual",
      "jurisdiction": "UK — DCMS / Parliament",
      "legal_stage": "draft_bill",
      "policy_signal": "draft_bill",
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
        "summary": "100–140 palabras en español que cubran qué ocurrió, etapa, normas/políticas aplicables, objetos/afectados, métricas y próximos pasos.",
        "laws_invoked": ["Directive 2001/84/EC","Artist's Resale Right Regulations 2006"],
        "objects": [
          {"artist":"[Nombre]","title":"[Título]","year":"[YYYY]","medium":"[Medio]","quantity":1,"period":"[p. ej., Moderno]"}
        ],
        "institutions": ["[Museo/Galería/Casa de subastas]","[Regulador/Fuerzas del orden]"],
        "remedies": ["injunction","damages"],
        "key_figures": {"amount":"[valor]","items_returned":"[n]"},
        "next_milestones": ["[Fecha de audiencia]","[Paso de implementación]"],
        "case_refs": ["https://hudoc.echr.coe.int/...","https://curia.europa.eu/..."]
      },
      "political_entities": [
        {"name":"[Ministerio/Autoridad]","role":"[ministro/regulador]","affiliation":"[partido]"}
      ],
      "platforms": ["Instagram","YouTube"],
      "classification": {
        "primary_category": "restitution|ip_copyright|aml_sanctions|fraud_authenticity|ethics_governance|free_expression|market_auction",
        "secondary_tags": ["UNESCO1970","UNIDROIT1995","ARR","VARA","AI_copyright","Reg2019_880"],
        "instruments": ["ICPRCP","ICOM_RedList"],
        "institutions": ["UNESCO","UNIDROIT","WIPO","EU","GOV.UK"]
      },
      "compliance_flags": {"aml": false, "sanctions": false, "ethics_guidance": false, "platform_policy": true, "speech_censorship": false, "charity_compliance": false, "data_privacy": false}
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
      "jurisdiction_distribution": {"EU":0,"UK":0,"US":0,"Global":0},
      "category_distribution": {
        "restitution": 0,
        "ip_copyright": 0,
        "aml_sanctions": 0,
        "fraud_authenticity": 0,
        "ethics_governance": 0,
        "free_expression": 0,
        "policy_politics": 0,
        "platform_governance": 0,
        "labor_employment": 0,
        "tax_charity": 0,
        "public_art": 0,
        "data_privacy": 0,
        "market_auction": 0
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
    "data_gaps": ["Documentos faltantes","Métricas no disponibles"]
  },
  "quality_assurance": {
    "editorial_notes": ["Nota sobre cifras conflictivas entre fuentes A/B"],
    "source_reliability": {"tier_1_percentage": 50, "tier_2_percentage": 30, "tier_3_percentage": 15, "tier_4_percentage": 5},
    "fact_checking": {"claims_verified": 0, "cross_references": 0, "potential_discrepancies": 0}
  }
}
