# Digital Sustainability Curriculum Generator (DSCG)

A comprehensive toolkit for generating, analyzing, and evaluating modular, outcome-based curricula for digital sustainability education. The DSCG supports both full educational programs and specific micro-credential pathways across EQF levels 4-8.

## Key Features

- **Full & Specific Curricula**: Generate complete educational programs or targeted micro-credential pathways
- **Multi-level Support**: Design curricula across EQF levels 4-8 for various digital sustainability roles
- **Standards Compliance**: Built-in validation against European educational frameworks and standards
- **Stackable Credentials**: Create and visualize flexible, personalized learning pathways
- **Rich Evaluation**: Comprehensive assessment against accreditation and educational criteria
- **Work-based Learning**: Support for dual principle education with industry-aligned components
- **Competency Mapping**: Visual mapping between job roles, competencies, and learning outcomes
- **Recognition Mechanisms**: European and national recognition pathways with cross-border portability
- **Accreditation Support**: Quality assurance, provider information, and diploma supplement previews
- **User Group Targeting**: Clear sections for educators, accreditation specialists, students, and industry
- **Web Interface**: User-friendly web application for curriculum management and visualization
- **Command-line Tools**: Powerful scripts for batch processing and automation

## Installation

### Requirements

- Python 3.8 or higher
- pip package manager
- Recommended: virtualenv or conda for environment management

### CLI Installation

1. Clone the repository:
git clone https://github.com/yourusername/dscg.git
cd dscg

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install required packages:
pip install -r requirements.txt

4. Create necessary directories:
mkdir -p input/modules input/roles input/standards dscg/static/css dscg/static/js output/curricula output/enhanced_curricula

### Web Interface Installation

1. Follow steps 1-4 from CLI Installation above.

2. Install Flask and web dependencies if not already included in requirements.txt:
pip install flask werkzeug jinja2 pandas matplotlib seaborn

3. Ensure the templates folder exists with all required template files:
mkdir -p templates
Template files should be copied to the templates directory
(base.html, index.html, batch_generate.html, etc.)

4. Configure the web server (optional for production):
For production with gunicorn (install with: `pip install gunicorn`)
For production with Apache or Nginx, set up WSGI configuration (`pip install mod_wsgi` for Apache)

## Usage

### Command Line Interface

#### Curriculum Generation

```
#Generate a curriculum for a specific role and EQF level:
python scripts/generate_curriculum.py --role DAN --eqf 6 --output-dir output/curricula
```

```
#Generate all curricula for all defined roles and EQF levels:
#python scripts/batch_generate_curricula.py --output-dir output/curricula
python scripts/batch_enhance_curricula_v2.py --input-dir output/curricula --output-dir output/enhanced_curricula --modules-json input/modules.json --roles-json input/roles.json --static-dir dscg/static
```



#### Enhanced Curriculum Generation with Accreditation Support

Enhance an existing curriculum with competency mapping, stacking pathways, and recognition mechanisms:
python scripts/enhance_curriculum_v2.py --input output/curricula/curriculum_DAN_6.html --output output/enhanced_curricula/curriculum_DAN_6_enhanced.html --modules-json input/modules.json --roles-json input/roles.json --static-dir dscg/static

Batch enhance multiple curricula:
python scripts/batch_enhance_curricula_v2.py --input-dir output/curricula --output-dir output/enhanced_curricula --modules-json input/modules.json --roles-json input/roles.json --static-dir dscg/static

#### Micro-credential Management

Generate micro-credential sample data:
python scripts/microcredential_curriculum_builder.py --create-sample --data-dir input

Build a role-based specific curriculum from micro-credentials:
python scripts/microcredential_curriculum_builder.py --build-curriculum --role-id DSL --eqf-level 5 --data-dir input --output-dir output/specific_curricula

Create a custom curriculum from selected micro-credentials:
python scripts/microcredential_curriculum_builder.py --build-curriculum --micro-credentials MC001,MC003,MC007 --name "Green Computing Fundamentals" --description "A focused curriculum on green computing basics" --data-dir input --output-dir output/specific_curricula

#### Analysis & Quality Improvement

Fix compliance issues in existing curricula:
python scripts/fix_curriculum_issues.py --input-dir output/curricula --output-dir output/curricula_fixed --standards-dir input/standards

Evaluate curricula against standards and requirements:
python scripts/curriculum_evaluation_framework.py --input-dir output/curricula_fixed --output-dir output/assessment --include-specific

Generate curriculum summary and validation report:
python scripts/enhanced_curriculum_summary.py --output-dir output/curricula --modules-json input/modules/modules.json

#### Visualization & Mapping

Generate competence matrix:
python scripts/generate_competence_matrix.py --modules-json input/modules/modules.json --roles-json input/roles/roles.json --output-dir output/matrix --include-heatmap

Visualize stacking paths for micro-credentials:
python scripts/visualize_stacking_paths.py --data-dir input --micro-credentials-file micro_credentials.json --roles-file roles/roles.json --output-dir output/visualizations

### Web Interface

1. Start the web application:
python app.py

2. Open your browser and go to: `http://localhost:5000`

3. Web Interface Features:
   - **Dashboard**: Overview of available curricula, roles, modules, and micro-credentials
   - **Generate Curriculum**: Create a new curriculum for a specific role and EQF level
   - **Batch Generate**: Generate multiple curricula for different roles and EQF levels
   - **View Curricula**: Browse, download, and manage generated curricula
   - **Fix Curricula**: Automatically correct accreditation issues in existing curricula
   - **Micro-credentials**: Manage micro-credentials and build specific curricula
   - **Competence Matrix**: Generate and visualize role-module competence mappings
   - **Visualizations**: Create stacking path and competence visualizations
   - **Assessment**: Evaluate curricula against standards and accreditation criteria
   - **Uploads**: Manage data files (modules, roles, standards)

## Enhanced Curriculum Features

The enhanced curriculum generator (v2) adds several key features to support T3.2, T3.4, and accreditation requirements:

### Competency Mapping
- Visual representation of relationships between job roles, competencies, and learning outcomes
- Color-coded skill tags showing skill matches between roles and modules
- Direct connection between competencies and assessment criteria

### Stacking Framework
- Micro-credential definitions with clear module compositions
- Visual stacking pathways showing progression from foundation to full qualification
- Credit accumulation visualization with ECTS values

### Recognition Mechanisms
- European framework alignment (EQF, ECTS, ESG, ESCO)
- National qualification framework mapping for multiple countries
- Recognition procedures and cross-border portability examples

### Accreditation Support
- Provider information with accreditation status and period
- Quality assurance system details and documentation
- Curriculum governance structure and functions
- Certification processes and technology infrastructure

### User-Targeted Information
- Clear table of contents with user group tags (educators, accreditation specialists, students, industry)
- Section organization following accreditation requirements
- Diploma supplement preview following Europass standard

## Example Data Flow

1. **Prepare Input Data**:
   - Define role profiles in `input/roles.json`
   - Define modules in `input/modules.json`
   - Set up standards in `input/standards/`

2. **Generate Curricula**:
   - Generate curricula for all roles and EQF levels
   - Create specific curricula using micro-credentials

3. **Enhance Curricula**:
   - Add competency mapping and stacking frameworks
   - Include recognition mechanisms and accreditation information

4. **Improve Quality**:
   - Fix accreditation issues in generated curricula
   - Validate against educational standards

5. **Analyze & Visualize**:
   - Generate competence matrix and visualizations
   - Create assessment reports
   - Visualize stacking paths

## Project Structure
bash
```
curriculum_generator/                        # Project root
├── app.py                                   # Web application entry point
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
│   ├── generate_curriculum.py               # Curriculum generation script
│   ├── batch_generate_curricula.py          # Batch curriculum generation script
│   ├── enhance_curriculum_v2.py             # Enhanced curriculum script with recognition
│   ├── batch_enhance_curricula_v2.py        # Batch enhance curricula script
│   ├── fix_curriculum_issues.py             # Fix compliance issues script
│   └── curriculum_evaluation_framework.py   # Curriculum assessment script
├── templates/                               # HTML templates for web interface
├── static/                                  # Static assets for web interface
│   ├── css/                                 # Stylesheets
│   ├── js/                                  # JavaScript files
│   └── img/                                 # Images and icons
└── output/                                  # Generated output
├── curricula/                           # Generated curricula
├── enhanced_curricula/                  # Enhanced curricula with recognition mechanisms
├── assessment/                          # Evaluation reports
├── matrix/                              # Competence matrices
├── visualizations/                      # Visual representations
└── specific_curricula/                  # Micro-credential-based curricula
```




## Standards Alignment

The system aligns with the following European standards:

- **EQF**: Levels 4–8 structuring; outcome-based design and transparency across national systems
- **ECTS**: Credit weighting, workload calculation, and validation of learning modules
- **ECVET**: Modular and transferable design for vocational and work-based learning
- **e-CF**: Structuring ICT competences aligned to EQF and supporting digital role profiles
- **ESCO**: Mapping of learning outcomes to labor market competences and job roles
- **GreenComp**: Embedding sustainability competencies into transversal learning outcomes
- **EU Micro-Credentials**: Quality, granularity, and stackability for short-form learning units
- **Tuning**: Alignment and calibration of learning outcomes from program to module level


## Current Development Plan

Create a curriculum_accreditation_check.py script that will:

Analyze curriculum HTML files against accreditation standards
Check for required components like competency frameworks, recognition mechanisms
Validate ECTS credits against EQF level requirements
Analyze learning outcomes for alignment with standards
Generate detailed reports on compliance issues
Provide specific recommendations for improvements


Implement a file-based micro-credential system:

Create a micro-credential data structure following standard_microcredentials.json format
Develop schema validation for micro-credential data files
Build import/export functionality for micro-credential definitions
Implement stacking rules and relationship management
Support granularity levels and proper credit values
Create visualization tools for stacking pathways


Integrate with existing system:

Ensure compatibility with the batch processing scripts
Use existing data structures and file formats
Support both CLI and potential web interface usage
Update enhance_curriculum_v2.py to use file-based micro-credentials


Focus on standards compliance:

Implement checks for all standards mentioned in the README (EQF, ECTS, ECVET, e-CF, ESCO, GreenComp)
Pay special attention to micro-credentials and stackability validation
Address the specific areas mentioned in "Current Work Focus"


Generate actionable outputs:

Provide detailed compliance reports
Create visual representation of compliance status
Generate recommendations for fixing issues




## Roadmap

- Integration of Bib-tex reference so that the curricula include a reading list
- Export to **xAPI/SCORM** for LMS integration

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- European Qualifications Framework (EQF)
- European Credit Transfer and Accumulation System (ECTS)
- European Skills, Competences, Qualifications and Occupations (ESCO)
- GreenComp: The European sustainability competence framework
- European Credit System for Vocational Education and Training (ECVET)
- European Standards and Guidelines for Quality Assurance (ESG)
- European Approach to Micro-credentials
