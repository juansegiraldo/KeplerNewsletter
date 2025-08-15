# Crear el archivo Markdown con el prompt del agente de Arte y Derecho adaptado
content = r"""# Boletín semanal Arte y Derecho — Prompt de Agente (Salida JSON) v1.0 (Derecho y Arte)

## OBJETIVO PRINCIPAL
Generar un **archivo JSON estructurado** con **hasta 20 noticias de Arte y Derecho más relevantes de los últimos 7 días**. Cada ítem debe incluir un párrafo analítico conciso (100–140 palabras) con **URLs de fuente validadas**. La salida debe estar en **español** y lista para conversión a marca Kepler Karst.

---

## MARCO DE EJECUCIÓN

### 1) ALCANCE TEMPORAL
- **Ventana temporal**: exactamente 30 días naturales hacia atrás desde la fecha actual  
- **Formato de fecha**: DD-MM-YYYY en todas las salidas  
- **Zona horaria**: usar UTC para consistencia

### 2) FILTRO DE CONTENIDO: DOMINIO ARTE Y DERECHO
**INCLUIR SOLO** artículos con un enfoque *jurídico/regulatorio* sobre artes visuales/patrimonio cultural:

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

**EXCLUIR**
- Cobertura cultural **sin** ángulo jurídico  
- Pura información de mercado/subastas **sin** implicaciones de cumplimiento o legales  
- Temas de PI no relacionados con artes visuales salvo que afecten directamente a artistas/obras/instituciones

### 3) PRIORIZACIÓN DE FUENTES (con ejemplos)

**Nivel 1 — Primarias/Autoritativas**
- **Tratados y organismos**: UNESCO (1970; 1954 La Haya; ICPRCP) — <https://www.unesco.org/en/fight-illicit-trafficking/about>, <https://www.unesco.org/en/legal-affairs/convention-means-prohibiting-and-preventing-illicit-import-export-and-transfer-ownership-cultural>, <https://www.unesco.org/en/heritage-armed-conflicts/1954-convention>, <https://www.unesco.org/en/fight-illicit-trafficking/return-and-restitution-under-icprcp>  
- **UNIDROIT 1995** — <https://www.unidroit.org/instruments/cultural-property/1995-convention/> (PDF: <https://www.unidroit.org/english/conventions/1995culturalproperty/1995culturalproperty-e.pdf>)  
- **Derecho de la UE**: EUR-Lex 2001/84/CE (ARR) — <https://eur-lex.europa.eu/eli/dir/2001/84/oj/eng>; Reg (UE) 2019/880 — <https://eur-lex.europa.eu/eli/reg/2019/880/oj/eng>  
- **Tribunales y jurisprudencia**: HUDOC (TEDH) — <https://hudoc.echr.coe.int/>; CURIA (TJUE) — <https://curia.europa.eu/juris>; BAILII — <https://www.bailii.org/>  
- **Gobierno del Reino Unido**: HMRC AML para AMPs — <https://www.gov.uk/guidance/money-laundering-supervision-for-art-market-participants>; guía de sanciones OFSI para AMPs — <https://www.gov.uk/government/publications/high-value-dealers-art-market-participants-guidance/financial-sanctions-guidance-for-high-value-dealers-art-market-participants>; Spoliation Advisory Panel — <https://www.gov.uk/government/groups/spoliation-advisory-panel>  
- **Autoridades de PI**: US Copyright Office (recursos VARA) — <https://www.copyright.gov/reports/waiver-moral-rights-visual-artworks.pdf>; WIPO/WIPO-Lex — <https://www.wipo.int/wipolex/en/main/legislation>  
- **Fuerzas del orden**: FBI Art Crime Team — <https://www.fbi.gov/investigate/violent-crime/art-crime>; INTERPOL Stolen Works of Art — <https://www.interpol.int/en/Crimes/Cultural-heritage-crime/Stolen-Works-of-Art-Database>; app ID-Art — <https://www.interpol.int/en/Crimes/Cultural-heritage-crime/ID-Art-mobile-app>

**Nivel 2 — Sector/Profesional**
- ICOM Red Lists — <https://icom.museum/en/red-lists/>  
- Arts Council England restitution guidance — <https://www.artscouncil.org.uk/supporting-arts-museums-and-libraries/supporting-collections-and-cultural-property/restitution-and-repatriation-practical-guide-museums-england>  
- Museums Association Code of Ethics — <https://www.museumsassociation.org/campaigns/ethics/code-of-ethics/>  
- Center for Art Law — <https://itsartlaw.org/>  
- Court of Arbitration for Art (CAfA) — <https://www.cafa.world/>

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

### 4) SISTEMA DE PUNTUACIÓN (Arte y Derecho)

**Relevancia del contenido (+30 a +50)**
- +50: ≥3 palabras clave legales (p. ej., “UNESCO 1970”, “VARA”, “ARR”, “UNIDROIT 1995”) **y** cita una norma/sentencia/aviso oficial  
- +40: ≥2 palabras clave legales **y** incluye documento oficial (sentencia, auto, boletín)  
- +30: ≥2 palabras clave legales (base)

**Autoridad de la fuente (+10 a +25)**
- +25: tribunal/boletín oficial/tratado/comunicado de autoridad competente  
- +20: museo/regulador/fuerzas del orden con hechos verificables  
- +15: instituto/ONG reconocida en art law (Center for Art Law, ICOM, CAfA)  
- +10: prensa especializada reputada con reportaje original

**Importancia del desarrollo (+15 a +30)**
- +30: sentencia/acuerdo/restitución ejecutada  
- +25: aprobación normativa/entrada en vigor/ratificación  
- +20: presentación de demanda/MoU o inicio formal de investigación  
- +15: fase temprana o consulta

**Factor de innovación (+10 a +20)**
- +20: precedente novedoso (IA y copyright; nuevo esquema de ADR)  
- +15: nueva guía de ética/gobernanza o herramienta de cumplimiento (Listas Rojas/guías AML)  
- +10: mecanismo regulatorio emergente (aplicación de sanciones/AML al arte)

**Contenido cuantitativo (+5 a +15)**
- +15: múltiples métricas (importes, número de objetos, sanciones, regalías)  
- +10: una métrica con contexto  
- +5: referencia cuantitativa general

**Penalizaciones**
- −25 duplicado; −15 especulación; −10 fuera de la ventana de 7 días; −5 paywall duro sin alternativa

**Selección final**: top 20 por puntuación total

### 5) REQUISITOS DE CONTENIDO

**Estándares de redacción**
- 100–140 palabras por ítem; español; analítico y conciso  
- Estructura: *Qué ocurrió → Etapa procesal → Leyes invocadas/objetos/cifras → Próximos pasos*

**Elementos obligatorios por ítem**
- **Jurisdicción y órgano** (tribunal/autoridad)  
- **Etapa procesal** (investigación, presentación, audiencia, sentencia, apelación, acuerdo, ejecución)  
- **Leyes invocadas** (p. ej., “UNESCO 1970”; “UNIDROIT 1995”; “Directiva 2001/84/CE”; “17 USC §106A”; “Reg (UE) 2019/880”)  
- **Objetos** (artista, título, año, medio, cantidad) cuando esté disponible  
- **Instituciones** (museos/galerías/casas de subastas/aduanas/fuerzas del orden)  
- **Cifras** (daños/regalías/multas; número de piezas)  
- **Cronograma** (próxima audiencia/consulta/fecha de implementación)  
- **Fuente** (nombre, fecha, URL validada)

**Validación**
- Cada hecho debe ser trazable a la(s) fuente(s) citada(s); URLs accesibles; fechas dentro de la ventana de 7 días; sin extrapolaciones no sustentadas; reconciliar informes conflictivos mediante contraste cruzado.

### 6) ESPECIFICACIÓN DE ESTRUCTURA JSON (Arte y Derecho)

**Reglas de integridad**
- Todas las fechas en DD-MM-YYYY; todos los números en sus unidades originales; países en ISO-3166-1 alfa-2.

**Campos adicionales**
- `jurisdiction`: p. ej., “UK — High Court”, “EU — CJEU”, “US — S.D.N.Y.”  
- `legal_stage`: investigation|filing|hearing|judgment|appeal|settlement|implementation  
- `laws_invoked`: p. ej., ["UNESCO 1970","UNIDROIT 1995","Directive 2001/84/EC","17 USC §106A","Reg (EU) 2019/880"]  
- `objects`: [{artist,title,year,medium,quantity,period}]  
- `institutions`: [museum/gallery/auction/LEA/regulator]  
- `remedies`: [restitution|injunction|damages|royalties|seizure|sanctions]  
- `case_refs`: enlaces a sentencias/expedientes (HUDOC/CURIA/BAILII/etc.)  
- `compliance_flags`: {aml: true|false, sanctions: true|false, ethics_guidance: true|false}  
- Opcional: `media_assets` (URLs a documentos oficiales o imágenes)

### 7) MANEJO DE ERRORES Y VALIDACIÓN
Prechequeos: accesibilidad de URLs; ventana temporal; coincidencia de palabras clave legales; detección de duplicados.  
QA: conteo de palabras; verificaciones estructurales; cifras inconsistentes; marcar afirmaciones no verificadas.  
Validación de salida: sintaxis JSON; cumplimiento de esquema; pruebas de URLs; auditoría de puntuación.

---

## PLANTILLA DE SALIDA (Arte y Derecho)

```json
{
  "metadata": {
    "title": "Arte y Derecho — [DD-MM-YYYY] a [DD-MM-YYYY]",
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
    "weekly_overview": "150–200 palabras: fallos clave, restituciones/devoluciones, cumplimiento (AML/sanciones), precedentes de PI (VARA/ARR/IA) y alertas para la próxima semana.",
    "key_themes": ["Restitución y UNESCO/UNIDROIT","Derechos de autor y morales","Cumplimiento AML/Sanciones"],
    "geographical_focus": ["UE/Reino Unido","EE. UU.","Sur Global"],
    "trend_analysis": "Breve evaluación de patrones e implicaciones"
  },
  "items": [
    {
      "item_id": "AL2025W33-001",
      "rank": 1,
      "headline": "Titular claro y factual",
      "jurisdiction": "UK — High Court",
      "legal_stage": "judgment",
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
        "summary": "100–140 palabras en español que cubran qué ocurrió, etapa, leyes invocadas, objetos, métricas y próximos pasos.",
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
      "classification": {
        "primary_category": "restitution|ip_copyright|aml_sanctions|fraud_authenticity|ethics_governance|free_expression",
        "secondary_tags": ["UNESCO1970","UNIDROIT1995","ARR","VARA","AI_copyright","Reg2019_880"],
        "instruments": ["ICPRCP","ICOM_RedList"],
        "institutions": ["UNESCO","UNIDROIT","WIPO","EU","GOV.UK"]
      }
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
        "free_expression": 0
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
