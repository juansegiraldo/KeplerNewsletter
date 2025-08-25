# Client Review Workflow Script for Kepler Karst Newsletters
# This script provides an easy way to manage the client review process

param(
    [Parameter(Mandatory=$true)]
    [ValidateSet("generate", "review", "publish", "help")]
    [string]$Action,
    
    [Parameter(Mandatory=$false)]
    [string]$InputFile,
    
    [Parameter(Mandatory=$false)]
    [string]$DraftFile,
    
    [Parameter(Mandatory=$false)]
    [string]$OutputDir
)

Write-Host "Kepler Karst Client Review Workflow" -ForegroundColor Green
Write-Host "=====================================" -ForegroundColor Green

# Check if Python is available
try {
    python --version | Out-Null
    Write-Host "Python found" -ForegroundColor Green
} catch {
    Write-Host "Python not found. Please install Python and try again." -ForegroundColor Red
    exit 1
}

function Show-Help {
    Write-Host "Client Review Workflow Usage:" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Commands:" -ForegroundColor Cyan
    Write-Host "  generate  - Generate editable draft from JSON file" -ForegroundColor White
    Write-Host "  review    - Launch client review interface" -ForegroundColor White
    Write-Host "  publish   - Generate final HTML with client changes" -ForegroundColor White
    Write-Host "  help      - Show this help message" -ForegroundColor White
    Write-Host ""
    Write-Host "Examples:" -ForegroundColor Cyan
    Write-Host "  .\client_review.ps1 generate -InputFile 'data/art-law/arte_derecho_report_2025_08_20_all_merged.json'" -ForegroundColor White
    Write-Host "  .\client_review.ps1 review -DraftFile 'drafts/arte_derecho_report_2025_08_20_all_merged_draft.md'" -ForegroundColor White
    Write-Host "  .\client_review.ps1 publish -DraftFile 'drafts/arte_derecho_report_2025_08_20_all_merged_draft.md' -OutputDir 'docs/art-law/issues/'" -ForegroundColor White
    Write-Host ""
    Write-Host "Workflow:" -ForegroundColor Cyan
    Write-Host "  1. generate - Creates editable draft from JSON" -ForegroundColor White
    Write-Host "  2. review   - Opens web interface for client editing" -ForegroundColor White
    Write-Host "  3. publish  - Generates final HTML with client changes" -ForegroundColor White
}

function Generate-Draft {
    param([string]$InputFile)
    
    if (-not $InputFile) {
        Write-Host "Input file is required for generate action" -ForegroundColor Red
        Write-Host "Usage: .\client_review.ps1 generate -InputFile 'path/to/file.json'" -ForegroundColor Yellow
        exit 1
    }
    
    if (-not (Test-Path $InputFile)) {
        Write-Host "Input file not found: $InputFile" -ForegroundColor Red
        exit 1
    }
    
    Write-Host "`nGenerating editable draft..." -ForegroundColor Yellow
    python scripts/client_review_workflow.py --stage 1 --input $InputFile
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`nDraft generated successfully!" -ForegroundColor Green
        Write-Host "Next step: Run '.\client_review.ps1 review -DraftFile [draft_file]'" -ForegroundColor Cyan
    } else {
        Write-Host "`nFailed to generate draft" -ForegroundColor Red
        exit 1
    }
}

function Start-Review {
    param([string]$DraftFile)
    
    if (-not $DraftFile) {
        Write-Host "Draft file is required for review action" -ForegroundColor Red
        Write-Host "Usage: .\client_review.ps1 review -DraftFile 'path/to/draft.md'" -ForegroundColor Yellow
        exit 1
    }
    
    if (-not (Test-Path $DraftFile)) {
        Write-Host "Draft file not found: $DraftFile" -ForegroundColor Red
        exit 1
    }
    
    Write-Host "`nLaunching client review interface..." -ForegroundColor Yellow
    Write-Host "The web interface will open in your browser" -ForegroundColor White
    Write-Host "Press Ctrl+C to stop the server when done" -ForegroundColor White
    
    python scripts/client_review_workflow.py --stage 2 --draft $DraftFile
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`nReview session completed!" -ForegroundColor Green
        Write-Host "Next step: Run '.\client_review.ps1 publish -DraftFile [draft_file] -OutputDir [output_dir]'" -ForegroundColor Cyan
    } else {
        Write-Host "`nReview session failed" -ForegroundColor Red
        exit 1
    }
}

function Publish-Final {
    param([string]$DraftFile, [string]$OutputDir)
    
    if (-not $DraftFile -or -not $OutputDir) {
        Write-Host "Both draft file and output directory are required for publish action" -ForegroundColor Red
        Write-Host "Usage: .\client_review.ps1 publish -DraftFile 'path/to/draft.md' -OutputDir 'path/to/output/'" -ForegroundColor Yellow
        exit 1
    }
    
    if (-not (Test-Path $DraftFile)) {
        Write-Host "Draft file not found: $DraftFile" -ForegroundColor Red
        exit 1
    }
    
    # Create output directory if it doesn't exist
    if (-not (Test-Path $OutputDir)) {
        New-Item -ItemType Directory -Path $OutputDir -Force | Out-Null
        Write-Host "Created output directory: $OutputDir" -ForegroundColor Yellow
    }
    
    Write-Host "`nGenerating final HTML..." -ForegroundColor Yellow
    python scripts/client_review_workflow.py --stage 3 --draft $DraftFile --output $OutputDir
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`nFinal HTML generated successfully!" -ForegroundColor Green
        Write-Host "Output location: $OutputDir" -ForegroundColor Cyan
        
        # Show generated files
        $htmlFiles = Get-ChildItem $OutputDir -Filter "*.html" | Where-Object { $_.Name -like "*$(Split-Path $DraftFile -LeafBase)*" }
        if ($htmlFiles) {
            Write-Host "`nGenerated files:" -ForegroundColor Yellow
            foreach ($file in $htmlFiles) {
                Write-Host "  - $($file.Name)" -ForegroundColor White
            }
        }
    } else {
        Write-Host "`nFailed to generate final HTML" -ForegroundColor Red
        exit 1
    }
}

# Main execution
switch ($Action) {
    "help" {
        Show-Help
    }
    "generate" {
        Generate-Draft -InputFile $InputFile
    }
    "review" {
        Start-Review -DraftFile $DraftFile
    }
    "publish" {
        Publish-Final -DraftFile $DraftFile -OutputDir $OutputDir
    }
    default {
        Write-Host "Unknown action: $Action" -ForegroundColor Red
        Show-Help
        exit 1
    }
}

Write-Host "`nClient review workflow completed!" -ForegroundColor Green
