# Digital Sustainability Curriculum Generator (CG)
A suite of Python scripts for modular curriculum generation and assessment that aligns with the Digital4Sustainability project. 
They automatically generate digital sustainability curricula at various EQF levels for different professional roles and assess their quality. 

## Key Features
- **Skill and Role Modeling:** Structured modeling of skills and professional roles
- **Modular Design:** Flexible curriculum generation with modular components
- **EQF Alignment:** Support for European Qualification Framework levels 4-8
- **Work-based Learning:** Integration of theoretical, practical, and work-based modules
- **Dynamic Semester Assignment:** Intelligent distribution of modules across semesters
- **Learning Outcomes Generation in Case it is missing:** Automatic generation of Bloom's taxonomy-aligned learning outcomes
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
├── assess_modules.py          # Script to assess the suitabiliy of the modules in modules.py for curriculum generation
├── generate_curriculum.py     # Main script for curriculum generation
└── generate_all_curricula.py  # Batch generation script to create all curricula
data/
├── modules.json     # Module definitions
├── roles.json      # Role definitions
└── skills.json     # Skill definitions
```



## Input Files
Essentially, curricula are generated on the basis of two input files

- roles.json and
- modules.json

The structure for each of them is defined via a JSON schema file that aligns with educational standards, frameworks and best practices like Tuning approach, 
EQF-levels and Bloom's taxonomy verbs. The validity of the schemas and the files build up on them are essential for the quality of the curricula generated. 





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
```


Running a batch job for generating all curricula can be done via `scripts/generate_all_curricula.py`:

```bash
python scripts/generate_all_curricula.py
```

A detailed analysis of the modules in modules.json is initiated with `scripts/assess_modules.py`:

```bash
python scripts/assess_modules.py > assessment_report.txt
```




## Future Enhancements

- Web Interface: Develop a user-friendly web interface for curriculum generation and visualization
- Integration of Literature from Googe Scholar that allows creating curricular which including a list of literature
- More transparancy on modules of the module repository not used and on modules not found in the module repository
- Interactive Visualizations: Enhance data visualization with interactive charts and diagrams
- Curriculum Validation: Implement more sophisticated validation against educational standards
- AI-driven Module Recommendations: Add AI capabilities to suggest optimal modules for specific roles
- Customizable Templates: Allow users to create and save custom curriculum templates
- Feedback Integration: Incorporate user feedback to improve module recommendations

