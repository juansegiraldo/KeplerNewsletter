# Weekly Sovereign Debt Digest - Prompt v2

## 🎯 **Objetivo**

Crear una **versión mejorada** del prompt que genere **datos estructurados en JSON** en lugar de HTML directo, resolviendo los problemas de edición y enlaces rotos del formato original.

## 🔄 **Cambios Principales**

### **Antes (v1): HTML Directo**
```html
<article class="item">
    <h3><a href="https://broken-link.com">Headline</a></h3>
    <div class="content">Content mixed with presentation...</div>
</article>
```

### **Ahora (v2): JSON Estructurado**
```json
{
  "items": [
    {
      "title": "Headline",
      "url": "https://valid-link.com",
      "content": "Clean content without presentation",
      "score": 85,
      "country": "Zambia",
      "date": "20-01-2025"
    }
  ]
}
```

## ✅ **Ventajas del Nuevo Formato**

### 1. **Fácil Edición**
- ✅ Modificar contenido sin tocar código de presentación
- ✅ Cambiar URLs sin romper la estructura
- ✅ Editar metadatos de forma independiente
- ✅ Agregar/quitar campos sin afectar el diseño

### 2. **URLs Válidas**
- ✅ URLs almacenadas como texto plano
- ✅ Fácil validación con herramientas automáticas
- ✅ Corrección de enlaces rotos sin afectar HTML
- ✅ Verificación de accesibilidad de enlaces

### 3. **Datos Estructurados**
- ✅ Separación clara entre contenido y presentación
- ✅ Metadatos organizados (país, fecha, fuente, puntuación)
- ✅ Estadísticas agregadas para transparencia
- ✅ Lista de elementos descartados con razones

### 4. **Múltiples Formatos de Salida**
- ✅ Convertir a HTML con plantillas
- ✅ Generar Markdown para documentación
- ✅ Crear CSV para análisis
- ✅ Construir APIs para aplicaciones web
- ✅ Generar PDFs para distribución

### 5. **Control de Versiones**
- ✅ JSON es más fácil de diff y merge
- ✅ Cambios claros en cada commit
- ✅ Historial de modificaciones legible
- ✅ Comparación de versiones simplificada

### 6. **Listo para APIs**
- ✅ Consumible por otras aplicaciones
- ✅ Estructura consistente y predecible
- ✅ Validación con esquemas JSON
- ✅ Integración con sistemas existentes

## 🛠️ **Herramientas Incluidas**

### **Conversor JSON a HTML**
```powershell
python json_to_html_converter.py weekly_digest.json
```

### **Ejemplo de Uso**
```powershell
# 1. Generar JSON con el prompt v2
# 2. Validar URLs
# 3. Convertir a HTML
python json_to_html_converter.py example_weekly_digest.json
```

## 📊 **Estructura del JSON**

```json
{
  "metadata": {
    "title": "Sovereign Debt Weekly — [PERIODO]",
    "subtitle": "#BRAVE ADVOCACY",
    "period": {"start": "DD-MM-YYYY", "end": "DD-MM-YYYY"},
    "generated_at": "TIMESTAMP",
    "version": "2.0",
    "brand": "Kepler Karst"
  },
  "tldr": {
    "summary": "Resumen semanal en un párrafo"
  },
  "items": [
    {
      "id": 1,
      "title": "Título del artículo",
      "url": "https://link.to/article",
      "country": "País",
      "date": "DD-MM-YYYY",
      "source": "Fuente",
      "score": 85,
      "content": "Contenido del artículo (100-140 palabras)",
      "keywords": ["keyword1", "keyword2"],
      "category": "restructuring|IMF|rating|innovation|analysis"
    }
  ],
  "statistics": {
    "sources_scanned": 45,
    "articles_shortlisted": 67,
    "articles_published": 15,
    "duplicates_removed": 23,
    "average_score": 78.5
  },
  "discarded_items": [
    {
      "title": "Título descartado",
      "url": "https://link.to/discarded",
      "score": 45,
      "reason": "Below threshold",
      "source": "Fuente",
      "date": "DD-MM-YYYY"
    }
  ],
  "processing_notes": {
    "topics_covered": ["tema1", "tema2"],
    "geographic_focus": ["región1", "región2"],
    "key_developments": ["desarrollo1", "desarrollo2"],
    "next_week_watch": ["evento1", "evento2"]
  }
}
```

## 🔧 **Flujo de Trabajo Recomendado**

1. **Generar JSON** usando el prompt v2
2. **Validar URLs** con herramientas automáticas
3. **Revisar contenido** y editar si es necesario
4. **Convertir a HTML** usando el conversor
5. **Personalizar diseño** si es necesario
6. **Publicar** en el formato deseado

## 📈 **Beneficios Adicionales**

- **Automatización**: Procesamiento programático del contenido
- **Escalabilidad**: Fácil agregar nuevos campos o formatos
- **Mantenimiento**: Actualizaciones sin afectar la presentación
- **Colaboración**: Múltiples personas pueden trabajar en el contenido
- **Análisis**: Datos estructurados para análisis y reportes
- **Integración**: Conectable con sistemas CRM, CMS, etc.

## 🎨 **Personalización**

El JSON permite fácil personalización:

- **Temas**: Cambiar colores y fuentes sin tocar contenido
- **Layouts**: Diferentes diseños para diferentes usos
- **Formatos**: HTML, PDF, email, social media
- **Idiomas**: Traducción sin afectar estructura

## 🚀 **Próximos Pasos**

1. Probar el prompt v2 con datos reales
2. Validar URLs automáticamente
3. Crear plantillas HTML adicionales
4. Desarrollar herramientas de análisis
5. Integrar con sistemas de publicación

---

**El formato JSON resuelve los problemas principales del HTML directo: edición difícil, enlaces rotos y falta de flexibilidad. Ahora tienes contenido estructurado que es fácil de mantener, validar y convertir a cualquier formato necesario.** 