# Digital Sustainability Curriculum Generator (DSCG) - 3-Tier Framework

A comprehensive toolkit for generating, analyzing, and evaluating modular, outcome-based curricula for digital sustainability education. The DSCG now supports a new **3-tier architecture** with Nano credentials, Microcredentials, and Modules, providing unprecedented granularity and flexibility in curriculum design across EQF levels 4-8.

## Overview

The enhanced 3-Tier Curriculum Framework provides a sophisticated approach to curriculum design and management available, allowing for atomic-level control over educational content while maintaining coherence across different levels of learning complexity. This framework supports both full educational programs and specific micro-credential pathways with seamless integration across all three tiers.

### Framework Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    3-Tier Framework                         │
├─────────────────────────────────────────────────────────────┤
│ Tier 3: MODULES (30+ ECTS)                                 │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ • Specializations (30-60 ECTS)                         │ │
│ │ • Full Qualifications (60+ ECTS)                       │ │
│ │ • Degree Programs (120-240 ECTS)                       │ │
│ └─────────────────────────────────────────────────────────┘ │
│                              ▲                             │
│                              │ builds from                 │
├─────────────────────────────────────────────────────────────┤
│ Tier 2: MICROCREDENTIALS (1-30 ECTS)                       │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ • Module Components (1-5 ECTS)                         │ │
│ │ • Full Modules (5-15 ECTS)                             │ │
│ │ • Module Clusters (15-30 ECTS)                         │ │
│ └─────────────────────────────────────────────────────────┘ │
│                              ▲                             │
│                              │ builds from                 │
├─────────────────────────────────────────────────────────────┤
│ Tier 1: NANO CREDENTIALS (0.1-5 ECTS)                      │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ • Learning Outcomes (0.2 ECTS)                         │ │
│ │ • Skill Elements (0.5 ECTS)                            │ │
│ │ • Competency Units (1.0 ECTS)                          │ │
│ │ • Knowledge Units (0.3 ECTS)                           │ │
│ │ • Performance Elements (0.8 ECTS)                      │ │
│ │ • Assessment Tasks (0.1 ECTS)                          │ │
│ └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## Key Features

### 🎯 **New 3-Tier Architecture**
- **Nano credentials**: Atomic learning components (0.1-5 ECTS) - Individual learning outcomes, skills, and competencies
- **Microcredentials**: Modular learning units (1-30 ECTS) - Module components and full modules  
- **Modules**: Comprehensive programs (30+ ECTS) - Specializations and full qualifications

### 🔗 **Seamless Cross-Tier Integration**
- Build microcredentials from collections of nano credentials
- Assemble modules from related microcredentials
- Maintain coherence and progression across all levels
- Backward compatibility with existing 2-tier systems

### 📚 **Comprehensive Curriculum Support**
- **Full & Specific Curricula**: Generate complete educational programs or targeted micro-credential pathways
- **Multi-level Support**: Design curricula across EQF levels 4-8 for various digital sustainability roles
- **Standards Compliance**: Built-in validation against European educational frameworks and standards
- **Stackable Credentials**: Create and visualize flexible, personalized learning pathways

### ✅ **Advanced Validation & Quality Assurance**
- EQF level consistency checking across all tiers
- Prerequisites and dependency validation
- Stacking rules enforcement with cross-tier support
- Quality assurance metrics and coherence scoring
- **Rich Evaluation**: Comprehensive assessment against accreditation and educational criteria

### 🚀 **Intelligent Curriculum Generation**
- Complete pathway generation from nano to qualification level
- Adaptive curriculum sizing (15 ECTS to 240+ ECTS)
- Focus area filtering and specialization support
- Implementation planning and resource estimation
- **Work-based Learning**: Support for dual principle education with industry-aligned components

### 📊 **Advanced Analysis & Visualization**
- **Competency Mapping**: Visual mapping between job roles, competencies, and learning outcomes
- **Recognition Mechanisms**: European and national recognition pathways with cross-border portability
- **Accreditation Support**: Quality assurance, provider information, and diploma supplement previews
- Coherence scoring across tiers and balance metrics for tier distribution

### 🌐 **Multi-Interface Support**
- **Web Interface**: User-friendly web application for curriculum management and visualization
- **Command-line Tools**: Powerful scripts for batch processing and automation
- **User Group Targeting**: Clear sections for educators, accreditation specialists, students, and industry

## Installation

### Requirements

- Python 3.8 or higher
- pip package manager
- Recommended: virtualenv or conda for environment management

### Complete 3-Tier Framework Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/dscg.git
cd dscg
```

2. **Create and activate a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install required packages:**
```bash
pip install -r requirements.txt
```

4. **Create necessary directories for 3-tier framework:**
```bash
mkdir -p input/nano_credentials input/micro_credentials input/modules input/roles input/standards
mkdir -p input/relationships input/curricula input/config
mkdir -p dscg/static/css dscg/static/js 
mkdir -p output/curricula output/enhanced_curricula output/three_tier_profiles
mkdir -p output/validation_reports output/implementation_plans
```

### Web Interface Installation

1. Follow steps 1-4 from Complete 3-Tier Framework Installation above.

2. Install Flask and web dependencies if not already included in requirements.txt:
```bash
pip install flask werkzeug jinja2 pandas matplotlib seaborn
```

3. Ensure the templates folder exists with all required template files:
```bash
mkdir -p templates
# Template files should be copied to the templates directory
# (base.html, index.html, batch_generate.html, etc.)
```

4. Configure the web server (optional for production):
```bash
# For production with gunicorn
pip install gunicorn

# For production with Apache or Nginx, set up WSGI configuration
pip install mod_wsgi  # for Apache
```

## Usage

### 3-Tier Framework CLI (New Primary Interface)

#### Basic 3-Tier Operations
```bash
# List all credentials across all tiers
python scripts/three_tier_cli.py --list

# List only nano credentials
python scripts/three_tier_cli.py --list --tier nano

# Show specific credential details
python scripts/three_tier_cli.py --show LO_SUAS_12345

# Show framework statistics
python scripts/three_tier_cli.py --statistics
```

#### Creating Credentials in Each Tier

**Create Nano Credentials:**
```bash
# Create a learning outcome nano credential
python scripts/three_tier_cli.py --create --tier nano \
  --name "Identify Sustainability Principles" \
  --level 5 --ects 0.2 --granularity learning_outcome \
  --learning-outcome "Identify and explain core sustainability principles"

# Create a skill element nano credential  
python scripts/three_tier_cli.py --create --tier nano \
  --name "Carbon Footprint Calculation" \
  --level 5 --ects 0.5 --granularity skill_element \
  --skill-type technical
```

**Create Microcredentials:**
```bash
# Create a microcredential directly
python scripts/three_tier_cli.py --create --tier micro \
  --name "Sustainability Assessment Basics" \
  --level 5 --ects 5.0 --granularity module_component \
  --desc "Foundation skills for sustainability assessment"
```

**Create Modules:**
```bash
# Create a specialization module
python scripts/three_tier_cli.py --create --tier module \
  --name "Digital Sustainability Specialization" \
  --level 6 --ects 60.0 --granularity specialization \
  --qualification-type certificate
```

#### Building Higher-Tier Credentials from Lower Tiers

**Build Microcredentials from Nano Credentials:**
```bash
# Build a microcredential from nano credentials
python scripts/three_tier_cli.py --build-micro \
  --nano-ids "LO_IDSU_12345,SE_CACF_67890,CU_ASEI_11111" \
  --micro-name "Sustainability Assessment Fundamentals" \
  --micro-desc "Core skills for sustainability assessment"
```

**Build Modules from Microcredentials:**
```bash
# Build a module from microcredentials
python scripts/three_tier_cli.py --build-module \
  --micro-ids "MC_SUAS_12345,FM_GRCO_67890,CL_DIGE_11111" \
  --module-name "Green Technology Certificate" \
  --module-desc "Complete certification in green technology"
```

#### Complete Curriculum Generation

**Generate 3-Tier Curricula:**
```bash
# Generate a 60 ECTS certificate program using all three tiers
python scripts/three_tier_cli.py --generate-curriculum \
  --target-ects 60 --target-level 6 \
  --focus-areas "sustainability,software" \
  --output "sustainability_certificate.json"

# Generate a 180 ECTS bachelor's degree
python scripts/three_tier_cli.py --generate-curriculum \
  --target-ects 180 --target-level 6 \
  --curriculum-type bachelor_degree \
  --output "sustainability_degree.json"

# Generate a micro-qualification (15-30 ECTS)
python scripts/three_tier_cli.py --generate-curriculum \
  --target-ects 30 --target-level 5 \
  --curriculum-type micro_qualification \
  --focus-areas "green_coding" \
  --output "green_coding_micro_qual.json"
```

#### Validation and Quality Assurance

**Validate 3-Tier Stacking:**
```bash
# Validate that credentials can be stacked together
python scripts/three_tier_cli.py --validate-stacking \
  --credential-ids "LO_IDSU_123,MC_SUAS_456,SP_GRTE_789"

# Check curriculum coherence across all tiers
python scripts/three_tier_cli.py --validate-coherence \
  --validate-nano-ids "LO_1,SE_2,CU_3" \
  --validate-micro-ids "MC_1,FM_2"
```

**Export and Analysis:**
```bash
# Export complete 3-tier framework data
python scripts/three_tier_cli.py --export --output framework_export.json

# Export specific tier data
python scripts/three_tier_cli.py --export --tier nano --output nano_credentials.json
```

### Legacy 2-Tier System Support (Backward Compatibility)

The framework maintains full backward compatibility with the existing 2-tier system:

#### Traditional Curriculum Generation
```bash
# Generate a curriculum for a specific role and EQF level (legacy)
python scripts/generate_curriculum.py --role DAN --eqf 6 --output-dir output/curricula

# Batch generate all curricula for all defined roles and EQF levels (legacy)
python scripts/batch_generate_curricula.py --output-dir output/curricula
python scripts/batch_enhance_curricula_v2.py --input-dir output/curricula \
  --output-dir output/enhanced_curricula --modules-json input/modules.json \
  --roles-json input/roles.json --static-dir dscg/static
```

#### Enhanced Curriculum Generation with Accreditation Support

**Enhance existing curricula with 3-tier features:**
```bash
# Enhance an existing curriculum with competency mapping and 3-tier breakdown
python scripts/enhance_curriculum_v2.py \
  --input output/curricula/curriculum_DAN_6.html \
  --output output/enhanced_curricula/curriculum_DAN_6_enhanced.html \
  --modules-json input/modules.json --roles-json input/roles.json \
  --static-dir dscg/static

# Batch enhance multiple curricula with 3-tier support
python scripts/batch_enhance_curricula_v2.py \
  --input-dir output/curricula --output-dir output/enhanced_curricula \
  --modules-json input/modules.json --roles-json input/roles.json \
  --static-dir dscg/static
```

#### Micro-credential Management (Enhanced with Nano Support)

**Generate enhanced micro-credential data:**
```bash
# Generate micro-credential sample data with nano credential integration
python scripts/microcredential_curriculum_builder.py --create-sample --data-dir input

# Build a role-based specific curriculum from micro-credentials
python scripts/microcredential_curriculum_builder.py --build-curriculum \
  --role-id DSL --eqf-level 5 --data-dir input --output-dir output/specific_curricula

# Create a custom curriculum from selected micro-credentials
python scripts/microcredential_curriculum_builder.py --build-curriculum \
  --micro-credentials MC001,MC003,MC007 \
  --name "Green Computing Fundamentals" \
  --description "A focused curriculum on green computing basics" \
  --data-dir input --output-dir output/specific_curricula
```

#### Analysis & Quality Improvement

**3-Tier enhanced analysis:**
```bash
# Fix compliance issues in existing curricula with 3-tier validation
python scripts/fix_curriculum_issues.py \
  --input-dir output/curricula --output-dir output/curricula_fixed \
  --standards-dir input/standards

# Evaluate curricula against standards with 3-tier framework requirements
python scripts/curriculum_evaluation_framework.py \
  --input-dir output/curricula_fixed --output-dir output/assessment \
  --include-specific

# Generate curriculum summary with 3-tier validation report
python scripts/enhanced_curriculum_summary.py \
  --output-dir output/curricula --modules-json input/modules/modules.json
```

#### Visualization & Mapping

**Enhanced 3-tier visualizations:**
```bash
# Generate competence matrix with nano credential breakdown
python scripts/generate_competence_matrix.py \
  --modules-json input/modules/modules.json \
  --roles-json input/roles/roles.json --output-dir output/matrix \
  --include-heatmap

# Visualize stacking paths across all three tiers
python scripts/visualize_stacking_paths.py --data-dir input \
  --micro-credentials-file micro_credentials.json \
  --roles-file roles/roles.json --output-dir output/visualizations
```

## File Structure

```
curriculum_generator/
├── README.md                                   # This file
├── requirements.txt                            # Python dependencies
├── setup.py                                    # Package setup
│
├── dscg/                                       # Core package directory
│   ├── __init__.py
│   ├── package/                                # Main framework components
│   │   ├── __init__.py
│   │   ├── nano_credential_manager.py          # Nano credential management
│   │   ├── enhanced_micro_credential_manager.py # Enhanced micro credential management
│   │   ├── module_manager.py                   # Module and qualification management
│   │   ├── relationship_manager.py             # Cross-tier relationships
│   │   ├── three_tier_manager.py               # Unified framework manager
│   │   └── curriculum_pathway_generator.py     # Curriculum generation
│   │
│   ├── core/                                   # Core framework utilities
│   │   ├── __init__.py
│   │   ├── three_tier_config.py                # Configuration management
│   │   ├── validation_rules.py                 # Validation rules
│   │   ├── ects_calculator.py                  # ECTS calculations
│   │   └── quality_assurance.py                # Quality assurance framework
│   │
│   └── utils/                                  # Utility functions
│       ├── __init__.py
│       ├── migration_tools.py                  # Migration utilities
│       ├── data_validator.py                   # Data validation
│       └── export_helpers.py                   # Export utilities
│
├── scripts/                                    # Command-line interfaces
│   ├── export_profiles.py                      # Original profile export
│   ├── export_profiles_enhanced.py             # Enhanced profile export
│   ├── three_tier_profile_generator.py         # 3-tier profile generation
│   ├── micro_credential_cli.py                 # Micro credential CLI
│   ├── three_tier_cli.py                       # Unified 3-tier CLI
│   ├── nano_credential_cli.py                  # Nano-specific CLI
│   ├── module_cli.py                           # Module-specific CLI
│   ├── curriculum_builder.py                   # Interactive curriculum builder
│   └── migration_script.py                     # Migration from 2-tier
│
├── input/                                      # Data directory
│   ├── roles/                                  # Role definitions
│   │   ├── roles.json                          # Role definitions
│   │   └── role_variants.json                  # Role variants
│   │
│   ├── nano_credentials/                       # Nano credential data
│   │   ├── nano_credentials.json               # All nano credentials
│   │   ├── learning_outcomes.json              # Learning outcome templates
│   │   ├── skill_elements.json                 # Skill element templates
│   │   └── nano_templates/                     # Templates by type
│   │       ├── technical_skills.json
│   │       ├── soft_skills.json
│   │       └── domain_knowledge.json
│   │
│   ├── micro_credentials/                      # Microcredential data
│   │   ├── micro_credentials.json              # All microcredentials
│   │   ├── stacking_rules.json                 # Stacking rules
│   │   └── micro_templates.json                # Enhanced templates
│   │
│   ├── modules/                                # Module data
│   │   ├── modules.json                        # All modules
│   │   ├── specializations.json                # Specialization definitions
│   │   ├── qualifications.json                 # Full qualification definitions
│   │   └── module_templates.json               # Module templates
│   │
│   ├── relationships/                          # Cross-tier relationships
│   │   ├── nano_to_micro.json                  # Nano→Micro mappings
│   │   ├── micro_to_module.json                # Micro→Module mappings
│   │   ├── prerequisites.json                  # All prerequisite relationships
│   │   └── equivalencies.json                  # Equivalent credentials
│   │
│   ├── curricula/                              # Generated curricula
│   │   ├── pathways/                           # Generated pathways
│   │   ├── templates/                          # Curriculum templates
│   │   └── implementations/                    # Implementation plans
│   │
│   └── config/                                 # Configuration files
│       ├── three_tier_config.yaml              # Main configuration
│       ├── validation_rules.yaml               # Validation rules
│       ├── ects_mappings.yaml                  # ECTS calculation rules
│       └── quality_standards.yaml              # Quality standards
│
├── output/                                     # Generated output
│   ├── profiles/                               # Educational profiles
│   │   ├── index.html
│   │   ├── profile_*.json
│   │   └── profile_*.html
│   │
│   ├── three_tier_profiles/                    # 3-tier profiles
│   │   ├── nano_breakdown/                     # Nano-level breakdowns
│   │   ├── integrated_profiles/                # Cross-tier profiles
│   │   └── curriculum_pathways/                # Complete pathways
│   │
│   ├── curricula/                              # Generated curricula
│   │   ├── micro_qualifications/               # Short programs (15-30 ECTS)
│   │   ├── certificates/                       # Certificate programs (30-60 ECTS)
│   │   ├── diplomas/                           # Diploma programs (60-120 ECTS)
│   │   └── degrees/                            # Degree programs (120+ ECTS)
│   │
│   ├── validation_reports/                     # Validation results
│   │   ├── coherence_reports/                  # Coherence validation
│   │   ├── quality_reports/                    # Quality assurance
│   │   └── compliance_reports/                 # Standards compliance
│   │
│   └── implementation_plans/                   # Implementation guidance
│       ├── phase_plans/                        # Phased implementation
│       ├── resource_requirements/              # Resource planning
│       └── timeline_schedules/                 # Implementation timelines
│
├── tests/                                      # Test suite
│   ├── __init__.py
│   ├── test_nano_credentials.py                # Nano credential tests
│   ├── test_micro_credentials.py               # Micro credential tests
│   ├── test_modules.py                         # Module tests
│   ├── test_three_tier_integration.py          # Integration tests
│   ├── test_validation.py                      # Validation tests
│   ├── test_curriculum_generation.py           # Curriculum generation tests
│   ├── test_migration.py                       # Migration tests
│   └── fixtures/                               # Test data
│       ├── sample_nano_credentials.json
│       ├── sample_micro_credentials.json
│       ├── sample_modules.json
│       └── test_relationships.json
│
├── docs/                                       # Documentation
│   ├── README.md
│   ├── three_tier_framework.md                 # Framework documentation
│   ├── api_reference.md                        # API documentation
│   ├── user_guide.md                           # User guide
│   ├── migration_guide.md                      # Migration guide
│   ├── examples/                               # Usage examples
│   │   ├── basic_nano_creation.md
│   │   ├── building_microcredentials.md
│   │   ├── curriculum_pathways.md
│   │   └── quality_assurance.md
│   └── schemas/                                # Data schemas
│       ├── nano_credential_schema.json
│       ├── micro_credential_schema.json
│       ├── module_schema.json
│       └── relationship_schema.json
│
├── examples/                                   # Example implementations
│   ├── sample_curricula/                       # Sample curricula
│   │   ├── sustainability_micro_qual.json      # 30 ECTS micro-qualification
│   │   ├── digital_sustainability_cert.json    # 60 ECTS certificate
│   │   └── full_degree_program.json            # 180 ECTS degree
│   │
│   ├── migration_examples/                     # Migration examples
│   │   ├── existing_profile_breakdown.py       # Break existing profiles
│   │   └── nano_generation_example.py          # Generate nanos from outcomes
│   │
│   └── integration_examples/                   # Integration examples
│       ├── api_usage.py                        # API usage examples
│       └── cli_workflows.py                    # CLI workflow examples
│
└── tools/                                      # Development tools
    ├── data_generators/                        # Data generation tools
    │   ├── generate_sample_nanos.py            # Generate sample nano credentials
    │   ├── generate_test_data.py               # Generate test datasets
    │   └── validate_data_integrity.py          # Data integrity checker
    │
    ├── migration_tools/                        # Migration utilities
    │   ├── analyze_existing_data.py            # Analyze current data
    │   ├── generate_migration_plan.py          # Create migration plan
    │   └── verify_migration.py                 # Verify migration success
    │
    └── quality_tools/                          # Quality assurance tools
        ├── validate_curricula.py               # Curriculum validation
        ├── check_coherence.py                  # Coherence checking
        └── generate_qa_reports.py              # QA report generation
```

## Architecture Details

### Tier 1: Nano Credentials (0.1-5 ECTS)
The most granular level representing individual learning components:

- **Learning Outcomes** (0.2 ECTS): Single specific learning outcomes
- **Skill Elements** (0.5 ECTS): Individual skill demonstrations  
- **Competency Units** (1.0 ECTS): Specific competency elements
- **Knowledge Units** (0.3 ECTS): Discrete knowledge components
- **Performance Elements** (0.8 ECTS): Performance demonstrations
- **Assessment Tasks** (0.1 ECTS): Single assessment activities

### Tier 2: Microcredentials (1-30 ECTS)
Module-level components built from nano credentials:

- **Module Components** (1-5 ECTS): Parts of larger modules
- **Full Modules** (5-15 ECTS): Complete standalone modules
- **Module Clusters** (15-30 ECTS): Groups of related modules

### Tier 3: Modules (30+ ECTS)
Program-level structures built from microcredentials:

- **Specializations** (30-60 ECTS): Focused areas of study
- **Full Qualifications** (60+ ECTS): Complete programs/degrees

## Configuration

The framework uses YAML configuration files for customization:

### Main Configuration (`input/config/three_tier_config.yaml`)
```yaml
nano_config:
  min_ects: 0.1
  max_ects: 5.0
  valid_granularities:
    - learning_outcome
    - skill_element
    - competency_unit
    - knowledge_unit
    - performance_element
    - assessment_task

micro_config:
  min_ects: 1.0
  max_ects: 30.0
  valid_granularities:
    - module_component
    - full_module
    - module_cluster

module_config:
  min_ects: 30.0
  max_ects: 240.0
  qualification_types:
    bachelor_degree:
      min_ects: 180
      max_ects: 240
      eqf_levels: [6]
    master_degree:
      min_ects: 120
      max_ects: 180
      eqf_levels: [7]
```

### Environment-Specific Configuration
Create environment-specific overrides:
- `three_tier_config_development.yaml`
- `three_tier_config_staging.yaml`  
- `three_tier_config_production.yaml`

## CLI Reference

### Basic Operations
```bash
# List credentials
python scripts/three_tier_cli.py --list [--tier nano|micro|module|all]

# Show credential details
python scripts/three_tier_cli.py --show <credential_id>

# Create new credential
python scripts/three_tier_cli.py --create --tier <tier> --name "<name>" 
  --level <eqf_level> --ects <ects_points> --granularity <granularity>
```

### Building Higher-Tier Credentials
```bash
# Build microcredential from nanos
python scripts/three_tier_cli.py --build-micro 
  --nano-ids "nano1,nano2,nano3" --micro-name "Micro Name"

# Build module from micros
python scripts/three_tier_cli.py --build-module 
  --micro-ids "micro1,micro2,micro3" --module-name "Module Name"
```

### Curriculum Generation
```bash
# Generate complete curriculum
python scripts/three_tier_cli.py --generate-curriculum 
  --target-ects <ects> --target-level <eqf_level> 
  [--focus-areas "area1,area2"] [--curriculum-type <type>]
  [--output <filename>]
```

### Validation and Analysis
```bash
# Validate stacking
python scripts/three_tier_cli.py --validate-stacking 
  --credential-ids "id1,id2,id3"

# Show statistics
python scripts/three_tier_cli.py --statistics

# Export data
python scripts/three_tier_cli.py --export [--tier <tier>] [--output <filename>]
```

## API Usage

### Python API
```python
from dscg.package.three_tier_manager import ThreeTierManager

# Initialize framework
manager = ThreeTierManager("input")

# Generate curriculum
curriculum = manager.build_complete_curriculum(
    target_ects=60,
    eqf_level=6,
    focus_areas=["sustainability", "software"]
)

# Get all credentials
credentials = manager.get_all_credentials()

# Validate stacking
is_valid, errors = manager.relationship_manager.validate_stacking_combination(
    ["nano1", "micro1", "module1"], credentials
)
```

## Migration from 2-Tier System

The framework provides full backward compatibility with existing 2-tier systems:

### Migration Steps
1. **Analyze existing data**: `python tools/migration_tools/analyze_existing_data.py`
2. **Generate migration plan**: `python tools/migration_tools/generate_migration_plan.py`
3. **Execute migration**: `python scripts/migration_script.py`
4. **Verify migration**: `python tools/migration_tools/verify_migration.py`

### Backward Compatibility
- All existing microcredentials remain valid
- Existing modules work without modification  
- New nano credentials can be added to support existing microcredentials
- Gradual enhancement rather than replacement

## Quality Assurance

### Validation Features
- **EQF Level Consistency**: Ensures proper level progression
- **ECTS Coherence**: Validates ECTS distribution and totals
- **Prerequisites**: Enforces prerequisite relationships
- **Stacking Rules**: Validates credential combinations
- **Granularity Alignment**: Ensures appropriate granularity usage

### Quality Metrics
- **Coherence Score**: Measures logical flow and consistency
- **Balance Score**: Evaluates tier distribution
- **Progression Score**: Assesses prerequisite satisfaction
- **Overall Quality Score**: Composite quality measure

## Supported Curriculum Types

| Type | ECTS Range | EQF Level | Description |
|------|------------|-----------|-------------|
| Micro Qualification | 15-30 | 4-6 | Short professional development |
| Certificate | 30-60 | 4-7 | Focused skill certification |
| Diploma | 60-120 | 5-7 | Comprehensive professional training |
| Bachelor's Degree | 180-240 | 6 | Undergraduate qualification |
| Master's Degree | 120-180 | 7 | Postgraduate qualification |
| Doctoral Degree | 180+ | 8 | Research qualification |

## Contributing

### Development Setup
```bash
# Clone repository
git clone <repository-url>
cd curriculum-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/
```

### Code Standards
- Follow PEP 8 style guidelines
- Include comprehensive docstrings
- Write unit tests for new features
- Validate against framework schemas

## Support and Documentation

- **User Guide**: `docs/user_guide.md`
- **API Reference**: `docs/api_reference.md`
- **Migration Guide**: `docs/migration_guide.md`
- **Examples**: `examples/` directory
- **Schemas**: `docs/schemas/` directory

## License

[Specify license information]

## Changelog

### Version 3.0.0 (3-Tier Framework)
- Added nano credential support
- Implemented cross-tier relationships
- Enhanced curriculum generation
- Added comprehensive validation
- Improved quality assurance

### Version 2.0.0 (2-Tier Framework)
- Microcredential and module support
- Basic curriculum generation
- Role-based profile generation

### Version 1.0.0 (Initial Release)
- Basic role definitions
- Educational profile export
- HTML and JSON output formats
