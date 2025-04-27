# Digital Sustainability Curriculum Generator (CG)

A modular curriculum generation system that aligns with the Digital4Sustainability project. This tool automatically generates digital sustainability curricula at various EQF levels for different professional roles.

## Key Features

- **Multiple Export Formats**: HTML, JSON, PDF, SCORM, and xAPI
- **Skill and Role Modeling**: Structured modeling of skills and professional roles
- **Modular Design**: Flexible curriculum generation with modular components
- **EQF Alignment**: Support for European Qualification Framework levels 4-8
- **Work-based Learning**: Integration of theoretical, practical, and work-based modules
- **Dynamic Semester Assignment**: Intelligent distribution of modules across semesters
- **Learning Outcomes Generation**: Automatic generation of Bloom's taxonomy-aligned learning outcomes

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

| Method | CurriculumGenerator (models.py) | Curriculum (models.py) | Module (models.py) | Role (models.py) |
|--------|----------------------------------|------------------------|---------------------|------------------|
| **Constructor** | `__init__()` | `__init__(role, eqf_level, modules, ...)` | `__init__(id, name, ...)` | `__init__(id, name, ...)` |
| **Data Loading** | `load_modules_from_json(json_file)` <br> `load_roles_from_json(json_file)` | | | |
| **Curriculum Generation** | `generate_curriculum(role_id, eqf_level, ...)` <br> `generate_additional_modules(base_modules, ...)` <br> `generate_learning_outcomes(module_name, ...)` | | | |
| **Module Management** | `distribute_modules_to_semesters(modules, ...)` <br> `finalize_curriculum(curriculum)` | `add_module(module)` <br> `remove_module(module_id)` | | |
| **Export Functions** | | `export_as_html(output_path)` <br> `export_as_json(output_path)` | | |
| **Accessors/Helpers** | `get_role(role_id)` | `get_modules_by_semester(semester)` <br> `calculate_total_ects()` | | |

## Key Enhancement Methods

The following methods have been implemented or improved to enhance curriculum generation:

### CurriculumGenerator Class

1. **`finalize_curriculum(curriculum)`**
   - Performs final validation and cleanup of the curriculum
   - Detects and resolves duplicate module names using multiple renaming strategies
   - Ensures all modules have proper learning outcomes
   - Verifies that all required curriculum attributes are set

2. **`generate_learning_outcomes(module_name, module_type, eqf_level, thematic_area)`**
   - Generates detailed learning outcomes using Bloom's taxonomy
   - Adjusts the language and complexity based on the EQF level
   - Creates specific outcomes reflecting module content and type
   - Produces a balanced mix of cognitive, practical, and attitudinal outcomes

3. **`generate_additional_modules(base_modules, target_ects, eqf_level, role_id)`**
   - Creates new modules to reach the target ECTS points
   - Ensures unique naming using various strategies
   - Assigns appropriate module IDs aligned with the role
   - Generates specific learning outcomes for each new module

4. **`distribute_modules_to_semesters(modules, program_duration)`**
   - Intelligently assigns modules to semesters based on prerequisites
   - Ensures balanced ECTS load across semesters
   - Respects module dependencies and sequencing requirements

## Command-Line Usage

The main script for generating curricula is `scripts/generate_curriculum.py`:

```bash
python scripts/generate_curriculum.py --role DSL --eqf 7 --output output/curricula/curriculum_dsl_7.html
```

### Command-Line Arguments

- `--role`: Role ID (e.g., DSL for Digital Sustainability Lead)
- `--eqf`: EQF level (4-8)
- `--output`: Output file path (supports .html, .json)
- `--type`: Curriculum type (full or upskilling)
- `--skills`: Optional list of target skills for upskilling curriculum
- `--modules-json`: Path to modules JSON file (default: data/modules.json)
- `--roles-json`: Path to roles JSON file (default: data/roles.json)
- `--debug`: Enable debug logging

## Troubleshooting

### Common Issues

1. **Missing or Incorrect ECTS Points**
   - Check that modules have valid ECTS points defined
   - Verify that `calculate_total_ects()` is being called before HTML export

2. **Semester Assignment Problems**
   - Ensure `distribute_modules_to_semesters()` is being called in the generation process
   - Check that module prerequisites are correctly defined

3. **Duplicate Module Names**
   - Verify that `finalize_curriculum()` is being called before curriculum export
   - Check for duplicates in the source module data

4. **Generic Learning Outcomes**
   - Make sure `generate_learning_outcomes()` is being used for all modules
   - Verify the method has the proper Bloom's taxonomy verbs for each EQF level

## Recommended Fixes for Current Issues

Based on the latest output (`test_dsl_7.html`), the following fixes are recommended:

1. **Ensure Role and EQF Data is Loaded Properly**
   - Verify that roles.json contains the proper program_duration for each EQF level
   - Check that the expected ECTS for each EQF level is correctly defined

2. **Fix Module Selection**
   - Ensure modules with proper role-specific IDs are being created
   - Verify that enough modules are being generated to reach the target ECTS

3. **Fix Semester Assignment**
   - Verify that the distribute_modules_to_semesters method is being called
   - Check that module.semester values are being correctly set

4. **Fix Program Learning Outcomes**
   - Ensure role objects have program_learning_outcomes for each EQF level
   - Verify that these are being assigned to the curriculum object

5. **Fix Work-based Learning**
   - Ensure at least some modules have is_work_based=True
   - Verify that the work-based percentage is calculated correctly

6. **Fix Export Functionality**
   - Check that the Curriculum.export_as_html method is correctly formatting all values
   - Ensure no attributes are None before they're used in the HTML template

## Future Enhancements

1. **Web Interface**: Develop a user-friendly web interface for curriculum generation and visualization
2. **More Export Formats**: Add support for additional export formats (e.g., docx, xlsx)
3. **Interactive Visualizations**: Enhance data visualization with interactive charts and diagrams
4. **Curriculum Validation**: Implement more sophisticated validation against educational standards
5. **AI-driven Module Recommendations**: Add AI capabilities to suggest optimal modules for specific roles
