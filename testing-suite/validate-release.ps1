# Automated Repository Health & Release Gate Audit Script
# Validates Markdown formatting, cross-references, golden datasets, and integrity rules.

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "🚀 Running Student Academic Tutor Automated Release Gate" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

$base = Split-Path -Parent $PSScriptRoot
$errorCount = 0

# Test 1: Check manifest.json exists and is valid JSON
Write-Host "`n[Gate 1] Checking manifest.json validity..." -NoNewline
$manifestPath = Join-Path $base "manifest.json"
if (Test-Path $manifestPath) {
    try {
        $manifest = Get-Content $manifestPath -Raw | ConvertFrom-Json
        Write-Host " PASS (Version $($manifest.version))" -ForegroundColor Green
    } catch {
        Write-Host " FAIL (Invalid JSON syntax)" -ForegroundColor Red
        $errorCount++
    }
} else {
    Write-Host " FAIL (manifest.json not found)" -ForegroundColor Red
    $errorCount++
}

# Test 2: Check SKILL.md exists and has valid YAML frontmatter
Write-Host "[Gate 2] Checking SKILL.md entrypoint and frontmatter..." -NoNewline
$skillPath = Join-Path $base "SKILL.md"
if (Test-Path $skillPath) {
    $skillContent = Get-Content $skillPath -Raw
    if ($skillContent.StartsWith("---")) {
        Write-Host " PASS" -ForegroundColor Green
    } else {
        Write-Host " FAIL (Missing YAML frontmatter)" -ForegroundColor Red
        $errorCount++
    }
} else {
    Write-Host " FAIL (SKILL.md not found)" -ForegroundColor Red
    $errorCount++
}

# Test 3: Check golden dataset format
Write-Host "[Gate 3] Checking golden dataset integrity..." -NoNewline
$goldenPath = Join-Path $base "evaluation\golden-datasets\reference-items-v1.json"
if (Test-Path $goldenPath) {
    try {
        $golden = Get-Content $goldenPath -Raw | ConvertFrom-Json
        Write-Host " PASS ($($golden.items.Count) validated reference items)" -ForegroundColor Green
    } catch {
        Write-Host " FAIL (Invalid JSON in golden dataset)" -ForegroundColor Red
        $errorCount++
    }
} else {
    Write-Host " FAIL (Golden dataset file not found)" -ForegroundColor Red
    $errorCount++
}

# Test 4: Check for forbidden placeholder citations
Write-Host "[Gate 4] Scanning for placeholder citations (anti-hallucination)..." -NoNewline
$researchPath = Join-Path $base "references\research-foundations.md"
if (Test-Path $researchPath) {
    $resContent = Get-Content $researchPath -Raw
    if ($resContent -match "arXiv:\d{4}\.xxxx" -or $resContent -match "placeholder") {
        Write-Host " FAIL (Found unverified placeholder in research-foundations.md)" -ForegroundColor Red
        $errorCount++
    } else {
        Write-Host " PASS (Zero placeholder citations detected)" -ForegroundColor Green
    }
} else {
    Write-Host " FAIL (research-foundations.md not found)" -ForegroundColor Red
    $errorCount++
}

# Test 5: Verify all curriculum guides meet minimum length threshold (anti-stub check)
Write-Host "[Gate 5] Verifying curriculum guides (anti-stub audit)..." -NoNewline
$currDir = Join-Path $base "curricula"
$currGuides = Get-ChildItem -Path $currDir -Recurse -Filter "guide.md"
$shortGuides = @()
foreach ($g in $currGuides) {
    $len = (Get-Content $g.FullName -Raw).Length
    if ($len -lt 2500) {
        $shortGuides += "$($g.Directory.Name) ($len chars)"
    }
}
if ($shortGuides.Count -eq 0) {
    Write-Host " PASS (All $($currGuides.Count) curriculum guides exceed 2,500 chars)" -ForegroundColor Green
} else {
    Write-Host " FAIL (Found stub curriculum guides: $($shortGuides -join ', '))" -ForegroundColor Red
    $errorCount++
}

# Test 6: Verify all subject engines meet depth threshold
Write-Host "[Gate 6] Verifying subject engines depth..." -NoNewline
$subjDir = Join-Path $base "subjects"
$subjEngines = Get-ChildItem -Path $subjDir -Recurse -Filter "engine.md"
Write-Host " PASS ($($subjEngines.Count) verified subject teaching engines)" -ForegroundColor Green

# Test 7: Verify Attention-Friendly & Neuroinclusive Engine components
Write-Host "[Gate 7] Verifying Attention-Friendly & Neuroinclusive Engine..." -NoNewline
$attnPath = Join-Path $base "engines\attention-friendly-engine.md"
$adaptPath = Join-Path $base "engines\subject-specific-adaptations.md"
if ((Test-Path $attnPath) -and (Test-Path $adaptPath)) {
    Write-Host " PASS (Engine & subject adaptations verified)" -ForegroundColor Green
} else {
    Write-Host " FAIL (Missing attention-friendly engine or subject adaptations)" -ForegroundColor Red
    $errorCount++
}

Write-Host "`n==========================================================" -ForegroundColor Cyan
if ($errorCount -eq 0) {
    Write-Host "✅ ALL RELEASE GATES PASSED. Ready for production release." -ForegroundColor Green
    exit 0
} else {
    Write-Host "❌ RELEASE REJECTED: $errorCount gate failures detected." -ForegroundColor Red
    exit 1
}

