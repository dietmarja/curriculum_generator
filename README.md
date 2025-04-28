# Digital Sustainability Curriculum Generator (CG)
A modular curriculum generation system that aligns with the Digital4Sustainability project. This tool automatically generates digital sustainability curricula at various EQF levels for different professional roles.

## Key Features
- **Skill and Role Modeling:** Structured modeling of skills and professional roles
- **Modular Design:** Flexible curriculum generation with modular components
- **EQF Alignment:** Support for European Qualification Framework levels 4-8
- **Work-based Learning:** Integration of theoretical, practical, and work-based modules
- **Dynamic Semester Assignment:** Intelligent distribution of modules across semesters
- **Learning Outcomes Generation in Case it ia missing:** Automatic generation of Bloom's taxonomy-aligned learning outcomes
- **Multiple Export Formats:** HTML, JSON, PDF, SCORM, and xAPI

## Project Structure
The project is organized as follows:

```
dscg/
├── package/
│   ├── models.py        # Core curriculum generation classes
│   └── enhancements.py  # Extended functionality
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
├── generate_curriculum.py     # Main script for curriculum generation
└── generate_all_curricula.py  # Batch generation script
data/
├── modules.json     # Module definitions
├── roles.json      # Role definitions
└── skills.json     # Skill definitions
```



## Core Classes and Methods

The following table provides an overview of the main classes and their methods:

| Method                | CurriculumGenerator (models.py) | Curriculum (models.py) | Module (models.py) | Role (models.py) |
|-----------------------|----------------------------------|-------------------------|--------------------|------------------|
| Constructor           | `__init__()`                    | `__init__(role, eqf_level, modules, ...)` | `__init__(id, name, ...)` | `__init__(id, name, ...)` |
| Data Loading          | `load_modules_from_json(json_file)` `load_roles_from_json(json_file)` | | | |
| Curriculum Generation | `generate_curriculum(role_id, eqf_level, ...)` `generate_additional_modules(base_modules, ...)` `generate_learning_outcomes(module_name, ...)` | | | |
| Module Management     | `distribute_modules_to_semesters(modules, ...)` `finalize_curriculum(curriculum)` `ensure_work_based_properties(curriculum)` | `add_module(module)` `remove_module(module_id)` | | |
| Export Functions      | | `export_as_html(output_path)` `export_as_json(output_path)` | | |
| Accessors/Helpers     | `get_role(role_id)` | `get_modules_by_semester(semester)` `calculate_total_ects()` | | |

## Key Enhancement Methods

The following methods have been implemented or improved to enhance curriculum generation:

### CurriculumGenerator Class

#### `finalize_curriculum(curriculum)`

- Performs final validation and cleanup of the curriculum
- Detects and resolves duplicate module names using multiple renaming strategies
- Ensures all modules have proper learning outcomes
- Verifies that all required curriculum attributes are set
- Properly identifies and tags work-based modules

#### `generate_learning_outcomes(module_name, module_type, eqf_level, thematic_area)`

- Generates detailed learning outcomes using Bloom's taxonomy
- Adjusts the language and complexity based on the EQF level
- Creates specific outcomes reflecting module content and type
- Produces a balanced mix of cognitive, practical, and attitudinal outcomes
- Avoids redundant phrasing through improved verb selection

#### `generate_additional_modules(base_modules, target_ects, eqf_level, role_id)`

- Creates new modules to reach the target ECTS points
- Ensures unique naming using various strategies
- Assigns appropriate module IDs aligned with the role
- Generates specific learning outcomes for each new module
- Prioritizes work-based modules when needed to meet target percentages

#### `distribute_modules_to_semesters(modules, program_duration)`

- Intelligently assigns modules to semesters based on prerequisites
- Ensures balanced ECTS load across semesters
- Respects module dependencies and sequencing requirements
- Distributes work-based modules appropriately throughout the curriculum

#### `ensure_work_based_properties(curriculum)`

- Identifies modules that should be tagged as work-based learning
- Ensures proper calculation of work-based learning percentage
- Maintains alignment with dual education principles

## Command-Line Usage

The main script for generating curricula is `scripts/generate_curriculum.py`:

```
python scripts/generate_curriculum.py --role DSL --eqf 7 --output output/curricula/curriculum_dsl_7.html
```

#### `finalize_curriculum(curriculum)`
- Performs final validation and cleanup of the curriculum
- Detects and resolves duplicate module names using multiple renaming strategies
- Ensures all modules have proper learning outcomes
- Verifies that all required curriculum attributes are set
- Properly identifies and tags work-based modules

#### `generate_learning_outcomes(module_name, module_type, eqf_level, thematic_area)`
- Generates detailed learning outcomes using Bloom's taxonomy
- Adjusts the language and complexity based on the EQF level
- Creates specific outcomes reflecting module content and type
- Produces a balanced mix of cognitive, practical, and attitudinal outcomes
- Avoids redundant phrasing through improved verb selection

#### `generate_additional_modules(base_modules, target_ects, eqf_level, role_id)`
- Creates new modules to reach the target ECTS points
- Ensures unique naming using various strategies
- Assigns appropriate module IDs aligned with the role
- Generates specific learning outcomes for each new module
- Prioritizes work-based modules when needed to meet target percentages

#### `distribute_modules_to_semesters(modules, program_duration)`
- Intelligently assigns modules to semesters based on prerequisites
- Ensures balanced ECTS load across semesters
- Respects module dependencies and sequencing requirements
- Distributes work-based modules appropriately throughout the curriculum

#### `ensure_work_based_properties(curriculum)`
- Identifies modules that should be tagged as work-based learning
- Ensures proper calculation of work-based learning percentage
- Maintains alignment with dual education principles

## Command-Line Usage
The main script for generating curricula is `scripts/generate_curriculum.py`:

```bash
python scripts/generate_curriculum.py --role DSL --eqf 7 --output output/curricula/curriculum_dsl_7.html
Command-Line Arguments

--role: Role ID (e.g., DSL for Digital Sustainability Lead)
--eqf: EQF level (4-8)
--output: Output file path (supports .html, .json)
--type: Curriculum type (full or upskilling)
--skills: Optional list of target skills for upskilling curriculum
--modules-json: Path to modules JSON file (default: data/modules.json)
--roles-json: Path to roles JSON file (default: data/roles.json)
--debug: Enable debug logging

Troubleshooting
Common Issues
Missing or Incorrect ECTS Points

Check that modules have valid ECTS points defined
Verify that calculate_total_ects() is being called before HTML export

Semester Assignment Problems

Ensure distribute_modules_to_semesters() is being called in the generation process
Check that module prerequisites are correctly defined

Duplicate Module Names

Verify that finalize_curriculum() is being called before curriculum export
Check for duplicates in the source module data

Generic Learning Outcomes

Make sure generate_learning_outcomes() is being used for all modules
Verify the method has the proper Bloom's taxonomy verbs for each EQF level

Work-based Learning Percentage

Ensure modules with work-based content have the is_work_based flag set to True
Check that ensure_work_based_properties() is being called in finalize_curriculum()
Verify that both calculate_total_ects() and calculate_work_based_percentage() are up to date

Redundant Learning Outcomes

Check for redundant phrases like "innovate innovative solutions" in learning outcomes
Ensure the _select_unique_verb helper method is being used correctly

Future Enhancements

Web Interface: Develop a user-friendly web interface for curriculum generation and visualization
More Export Formats: Add support for additional export formats (e.g., docx, xlsx)
Interactive Visualizations: Enhance data visualization with interactive charts and diagrams
Curriculum Validation: Implement more sophisticated validation against educational standards
AI-driven Module Recommendations: Add AI capabilities to suggest optimal modules for specific roles
Improved Learning Outcomes: Further refine the learning outcomes generator to eliminate redundancies
Customizable Templates: Allow users to create and save custom curriculum templates
Feedback Integration: Incorporate user feedback to improve module recommendations

