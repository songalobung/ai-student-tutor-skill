import os

base_dir = 'repo_temp'
dist_packs = os.path.join(base_dir, 'dist', 'packs')

def read_source(rel_path):
    p = os.path.join(base_dir, rel_path)
    if not os.path.exists(p):
        raise FileNotFoundError(f"Missing source file: {p}")
    with open(p, 'r', encoding='utf-8') as f:
        return f.read().strip()

def build_pack(dest_rel_path, title, description, sources):
    out_path = os.path.join(dist_packs, dest_rel_path)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    
    parts = []
    parts.append(f"# {title}")
    parts.append(f"**Pack Module**: `{dest_rel_path}`")
    parts.append(f"**Description**: {description}")
    parts.append(f"**Included Sources**: {', '.join(s[0] for s in sources)}")
    parts.append("\n---\n")
    
    for label, src_path in sources:
        content = read_source(src_path)
        parts.append(f"## Module: {label}")
        parts.append(f"*Source: `{src_path}`*\n")
        parts.append(content)
        parts.append("\n---\n")
        
    full_content = "\n\n".join(parts)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(full_content.strip() + "\n")
        
    size = os.path.getsize(out_path)
    tokens = int(size / 4)
    print(f"Built {dest_rel_path}: {size:,} bytes ({size/1024:.1f} KB), approx {tokens:,} tokens")
    return {
        'path': dest_rel_path,
        'title': title,
        'description': description,
        'size': size,
        'tokens': tokens,
        'sources_count': len(sources)
    }

print("Building Modular Knowledge Packs...")

pack_manifest = []

# --- 1. SUBJECTS ---
pack_manifest.append(build_pack(
    os.path.join('subjects', 'stem-sciences.md'),
    "STEM Sciences Subject Knowledge Pack",
    "Comprehensive pedagogical engines for Mathematics, Physics, Chemistry, Biology, Computer Science, and Statistics.",
    [
        ("Mathematics", "subjects/mathematics/engine.md"),
        ("Physics", "subjects/physics/engine.md"),
        ("Chemistry", "subjects/chemistry/engine.md"),
        ("Biology", "subjects/biology/engine.md"),
        ("Computer Science", "subjects/computer-science/engine.md"),
        ("Statistics", "subjects/statistics/engine.md")
    ]
))

pack_manifest.append(build_pack(
    os.path.join('subjects', 'humanities-social-sciences.md'),
    "Humanities & Social Sciences Subject Knowledge Pack",
    "Comprehensive pedagogical engines for History, Geography, Economics, Business Studies, English Language & Literature, Philosophy, Psychology, Sociology, and Linguistics.",
    [
        ("History", "subjects/history/engine.md"),
        ("Geography", "subjects/geography/engine.md"),
        ("Economics", "subjects/economics/engine.md"),
        ("Business Studies", "subjects/business-studies/engine.md"),
        ("English", "subjects/english/engine.md"),
        ("Philosophy", "subjects/philosophy/engine.md"),
        ("Psychology", "subjects/psychology/engine.md"),
        ("Sociology", "subjects/sociology/engine.md"),
        ("Linguistics", "subjects/linguistics/engine.md")
    ]
))

pack_manifest.append(build_pack(
    os.path.join('subjects', 'professional-applied.md'),
    "Professional & Applied Sciences Subject Knowledge Pack",
    "Comprehensive pedagogical engines for Engineering, Law, Medicine & Health Sciences, Accounting, and Environmental Science.",
    [
        ("Engineering", "subjects/engineering/engine.md"),
        ("Law", "subjects/law/engine.md"),
        ("Medicine & Health", "subjects/medicine-health/engine.md"),
        ("Accounting", "subjects/accounting/engine.md"),
        ("Environmental Science", "subjects/environmental-science/engine.md")
    ]
))

# --- 2. CURRICULA ---
pack_manifest.append(build_pack(
    os.path.join('curricula', 'uk-and-british.md'),
    "UK & British Examination Frameworks Knowledge Pack",
    "Syllabi, assessment objectives, grade boundaries, and command words for GCSE, GCE A-Level, Cambridge IGCSE, Cambridge International A-Level, and Scotland SQA Highers.",
    [
        ("GCSE Framework", "curricula/gcse/guide.md"),
        ("GCE A-Level Framework", "curricula/a-level/guide.md"),
        ("Cambridge IGCSE", "curricula/cambridge-igcse/guide.md"),
        ("Cambridge International A-Level", "curricula/cambridge-a-level/guide.md"),
        ("Scotland SQA Highers", "curricula/scotland-sqa-highers/guide.md")
    ]
))

pack_manifest.append(build_pack(
    os.path.join('curricula', 'north-america.md'),
    "North American Curricula & Testing Knowledge Pack",
    "Curriculum requirements, course frameworks, and assessment structures for US Advanced Placement (AP), SAT & ACT College Entrance Exams, and Canada Ontario OSSD.",
    [
        ("Advanced Placement (AP)", "curricula/ap/guide.md"),
        ("SAT & ACT Examinations", "curricula/sat-act/guide.md"),
        ("Canada Ontario OSSD", "curricula/canada-ontario-ossd/guide.md")
    ]
))

pack_manifest.append(build_pack(
    os.path.join('curricula', 'international-baccalaureate-and-higher-ed.md'),
    "International Baccalaureate & Higher Education Knowledge Pack",
    "Standards, criterion rubrics, and research frameworks for International Baccalaureate (IB DP/MYP/PYP) and University Undergraduate/Postgraduate Studies.",
    [
        ("International Baccalaureate (IB)", "curricula/ib/guide.md"),
        ("University & Higher Education Framework", "curricula/university/guide.md")
    ]
))

pack_manifest.append(build_pack(
    os.path.join('curricula', 'asia-pacific.md'),
    "Asia-Pacific National Curricula Knowledge Pack",
    "Syllabi, grading standards, and exam patterns for India CBSE, Singapore GCE A-Level, China Gaokao, Japan Common Test, Australia VCE/HSC, and New Zealand NCEA.",
    [
        ("India CBSE", "curricula/cbse/guide.md"),
        ("Singapore GCE A-Level", "curricula/singapore-gce-al/guide.md"),
        ("China National Gaokao", "curricula/china-gaokao/guide.md"),
        ("Japan University Common Test", "curricula/japan-common-test/guide.md"),
        ("Australia VCE & HSC", "curricula/australia-vce-hsc/guide.md"),
        ("New Zealand NCEA", "curricula/new-zealand-ncea/guide.md")
    ]
))

pack_manifest.append(build_pack(
    os.path.join('curricula', 'africa-caribbean-latin.md'),
    "Africa, Caribbean & Latin America Curricula Knowledge Pack",
    "National syllabus standards and exam formats for Kenya CBC, Uganda UNEB, South Sudan National, WAEC/WASSCE West Africa, South Africa CAPS/IEB, Caribbean CXC CSEC/CAPE, and Brazil ENEM.",
    [
        ("Kenya Competency-Based Curriculum (CBC)", "curricula/kenya-cbc/guide.md"),
        ("Uganda National Examinations Board (UNEB)", "curricula/uganda/guide.md"),
        ("South Sudan Secondary Certificate", "curricula/south-sudan/guide.md"),
        ("West African Examinations Council (WAEC/WASSCE)", "curricula/waec-wassce/guide.md"),
        ("South Africa CAPS & IEB", "curricula/south-africa-caps-iebe/guide.md"),
        ("Caribbean CXC CSEC & CAPE", "curricula/caribbean-csec-cape/guide.md"),
        ("Brazil National ENEM", "curricula/brazil-enem/guide.md")
    ]
))

pack_manifest.append(build_pack(
    os.path.join('curricula', 'europe-and-admissions.md'),
    "European National Curricula & Graduate Admissions Knowledge Pack",
    "Frameworks for French Baccalauréat, German Abitur, Ireland Leaving Certificate, and Graduate/Professional Admissions Tests (MCAT, USMLE, LSAT, GRE, GMAT, IELTS, TOEFL).",
    [
        ("French Baccalauréat", "curricula/french-baccalaureat/guide.md"),
        ("German Abitur", "curricula/german-abitur/guide.md"),
        ("Ireland Leaving Certificate", "curricula/ireland-leaving-cert/guide.md"),
        ("MCAT & USMLE Medical Admissions", "curricula/mcat-usmle/guide.md"),
        ("LSAT Law School Admissions", "curricula/lsat/guide.md"),
        ("GRE & GMAT Graduate Admissions", "curricula/gre-gmat/guide.md"),
        ("IELTS & TOEFL Language Proficiency", "curricula/ielts-toefl/guide.md")
    ]
))

# --- 3. PEDAGOGY ---
pack_manifest.append(build_pack(
    os.path.join('pedagogy', 'learning-science-and-pedagogy.md'),
    "Learning Science & Core Pedagogy Knowledge Pack",
    "Comprehensive guides for formative assessment, retrieval practice, spaced repetition schedules, Bloom's mastery learning, scaffolding hierarchies, faded worked examples, and metacognitive self-regulation.",
    [
        ("Formative Assessment", "pedagogy/formative-assessment.md"),
        ("Retrieval Practice", "pedagogy/retrieval-practice.md"),
        ("Spaced Repetition", "pedagogy/spaced-repetition.md"),
        ("Mastery Learning", "pedagogy/mastery-learning.md"),
        ("Scaffolding & Fading", "pedagogy/scaffolding.md"),
        ("Worked Examples & Cognitive Load", "pedagogy/worked-examples.md"),
        ("Metacognitive Regulation", "pedagogy/metacognition.md")
    ]
))

pack_manifest.append(build_pack(
    os.path.join('pedagogy', 'student-intelligence-and-prerequisites.md'),
    "Student Intelligence, Profiling & Prerequisite Graphs Knowledge Pack",
    "Student state modeling (dual-axis mastery and confidence), misconception profiling, prerequisite dependency graph tracing, and stakeholder dashboards.",
    [
        ("Student State Model", "intelligence/student-state-model.md"),
        ("Misconception Profiling", "intelligence/misconception-profiling.md"),
        ("Prerequisite Dependency Graph", "prerequisites/dependency-graph.md"),
        ("Stakeholder Reporting Dashboards", "dashboards/stakeholder-reporting.md")
    ]
))

# --- 4. EXAMINATION ---
pack_manifest.append(build_pack(
    os.path.join('examination', 'exam-intelligence-and-analytics.md'),
    "Examination Intelligence, Analytics & Question Laboratory Knowledge Pack",
    "Exam pattern reverse engineering, command word taxonomy, mark distribution analytics, timed exam simulation, oral viva voce examination, question laboratory distractor design, and universal marking rubrics.",
    [
        ("Exam Analytics & Patterns", "examination-intelligence/exam-analytics.md"),
        ("Examination Mode Simulation", "modes/examination.md"),
        ("Oral Viva Voce Examination", "modes/oral-examination.md"),
        ("AI Question Generation Laboratory", "question-laboratory/generator-engine.md"),
        ("Marking Rubrics & Taxonomy", "assessments/marking-rubrics.md")
    ]
))

# --- 5. VOICE & MULTIMODAL ---
pack_manifest.append(build_pack(
    os.path.join('voice-and-multimodal', 'voice-and-multimodal.md'),
    "Voice, Vision & Multimodal Tutoring Knowledge Pack",
    "Speech-to-speech cadence, audio pauses, mathematical formula verbalization, visual learning diagram standards (ASCII, Mermaid, SVG), and multilingual scaffolding.",
    [
        ("Multimodal & Voice Protocols", "references/multimodal-protocols.md"),
        ("Visual Learning Engine", "engines/visual-learning-engine.md"),
        ("Multilingual Scaffolding", "multilingual/language-support.md")
    ]
))

# --- BUILD INDEX.md ---
index_path = os.path.join(dist_packs, 'INDEX.md')
index_lines = [
    "# AI Student Tutor: Optional Knowledge Packs Index",
    "**Version**: 2.0.0-Portable",
    "**Architecture**: Modular Extension System for Custom GPTs, Claude Projects, Gemini Gems, and Local Models\n",
    "This directory contains self-contained, modular knowledge packs designed to accompany `dist/portable/AI-STUDENT-TUTOR.md`.",
    "Users and educators only need to upload the specific packs relevant to their subject, curriculum, or instructional focus.\n",
    "## Knowledge Pack Directory & Size Matrix\n",
    "| Pack Category | Pack File | Size (KB) | Approx. Tokens | Primary Educational Scope |",
    "| :--- | :--- | :---: | :---: | :--- |"
]

for item in pack_manifest:
    category = item['path'].split(os.sep)[0]
    fname = os.path.basename(item['path'])
    index_lines.append(f"| `{category}/` | [{fname}](./{item['path'].replace(os.sep, '/')}) | {item['size']/1024:.1f} KB | ~{item['tokens']:,} | {item['description']} |")

index_lines.append("\n---\n")
index_lines.append("## How to Use Knowledge Packs\n")
index_lines.append("1. **Core Only**: For everyday Socratic tutoring across common topics, `AI-STUDENT-TUTOR.md` is fully self-contained.")
index_lines.append("2. **Add Your Subject**: If you are teaching advanced STEM, upload `subjects/stem-sciences.md`. For essays and humanities, upload `subjects/humanities-social-sciences.md`.")
index_lines.append("3. **Add Your Curriculum**: Select the single curriculum pack matching your student's examination board (e.g., `curricula/uk-and-british.md` for GCSE/A-Levels, or `curricula/north-america.md` for AP/SAT).")
index_lines.append("4. **For Exam Preparation**: Add `examination/exam-intelligence-and-analytics.md` to unlock past-paper analysis, command word rubrics, and mock exam simulations.")
index_lines.append("5. **For Voice / Audio Apps**: Add `voice-and-multimodal/voice-and-multimodal.md` for speech-to-speech turn-taking and spoken math verbalization.\n")

with open(index_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(index_lines) + "\n")

print(f"Generated {index_path} successfully.")
