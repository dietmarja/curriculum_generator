# Digital Sustainability Curriculum Generator (DSCG)

A comprehensive toolkit for generating, analyzing, and evaluating modular, outcome-based curricula for digital sustainability education. The DSCG supports both full educational programs and specific micro-credential pathways across EQF levels 4-8.

## Key Features

- **Full & Specific Curricula**: Generate complete educational programs or targeted micro-credential pathways
- **Multi-level Support**: Design curricula across EQF levels 4-8 for various digital sustainability roles
- **Standards Compliance**: Built-in validation against European educational frameworks and standards
- **Stackable Credentials**: Create and visualize flexible, personalized learning pathways
- **Rich Evaluation**: Comprehensive assessment against accreditation and T3.2 criteria
- **Work-based Learning**: Support for dual principle education with industry-aligned components


## Project Structure

curriculum_generator/                        # Project root
├── dscg/                                    # Main package
│   ├── config.py                            # Centralized configuration
│   ├── standards.py                         # Standards manager
│   ├── package/                             # Core functionality
│   │   ├── module.py                        # Module class
│   │   ├── role.py                          # Role class
│   │   ├── curriculum.py                    # Curriculum class
│   │   ├── generator.py                     # CurriculumGenerator class
│   │   └── ects_validator.py                # ECTS validation
│   └── utils/                               # Utility functions
├── input/                                   # Input data
│   ├── modules/                             # Module definitions
│   ├── roles/                               # Role definitions
│   └── standards/                           # Educational standards
├── scripts/                                 # CLI scripts
└── output/                                  # Generated output
    ├── curricula/                           # Generated curricula
    ├── profiles/                            # Educational profiles
    ├── accreditation/                       # Evaluation reports
    └── micro_credentials/                   # Micro-credential definitions


## Standards Alignment

| Standard | Implementation |
|----------|----------------|
| **EQF** | Levels 4–8 structuring; outcome-based design and transparency across national systems |
| **ECTS** | Credit weighting, workload calculation, and validation of learning modules |
| **ECVET** | Modular and transferable design for vocational and work-based learning |
| **e-CF** | Structuring ICT competences aligned to EQF and supporting digital role profiles |
| **ESCO** | Mapping of learning outcomes to labor market competences and job roles |
| **GreenComp** | Embedding sustainability competencies into transversal learning outcomes |
| **EU Micro-Credentials** | Quality, granularity, and stackability for short-form learning units |
| **Tuning** | Alignment and calibration of learning outcomes from program to module level |





## Code Examples

### 1. Curriculum Generation

```python
# Generate a single curriculum for Digital Sustainability Lead at EQF level 7
python scripts/generate_curriculum.py --role DSL --eqf 7 \
  --output output/curricula/curriculum_DSL_7.html \
  --modules-json input/modules/modules.json
```
# Generate all curricula for all defined roles and EQF levels
```
python scripts/generate_all_curricula.py \
  --output-dir output/curricula \
  --modules-json input/modules/modules.json
```

2. Micro-credential Management
```
python# Generate micro-credential definitions
python scripts/microcredential_curriculum_builder.py --create-sample --data-dir data
```

# Build a role-based specific curriculum from micro-credentials
```
python scripts/microcredential_curriculum_builder.py --build-curriculum \
  --role-id DSL --eqf-level 5 \
  --data-dir data --output-dir output/specific_curricula
```

# Create a custom curriculum from selected micro-credentials
```
python scripts/microcredential_curriculum_builder.py --build-curriculum \
  --micro-credentials MC001,MC003,MC007 \
  --name "Green Computing Fundamentals" \
  --description "A focused curriculum on green computing basics" \
  --data-dir data --output-dir output/specific_curricula
```

3. Evaluation & Analysis
```
python# Evaluate all curricula for standards compliance
python scripts/curriculum_evaluation_framework.py \
  --input-dir output --output-dir output/accreditation --include-specific
```

# Generate validation summary for curricula
```
python scripts/improved_curriculum_summary.py \
  --output-dir output/curricula \
  --modules-json input/modules/modules.json
```

# Fix compliance issues in existing curricula
```
python scripts/fix_curriculum_issues.py \
  --input-dir output/curricula \
  --output-dir output/curricula_fixed
```

4. Visualization & Export
```
python scripts/visualize_stacking_paths.py
```

# Export educational profiles for all roles
```
python scripts/export_profiles.py --output output/profiles --format both
```

# Generate accreditation-ready reports
```
python scripts/curriculum_accreditation_check.py \
  --input-dir output/curricula_fixed \
  --output-dir output/accreditation
```

## Workflow

Role Definition: Define digital sustainability roles in roles.json
Educational Profiles: Generate educational profiles based on roles
Curriculum Generation: Create full curricula for each role and EQF level
Micro-credential Generation: Define modular, stackable learning units
Evaluation & Compliance: Assess curricula against standards and requirements
Visualization: Generate pathway visualizations and learning maps

## Types of Analysis

Standards Validation: EQF, ECTS, ECVET, micro-credential compliance
Curriculum Evaluation: Accreditation readiness, T3.2 requirements
Competency Mapping: Job-role to outcome traceability via ESCO
Pathway Analysis: Stackability and credential progression logic
Delivery Assessment: Distribution across semesters and learning types (theory, practice, work-based)

## Supported Use Cases

- Full Educational Programs: Complete degree programs across EQF levels
- Targeted Upskilling: Specific modules to address skill gaps
- Industry Reskilling: Focused pathways for career transitions
- Dual Learning: Combined academic and work-based components
- Stackable Credentials: Modular, cumulative achievement paths


---

## Roadmap

- Web-based Interface on top of the CCL interface
- Integrationn of Bib-tex reference so that the curricula include a reading list
- Not only full curricula but tailored curricula 
- Export to **xAPI/SCORM** for LMS integration

---

## Contributing

This project supports modular curriculum and certification development for high-impact skills frameworks. Contributions and collaborations are welcome.
## License

This project is licensed under the MIT License - see the LICENSE file for details.
