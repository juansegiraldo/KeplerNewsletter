# 🔧 Client Review Workflow for Kepler Karst Newsletters

Este flujo de trabajo permite que tu cliente revise y edite el contenido de los boletines antes de la publicación final.

## 📋 Resumen del Flujo de Trabajo

### Flujo Actual (Sin Revisión del Cliente)
```
Agentes → JSON → HTML → Publicación
```

### Nuevo Flujo (Con Revisión del Cliente)
```
Agentes → JSON → Borrador Editable → Revisión del Cliente → HTML Final → Publicación
```

## 🚀 Uso Rápido

### Opción 1: Usando PowerShell (Recomendado)
```powershell
# 1. Generar borrador editable
.\client_review.ps1 generate -InputFile "data/art-law/arte_derecho_report_2025_08_20_all_merged.json"

# 2. Lanzar interfaz de revisión del cliente
.\client_review.ps1 review -DraftFile "drafts/arte_derecho_report_2025_08_20_all_merged_draft.md"

# 3. Generar HTML final con cambios del cliente
.\client_review.ps1 publish -DraftFile "drafts/arte_derecho_report_2025_08_20_all_merged_draft.md" -OutputDir "docs/art-law/issues/"
```

### Opción 2: Usando Python directamente
```bash
# 1. Generar borrador editable
python scripts/client_review_workflow.py --stage 1 --input data/art-law/arte_derecho_report_2025_08_20_all_merged.json

# 2. Lanzar interfaz de revisión del cliente
python scripts/client_review_workflow.py --stage 2 --draft drafts/arte_derecho_report_2025_08_20_all_merged_draft.md

# 3. Generar HTML final con cambios del cliente
python scripts/client_review_workflow.py --stage 3 --draft drafts/arte_derecho_report_2025_08_20_all_merged_draft.md --output docs/art-law/issues/
```

## 📁 Estructura de Archivos

```
PromptRodrigo/
├── data/                          # Datos JSON originales de los agentes
├── drafts/                        # Borradores editables (nuevo)
│   ├── *_draft.md                # Archivos de revisión del cliente
│   └── client_interface.html     # Interfaz web para edición
├── docs/                          # HTML final para publicación
├── scripts/
│   ├── client_review_workflow.py  # Script principal del flujo
│   └── converters/               # Convertidores existentes
└── client_review.ps1             # Script PowerShell para facilitar uso
```

## 🔄 Etapas del Flujo de Trabajo

### Etapa 1: Generación de Borrador Editable
- **Entrada**: Archivo JSON generado por agentes
- **Proceso**: Convierte JSON a formato Markdown editable
- **Salida**: Archivo `.md` con marcadores de edición
- **Ubicación**: `drafts/`

**Características del borrador:**
- Formato Markdown legible
- Marcadores `<!-- EDITABLE START -->` y `<!-- EDITABLE END -->`
- Instrucciones claras para el cliente
- Preserva toda la estructura original

### Etapa 2: Revisión del Cliente
- **Entrada**: Archivo de borrador `.md`
- **Proceso**: Interfaz web para edición
- **Salida**: Archivo `.md` actualizado con cambios del cliente
- **Interfaz**: Navegador web en `http://localhost:8080`

**Características de la interfaz:**
- Editor de texto en línea
- Guardado automático
- Vista previa del contenido
- Descarga del archivo editado
- Interfaz intuitiva y responsive

### Etapa 3: Generación Final
- **Entrada**: Archivo `.md` con cambios del cliente
- **Proceso**: Aplica cambios y genera HTML final
- **Salida**: Archivo HTML listo para publicación
- **Ubicación**: `docs/[categoria]/issues/`

## 📝 Instrucciones Detalladas

### Para el Equipo de Desarrollo

#### 1. Preparar el Borrador
```powershell
# Generar borrador desde JSON existente
.\client_review.ps1 generate -InputFile "data/art-law/arte_derecho_report_2025_08_20_all_merged.json"
```

#### 2. Enviar al Cliente
- El archivo generado estará en `drafts/arte_derecho_report_2025_08_20_all_merged_draft.md`
- Enviar este archivo al cliente para revisión
- El cliente puede editar directamente en el archivo o usar la interfaz web

#### 3. Recibir Cambios del Cliente
- El cliente devuelve el archivo `.md` editado
- Colocar el archivo actualizado en `drafts/`

#### 4. Generar HTML Final
```powershell
# Generar HTML final con cambios del cliente
.\client_review.ps1 publish -DraftFile "drafts/arte_derecho_report_2025_08_20_all_merged_draft.md" -OutputDir "docs/art-law/issues/"
```

### Para el Cliente

#### Opción A: Edición Directa del Archivo
1. Abrir el archivo `.md` en cualquier editor de texto
2. Buscar las secciones marcadas con `<!-- EDITABLE START -->` y `<!-- EDITABLE END -->`
3. Hacer los cambios necesarios
4. Guardar el archivo
5. Devolver el archivo actualizado

#### Opción B: Interfaz Web (Recomendado)
1. Ejecutar el comando de revisión
2. Se abrirá automáticamente el navegador
3. Editar el contenido en la interfaz web
4. Hacer clic en "Save Changes" para guardar
5. Hacer clic en "Download File" para descargar el archivo actualizado

## 🎯 Ventajas del Nuevo Flujo

### Para el Equipo de Desarrollo
- ✅ Control total sobre el proceso de revisión
- ✅ Trazabilidad de cambios del cliente
- ✅ Integración con el flujo existente
- ✅ Automatización del proceso final

### Para el Cliente
- ✅ Interfaz simple y intuitiva
- ✅ Posibilidad de edición directa o web
- ✅ Vista previa del contenido
- ✅ Control total sobre el contenido final

### Para el Proyecto
- ✅ Calidad mejorada del contenido
- ✅ Proceso de revisión estructurado
- ✅ Versionado de cambios
- ✅ Flexibilidad en el formato de edición

## 🔧 Configuración y Personalización

### Personalizar Marcadores de Edición
En `scripts/client_review_workflow.py`, puedes modificar los marcadores:
```python
EDITABLE_START = "<!-- EDITABLE START -->"
EDITABLE_END = "<!-- EDITABLE END -->"
```

### Personalizar Interfaz Web
El archivo `client_interface.html` se genera dinámicamente. Puedes modificar:
- Estilos CSS
- Funcionalidades JavaScript
- Texto de instrucciones
- Botones y acciones

### Agregar Validaciones
Puedes agregar validaciones en la función `_apply_client_changes()` para:
- Verificar formato de fechas
- Validar URLs
- Comprobar longitud de contenido
- Validar estructura de datos

## 🚨 Solución de Problemas

### Error: "Python not found"
```powershell
# Instalar Python desde python.org
# O usar winget en Windows
winget install Python.Python.3.11
```

### Error: "Port 8080 already in use"
```powershell
# Cambiar puerto en el script o liberar el puerto
netstat -ano | findstr :8080
taskkill /PID [PID] /F
```

### Error: "Draft file not found"
- Verificar que el archivo existe en `drafts/`
- Verificar la ruta del archivo
- Asegurar que se ejecutó la Etapa 1 primero

### Error: "Output directory not found"
- El script creará automáticamente el directorio
- Verificar permisos de escritura
- Asegurar que la ruta es válida

## 📞 Soporte

Para problemas o preguntas sobre el flujo de trabajo:
1. Revisar este documento
2. Verificar los logs de error
3. Contactar al equipo de desarrollo

## 🔄 Próximas Mejoras

- [ ] Interfaz de revisión más avanzada con resaltado de sintaxis
- [ ] Sistema de versionado automático
- [ ] Integración con control de versiones (Git)
- [ ] Validación automática de cambios
- [ ] Plantillas personalizables por tipo de contenido
- [ ] Sistema de comentarios y anotaciones
- [ ] Exportación a múltiples formatos (PDF, Word, etc.)

