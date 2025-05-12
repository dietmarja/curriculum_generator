# Curriculum Generator (CG)

**Curriculum Generator (CG)** is a Python-based toolkit for the  generation, analysis, and visualization of modular, outcome-based curricula for diverse target groups. 
Designed to accommodate multiple roles and EQF levels (4–8), it supports full programme development as well as granular micro-credential pathways.

## Highlights

- **Role-to-Profile Mapping**: Converts job role definitions into educational profiles with EQF and ESCO alignment
- **Modular Curriculum Generation**: Builds curricula from flexible, ECTS-compliant learning modules
- **Micro-Credential Support**: Generates stackable credentials and visualizes learning pathways
- **Learning Outcomes**: Generates multi-level outcomes aligned with Bloom's taxonomy and Tuning methodology
- **Standards Compliance**: Incorporates EQF, ECTS, ECVET, ESCO, and micro-credential guidelines
- **Assessment Tools**: Evaluate modules, curricula, and micro-credentials for standard compliance
- **Flexible Learning Pathways**: Supports full, upskilling, reskilling, dual, and work-based arrangements
- **Rich Export Options**: Outputs in HTML, JSON, PDF, SCORM, and xAPI formats

---

## Standards Integration

| Standard      | Role in CG                                                                 |
|---------------|----------------------------------------------------------------------------|
| **EQF**       | Levels 4–8 structuring; stacking logic for curricula and credentials       |
| **ECTS**      | Credit weighting and validation of learning modules                        |
| **ECVET**     | Support for modular, transferable work-based learning                      |
| **ESCO**      | Competence-to-role matching; profile enrichment                            |
| **Tuning**    | Structuring of learning outcomes from program to module level              |
| **EU Micro-Credentials** | Recognition, granularity, and stackability of short-form learning units |

---

## Example Commands

### Generate One Curriculum
```bash
python scripts/generate_curriculum.py --role DSL --eqf 7 --output output/curricula/curriculum_DSL_7.html
```

### Generate All Curricula
```bash
python scripts/generate_all_curricula.py --output-dir output/curricula
```

### Create Micro-Credentials
```bash
python scripts/generate_micro_credentials.py --output output/micro_credentials
python scripts/improve_micro_credentials.py --force
```

### Visualize Credential Stacking
```bash
pip install matplotlib networkx
python scripts/visualize_stacking_paths.py
```

### Export Educational Profiles
```bash
python scripts/export_profiles.py --output output/profiles --format both
```

### Standards-Based Assessment
```bash
python scripts/assess_modules_against_standards.py --check-standards --standards-dir data/
```

---

## Project Overview

```text
roles.json 
  ↓
Educational Profiles 
  ↓
Curriculum Generator 
  ↓
Curricula + Micro-Credentials + Visual Stack Pathways
```

---

## Directory Structure (Condensed)

```bash
.
├── README.md
├── requirements.txt
├── run_curriculum.sh
├── data/
│   ├── modules.json
│   ├── roles.json
│   ├── curriculum_design_standards.json
│   ├── ects_standards.json
│   ├── educational_profile_standards.json
│   └── micro_credentials/
│       ├── certification_framework.json
│       └── micro_credential_standards.json
├── dscg/
│   ├── __init__.py
│   ├── __pycache__/
│   ├── package/
│   │   ├── __init__.py
│   │   ├── curriculum.py
│   │   ├── ects_validator.py
│   │   ├── generator.py
│   │   ├── micro_credentials.py
│   │   ├── models.py
│   │   ├── module.py
│   │   └── role.py
│   └── utils/
│       ├── __init__.py
│       ├── config.py
│       └── learning_outcomes.py
├── scripts/
│   ├── assess_curricula_against_standards.py
│   ├── assess_educational_profiles_against_standards.py
│   ├── assess_micro_credentials.py
│   ├── assess_modules.py
│   ├── assess_modules_against_standards.py
│   ├── export_profiles.py
│   ├── generate_all_curricula.py
│   ├── generate_curriculum.py
│   ├── generate_micro_credentials.py
│   ├── improved_generate_curriculum.py
│   └── visualize_stacking_paths.py
├── output/
│   ├── curricula/                   # Generated curricula (HTML, JSON)
│   ├── profiles/                    # Exported educational profiles
│   └── micro_credentials/          # Micro-credential JSON sets
├── exporters/
├── generate_curriculum/
├── assess_modules.txt
├── export_profiles.txt
├── generate_all_curricula.txt
├── generate_curriculum.txt
├── tree.txt
```
---

## Types of Analysis

- **Curriculum/Module Validation**: ECTS, ECVET, micro-credential criteria
- **Competency Matching**: Job-role to outcome traceability via ESCO
- **Pathway Structuring**: Stackability and credential logic
- **Balance & Delivery**: Distribution across semesters and learning types (theory, practice, work-based)

---

## Roadmap

- Web-based **Profile & Credential Builder**
- **Cross-role analytics** and credential clustering
- Support for **localized curriculum adaptation**
- Export to **xAPI/SCORM** for LMS integration

---

## Contributing

This project supports modular curriculum and certification development for high-impact skills frameworks. Contributions and collaborations are welcome.
## License

This project is licensed under the MIT License - see the LICENSE file for details.
