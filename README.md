# Kepler Karst Newsletters

A GitHub Pages repository for publishing two separate newsletters: **Sovereign Debt Weekly** and **Arte y Derecho**.

## 📁 Repository Structure

```
docs/                          # GitHub Pages static site
├── index.html                 # Main homepage
├── sovereign-debt/
│   ├── index.html            # Sovereign Debt landing page
│   ├── issues/               # HTML newsletter files
│   └── assets/
│       ├── headers/          # Header images
│       └── fonts/            # Font files
└── art-law/
    ├── index.html            # Art Law landing page
    ├── issues/               # HTML newsletter files
    └── assets/
        ├── headers/          # Header images
        └── fonts/            # Font files

data/                         # JSON source files (not public)
├── sovereign-debt/           # Sovereign debt JSON files
└── art-law/                  # Art law JSON files

scripts/
├── converters/               # JSON to HTML converters
└── build_index.py           # Dynamic index builder

prompts/                      # Newsletter prompts (not public)
├── sovereign-debt/           # Sovereign debt prompts
└── art-law/                  # Art law prompts
```

## 🚀 Quick Start

### 1. Add New Newsletter Issues

1. **Generate JSON** using your prompts
2. **Convert to HTML** using the converters:
   ```powershell
   # For Sovereign Debt
   python scripts/converters/json_to_html_converter_v2.py data/sovereign-debt/your_file.json
   
   # For Art Law
   python scripts/converters/json_to_html_converter_artlaw.py data/art-law/your_file.json
   ```
3. **Move HTML files** to the appropriate `docs/[newsletter]/issues/` folder
4. **Rebuild indexes** to update the landing pages:
   ```powershell
   .\build.ps1
   ```

### 2. Automatic Index Updates

The `build.ps1` script automatically:
- Scans all HTML files in the `issues/` folders
- Extracts titles and dates from the files
- Generates updated `index.html` files for both newsletters
- Shows statistics of published issues

### 3. GitHub Pages Deployment

1. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add new newsletter issue"
   git push
   ```

2. **GitHub Pages** will automatically deploy from the `docs/` folder

## 📝 Workflow

### Adding a New Issue

1. **Create JSON** using your prompt
2. **Convert to HTML** using the appropriate converter
3. **Move files** to the correct `issues/` folder
4. **Run build script** to update indexes:
   ```powershell
   .\build.ps1
   ```
5. **Commit and push** to GitHub

### File Naming Convention

- **Sovereign Debt**: `DDMMYYYY.html` (e.g., `05082025.html`)
- **Art Law**: Descriptive names (e.g., `arte_derecho_politica_cultural.html`)
- **Analytics**: Add `_meta.html` suffix (e.g., `05082025_meta.html`)

## 🔧 Scripts

### `build.ps1`
Main build script that:
- Rebuilds dynamic indexes
- Shows repository statistics
- Validates structure

### `scripts/build_index.py`
Python script that:
- Scans `issues/` folders for HTML files
- Extracts metadata (title, date)
- Generates updated `index.html` files
- Sorts issues by date (newest first)

### Converters
- `scripts/converters/json_to_html_converter_v2.py` - Sovereign Debt
- `scripts/converters/json_to_html_converter_artlaw.py` - Art Law

## 🌐 Website Structure

- **Main Site**: `https://[username].github.io/[repo-name]/`
- **Sovereign Debt**: `https://[username].github.io/[repo-name]/sovereign-debt/`
- **Art Law**: `https://[username].github.io/[repo-name]/art-law/`

## 📊 Current Statistics

- **Sovereign Debt**: 6 issues published
- **Art Law**: 2 issues published

## 🎯 Benefits of This Structure

1. **Separation of Concerns**: Each newsletter has its own space
2. **Dynamic Indexes**: Automatically updates when new issues are added
3. **GitHub Pages Ready**: Optimized for static site hosting
4. **Maintainable**: Clear organization and automated workflows
5. **Scalable**: Easy to add more newsletters in the future

## 🔄 Maintenance

- **Regular builds**: Run `.\build.ps1` after adding new issues
- **Asset management**: Keep images and fonts in `assets/` folders
- **Prompt versioning**: Store prompts in `prompts/` with version numbers
- **JSON backups**: Keep source JSON files in `data/` folders

---

**Generated in partnership by**: Rodrigo Olivares, Laura Villarraga and Juan Giraldo 