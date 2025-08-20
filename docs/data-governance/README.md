# Gobernanza de Datos Empresarial - Suite Completa

Esta suite proporciona herramientas completas para generar y procesar boletines semanales sobre Gobernanza de Datos Empresarial, siguiendo la marca Kepler Karst.

## 📁 Estructura de Carpetas

```
data-governance/
├── assets/
│   ├── fonts/
│   │   └── SharpGroteskBook16-Regular.ttf
│   └── headers/
│       └── HeaderDataGovernance.jpeg
├── issues/
│   ├── sample_datagovernance_digest.html
│   └── sample_datagovernance_digest_meta.html
├── index.html
└── README.md
```

## 🎯 Componentes de la Suite

### 1. Prompt de Generación
**Archivo:** `prompts/data-governance/PromptDataGovernance.md`

Este prompt está diseñado para generar archivos JSON estructurados con hasta 50 noticias relevantes de gobernanza de datos empresarial de los últimos 30 días.

**Características principales:**
- **Alcance:** Privacidad (GDPR, CCPA, LGPD), seguridad, IA, transferencias internacionales
- **Fuentes prioritarias:** Autoridades de protección de datos, reguladores, tribunales
- **Sistema de puntuación:** 100 puntos basado en impacto jurídico, autoridad de fuente, y relevancia
- **Estructura JSON:** Completa con metadatos, analytics y validación

### 2. Convertidor JSON a HTML
**Archivo:** `scripts/converters/json_to_html_converter_datagovernance.py`

Convierte los archivos JSON generados en dos formatos HTML:
- **Digest original:** Boletín semanal con diseño Kepler Karst
- **Dashboard de analytics:** Métricas y gráficos de distribución

**Uso:**
```bash
python scripts/converters/json_to_html_converter_datagovernance.py <archivo.json>
```

**Características:**
- Diseño responsivo con marca Kepler Karst
- Color scheme azul (#4A90E2) para data governance
- Gráficos de distribución por jurisdicción y categorías
- Enlaces automáticos a Google Search como fallback
- Resaltado de países y ciudades relevantes

### 3. Estructura de Datos JSON

El JSON generado incluye:

```json
{
  "metadata": {
    "title": "Gobernanza de Datos Empresarial — [DD-MM-YYYY] a [DD-MM-YYYY]",
    "subtitle": "#DATA GOVERNANCE INSIGHTS",
    "period": {"start_date":"[DD-MM-YYYY]","end_date":"[DD-MM-YYYY]","days_covered":7}
  },
  "executive_summary": {
    "weekly_bullets": ["5-8 viñetas de resumen"],
    "key_themes": ["Privacidad y GDPR/CCPA/LGPD","Seguridad y ciberseguridad","IA y gobernanza de datos"],
    "geographical_focus": ["UE/Reino Unido","EE. UU.","Brasil","Global"]
  },
  "items": [
    {
      "item_id": "DG2025W33-001",
      "headline": "Titular claro y factual",
      "jurisdiction": "UK — ICO",
      "legal_stage": "fine_imposed",
      "content": {
        "summary": "100-140 palabras en español",
        "laws_invoked": ["GDPR Art. 32","Data Protection Act 2018"],
        "entities": [{"name":"British Airways","type":"Airlines","sector":"Transportation"}],
        "key_figures": {"amount":"£12.7M","records_affected":"429,612"}
      },
      "classification": {
        "primary_category": "privacy_gdpr",
        "secondary_tags": ["GDPR","Enforcement","Data Breach"],
        "instruments": ["ICO_Enforcement_Notice","GDPR_Article_32"]
      }
    }
  ],
  "analytics": {
    "processing_statistics": {"sources_scanned": 150, "items_published": 3},
    "coverage_analysis": {
      "jurisdiction_distribution": {"UK":1,"EU":1,"US":1},
      "category_distribution": {"privacy_gdpr": 1, "ai_governance": 1}
    }
  }
}
```

## 🎨 Categorías Principales

1. **Privacidad y GDPR/CCPA/LGPD**
   - Enforcement de regulaciones de privacidad
   - Multas y sanciones
   - Decisiones de autoridades de protección de datos

2. **Seguridad y Ciberseguridad**
   - Incidentes de seguridad
   - Violaciones de datos
   - Cumplimiento SOC2/ISO27001

3. **IA y Gobernanza de Datos**
   - Regulaciones de IA (AI Act)
   - Transparencia algorítmica
   - Sesgos y ética de datos

4. **Transferencias Internacionales**
   - Cláusulas contractuales estándar
   - Decisiones de adecuación
   - Schrems II y consecuencias

5. **Cumplimiento Sectorial**
   - Regulaciones financieras (BCBS)
   - Salud (HIPAA)
   - Telecomunicaciones

## 🔧 Flujo de Trabajo

1. **Generación:** Usar el prompt con un modelo de IA para generar el JSON
2. **Validación:** Revisar la estructura y contenido del JSON
3. **Conversión:** Ejecutar el convertidor para generar HTML
4. **Publicación:** Los archivos se guardan en `docs/data-governance/issues/`

## 📊 Analytics Incluidos

- **Estadísticas de procesamiento:** Fuentes escaneadas, artículos revisados
- **Métricas de contenido:** Puntuación promedio, distribución de puntuaciones
- **Análisis de cobertura:** Distribución por jurisdicción y categorías
- **Top instrumentos legales:** Marcos regulatorios más mencionados
- **Nube de tags:** Tags secundarios más frecuentes

## 🎯 Fuentes Prioritarias

**Nivel 1 — Autoritativas:**
- ICO (UK), CNIL (Francia), AEPD (España), FTC (US), OPC (Canadá), ANPD (Brasil)
- EDPB, Comisión Europea, Parlamento Europeo
- Tribunales y decisiones judiciales

**Nivel 2 — Sector/Profesional:**
- IAPP, ISACA, DAMA, IEEE, ACM
- Gartner, Forrester, IDC (reportes regulatorios)
- Blogs oficiales de Google, Microsoft, AWS, Meta

## 🚀 Uso Rápido

1. **Generar JSON:**
   ```bash
   # Usar el prompt con tu modelo de IA preferido
   # Guardar resultado en data/data-governance/tu_digest.json
   ```

2. **Convertir a HTML:**
   ```bash
   python scripts/converters/json_to_html_converter_datagovernance.py data/data-governance/tu_digest.json
   ```

3. **Resultado:**
   - `docs/data-governance/issues/tu_digest.html` (boletín)
   - `docs/data-governance/issues/tu_digest_meta.html` (analytics)

## 📝 Notas de Diseño

- **Color principal:** #4A90E2 (azul para data governance)
- **Fuente:** Sharp Grotesk (Georgia para títulos)
- **Diseño:** Responsivo, moderno, profesional
- **Marca:** Kepler Karst consistente

## 🔄 Mantenimiento

- Actualizar el prompt según nuevas regulaciones
- Ajustar categorías según tendencias emergentes
- Revisar fuentes prioritarias periódicamente
- Actualizar el convertidor para nuevas funcionalidades

---

**Desarrollado para Kepler Karst Law Firm**  
*Suite completa para Gobernanza de Datos Empresarial*
