# Digital Sustainability Curriculum Generator

## Overview

The Digital Sustainability Curriculum Generator (DSCG) is a comprehensive tool designed to create flexible, modular curricula for different digital sustainability roles across various European Qualification Framework (EQF) levels. Developed as part of the Digital4Sustainability EU project in Task 3.2, this tool addresses the need for standardized yet adaptable educational pathways that meet the evolving demands of the Twin Transition (digital + sustainability).

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

Each role is defined with specific competence requirements, EQF level ranges, and core skills needed.

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
- **Visual Curriculum Mapping**: Generate Sankey diagrams showing relationships between roles, modules, and skills
- **Prerequisites Visualization**: Create module dependency graphs
- **ECTS Mapping**: Assign and track credit points for cross-program comparability

## System Architecture

The DSCG is composed of four main classes:
1. `Module`: Represents a learning component
2. `Role`: Represents a digital sustainability role
3. `Curriculum`: Represents a generated curriculum
4. `CurriculumGenerator`: Core engine for curriculum generation

## Installation

```bash
git clone https://github.com/digital4sustainability/curriculum-generator.git
cd curriculum-generator
pip install -r requirements.txt
```

## Configuration

### Parameters File (config.json)

The system is highly parameterizable through a configuration file (`config.json`). Key parameters include:

```json
{
  "output_formats": ["html", "pdf", "json", "scorm"],
  "instructional_design_model": "ADDIE",
  "ects_defaults": {
    "4": 60,
    "5": 120,
    "6": 180,
    "7": 120,
    "8": 180
  },
  "work_based_learning_targets": {
    "4": 50,
    "5": 40,
    "6": 30,
    "7": 20,
    "8": 10
  },
  "default_delivery_method": "blended",
  "min_module_relevance": 50,
  "visualization": {
    "sankey_width": 1200,
    "sankey_height": 800,
    "sankey_node_colors": ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
  },
  "data_paths": {
    "modules": "data/modules.json",
    "roles": "data/roles.json",
    "output_dir": "output/"
  },
  "standards_compliance": {
    "enable_scorm": true,
    "enable_xapi": true,
    "enable_competence_based_assessment": true
  }
}
```

### Educational Standards Support

The generator can produce curricula compatible with:
- **SCORM** (Shareable Content Object Reference Model)
- **xAPI** (Experience API)
- **ADDIE** (Analysis, Design, Development, Implementation, Evaluation) instructional design model
- **Bloom's Taxonomy** for learning outcome classification

## Usage

### Command Line Interface

```bash
# Generate a full curriculum for Digital Sustainability Lead at EQF level 6
python generate_curriculum.py --role DSL --eqf 6 --full --ects 60

# Generate an upskilling curriculum focusing on specific skills
python generate_curriculum.py --role DSL --eqf 6 --skills "esg_reporting,data_analytics" --ects 20

# Generate a multi-level curriculum for Software Developer for Sustainability
python generate_curriculum.py --role SDS --eqf 4,5,6 --full

# Generate comprehensive Sankey diagram for all roles and modules
python generate_sankey.py --output curriculum_flow.html
```

### Python API

```python
from dscg import CurriculumGenerator, Module, Role

# Initialize the generator
generator = CurriculumGenerator()

# Load modules and roles
generator.load_modules_from_json("data/modules.json")
generator.load_roles_from_json("data/roles.json")

# Generate curriculum
curriculum = generator.generate_curriculum(
    role_id="DSL",
    eqf_level=6,
    is_full_curriculum=True,
    target_ects=60
)

# Export in different formats
curriculum.export_as_pdf("output/dsl_curriculum.pdf")
curriculum.export_as_html("output/dsl_curriculum.html")
curriculum.export_as_scorm("output/dsl_curriculum_scorm")

# Visualize the curriculum
curriculum.generate_sankey_diagram("output/dsl_curriculum_sankey.html")
curriculum.generate_module_prerequisite_graph("output/dsl_prerequisites.png")
```

### Web Interface

The system can also be deployed as a web application:

```bash
# Start the web interface
python app.py
```

Then navigate to `http://localhost:5000` to access the web interface.

## Examples

### Example Curriculum Output (JSON)

```json
{
  "name": "Digital Sustainability Lead Curriculum (EQF Level 6)",
  "description": "Full curriculum for Digital Sustainability Lead at EQF Level 6",
  "role": {
    "id": "DSL",
    "name": "Digital Sustainability Lead",
    "description": "Drives digital sustainability initiatives within organizations",
    "main_area": "Management & Consultancy",
    "eqf_levels": [5, 6, 7],
    "core_skills": ["sustainability_strategy", "leadership", "data_analytics"]
  },
  "eqf_level": 6,
  "modules": [
    {
      "id": "DSL601",
      "name": "Introduction to Digital Sustainability",
      "description": "Fundamentals of digital sustainability concepts and principles",
      "eqf_level": 6,
      "ects_points": 5,
      "prerequisites": [],
      "delivery_methods": ["classroom", "online"],
      "module_type": ["theoretical"],
      "skills": ["sustainability_basics", "critical_thinking"]
    },
    // Additional modules...
  ],
  "total_ects": 60,
  "work_based_percentage": 30
}
```

### Example Visualization

The system produces Sankey diagrams that visualize the flow from roles to modules to skills:

```
Digital Sustainability Lead → Introduction to Digital Sustainability → sustainability_basics
                                                                    → critical_thinking
                         → Sustainability Frameworks and Standards → sustainability_regulations
                                                                  → esg_reporting
                         → Digital Technologies for Sustainability → digital_technology
                                                                  → sustainable_it
                         // Additional modules and skills...
```

## References
Wanda Saabeel & Paul Aertsen (2024). D2.1 occupational profiles and needs analysis report the roles and skills for digital professionals providing sustainability solutions. Deliverable D2.1, European Union, Brussels, Belgium, October, 11 2024.



## Contributing

We welcome contributions to improve and extend the Digital Sustainability Curriculum Generator. Please see CONTRIBUTING.md for details.

## License

This project is licensed under the Creative Commons license 4.0 B.Y. as specified in the Digital4Sustainability project documentation.

## Acknowledgements

This tool is part of the Digital4Sustainability project, funded by the European Union under project number 101140316. The project resources contained herein are publicly available under the Creative Commons license 4.0 B.Y.
