## OBJETIVO PRINCIPAL
Generar un **archivo JSON estructurado** con **hasta 20 noticias de Arte, Derecho y Política Cultural más relevantes de los últimos 7 días**. El alcance incluye **señales prejurídicas** (consultas públicas, anteproyectos, políticas de plataformas, decisiones de financiación) con alta probabilidad de traducirse en efectos **normativos, de cumplimiento o contenciosos**. Cada ítem debe incluir un párrafo analítico conciso (100–140 palabras) con **URLs de fuente validadas**. La salida debe estar en **español** y lista para conversión a marca Kepler Karst.

---

## MARCO DE EJECUCIÓN

### 1) ALCANCE TEMPORAL
- **Búsqueda ampliada**: 30 días naturales hacia atrás desde la fecha actual
- **Selección final**: ítems publicados en los últimos 7 días
- **Formato de fecha**: DD-MM-YYYY en todas las salidas  
- **Zona horaria**: usar UTC para consistencia

### 2) FILTRO DE CONTENIDO: DOMINIO ARTE, DERECHO Y POLÍTICA CULTURAL
**INCLUIR SOLO** artículos con un enfoque *jurídico/regulatorio* sobre artes visuales/patrimonio cultural, así como **señales de política pública** y **gobernanza de plataformas** con posible impacto jurídico:

**Patrimonio y restitución**
- UNESCO 1970; UNIDROIT 1995; ICPRCP; Convenio de La Haya de 1954; Listas Rojas ICOM; importación/exportación y decomisos; devoluciones/restituciones bilaterales; derecho internacional público/privado comparado.

**Derechos de autor y derechos morales**
- VARA (17 USC §106A); derecho de participación (ARR); jurisprudencia TJUE/TEDH que afecte la expresión artística; copyright en IA generativa cuando impacta directamente a artistas, obras o museos.

**Regulación de mercado y cumplimiento**
- AML/KYC para Art Market Participants (UK/UE); OFSI/sanciones financieras; supervisión/registro HMRC; control aduanero/importación (p. ej., Reg (UE) 2019/880).

**Fraude, autenticidad y actuaciones**
- Litigios o ejecución sobre autenticidad/procedencia; delitos contra el patrimonio; incautaciones/decomisos; ADR (p. ej., CAfA).

**Gobernanza y ética en museos**
- Códigos ICOM/Asociación de Museos; guía de restitución del Arts Council England; políticas de gobernanza y dictámenes éticos con impacto operativo.

**Política cultural y financiación pública**
- Presupuestos, recortes, subvenciones condicionadas; marcos de mecenazgo/charities; cambios en estatutos de entidades culturales; contratación/encargos públicos.

**Libertad de expresión, censura y ciclo electoral**
- Retiradas de obras/exposiciones por decisiones de autoridades; órdenes administrativas; leyes de orden público/seguridad nacional aplicadas a artistas; regulación de protestas en museos; intervenciones en periodo electoral que afecten a instituciones culturales.

**Plataformas y gobernanza de contenidos**
- Cambios de políticas de moderación (Meta/YouTube/X/TikTok), geobloqueos, transparencia y normas de publicidad que afecten a difusión de obras/artistas/museos; DMCA/notice-and-takedown; acuerdos de licencias con plataformas.

**Trabajo y empleo en el sector cultural**
- Huelgas/negociación colectiva; litigios laborales y de discriminación; salud y seguridad; estatus laboral de artistas independientes.

**Espacio público y urbanismo**
- Permisos, ordenanzas y licitaciones para arte público; remociones por orden público; debates sobre memoria histórica con efectos regulatorios.

**Fiscalidad y mecenazgo**
- IVA/aduanas aplicables al arte; exenciones fiscales; compliance de entidades sin ánimo de lucro y fundaciones.

**Protección de datos y ciberseguridad**
- GDPR/CCPA y brechas de datos en museos/galerías; scraping de imágenes/colecciones; biometría en exposiciones.

**Movilidad internacional de artistas**
- Visados, denegaciones y controles fronterizos que impacten giras/exposiciones; listados de sanciones vinculados a artistas/instituciones.

**IA y cultura digital**
- Deepfakes, derechos de imagen y voz; datasets de entrenamiento con colecciones; directrices gubernamentales o de plataformas aplicables al arte.

**EXCLUIR**
- Cobertura cultural **sin** ángulo jurídico  
- Pura información de mercado/subastas **sin** implicaciones de cumplimiento o legales  
- Temas de PI no relacionados con artes visuales salvo que afecten directamente a artistas/obras/instituciones
 - Opinión/comentario sin documento/acto oficial o hechos verificables
 - Anécdotas políticas sin trayecto plausible a efectos jurídicos o regulatorios

### 3) PRIORIZACIÓN DE FUENTES (con ejemplos)

**Nivel 1 — Primarias/Autoritativas**
- **Tratados y organismos**: UNESCO (1970; 1954 La Haya; ICPRCP) — <https://www.unesco.org/en/fight-illicit-trafficking/about>, <https://www.unesco.org/en/legal-affairs/convention-means-prohibiting-and-preventing-illicit-import-export-and-transfer-ownership-cultural>, <https://www.unesco.org/en/heritage-armed-conflicts/1954-convention>, <https://www.unesco.org/en/fight-illicit-trafficking/return-and-restitution-under-icprcp>  
- **UNIDROIT 1995** — <https://www.unidroit.org/instruments/cultural-property/1995-convention/> (PDF: <https://www.unidroit.org/english/conventions/1995culturalproperty/1995culturalproperty-e.pdf>)  
- **Derecho de la UE**: EUR-Lex 2001/84/CE (ARR) — <https://eur-lex.europa.eu/eli/dir/2001/84/oj/eng>; Reg (UE) 2019/880 — <https://eur-lex.europa.eu/eli/reg/2019/880/oj/eng>  
- **Tribunales y jurisprudencia**: HUDOC (TEDH) — <https://hudoc.echr.coe.int/>; CURIA (TJUE) — <https://curia.europa.eu/juris>; BAILII — <https://www.bailii.org/>  
- **Gobierno del Reino Unido**: HMRC AML para AMPs — <https://www.gov.uk/guidance/money-laundering-supervision-for-art-market-participants>; guía de sanciones OFSI para AMPs — <https://www.gov.uk/government/publications/high-value-dealers-art-market-participants-guidance/financial-sanctions-guidance-for-high-value-dealers-art-market-participants>; Spoliation Advisory Panel — <https://www.gov.uk/government/groups/spoliation-advisory-panel>  
- **Autoridades de PI**: US Copyright Office (recursos VARA) — <https://www.copyright.gov/reports/waiver-moral-rights-visual-artworks.pdf>; WIPO/WIPO-Lex — <https://www.wipo.int/wipolex/en/main/legislation>  
- **Fuerzas del orden**: FBI Art Crime Team — <https://www.fbi.gov/investigate/violent-crime/art-crime>; INTERPOL Stolen Works of Art — <https://www.interpol.int/en/Crimes/Cultural-heritage-crime/Stolen-Works-of-Art-Database>; app ID-Art — <https://www.interpol.int/en/Crimes/Cultural-heritage-crime/ID-Art-mobile-app>
 - **Ministerios y parlamentos**: ministerios de cultura y reguladores; diarios oficiales (BOE/DOUE/DOEs/BOCM/etc.); gacetas parlamentarias; consultas públicas regulatorias; autoridades audiovisuales/medios.
 - **Ámbito local**: diarios/boletines oficiales autonómicos y municipales; ordenanzas urbanísticas aplicables al espacio público.

**Nivel 2 — Sector/Profesional**
- ICOM Red Lists — <https://icom.museum/en/red-lists/>  
- Arts Council England restitution guidance — <https://www.artscouncil.org.uk/supporting-arts-museums-and-libraries/supporting-collections-and-cultural-property/restitution-and-repatriation-practical-guide-museums-england>  
- Museums Association Code of Ethics — <https://www.museumsassociation.org/campaigns/ethics/code-of-ethics/>  
- Center for Art Law — <https://itsartlaw.org/>  
- Court of Arbitration for Art (CAfA) — <https://www.cafa.world/>
 - **Plataformas**: centros de transparencia y actualizaciones de políticas de Meta/Instagram, YouTube, X, TikTok (blogs oficiales; repositorios de políticas).
 - **Agencias de financiación**: NEA/Arts Council/Creative Europe y equivalentes.

**Nivel 3 — Prensa especializada (cobertura legal)**
- The Art Newspaper (Law) — <https://www.theartnewspaper.com/keywords/law>
- Artnet News (legal/IP) — <https://news.artnet.com/> (artículos con etiqueta legal)
- ArtReview — <https://artreview.com/>
- ArtNews — <https://www.artnews.com/>
- El Grito — <https://elgrito.com/>
- Hyperallergic (Art Law) — <https://hyperallergic.com/tag/art-law/>

**Nivel 4 — Prensa general (cuando aporta docs primarios o grandes desarrollos legales)**
- The Guardian — <https://www.theguardian.com/>
- El Confidencial — <https://www.elconfidencial.com/>
- FT/Reuters/AP/WSJ — para actualizaciones de sanciones/AML o cambios normativos que impacten el mercado del arte.

**Reglas de selección de fuentes**
- Preferir **documentos/decisiones oficiales** frente a comentarios; elegir la fecha de publicación **más temprana y autorizada**; validar URLs; fusionar duplicados en un solo ítem con múltiples fuentes cuando sea útil.
 - Asegurar **diversidad temática y geográfica**; evitar monocultivo de restitución/UNESCO cuando existan desarrollos relevantes en política cultural o plataformas.

### 4) SISTEMA DE PUNTUACIÓN (Arte, Derecho y Política Cultural)

**Relevancia del contenido (+30 a +45)**
- +45: acto/documento oficial o equivalente que incide directamente en el marco jurídico/regulatorio o su aplicación (sentencia, normativa, guía, política de plataforma)  
- +40: señal prejurídica con alta probabilidad de enforcement (consulta pública, anteproyecto, presupuesto/orden administrativa, actualización de política de plataforma)  
- +30: reporte sólido con ≥2 conceptos legales/regulatorios aplicables

**Autoridad de la fuente (+10 a +25)**
- +25: tribunal/boletín oficial/tratado/comunicado de autoridad competente  
- +20: ministerio/regulador/museo/fuerzas del orden; centros oficiales de políticas de plataformas  
- +15: instituto/ONG reconocida en art law/libertad de expresión (Center for Art Law, ICOM, CAfA, PEN, EFF)  
- +10: prensa especializada reputada con reportaje original

**Importancia del desarrollo (+15 a +30)**
- +30: sentencia/acuerdo/implementación ejecutada (incluye enforcement/plataformas)  
- +25: aprobación normativa/entrada en vigor/ratificación/presupuesto aprobado  
- +20: presentación de demanda/consulta formal/anteproyecto/orden administrativa  
- +15: fase temprana (anuncio de intención/lineamientos preliminares)

**Factor de innovación (+5 a +20)**
- +20: precedente novedoso (IA y copyright; gobernanza de plataformas con impacto en arte)  
- +15: nueva guía de ética/gobernanza o herramienta de cumplimiento (Listas Rojas/guías AML; políticas de plataforma)  
- +5–10: mecanismo regulatorio emergente (sanciones/AML; contenido/espacio público)

**Contenido cuantitativo (+5 a +15)**
- +15: múltiples métricas (importes, número de objetos, sanciones, regalías)  
- +10: una métrica con contexto  
- +5: referencia cuantitativa general

**Señal de política y probabilidad de justiciabilidad (+10 a +20)**
- +20: acto con calendario y autoridad competente identificada; alta probabilidad de litigio/enforcement  
- +10: señal consistente pero sin calendario claro

**Penalizaciones**
- −25 duplicado; −15 especulación; −15 sobreconcentración temática (>40% de la preselección en la misma categoría); −10 fuera de la ventana de 7 días; −5 paywall duro sin alternativa

**Bonificación de diversidad (+0 a +10)**
- +10 si la pieza mejora equilibrio geográfico/temático del conjunto semanal

**Selección final**: top 20 por puntuación total, asegurando al menos 4 categorías representadas y ≤40% del total en «restitución».

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
- Cada hecho debe ser trazable a la(s) fuente(s) citada(s); URLs accesibles; fechas dentro de la ventana de 7 días; sin extrapolaciones no sustentadas; reconciliar informes conflictivos mediante contraste cruzado.

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
    "weekly_overview": "150–200 palabras: fallos clave, restituciones/devoluciones, cumplimiento (AML/sanciones), precedentes de PI (VARA/ARR/IA), política cultural (presupuestos/consultas) y gobernanza de plataformas (cambios de políticas) con alertas para la próxima semana.",
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
        "primary_category": "restitution|ip_copyright|aml_sanctions|fraud_authenticity|ethics_governance|free_expression",
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
        "data_privacy": 0
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
