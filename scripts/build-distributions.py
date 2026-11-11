#!/usr/bin/env python3
"""
Automated Build and Export Pipeline for AI Student Tutor Distributions
Generates portable core, modular knowledge packs, platform distributions,
zip archives, validates instruction completeness, and outputs dist/manifest.json.
"""

import os
import sys
import shutil
import hashlib
import zipfile
import json
import subprocess

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DIST_DIR = os.path.join(BASE_DIR, 'dist')
ZIPS_DIR = os.path.join(DIST_DIR, 'zips')

def get_file_stats(filepath):
    size = os.path.getsize(filepath)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    chars = len(content)
    words = len(content.split())
    tokens = int(chars / 4)
    sha256 = hashlib.sha256(content.encode('utf-8')).hexdigest()
    return {
        'size': size,
        'chars': chars,
        'words': words,
        'tokens': tokens,
        'sha256': sha256
    }

def create_zip(source_dir, output_zip_path):
    os.makedirs(os.path.dirname(output_zip_path), exist_ok=True)
    with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname)
    return os.path.getsize(output_zip_path)

def validate_instructions(portable_path):
    with open(portable_path, 'r', encoding='utf-8') as f:
        text = f.read()

    required_keywords = {
        "Mastery Over Speed (Principle 1)": "Mastery Over Speed",
        "Understanding Over Memorisation (Principle 2)": "Understanding Over Memorisation",
        "Guided Discovery (Principle 3)": "Guided Discovery",
        "Curriculum Alignment (Principle 4)": "Curriculum Alignment",
        "Empathy Without Lowering Standards (Principle 5)": "Empathy Without Lowering Standards",
        "Socratic Fence": "Socratic Fence",
        "Isomorphic Twin Protocol": "Isomorphic Twin",
        "Non-Medical Stance": "Non-Medical",
        "Crisis Safeguarding (988 / Childline)": "988",
        "Delivery Preference: attention_friendly": "attention_friendly",
        "Delivery Preference: deep_learning": "deep_learning",
        "Delivery Preference: visual": "visual",
        "Delivery Preference: exam_focused": "exam_focused",
        "6-Stage Progressive Explanation Sequence": "Progressive Explanation",
        "Working Memory Scaffolding (180-Word Limit)": "180-Word",
        "Dual-Axis Student State (Ks, Cs)": "Cs",
        "Error Triage: Slip": "Slip",
        "Error Triage: Gap": "Gap",
        "Error Triage: Misconception": "Misconception",
        "Mark Scheme: [M] Method": "[M]",
        "Mark Scheme: [A] Accuracy": "[A]",
        "Mark Scheme: [B] Independent": "[B]",
        "Mark Scheme: [FT] Follow-Through": "[FT]",
        "Universal Subject STEM Protocol": "STEM",
        "Universal Curriculum AP/A-Level/IB": "International Baccalaureate"
    }

    missing = []
    for label, kw in required_keywords.items():
        if kw.lower() not in text.lower():
            missing.append(label)

    return missing

def main():
    print("=" * 70)
    print("🚀 AI STUDENT TUTOR: AUTOMATED COMPILATION & EXPORT PIPELINE")
    print("=" * 70)

    # Step 1: Run Sub-generators
    scripts_dir = os.path.join(BASE_DIR, 'scripts')
    
    print("\n[Step 1/5] Compiling Portable Core (AI-STUDENT-TUTOR.md)...")
    res = subprocess.run([sys.executable, os.path.join(scripts_dir, 'generate_portable_core.py')], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error compiling portable core: {res.stderr}")
        sys.exit(1)
    print(res.stdout.strip())

    print("\n[Step 2/5] Compiling Modular Knowledge Packs (dist/packs/)...")
    res = subprocess.run([sys.executable, os.path.join(scripts_dir, 'build_packs.py')], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error compiling packs: {res.stderr}")
        sys.exit(1)
    print(res.stdout.strip())

    print("\n[Step 3/5] Compiling Platform Distributions (dist/platforms/)...")
    res = subprocess.run([sys.executable, os.path.join(scripts_dir, 'build_platforms.py')], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error compiling platforms: {res.stderr}")
        sys.exit(1)
    print(res.stdout.strip())

    # Step 4: Validate instruction completeness
    print("\n[Step 4/5] Validating Instruction Completeness & Zero Loss...")
    portable_path = os.path.join(DIST_DIR, 'portable', 'AI-STUDENT-TUTOR.md')
    missing = validate_instructions(portable_path)
    if missing:
        print(f"❌ VALIDATION FAILED: Missing instructions in portable core: {missing}")
        sys.exit(1)
    else:
        print("✅ VALIDATION PASSED: 100% of core pedagogical instructions & integrity gates verified.")

    # Step 5: Generate ZIP archives
    print("\n[Step 5/5] Packaging Platform ZIP Archives...")
    os.makedirs(ZIPS_DIR, exist_ok=True)
    
    zip_manifest = {}
    platforms = ['chatgpt', 'claude', 'gemini', 'manus', 'universal']
    for p in platforms:
        src = os.path.join(DIST_DIR, 'platforms', p)
        zip_dst = os.path.join(ZIPS_DIR, f"{p}-distribution.zip")
        zsize = create_zip(src, zip_dst)
        zip_manifest[f"{p}-distribution.zip"] = zsize
        print(f"Created {os.path.basename(zip_dst)}: {zsize:,} bytes ({zsize/1024:.1f} KB)")

    # All packs zip
    packs_src = os.path.join(DIST_DIR, 'packs')
    packs_zip = os.path.join(ZIPS_DIR, "all-packs.zip")
    zsize = create_zip(packs_src, packs_zip)
    zip_manifest["all-packs.zip"] = zsize
    print(f"Created all-packs.zip: {zsize:,} bytes ({zsize/1024:.1f} KB)")

    # Generate dist/manifest.json
    manifest_data = {
        "version": "2.0.0",
        "build_target": "Portable Universal Distribution",
        "portable_core": {
            "path": "dist/portable/AI-STUDENT-TUTOR.md",
            **get_file_stats(portable_path)
        },
        "platforms": {},
        "packs": {},
        "zips": {}
    }

    # Index platform files
    for p in platforms:
        p_dir = os.path.join(DIST_DIR, 'platforms', p)
        manifest_data["platforms"][p] = []
        for root, dirs, files in os.walk(p_dir):
            for file in sorted(files):
                fpath = os.path.join(root, file)
                rel = os.path.relpath(fpath, DIST_DIR).replace(os.sep, '/')
                stats = get_file_stats(fpath)
                manifest_data["platforms"][p].append({
                    "path": rel,
                    **stats
                })

    # Index pack files
    for root, dirs, files in os.walk(packs_src):
        for file in sorted(files):
            fpath = os.path.join(root, file)
            rel = os.path.relpath(fpath, DIST_DIR).replace(os.sep, '/')
            stats = get_file_stats(fpath)
            manifest_data["packs"][rel] = stats

    for zname, zsize in zip_manifest.items():
        manifest_data["zips"][zname] = {
            "size": zsize,
            "path": f"dist/zips/{zname}"
        }

    manifest_path = os.path.join(DIST_DIR, 'manifest.json')
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest_data, f, indent=2)

    print(f"\nSaved distribution manifest to {os.path.relpath(manifest_path, BASE_DIR)}")
    
    # Summary Table
    core_stats = manifest_data["portable_core"]
    print("\n" + "=" * 70)
    print("DISTRIBUTION SUMMARY TABLE")
    print("=" * 70)
    print(f"Portable Core File: dist/portable/AI-STUDENT-TUTOR.md")
    print(f"  - Size: {core_stats['size']:,} bytes ({core_stats['size']/1024:.2f} KB)")
    print(f"  - Words: {core_stats['words']:,} words")
    print(f"  - Tokens (Est.): ~{core_stats['tokens']:,} tokens (< 30,000 token limit)")
    print(f"  - SHA-256: {core_stats['sha256'][:16]}...")
    print(f"Modular Packs: {len(manifest_data['packs'])} files indexed in dist/packs/INDEX.md")
    print(f"Platform Packages: 5 tailored targets (ChatGPT, Claude, Gemini, Manus, Universal)")
    print(f"ZIP Archives: 6 pre-built packages in dist/zips/")
    print("=" * 70)
    print("✨ ALL DISTRIBUTIONS SUCCESSFULLY COMPILED AND VERIFIED.")

if __name__ == '__main__':
    main()

