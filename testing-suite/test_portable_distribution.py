#!/usr/bin/env python3
"""
Automated Quality Assurance & Feature Parity Regression Suite
Validates portable core self-containment, platform distributions,
zip integrity, and pedagogical regression scenarios.
"""

import os
import sys
import re
import json
import zipfile

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DIST_DIR = os.path.join(BASE_DIR, 'dist')

def test_portable_core():
    print("\n[QA Test 1] Testing Portable Core Self-Containment...")
    core_path = os.path.join(DIST_DIR, 'portable', 'AI-STUDENT-TUTOR.md')
    assert os.path.exists(core_path), "AI-STUDENT-TUTOR.md does not exist"
    
    with open(core_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Check token size
    token_est = int(len(text) / 4)
    print(f"  - Token estimate: {token_est:,} tokens (Limit: 30,000)")
    assert token_est < 30000, f"Core exceeds 30,000 tokens: {token_est}"

    # Check for broken relative local markdown links (e.g. [text](../file.md))
    broken_links = re.findall(r'\[([^\]]+)\]\((?!http|#)([^\)]+\.md[^\)]*)\)', text)
    if broken_links:
        raise AssertionError(f"Found relative file links in self-contained core: {broken_links}")
    print("  - Zero relative broken file dependencies found.")

    # Check key sections
    required_sections = [
        "Identity, Mission & Defining Principles",
        "Core Operating Rules & Academic Integrity",
        "Safeguarding, Well-being & Ethical Boundaries",
        "Student State & Adaptive Profiling Engine",
        "Instructional Architecture: The 10-Stage Lesson Anatomy",
        "Attention-Friendly & Neuroinclusive Teaching Engine",
        "Cognitive Diagnosis & Prerequisite Gap Tracing",
        "Formative Assessment & Universal Marking Rubrics",
        "Visual Learning & Multimodal Standards",
        "Universal Subject & Curriculum Adaptation Protocols"
    ]
    for s in required_sections:
        assert s.lower() in text.lower(), f"Missing required section: {s}"
    print(f"  - All {len(required_sections)} required architectural sections present.")
    print("  PASS: Portable Core is verified self-contained.")

def test_packs_integrity():
    print("\n[QA Test 2] Testing Modular Knowledge Packs...")
    index_path = os.path.join(DIST_DIR, 'packs', 'INDEX.md')
    assert os.path.exists(index_path), "dist/packs/INDEX.md missing"
    
    packs_expected = [
        'subjects/stem-sciences.md',
        'subjects/humanities-social-sciences.md',
        'subjects/professional-applied.md',
        'curricula/uk-and-british.md',
        'curricula/north-america.md',
        'curricula/international-baccalaureate-and-higher-ed.md',
        'curricula/asia-pacific.md',
        'curricula/africa-caribbean-latin.md',
        'curricula/europe-and-admissions.md',
        'pedagogy/learning-science-and-pedagogy.md',
        'pedagogy/student-intelligence-and-prerequisites.md',
        'examination/exam-intelligence-and-analytics.md',
        'voice-and-multimodal/voice-and-multimodal.md'
    ]
    for p in packs_expected:
        full_p = os.path.join(DIST_DIR, 'packs', p.replace('/', os.sep))
        assert os.path.exists(full_p), f"Missing expected pack: {p}"
        size = os.path.getsize(full_p)
        assert size > 5000, f"Pack {p} is suspiciously small: {size} bytes"
    print(f"  PASS: All {len(packs_expected)} modular knowledge packs present and non-empty.")

def test_platform_distributions():
    print("\n[QA Test 3] Testing Platform Packages & ZIPs...")
    platforms = ['chatgpt', 'claude', 'gemini', 'manus', 'universal']
    for p in platforms:
        p_dir = os.path.join(DIST_DIR, 'platforms', p)
        assert os.path.exists(p_dir), f"Missing platform dir: {p}"
        readme = os.path.join(p_dir, 'README.md')
        assert os.path.exists(readme), f"Missing README.md in {p}"
        
        # Check ZIP
        zip_path = os.path.join(DIST_DIR, 'zips', f"{p}-distribution.zip")
        assert os.path.exists(zip_path), f"Missing zip: {zip_path}"
        with zipfile.ZipFile(zip_path, 'r') as z:
            names = z.namelist()
            assert len(names) > 0, f"Empty zip: {zip_path}"
        print(f"  - Platform {p:10}: Verified ({len(names)} files in zip, {os.path.getsize(zip_path):,} bytes)")

    all_packs_zip = os.path.join(DIST_DIR, 'zips', 'all-packs.zip')
    assert os.path.exists(all_packs_zip), "all-packs.zip missing"
    print("  PASS: All platform packages and zip archives verified.")

def test_manifest_integrity():
    print("\n[QA Test 4] Testing dist/manifest.json Integrity...")
    manifest_path = os.path.join(DIST_DIR, 'manifest.json')
    assert os.path.exists(manifest_path), "manifest.json missing"
    with open(manifest_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    assert data["version"] == "2.0.0"
    assert "portable_core" in data
    assert "platforms" in data
    assert "packs" in data
    assert "zips" in data
    print("  PASS: dist/manifest.json is valid and complete.")

def test_pedagogical_regression_scenarios():
    print("\n[QA Test 5] Running Pedagogical Capability Regression Checks...")
    core_path = os.path.join(DIST_DIR, 'portable', 'AI-STUDENT-TUTOR.md')
    with open(core_path, 'r', encoding='utf-8') as f:
        core = f.read()

    # Scenario 1: Socratic Questioning & Fence
    print("  - Testing Scenario 1 (Socratic Fence & Isomorphic Twin)...")
    assert "Never solve student homework" in core
    assert "Isomorphic Twin" in core
    assert "Decline the direct solution immediately and warmly" in core or "decline the direct solution" in core.lower()

    # Scenario 2: Cognitive Error Diagnosis
    print("  - Testing Scenario 2 (Cognitive Error Diagnosis Triage)...")
    assert "Slip" in core and "Gap" in core and "Misconception" in core
    assert "Cognitive conflict" in core

    # Scenario 3: Attention-Friendly Formatting & Cognitive Load
    print("  - Testing Scenario 3 (Attention-Friendly 6-Stage Progressive Explanation)...")
    assert "Direct Answer or Core Idea" in core
    assert "Simple Intuitive Explanation" in core
    assert "Step-by-Step Breakdown" in core
    assert "Quick Check-In Question" in core
    assert "180-Word Chunk Limit" in core

    # Scenario 4: Examination Intelligence & Rubrics
    print("  - Testing Scenario 4 (Universal Mark Taxonomy M/A/B/FT)...")
    assert "[M] Method Marks" in core
    assert "[A] Accuracy Marks" in core
    assert "[B] Independent Marks" in core
    assert "[FT] Follow-Through Marks" in core

    print("  PASS: All 4 pedagogical regression scenarios validated.")

def main():
    print("=" * 70)
    print("🧪 RUNNING QUALITY ASSURANCE & FEATURE PARITY REGRESSION TESTS")
    print("=" * 70)
    try:
        test_portable_core()
        test_packs_integrity()
        test_platform_distributions()
        test_manifest_integrity()
        test_pedagogical_regression_scenarios()
        print("\n" + "=" * 70)
        print("✅ ALL QUALITY ASSURANCE & REGRESSION TESTS PASSED.")
        print("=" * 70)
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
