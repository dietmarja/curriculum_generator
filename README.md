# Digital Sustainability Curriculum Generator (DSCG)

A comprehensive toolkit for generating, analyzing, and evaluating modular, outcome-based curricula for digital sustainability education. The DSCG supports both full educational programs and specific micro-credential pathways across EQF levels 4-8.

## Key Features

- **Full & Specific Curricula**: Generate complete educational programs or targeted micro-credential pathways
- **Multi-level Support**: Design curricula across EQF levels 4-8 for various digital sustainability roles
- **Standards Compliance**: Built-in validation against European educational frameworks and standards
- **Stackable Credentials**: Create and visualize flexible, personalized learning pathways
- **Rich Evaluation**: Comprehensive assessment against accreditation and educational criteria
- **Work-based Learning**: Support for dual principle education with industry-aligned components
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
./create_directories.sh

### Web Interface Installation

1. Follow steps 1-4 from CLI Installation above.

2. Install Flask and web dependencies if not already included in requirements.txt:
pip install flask werkzeug jinja2 pandas matplotlib seaborn

3. Ensure the templates folder exists with all required template files:
mkdir -p templates
Template files should be copied to the templates directory
(base.html, index.html, batch_generate.html, etc.)

4. Configure the web server (optional for production):
For production with gunicorn (install with: pip install gunicorn)
pip install gunicorn
For production with Apache or Nginx, set up WSGI configuration
pip install mod_wsgi  # For Apache

## Usage

### Web Interface

1. Start the web application:
python app.py

2. Open your browser and go to:
http://localhost:5000

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

4. Example Web Interface Workflow:
- Upload module and role data via the Uploads page
- Generate a curriculum using the Generate Curriculum form
- Fix accreditation issues with the Fix Curricula tool
- Assess the fixed curriculum with the Assessment tool
- Visualize competencies and stacking paths with the Visualizations tool


### Command Line Interface

#### Curriculum Generation

# Generate a curriculum for a specific role and EQF level:
```
python scripts/generate_curriculum.py --role DSL --eqf 7 
--output output/curricula/curriculum_DSL_7.html 
--modules-json input/modules/modules.json 
--roles-json input/roles/roles.json
```

```python
# Generate all curricula for all defined roles and EQF levels:
```
python scripts/generate_all_curricula.py 
--output-dir output/curricula 
--modules-json input/modules/modules.json 
--roles-json input/roles/roles.json
```

#### Micro-credential Management

# Generate micro-credential sample data:
```
python scripts/microcredential_curriculum_builder.py --create-sample --data-dir input
```

# Build a role-based specific curriculum from micro-credentials:
```
python scripts/microcredential_curriculum_builder.py --build-curriculum 
--role-id DSL --eqf-level 5 
--data-dir input --output-dir output/specific_curricula
```

# Create a custom curriculum from selected micro-credentials:
```
python scripts/microcredential_curriculum_builder.py --build-curriculum 
--micro-credentials MC001,MC003,MC007 
--name "Green Computing Fundamentals" 
--description "A focused curriculum on green computing basics" 
--data-dir input --output-dir output/specific_curricula
```

#### Analysis & Quality Improvement

# Fix compliance issues in existing curricula:
```
python scripts/fix_curriculum_issues.py 
--input-dir output/curricula 
--output-dir output/curricula_fixed 
--standards-dir input/standards
```

# Evaluate curricula against standards and requirements:
```
python scripts/curriculum_evaluation_framework.py 
--input-dir output/curricula_fixed 
--output-dir output/assessment 
--include-specific
```

# Generate curriculum summary and validation report:
```
python scripts/improved_curriculum_summary.py 
--output-dir output/curricula 
--modules-json input/modules/modules.json
```

#### Visualization & Mapping

# Generate competence matrix:
```
python scripts/generate_competence_matrix.py 
--modules-json input/modules/modules.json 
--roles-json input/roles/roles.json 
--output-dir output/matrix 
--include-heatmap
```

# Visualize stacking paths for micro-credentials:
```
python scripts/visualize_stacking_paths.py 
--data-dir input 
--micro-credentials-file micro_credentials.json 
--roles-file roles/roles.json 
--output-dir output/visualizations
```
---

## Example Data Flow

1. **Prepare Input Data**:
   - Define role profiles in 
   - Define modules in 
   - Set up standards in 

2. **Generate Curricula**:
   - Generate curricula for all roles and EQF levels
   - Create specific curricula using micro-credentials

3. **Improve Quality**:
   - Fix accreditation issues in generated curricula
   - Validate against educational standards

4. **Analyze & Visualize**:
   - Generate competence matrix and visualizations
   - Create assessment reports
   - Visualize stacking paths

## Project Structure
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
│   ├── batch_enhance_curricula.py           # Batch enhance curricula script
│   ├── enhance_curriculum.py                # Enhance curriculum script
│   └── enhanced_curriculum_summary.py       # Enhanced curriculum summary script
├── templates/                               # HTML templates for web interface
│   ├── base.html                            # Base template with navigation and layout
│   ├── index.html                           # Dashboard template
│   ├── curriculums.html                     # Curriculum listing template
│   ├── generate.html                        # Curriculum generation form
│   ├── batch_generate.html                  # Batch generation interface
│   ├── view_curriculum.html                 # Curriculum viewer template
│   ├── fixed_curricula.html                 # Fixed curricula listing
│   ├── micro_credentials.html               # Micro-credential management
│   ├── view_matrix.html                     # Competence matrix viewer
│   ├── view_assessment.html                 # Assessment report viewer
│   ├── uploads.html                         # File management interface
│   ├── visualizations.html                  # Visualizations gallery
│   ├── 404.html                             # Custom 404 error page
│   ├── 500.html                             # Custom 500 error page
│   └── partials/                            # Reusable template components
├── static/                                  # Static assets for web interface
│   ├── css/                                 # Stylesheets
│   ├── js/                                  # JavaScript files
│   ├── img/                                 # Images and icons
│   ├── fonts/                               # Font files
│   ├── lib/                                 # Third-party libraries
│   └── favicon.ico                          # Favicon
└── output/                                  # Generated output
    ├── curricula/                           # Generated curricula
    ├── curricula_fixed/                     # Fixed curricula
    ├── assessment/                          # Evaluation reports
    ├── matrix/                              # Competence matrices
    ├── visualizations/                      # Visual representations
    ├── specific_curricula/                  # Micro-credential-based curricula
    └── micro_credentials/                   # Micro-credential definitions
```


## Web Interface Components

The web interface consists of several key components:

### Templates

The  directory contains HTML templates for the web interface:

- **base.html**: The foundational template with navigation, common CSS, and layout
- **index.html**: Dashboard showing statistics and quick actions
- **generate.html**: Form for generating individual curricula
- **batch_generate.html**: Interface for generating multiple curricula
- **curriculums.html**: List view of all generated curricula
- **view_curriculum.html**: Viewer for individual curriculum content
- **fixed_curricula.html**: List view of fixed curricula
- **micro_credentials.html**: Management interface for micro-credentials
- **view_matrix.html**: Viewer for competence matrix visualizations
- **view_assessment.html**: Viewer for assessment reports
- **uploads.html**: Interface for managing input files
- **visualizations.html**: Gallery of visualizations

### Web Application (app.py)

The main Flask application provides routes for:

- Dashboard view
- Curriculum generation and management
- Micro-credential management
- Assessment and visualization tools
- File uploading and management

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

## Production Deployment of Web Interface

For production deployment of the web interface:

1. Set up a dedicated server or cloud instance.

2. Install required dependencies:
pip install -r requirements.txt
pip install gunicorn  # or use another WSGI server

3. Ensure all template files are correctly placed in the templates directory:
ls -la templates/
Should show all template files (base.html, index.html, etc.)

4. Configure a reverse proxy (e.g., Nginx or Apache):

**Nginx Example Config:**
server {
listen 80;
server_name your-dscg-server.com;
   location / {
       proxy_pass http://127.0.0.1:8000;
       proxy_set_header Host ;
       proxy_set_header X-Real-IP ;
   }
}

5. Set up a WSGI server:
gunicorn -w 4 -b 127.0.0.1:8000 app:app

6. Configure systemd for automatic startup (on Linux):
Create /etc/systemd/system/dscg.service
[Unit]
Description=Digital Sustainability Curriculum Generator
After=network.target
[Service]
User=dscg
WorkingDirectory=/path/to/dscg
ExecStart=/path/to/venv/bin/gunicorn -w 4 -b 127.0.0.1:8000 app:app
Restart=always
[Install]
WantedBy=multi-user.target

7. Enable and start the service:
sudo systemctl enable dscg
sudo systemctl start dscg

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch ()
3. Commit your changes ([feature/amazing-feature 8dab8d3] Add some amazing feature
 56 files changed, 5342 insertions(+)
 create mode 100644 digital-sustainability-curriculum-generator/.DS_Store
 create mode 100644 digital-sustainability-curriculum-generator/LICENSE
 create mode 100644 digital-sustainability-curriculum-generator/README.md
 create mode 100644 digital-sustainability-curriculum-generator/config.json
 create mode 100644 digital-sustainability-curriculum-generator/data/modules.json
 create mode 100644 digital-sustainability-curriculum-generator/data/roles copy.json
 create mode 100644 digital-sustainability-curriculum-generator/data/roles.json
 create mode 100644 digital-sustainability-curriculum-generator/data/skills.json
 create mode 100644 digital-sustainability-curriculum-generator/dscg/.DS_Store
 create mode 100644 digital-sustainability-curriculum-generator/dscg/__init__.py
 create mode 100644 digital-sustainability-curriculum-generator/dscg/__pycache__/__init__.cpython-39.pyc
 create mode 100644 digital-sustainability-curriculum-generator/dscg/exporters/__init__.py
 create mode 100644 digital-sustainability-curriculum-generator/dscg/exporters/html_exporter.py
 create mode 100644 digital-sustainability-curriculum-generator/dscg/exporters/json_exporter.py
 create mode 100644 digital-sustainability-curriculum-generator/dscg/exporters/pdf_exporter.py
 create mode 100644 digital-sustainability-curriculum-generator/dscg/exporters/scorm_exporter.py
 create mode 100644 digital-sustainability-curriculum-generator/dscg/exporters/xapi_exporter.py
 create mode 100644 digital-sustainability-curriculum-generator/dscg/generator.py
 create mode 100644 digital-sustainability-curriculum-generator/dscg/package/.DS_Store
 create mode 100644 digital-sustainability-curriculum-generator/dscg/package/__pycache__/models.cpython-39.pyc
 create mode 100644 digital-sustainability-curriculum-generator/dscg/package/models copy 2.py
 create mode 100644 digital-sustainability-curriculum-generator/dscg/package/models copy.py
 create mode 100644 digital-sustainability-curriculum-generator/dscg/package/models.py
 create mode 100644 digital-sustainability-curriculum-generator/dscg/utils/__init__.py
 create mode 100644 digital-sustainability-curriculum-generator/dscg/utils/config.py
 create mode 100644 digital-sustainability-curriculum-generator/dscg/utils/learning_outcomes.py
 create mode 100644 digital-sustainability-curriculum-generator/dscg/utils/validation.py
 create mode 100644 digital-sustainability-curriculum-generator/dscg/visualization/__init__.py
 create mode 100644 digital-sustainability-curriculum-generator/dscg/visualization/prerequisites.py
 create mode 100644 digital-sustainability-curriculum-generator/dscg/visualization/sankey.py
 create mode 100644 digital-sustainability-curriculum-generator/misc/file_structure+creation.txt
 create mode 100644 digital-sustainability-curriculum-generator/output/.DS_Store
 create mode 100644 digital-sustainability-curriculum-generator/output/curriculum.html
 create mode 100644 digital-sustainability-curriculum-generator/requirements.txt
 create mode 100644 digital-sustainability-curriculum-generator/scripts/generate_curriculum.py
 create mode 100644 digital-sustainability-curriculum-generator/scripts/generate_sankey.py
 create mode 100644 digital-sustainability-curriculum-generator/scripts/setup_data.py
 create mode 100644 digital-sustainability-curriculum-generator/setup.py
 create mode 100644 digital-sustainability-curriculum-generator/templates/.DS_Store
 create mode 100644 digital-sustainability-curriculum-generator/templates/html/curriculum.html
 create mode 100644 digital-sustainability-curriculum-generator/templates/html/module.html
 create mode 100644 digital-sustainability-curriculum-generator/templates/pdf/curriculum.html
 create mode 100644 digital-sustainability-curriculum-generator/tests/__init__.py
 create mode 100644 digital-sustainability-curriculum-generator/tests/test_exporters.py
 create mode 100644 digital-sustainability-curriculum-generator/tests/test_generator.py
 create mode 100644 digital-sustainability-curriculum-generator/tests/test_models.py
 create mode 100644 digital-sustainability-curriculum-generator/tree_structure.txt
 create mode 100644 digital-sustainability-curriculum-generator/web/.DS_Store
 create mode 100644 digital-sustainability-curriculum-generator/web/app.py
 create mode 100644 digital-sustainability-curriculum-generator/web/templates/base.html
 create mode 100644 digital-sustainability-curriculum-generator/web/templates/curriculum.html
 create mode 100644 digital-sustainability-curriculum-generator/web/templates/generator.html
 create mode 100644 digital-sustainability-curriculum-generator/web/templates/index.html
 create mode 100644 digital-sustainability-curriculum-generator/web/templates/modules.html
 create mode 100644 digital-sustainability-curriculum-generator/web/templates/roles.html
 create mode 100644 digital-sustainability-curriculum-generator/web/templates/visualization.html)
4. Push to the branch ()
5. Open a Pull Request

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
