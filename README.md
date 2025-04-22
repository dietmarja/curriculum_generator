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
1. Digital Sustainability Lead (DSL)
2. Digital Sustainability Manager (DSM)
3. Digital Sustainability Consultant (DSC)
4. Sustainability Business Analyst (SBA)
5. Sustainability Data Scientist (DSI)
6. Sustainability Data Analyst (DAN)
7. Sustainability Data Engineer (DSE)
8. Sustainable Digital Designer (SDD)
9. Software Developer for Sustainability (SSD)
10. Sustainability Technology Specialist (STS)

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
- **Multiple Export Formats**: Export curricula in HTML and JSON formats (PDF, SCORM, and xAPI coming soon)
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
git clone https://github.com/dietmarja/digital4sustainability.git
cd digital4sustainability/python/curriculum_generator
pip install -r requirements.txt
```

## Usage

### Command Line Interface

```bash
# Generate a full curriculum for Digital Sustainability Lead at EQF level 7
python scripts/generate_curriculum.py --role DSL --eqf 7 --output output/curricula/curriculum_dsl_7.html

# Generate a curriculum focusing on specific skills
python scripts/generate_curriculum.py --role SDD --eqf 6 --type upskilling --skills sustainability_basics data_analytics --output output/curricula/curriculum_sdd_6_upskilling.html

# Enable debug mode for detailed logging
python scripts/generate_curriculum.py --role DSC --eqf 7 --output output/curricula/curriculum_dsc_7.html --debug
```

### Using the Shell Script (Easier Method)

```bash
# Make the script executable
chmod +x scripts/run_generator.sh

# Basic usage
./scripts/run_generator.sh -r DSL -e 7

# Upskilling curriculum with specific skills
./scripts/run_generator.sh -r SDD -e 6 -t upskilling -s "sustainability_basics data_analytics"

# Custom output directory
./scripts/run_generator.sh -r DSC -e 7 -o output/custom_curricula
```

### Python API

```python
from models import CurriculumGenerator, Curriculum, Module, Role

# Initialize the generator
generator = CurriculumGenerator()

# Load modules and roles
generator.load_modules_from_json("data/modules.json")
generator.load_roles_from_json("data/roles.json")

# Generate curriculum
curriculum = generator.generate_curriculum(
    role_id="DSL",
    eqf_level=7,
    is_full_curriculum=True
)

# Export in different formats
curriculum.export_as_json("output/curricula/dsl_curriculum.json")
curriculum.export_as_html("output/curricula/dsl_curriculum.html")
```

## Data Structure

The generator relies on structured JSON files:

### modules.json

```json
[
  {
    "id": "M1",
    "name": "Introduction to Digital Sustainability",
    "description": "Fundamentals of digital sustainability concepts and principles",
    "eqf_level": 6,
    "ects_points": 5,
    "thematic_area": "sustainability",
    "prerequisites": [],
    "delivery_methods": ["classroom", "online"],
    "module_type": ["theoretical"],
    "skills": ["sustainability_basics", "critical_thinking"],
    "is_work_based": false,
    "learning_outcomes": [
      "Define key concepts and principles of digital sustainability",
      "Explain the relationship between digital technologies and sustainability",
      "Analyze organizational practices for sustainability improvement"
    ]
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
    "thematic_area": "sustainability",
    "eqf_levels": [6, 7, 8],
    "core_skills": ["sustainability_strategy", "leadership", "data_analytics"],
    "program_learning_outcomes": {
      "6": [
        "Knowledge: Analyze digital systems for sustainability improvement opportunities",
        "Understanding: Evaluate sustainability frameworks and their application",
        "Skills: Implement comprehensive sustainability strategies using digital tools"
      ],
      "7": [
        "Knowledge: Critically evaluate advanced sustainability concepts",
        "Understanding: Synthesize relationships between technology and sustainability challenges",
        "Skills: Design and lead digital sustainability initiatives"
      ]
    }
  },
  ...
]
```

## Module Duplication Fix

The latest version includes a fix for the module duplication problem that was causing issues in previous versions:

### Previous Issue
- When a curriculum didn't have enough modules to reach the required ECTS, the system created duplicates of existing modules with slightly modified IDs (e.g., M1_0, M1_1)
- This led to bloated curricula with repetitive content and poor distribution across semesters

### Current Solution
1. **Template-Based Generation**: Instead of duplicating existing modules, the system now uses a diverse set of module templates to generate unique new modules
2. **Unique IDs**: Generated modules have a distinct prefix ("G" for generated) and a unique ID structure (e.g., GDSL701)
3. **Improved Semester Distribution**: Modules are distributed using topological sorting based on prerequisites, ensuring logical progression
4. **ECTS Balancing**: The system balances ECTS credits across semesters by intelligently moving modules while respecting prerequisites
5. **Better Error Handling**: Comprehensive input validation and error logging help identify issues during curriculum generation

## Project Structure

```
curriculum_generator/
├── data/
│   ├── modules.json
│   └── roles.json
├── dscg/
│   └── package/
│       └── models.py
├── models.py
├── scripts/
│   ├── generate_curriculum.py
│   ├── test_module_duplication.py
│   └── run_generator.sh
├── output/
│   └── curricula/
└── requirements.txt
```

## Troubleshooting

### Common Issues and Solutions

1. **ModuleNotFoundError: No module named 'src.models'**
   - Solution: This happens when the script can't find the models file
   - Make sure to run the script from the curriculum_generator directory
   - Alternatively, set up the proper Python path or modify import paths

2. **No modules loaded errors**
   - Solution: Ensure data/modules.json and data/roles.json exist and contain valid JSON
   - Check file permissions and structure
   - Enable debug mode for more detailed logging

3. **Module duplication in output**
   - Solution: The latest version resolves this issue with template-based generation
   - Run test_module_duplication.py to verify the fix
   - If you still see duplicates, ensure you're using the latest version of models.py

### Debug Mode

Enable debug logging for more detailed output:
```bash
python scripts/generate_curriculum.py --role DSL --eqf 7 --output output/curricula/curriculum.html --debug
```

## Future Developments

- **Web Interface**: Development of a web-based interface for easier curriculum generation
- **Enhanced Export Options**: Additional export formats (PDF, SCORM, xAPI)
- **Visualization Tools**: Implementation of Sankey diagrams for visualizing relationships between roles, modules, and skills
- **Prerequisite Visualization**: Module dependency graphs to visualize curriculum structure
- **Microcredential Support**: Generation of microcredential pathways for more granular learning

## Contributing

Contributions to improve and extend the curriculum generator are welcome. Please feel free to submit issues or pull requests.

## License

This project is licensed under the Creative Commons license 4.0 B.Y. as specified in the Digital4Sustainability project documentation.

## Acknowledgements

This tool is part of the Digital4Sustainability project, funded by the European Union under project number 101140316. The project resources contained herein are publicly available under the Creative Commons license 4.0 B.Y.
