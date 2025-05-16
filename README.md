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
| Standard                 | Role in CG                                                                            |
| ------------------------ | ------------------------------------------------------------------------------------- |
| **EQF**                  | Levels 4–8 structuring; outcome-based design and transparency across national systems |
| **ECTS**                 | Credit weighting, workload calculation, and validation of learning modules            |
| **ECVET**                | Modular and transferable design for vocational and work-based learning                |
| **e-CF**                 | Structuring ICT competences aligned to EQF and supporting digital role profiles       |
| **ESCO**                 | Mapping of learning outcomes to labor market competences and job roles                |
| **GreenComp**            | Embedding sustainability competencies into transversal learning outcomes              |
| **EU Micro-Credentials** | Quality, granularity, and stackability for short-form learning units                  |
| **Tuning**               | Alignment and calibration of learning outcomes from program to module level           |
---






## Example Commands

### Generate One Curriculum
```bash
# Central CLI script
python scripts/generate_curriculum.py --role DSL --eqf 7 --output output/curricula/curriculum_DSL_7.html
```

### Generate All Curricula
```bash
python scripts/generate_all_curricula.py --output-dir output/curricula
```

### Create Micro-Credentials
```bash
#python scripts/generate_micro_credentials.py --output output/micro_credentials
#python scripts/improve_micro_credentials.py --force
python scripts/generate_enhanced_micro_credentials.py --generate-upskilling
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

## Directory Structure 

```bash
curriculum_generator/       # Project root
├── dscg/                  # Main package
│   ├── __init__.py
│   ├── config.py          # Centralized configuration
│   ├── standards.py       # Standards manager
│   ├── package/           # Core functionality
│   │   ├── __init__.py
│   │   ├── module.py      # Module class
│   │   ├── role.py        # Role class
│   │   ├── curriculum.py  # Curriculum class
│   │   ├── generator.py   # CurriculumGenerator class
│   │   └── ects_validator.py # ECTS validation
│   └── utils/             # Utility functions
│       ├── __init__.py
│       ├── file_utils.py  # File handling utilities
│       └── learning_outcomes.py # Learning outcome generation
├── input/                # Input data
│   ├── modules/          # Module definitions
│   ├── roles/            # Role definitions
│   └── standards/        # Educational standards
│       ├── standard_certification.json
│       ├── standard_curriculum.json
│       ├── standard_ecf_esco.json
│       ├── standard_ects.json
│       ├── standard_ecvet.json
│       ├── standard_greencomp.json
│       └── standard_microcredentials.json
├── scripts/              # CLI scripts
├── output/               # Generated output
│   ├── curricula/        # Generated curricula
│   ├── profiles/         # Educational profiles
│   └── micro_credentials/ # Micro-credential definitions
└── setup.py             # Package setup
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
