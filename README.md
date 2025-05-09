# Digital Sustainability Curriculum Generator (DSCG)

A suite of Python scripts for modular curriculum generation and assessment aligned with the Digital4Sustainability project. The system automatically generates digital sustainability curricula at various EQF levels for different professional roles and assesses their quality.

## Key Features

- **Educational Profile Generation**: Creation of detailed educational profiles from role definitions (`roles.json`)  
- **Skill and Role Mapping**: Structured modeling of skills and professional competencies mapped to EQF levels  
- **Profile-to-Curriculum Translation**: Transformation of educational profiles into concrete curricula  
- **Modular Design**: Flexible curriculum generation with modular components  
- **EQF Alignment**: Support for European Qualification Framework levels 4-8  
- **Work-based Learning**: Integration of theoretical, practical, and work-based modules  
- **Dynamic Semester Assignment**: Intelligent distribution of modules across semesters  
- **Intelligent Module Selection**: Enhanced algorithms for optimal module selection based on educational profiles  
- **Learning Outcomes Generation**: Automatic generation of Bloom's taxonomy-aligned learning outcomes  
- **Multiple Export Formats**: HTML, JSON, PDF, SCORM, and xAPI  

## Educational Profiles as Intermediate Data Structure

In the DSCG architecture, educational profiles serve as a critical intermediate data structure:

**Source Data → Educational Profiles**: The system parses the roles defined in `roles.json` to generate comprehensive educational profiles  
**Educational Profiles → Curricula**: These profiles then drive the curriculum generation process, determining module selection and organization  

This two-step approach allows for:

- Separation of role definitions from curriculum specifics  
- More flexible adaptation of curricula to different educational contexts  
- Clear traceability between professional requirements and educational implementation  

**Visualizing the Process Flow:**  
`roles.json → Educational Profiles → Curriculum Generation → Generated Curricula`

## Project Structure

```
dscg/
├── package/
│   ├── __init__.py
│   ├── module.py
│   ├── role.py
│   ├── curriculum.py
│   ├── generator.py
│   └── utils/
│       ├── __init__.py
│       ├── analysis.py
│       ├── exporters.py
│       └── learning_outcomes.py
├── exporters/
│   ├── html_exporter.py
│   ├── json_exporter.py
│   └── ...
├── utils/
│   ├── validation.py
│   └── config.py
└── visualization/
    └── sankey.py
scripts/
├── assess_modules.py
├── generate_curriculum.py
├── generate_all_curricula.py
└── export_profiles.py
data/
├── modules.json
├── roles.json
└── skills.json
```

## Input Files and Data Transformation

DSCG uses a multi-step data transformation process:

**Input Files:**

- `roles.json`: Defines professional roles with their skills, EQF levels, and requirements  
- `modules.json`: Contains module definitions with detailed educational specifications  

**Internal Transformation:**

- Roles are converted into comprehensive educational profiles  
- These profiles serve as the blueprint for curriculum generation  

**Output:**

- Generated curricula in various formats (HTML, JSON, etc.)  
- Educational profiles can be exported for inspection (see below)  

## Educational Profile Examples

The system generates educational profiles for various professional roles in digital sustainability:

- **Digital Sustainability Lead (DSL)**: Strategic leadership role focused on organizational transformation  
- **Sustainable Software Developer (SSD)**: Technical role focused on environmentally efficient software  
- **Sustainability Data Analyst (SDA)**: Analytical role focused on sustainability metrics and reporting  
- **Digital Sustainability Consultant (DSC)**: Advisory role spanning technical and business domains  
- **Sustainable Technology Specialist (STS)**: Specialized technical role for sustainable systems  

Each generated educational profile contains:

- Skill requirements by EQF level  
- Learning pathway specifications  
- Competency mappings  
- Required knowledge areas  
- Assessment criteria  

## Core Classes and Methods

| Class               | Key Methods                                          | Description |
|---------------------|------------------------------------------------------|-------------|
| `Module`            | `__init__`, `to_dict`                                | Represents individual learning modules with attributes like ECTS, skills, and outcomes |
| `Role`              | `__init__`, `from_dict`, `generate_educational_profile` | Represents professional roles and generates educational profiles |
| `Curriculum`        | `calculate_total_ects`, `export_as_html`, `export_as_json` | Manages a complete curriculum composed of modules |
| `CurriculumGenerator` | `generate_curriculum`, `distribute_modules_to_semesters` | Core engine for curriculum generation based on educational profiles |

## Command-Line Usage

### NEW: Export Educational Profiles for Inspection

```bash
python scripts/export_profiles.py --output output/profiles/
```

**Command-Line Arguments for `export_profiles.py`**

- `--output`: Directory to save the exported profiles  
- `--format`: Export format (`json`, `html`, or `both`) (default: both)  
- `--roles-json`: Path to roles JSON file (default: `data/roles.json`)  
- `--roles`: Specific roles to export (default: all roles)  
- `--eqf-levels`: Specific EQF levels to export (default: all levels)  

### Generate a curriculum for a specific educational profile

```bash
python scripts/generate_curriculum.py --role DSL --eqf 7 --output output/curricula/curriculum_dsl_7.html
```

**Command-Line Arguments**

- `--role`: Role ID corresponding to an educational profile (e.g., DSL for Digital Sustainability Lead)  
- `--eqf`: EQF level (4-8) for the educational profile  
- `--output`: Output file path (supports `.html`, `.json`)  
- `--type`: Curriculum type (`full` or `upskilling`)  
- `--skills`: Optional list of target skills for specialized educational profile  
- `--modules-json`: Path to modules JSON file (default: `data/modules.json`)  
- `--roles-json`: Path to roles JSON file (default: `data/roles.json`)  
- `--debug`: Enable debug logging  

### Generate curricula for all educational profiles

```bash
python scripts/generate_all_curricula.py
```

**Additional options:**

- `--output-dir`: Specify output directory  
- `--parallel`: Generate curricula in parallel  
- `--module-report`: Generate a consolidated report of module usage  
- `--report-html`: Save module usage report as HTML  

### Assess module quality against educational profiles

```bash
python scripts/assess_modules.py > assessment_report.txt
```

## Types of Analysis

The DSCG performs several types of analysis related to educational profiles:

- **Profile Generation Analysis**: Evaluation of how roles are translated into educational profiles  
- **Profile-Module Alignment Analysis**: Evaluates how well modules align with educational profile requirements  
- **Competency Coverage Analysis**: Assesses the coverage of required competencies in generated curricula  
- **Educational Pathway Analysis**: Analyses the progression of learning aligned with educational profiles  
- **ECTS Distribution Analysis**: Evaluates the appropriate allocation of ECTS across different competency areas  
- **Module Balance Analysis**: Ensures proper balance of theoretical, practical, and work-based learning  

## Future Enhancements

- **Enhanced Profile Export**: More detailed visualization and export options for educational profiles  
- **Profile Editing Interface**: Tools for manually refining auto-generated educational profiles  
- **Profile-Curriculum Traceability**: Visual mapping between profile requirements and curriculum components  
- **Profile Versioning**: Track changes to educational profiles over time  
- **Interactive Profile Builder**: Web-based tool for creating and editing educational profiles  
- **Profile Visualization**: Visual representation of educational profiles and competency mappings  
- **Cross-Profile Analysis**: Compare and contrast different educational profiles for synergies  
- **Profile Adaptation Tools**: Tools to adapt educational profiles to specific regional or institutional requirements  
- **Literature Integration**: Automatically include relevant literature aligned with educational profiles  
- **Competency-Based Assessment**: Generate assessment guidelines aligned with educational profiles  

## Contributing

Contributions to the Digital Sustainability Curriculum Generator are welcome. Please feel free to submit pull requests or open issues to improve the functionality or documentation, particularly around educational profiles.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
