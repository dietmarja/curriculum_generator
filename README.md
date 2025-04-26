# Digital Sustainability Curriculum Generator (CG)

CG is a suite of Python tools for generating and assessing educational curricula. It is a generic tool, but her the focus is on the thematic area of digital sustainability, aligned with the Bologna Process and European Qualifications Framework (EQF).

## Overview

The Digital Sustainability Curriculum Generator (CG) is designed to create and export curricula that meet educational standards, with a focus on digital sustainability. It enables the creation of full curricula or specialized learning paths tailored to specific professional roles and European Qualification Framework (EQF) levels.

### Key Features

- **Export Formats**: Supports exporting to HTML, JSON, PDF, SCORM, and xAPI
- **Skill and Role Modeling**: Utilizes structured JSON files for modeling skills and professional roles
- **Visualization Tools**: Includes Sankey diagrams for visualizing module relationships and prerequisites
- **Validation and Quality Assessment**: Built-in tools to validate module quality and curriculum structure
- **Learning Outcomes Generation**: Automatic generation of Bloom's taxonomy-aligned learning outcomes
- **Module Duplication Prevention**: Intelligent handling of module naming and semester distribution

## Project Structure

```
curriculum_generator/
├── data/
│   ├── modules.json           # Module definitions
│   ├── roles.json             # Professional role definitions
│   └── skills.json            # Skill definitions
├── dscg/
│   ├── __init__.py
│   ├── package/
│   │   ├── __init__.py
│   │   ├── models.py          # Core data models
│   │   └── enhancements.py    # Additional enhancements
│   ├── exporters/
│   │   ├── __init__.py
│   │   ├── html_exporter.py   # HTML export functionality
│   │   ├── json_exporter.py   # JSON export functionality
│   │   ├── pdf_exporter.py    # PDF export functionality
│   │   ├── scorm_exporter.py  # SCORM export functionality
│   │   └── xapi_exporter.py   # xAPI export functionality
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── validation.py      # Validation utilities
│   │   ├── config.py          # Configuration settings
│   │   └── learning_outcomes.py  # Learning outcomes utilities
│   └── visualization/
│       ├── __init__.py
│       ├── prerequisites.py   # Prerequisites visualization
│       └── sankey.py          # Sankey diagram generation
├── scripts/
│   ├── generate_curriculum.py       # Main script for generating a curriculum
│   ├── generate_all_curricula.py    # Generate multiple curricula
│   ├── assess_modules.py            # Assess module quality
│   ├── validate_learning_outcomes.py  # Validate learning outcomes
│   ├── test_module_duplication.py   # Test for module duplication issues
│   ├── curriculum_balance.py        # Check curriculum balance
│   └── generate_sankey.py           # Generate Sankey diagrams
├── output/
│   ├── curricula/              # Generated curricula
│   ├── reports/                # Validation reports
│   └── visualizations/         # Generated visualizations
├── tests/
│   ├── __init__.py
│   ├── test_exporters.py
│   ├── test_generator.py
│   └── test_models.py
└── requirements.txt
```

## Core Components

### Module

The `Module` class represents a learning unit with attributes such as:
- EQF level
- ECTS points
- Delivery method
- Skills
- Learning outcomes
- Prerequisites

### Role

The `Role` class defines professional profiles with:
- Required skills
- EQF levels
- Learning outcomes for each level
- Program duration

### Curriculum

The `Curriculum` class aggregates modules into a full curriculum:
- Calculates total ECTS
- Organizes modules by semester
- Ensures prerequisites are respected
- Balances workload across semesters
- Categorizes skills based on thematic areas
- Provides export functionality to various formats

### CurriculumGenerator

The `CurriculumGenerator` class is responsible for:
- Loading modules and roles from JSON files
- Generating curricula based on specified criteria
- Creating learning outcomes aligned with Bloom's taxonomy
- Ensuring proper module distribution across semesters
- Preventing duplicate modules and resolving naming conflicts

## Installation

Clone the repository and install the required packages:

```bash
git clone https://github.com/yourusername/curriculum-generator.git
cd curriculum-generator
pip install -r requirements.txt
```

## Usage Examples

### Generating a Curriculum

Generate a curriculum for a specific role and EQF level:

```bash
# Generate curriculum for Digital Sustainability Lead at EQF level 7
python scripts/generate_curriculum.py --role DSL --eqf 7 --output output/curricula/curriculum_dsl_7.html

# Generate an upskilling curriculum focused on specific skills
python scripts/generate_curriculum.py --role DSE --eqf 6 --type upskilling --skills data_management energy_efficiency --output output/curricula/upskilling_dse_6.html

# Generate curriculum with custom module and role files
python scripts/generate_curriculum.py --role DSM --eqf 6 --modules-json custom/modules.json --roles-json custom/roles.json --output output/curricula/custom_dsm_6.html
```

### Generating Multiple Curricula

Generate curricula for all roles and specified EQF levels:

```bash
python scripts/generate_all_curricula.py --eqf-levels 6 7 --output-dir output/curricula
```

### Assessing Module Quality

Evaluate the quality of modules based on educational standards:

```bash
# Assess all modules and generate a comprehensive report
python scripts/assess_modules.py --modules data/modules.json --roles data/roles.json --output reports/module_assessment.txt

# Get a JSON report for programmatic use
python scripts/assess_modules.py --format json --output reports/module_assessment.json
```

### Validating Learning Outcomes

Check if learning outcomes meet Bloom's taxonomy standards:

```bash
# Validate learning outcomes in a single curriculum
python scripts/validate_learning_outcomes.py --curriculum output/curricula/curriculum_dsl_7.html

# Validate learning outcomes across all curricula in a directory
python scripts/validate_learning_outcomes.py --directory output/curricula --output reports/learning_outcomes_report.txt
```

### Testing Module Duplication

Check for duplicate or similar module names:

```bash
# Test a single curriculum file for duplicates
python scripts/test_module_duplication.py --input output/curricula/curriculum_dsl_7.html

# Test all curricula in a directory
python scripts/test_module_duplication.py --directory output/curricula --similarity 0.7 --output reports/duplication_report.txt
```

### Checking Curriculum Balance

Evaluate if a curriculum is well-balanced:

```bash
# Check the balance of a curriculum
python scripts/curriculum_balance.py --input output/curricula/curriculum_dsl_7.json --target-ects 30
```

### Generating Visualizations

Create a Sankey diagram of module prerequisites:

```bash
python scripts/generate_sankey.py --curriculum output/curricula/curriculum_dsl_7.json --output output/visualizations/dsl_7_sankey.html
```

## Data Format

### modules.json

```json
[
  {
    "id": "DSL101",
    "name": "Digital Sustainability Fundamentals",
    "description": "Core concepts and principles of digital sustainability",
    "eqf_level": 7,
    "ects_points": 5,
    "thematic_area": "sustainability",
    "prerequisites": [],
    "delivery_methods": ["classroom", "online"],
    "module_type": ["theoretical"],
    "skills": ["sustainability_basics", "digital_literacy"],
    "is_work_based": false,
    "learning_outcomes": [
      "Analyze digital sustainability principles and their application in organizational contexts",
      "Evaluate the environmental impact of digital technology choices",
      "Design sustainable technology strategies aligned with organizational goals"
    ]
  }
]
```

### roles.json

```
[
  {
    "id": "DSL",
    "name": "Digital Sustainability Lead",
    "description": "Leads digital sustainability initiatives within organizations",
    "main_area": "Management & Consultancy",
    "thematic_area": "sustainability",
    "program_learning_outcomes": {
      "7": [
        "Critically evaluate advanced concepts in sustainability",
        "Synthesize complex relationships between digital technologies and sustainability challenges",
        "Design and lead comprehensive digital sustainability initiatives"
      ]
    },
    "required_skills": ["sustainability_strategy", "digital_transformation", "leadership"],
    "program_duration": {
      "7": 4
    }
  }
]
```

## Validation Tools

The Curriculum Generator includes several validation tools to ensure the quality of the generated curricula:

- **Module Assessment**: Evaluates modules based on educational standards and best practices
- **Learning Outcomes Validation**: Checks if learning outcomes follow Bloom's taxonomy and are appropriate for the EQF level
- **Module Duplication Testing**: Detects duplicate or similar module names to improve curriculum clarity
- **Curriculum Balance Check**: Ensures even distribution of ECTS across semesters and appropriate mix of module types

These tools provide detailed reports with recommendations for improvement, helping educators refine their curricula to meet the highest standards.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

The Digital Sustainability Curriculum Generator is inspired by the work of Pouyioutas et al. on the ReProTool system \[1\], which demonstrated the value of software tools for curriculum re-engineering using Bologna Process concepts.

## References

\[1\] Pouyioutas, P., Gjermundrod, H., & Dionysiou, I. (2012). ReProTool Version 2.0: Re-engineering academic curriculum using learning outcomes, ECTS and Bologna process concepts. Interactive Technology and Smart Education, 9(3), 136-152.
