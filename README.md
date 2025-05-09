# Digital Sustainability Curriculum Generator (DSCG)

A suite of Python scripts for modular curriculum generation and assessment aligned with the Digital4Sustainability project. The system automatically generates digital sustainability curricula at various EQF levels for different professional roles and assesses their quality.

## Key Features

- **Skill and Role Modeling**: Structured modeling of skills and professional roles  
- **Modular Design**: Flexible curriculum generation with modular components  
- **EQF Alignment**: Support for European Qualification Framework levels 4-8  
- **Work-based Learning**: Integration of theoretical, practical, and work-based modules  
- **Dynamic Semester Assignment**: Intelligent distribution of modules across semesters  
- **Intelligent Module Selection**: Enhanced algorithms for optimal module selection based on role relevance  
- **Learning Outcomes Generation**: Automatic generation of Bloom's taxonomy-aligned learning outcomes  
- **Multiple Export Formats**: HTML, JSON, PDF, SCORM, and xAPI  

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
└── generate_all_curricula.py
data/
├── modules.json
├── roles.json
└── skills.json
```

## Input Files

Curricula are generated based on two primary input files:

- `roles.json`: Defines professional roles with their skills, EQF levels, and requirements  
- `modules.json`: Contains module definitions with detailed educational specifications

These files follow a JSON schema that aligns with educational standards, frameworks, and best practices such as the Tuning approach, EQF levels, and Bloom's taxonomy. The quality of the generated curricula depends on the validity and completeness of these input files.

## Core Classes and Methods

| Class               | Key Methods                              | Description |
|---------------------|-------------------------------------------|-------------|
| `Module`            | `__init__`, `to_dict`                     | Represents individual learning modules with attributes like ECTS, skills, and outcomes |
| `Role`              | `__init__`, `from_dict`                   | Represents professional roles with specific requirements |
| `Curriculum`        | `calculate_total_ects`, `export_as_html`, `export_as_json` | Manages a complete curriculum composed of modules |
| `CurriculumGenerator` | `generate_curriculum`, `distribute_modules_to_semesters` | Core engine for curriculum generation |

## Enhanced Curriculum Generation

### Improved Module Selection

- **Role-based Filtering**: Better selection of modules based on relevance to specific roles  
- **Gap Analysis**: Sophisticated analysis of ECTS shortfalls with targeted recommendations  
- **Balanced Module Types**: Ensures proper mix of theoretical, practical, and work-based modules  

### Intelligent Semester Distribution

- **Dependency-aware Scheduling**: Places modules respecting prerequisites and knowledge progression  
- **ECTS Balancing**: Evenly distributes workload across semesters  
- **Work-based Integration**: Strategic placement of work-based modules in appropriate semesters  

### Better Learning Outcomes

- **EQF-aligned Outcomes**: Automatically generates appropriate learning outcomes based on EQF level  
- **Domain-specific Language**: Tailored to the module's content area and delivery methods  
- **Bloom's Taxonomy Integration**: Uses appropriate cognitive level verbs based on module type and EQF level  

## Command-Line Usage

### Generate a single curriculum

```bash
python scripts/generate_curriculum.py --role DSL --eqf 7 --output output/curricula/curriculum_dsl_7.html
```

**Command-Line Arguments**

- `--role`: Role ID (e.g., DSL for Digital Sustainability Lead)  
- `--eqf`: EQF level (4-8)  
- `--output`: Output file path (supports .html, .json)  
- `--type`: Curriculum type (full or upskilling)  
- `--skills`: Optional list of target skills for upskilling curriculum  
- `--modules-json`: Path to modules JSON file (default: data/modules.json)  
- `--roles-json`: Path to roles JSON file (default: data/roles.json)  
- `--debug`: Enable debug logging  

### Generate all curricula

```bash
python scripts/generate_all_curricula.py
```

**Additional options:**

- `--output-dir`: Specify output directory  
- `--parallel`: Generate curricula in parallel  
- `--module-report`: Generate a consolidated report of module usage  
- `--report-html`: Save module usage report as HTML  

### Assess module quality

```bash
python scripts/assess_modules.py > assessment_report.txt
```

## Types of Analysis

The DSCG performs several types of configuration and dependency analysis:

- **Module Utilization Analysis**: Evaluates which predefined modules are being used  
- **Dependency Tracking**: Identifies missing prerequisites and dependencies  
- **Resource Allocation Analysis**: Analyzes module distribution across EQF levels and curricula  
- **ECTS Gap Analysis**: Identifies shortfalls in ECTS coverage for different roles and levels  
- **Module Balance Analysis**: Evaluates the mix of theoretical, practical, and work-based modules  

## Future Enhancements

- **Web Interface**: Develop a user-friendly web interface for curriculum generation and visualization  
- **Literature Integration**: Automatically include relevant literature from academic sources  
- **Enhanced Visualization**: Interactive charts and diagrams for curriculum analysis  
- **Advanced Validation**: More sophisticated validation against educational standards  
- **AI-driven Recommendations**: Use AI to suggest optimal modules for specific roles  
- **Customizable Templates**: Allow users to create and save custom curriculum templates  
- **Feedback Integration**: Incorporate user feedback to improve module recommendations  

## Contributing

Contributions to the Digital Sustainability Curriculum Generator are welcome. Please feel free to submit pull requests or open issues to improve the functionality or documentation.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
