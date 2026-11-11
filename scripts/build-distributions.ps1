# PowerShell wrapper for automated distribution build pipeline
$scriptPath = Join-Path $PSScriptRoot "build-distributions.py"
python $scriptPath
if ($LASTEXITCODE -ne 0) {
    Write-Host "Build failed with exit code $LASTEXITCODE" -ForegroundColor Red
    exit $LASTEXITCODE
}

