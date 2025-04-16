# Curriculum Generator (CG)

## Overview

The Curriculum Generator (CG) is a Python-based tool designed to create flexible, modular curricula for different digital sustainability roles across various European Qualification Framework (EQF) levels. Developed as part of the Digital4Sustainability EU project (Task 3.2), this tool addresses the need for standardized yet adaptable educational pathways that support the Twin Transition (digital + sustainability).

The CG can be operated as a Python script through a command-line interface. It generates curricula based on structured data about modules, roles, and skills defined in JSON format.

While currently focused on digital sustainability roles, the CG is designed to be thematic-agnostic and can be applied to other domains such as business or cybersecurity.

## Educational Foundation

The Curriculum Generator is built on solid educational principles and frameworks:

### Learning Outcomes Framework

The system is based on a comprehensive set of learning outcomes derived from the Digital4Sustainability project's needs analysis (D2.1). Learning outcomes follow the Tuning formula with different levels of granularity:
- Program-level learning outcomes
- Module-level learning outcomes
- Specific learning outcomes within modules

Each learning outcome is mapped to specific skills and competencies identified in the digital sustainability field.

### Role Profiles

The system incorporates the 10 key digital sustainability roles identified in the D2.1 report:
1. Digital Sustainability Lead
2. Digital Sustainability Manager
3. Digital Sustainability Consultant
4. Sustainability Business Analyst
5. Sustainability Data Scientist
6. Sustainability Data Analyst
7. Sustainability Data Engineer
8. Sustainability Solution Designer
9. Software Developer for Sustainability
10. Sustainability Technical Specialist

Each role is defined with specific competence requirements, EQF level ranges, and core skills.

### Module Building Blocks

The system uses a modular approach with different types of learning components:
- Theoretical modules
- Practical modules
- Work-based learning modules

Each module is characterized by:
- Learning outcomes
- ECTS points
- Delivery methods
- Assessment methods
- Prerequisites
- Skills addressed
- Role relevance

### Educational Standards Compliance

The generator produces curricula that align with:
- European Qualification Framework (EQF) levels 4-8
- European Credit Transfer and Accumulation System (ECTS)
- The dual principle of alternating classroom and workplace learning
- European e-Competence Framework (e-CF)

## Key Features

- **Multi-EQF Level Support**: Generate curricula across EQF levels 4-8
- **Role-Specific Customization**: Create curricula tailored to specific digital sustainability roles
- **Flexible Delivery Methods**: Support for classroom, online, blended, and workplace learning
- **Full and Specialized Curricula**: Generate both complete educational programs and targeted upskilling/reskilling paths
- **Work-Based Learning Integration**: Ensure appropriate balance of theoretical and practical components
- **Multiple Export Formats**: Export curricula in HTML, JSON, PDF, SCORM, and xAPI formats
- **Dynamic Semester Assignment**: Automatically organize modules into semesters based on prerequisites
- **Skill Categorization**: Group skills by thematic areas for better organization
- **ECTS Mapping**: Assign and track credit points for cross-program comparability

## System Architecture

The CG is composed of four main classes:
1. `Module`: Represents a learning component with attributes like EQF level, ECTS points, and prerequisites
2. `Role`: Represents a digital sustainability role with associated skills and competencies
3. `Curriculum`: Aggregates modules into a structured curriculum with semester assignment
4. `CurriculumGenerator`: Core engine for curriculum generation based on role and EQF level

## Installation

```bash
git clone https://github.com/dietmarja/curriculum_generator.git
cd curriculum_generator
pip install -r requirements.txt
```

## Usage

### Command Line Interface

```bash
# Generate a full curriculum for Digital Sustainability Manager at EQF level 6
python scripts/generate_curriculum.py --role DSM --eqf 6 --output output/curriculum_dsm.html

# Generate a curriculum focusing on specific skills
python scripts/generate_curriculum.py --role DSL --eqf 6 --skills "esg_reporting,data_analytics" --output output/curriculum_dsl.json

# List available thematic areas
python scripts/generate_curriculum.py --list-areas

# List roles in a specific area
python scripts/generate_curriculum.py --area sustainability --list-roles
```

Note: Always specify a full path for the output file (e.g., `output/filename.html` or `./filename.json`) to avoid file path errors.

### Python API

```python
from dscg.package.models import Module, Role, Curriculum, CurriculumGenerator

# Initialize the generator
generator = CurriculumGenerator()

# Load modules and roles
generator.load_modules_from_json("data/modules.json")
generator.load_roles_from_json("data/roles.json")

# Generate curriculum
curriculum = generator.generate_curriculum(
    role_id="DSL",
    eqf_level=6,
    is_full_curriculum=True
)

# Export in different formats
curriculum.export_as_json("output/dsl_curriculum.json")
curriculum.export_as_html("output/dsl_curriculum.html")
```

## Data Structure

The generator relies on structured JSON files:

### modules.json

```json
[
  {
    "id": "MOD001",
    "name": "Introduction to Digital Sustainability",
    "description": "Fundamentals of digital sustainability concepts and principles",
    "eqf_level": 6,
    "ects_points": 5,
    "prerequisites": [],
    "delivery_methods": ["classroom", "online"],
    "module_type": ["theoretical"],
    "skills": ["sustainability_basics", "critical_thinking"]
  },
  ...
]
```

### roles.json

```json
[
  {
    "id": "DSL",
    "name": "Digital Sustainability Lead",
    "description": "Drives digital sustainability initiatives within organizations",
    "main_area": "Management & Consultancy",
    "eqf_levels": [5, 6, 7],
    "core_skills": ["sustainability_strategy", "leadership", "data_analytics"]
  },
  ...
]
```

## Future Developments

- **Visualization Tools**: Implementation of Sankey diagrams for visualizing relationships between roles, modules, and skills
- **Web Interface**: Development of a web-based interface for easier curriculum generation
- **Enhanced Export Options**: Additional export formats and customization options
- **Prerequisite Visualization**: Module dependency graphs to visualize curriculum structure

## Project Structure

```
curriculum_generator/
├── dscg/
│   ├── __init__.py
│   ├── generator.py
│   ├── package/
│   │   ├── __init__.py
│   │   └── models.py
│   ├── exporters/
│   │   ├── __init__.py
│   │   ├── html_exporter.py
│   │   ├── json_exporter.py
│   │   ├── pdf_exporter.py
│   │   ├── scorm_exporter.py
│   │   └── xapi_exporter.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── learning_outcomes.py
│   │   └── validation.py
│   └── visualization/
│       ├── __init__.py
│       ├── prerequisites.py
│       └── sankey.py
├── data/
│   ├── modules.json
│   ├── roles.json
│   └── skills.json
├── scripts/
│   ├── generate_curriculum.py
│   ├── generate_sankey.py
│   └── setup_data.py
├── output/
│   ├── curricula/
│   ├── packages/
│   └── visualizations/
├── tests/
│   ├── __init__.py
│   ├── test_generator.py
│   ├── test_models.py
│   └── test_exporters.py
├── requirements.txt
└── README.md
```

## Contributing

Contributions to improve and extend the curriculum generator are welcome. Please feel free to submit issues or pull requests.

## License

This project is licensed under the Creative Commons license 4.0 B.Y. as specified in the Digital4Sustainability project documentation.

## Acknowledgements

This tool is part of the Digital4Sustainability project, funded by the European Union under project number 101140316. The project resources contained herein are publicly available under the Creative Commons license 4.0 B.Y.
