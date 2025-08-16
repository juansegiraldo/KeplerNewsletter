# Build script for Kepler Karst Newsletters
# Automatically rebuilds indexes and performs maintenance tasks

Write-Host "🔧 Kepler Karst Newsletter Builder" -ForegroundColor Green
Write-Host "=================================" -ForegroundColor Green

# Check if Python is available
try {
    python --version | Out-Null
    Write-Host "✅ Python found" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found. Please install Python and try again." -ForegroundColor Red
    exit 1
}

# Rebuild dynamic indexes
Write-Host "`n📝 Rebuilding dynamic indexes..." -ForegroundColor Yellow
python scripts/build_index.py

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Indexes rebuilt successfully!" -ForegroundColor Green
} else {
    Write-Host "❌ Failed to rebuild indexes" -ForegroundColor Red
    exit 1
}

# Show current structure
Write-Host "`n📁 Current structure:" -ForegroundColor Yellow
Write-Host "docs/" -ForegroundColor Cyan
Write-Host "├── index.html (main homepage)" -ForegroundColor White
Write-Host "├── sovereign-debt/" -ForegroundColor White
Write-Host "│   ├── index.html (landing page)" -ForegroundColor White
Write-Host "│   └── issues/ (HTML files)" -ForegroundColor White
Write-Host "└── art-law/" -ForegroundColor White
Write-Host "    ├── index.html (landing page)" -ForegroundColor White
Write-Host "    └── issues/ (HTML files)" -ForegroundColor White

# Count files
$sovereignIssues = (Get-ChildItem "docs/sovereign-debt/issues/*.html" -ErrorAction SilentlyContinue).Count
$artLawIssues = (Get-ChildItem "docs/art-law/issues/*.html" -ErrorAction SilentlyContinue).Count

Write-Host "`n📊 Statistics:" -ForegroundColor Yellow
Write-Host "Sovereign Debt issues: $sovereignIssues" -ForegroundColor White
Write-Host "Art Law issues: $artLawIssues" -ForegroundColor White

Write-Host "`n🎉 Build completed successfully!" -ForegroundColor Green
Write-Host "You can now commit and push to GitHub Pages." -ForegroundColor Cyan
