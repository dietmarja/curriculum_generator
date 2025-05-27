# Digital Sustainability Curriculum Generator (DSCG) - 3-Tier Framework

A comprehensive toolkit for generating, analyzing, and evaluating modular, outcome-based curricula for digital sustainability education. The DSCG now supports a new **3-tier architecture** with Nano credentials, Microcredentials, and Modules, providing unprecedented granularity and flexibility in curriculum design across EQF levels 4-8.

---

# PART I - GENERAL INTRODUCTION

## 🆕 Latest Updates

### **Phase 5 - Topic-Specific Curriculum Generation**
- **Topic-Specific Generator**: Generate curricula for specific sustainability topics with full EU EQF compliance
- **Micro-ECTS Support**: Support for ECTS values down to 0.01 for maximum granularity (15 minutes learning time)
- **EU Framework Alignment**: Complete alignment with Bologna Process, Lisbon Recognition Convention, and EU Green Deal
- **Advanced Assessment Mapping**: EQF-appropriate assessment complexity across all levels
- **Multi-Delivery Support**: Workplace, classroom, blended, online, hybrid, and self-paced delivery modes

### **Phase 4 Complete - Production Ready**
- **Comprehensive Validation**: All framework components validated and optimized
- **EU Standards Compliance**: Full compliance with EU micro-credentials framework
- **Production Deployment**: Framework ready for institutional deployment
- **Emergency Recovery**: Robust error handling and recovery procedures established

### **Phase 3 Integration & Testing Complete**
- **Enhanced Three-Tier CLI**: Full integration testing and validation framework
- **Specification Compliance**: 100% compliance with nano-credentials standard
- **Integration Test Suite**: Comprehensive automated testing across all tiers
- **Curriculum Generation**: Live curriculum building with configurable parameters
- **Mathematical Validation**: Real-time ECTS coherence checking and relationship integrity

### **Configurable Nano Credential ECTS**
- **Adaptable ECTS Values**: Nano credentials learning units now support configurable ECTS values (default: 0.1, range: 0.01-0.5)
- **Mathematical Precision**: Exact ECTS calculations ensure alignment across all tiers
- **Parameter-Driven Generation**: Set values for nano ECTS per nano credentials learning units as a variable. The default is 0.1 ECTS
- **Standards Compliance**: Full compliance with EU micro-credentials framework recommendations

### **Enhanced Migration System**
- **Proper Generation Logic**: ECTS values set correctly from the start, not as post-processing fixes
- **Robust Error Handling**: Handles missing or insufficient learning outcomes gracefully
- **Backward Compatibility**: Seamless migration from existing 2-tier systems
- **Validation Framework**: Built-in validation ensures mathematical coherence

## Overview

The enhanced 3-Tier Curriculum Framework provides a sophisticated approach to curriculum design and management, allowing for atomic-level control over educational content while maintaining coherence across different levels of learning complexity. This framework supports both full educational programs and specific micro-credential pathways with seamless integration across all three tiers.


## Educational Profiles as Intermediate Data Structure

In the DSCG architecture, educational profiles serve as a critical intermediate data structure:

**Source Data → Educational Profiles**: The system parses the roles defined in `roles.json` to generate comprehensive educational profiles  
**Educational Profiles → Curricula**: These profiles then drive the curriculum generation process, determining module selection and organization  

This two-step approach allows for:

- Separation of role definitions from curriculum specifics  
- More flexible adaptation of curricula to different educational contexts  
- Clear traceability between professional requirements and educational implementation  

**Visualizing the Process Flow:**  
`roles.json → Educational Profiles → Curriculum Generation → Generated Curricula`




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
│ Tier 1: NANO CREDENTIALS (Micro-ECTS Support)              │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ • Learning Outcomes (default: 0.1 ECTS)                │ │
│ │ • Skill Elements (default: 0.1 ECTS)                   │ │
│ │ • Competency Units (default: 0.1 ECTS)                 │ │
│ │ • Knowledge Units (default: 0.1 ECTS)                  │ │
│ │ • Performance Elements (default: 0.1 ECTS)             │ │
│ │ • Assessment Tasks (default: 0.1 ECTS)                 │ │
│ │                                                         │ │
│ │ 📊 Micro-ECTS Range: 0.01-0.5 ECTS per nano            │ │
│ │ 🕐 Minimum Learning Time: 15 minutes (0.01 ECTS)       │ │
│ └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

```markdown
### File Structure & Output Organization

```bash
curriculum_generator/
├── README.md                                    # Main documentation (Parts I & II)
├── PHASE4_COMPLETION_SUMMARY.md                # Migration completion summary
├── DEPLOYMENT_MANIFEST.json                    # Production deployment manifest
├── QUICK_START.md                             # Quick start guide
├── PHASE4_COMPLETION_STATUS.json              # Phase 4 completion status
├── PHASE4_EMERGENCY_COMPLETION.json           # Emergency completion status
│
├── input/                                      # Input data directory
│   ├── micro_credentials.json                 # Micro credentials data
│   ├── nano_credentials/                      # Nano credentials directory
│   │   ├── nano_credentials_spec_compliant.json  # Specification-compliant nano credentials
│   │   └── nano_templates/                    # Nano credential templates
│   ├── relationships/                         # Relationship mappings
│   │   ├── nano_to_micro.json                # Nano-to-micro relationships
│   │   └── micro_to_module.json              # Micro-to-module relationships
│   ├── modules/                               # Module definitions
│   │   ├── modules.json                      # Module data
│   │   └── modules_v3.json                   # Enhanced module data
│   ├── config/                                # Configuration files
│   │   ├── three_tier_config.yaml            # Main framework configuration
│   │   ├── validation_rules.yaml             # Validation rules
│   │   └── config_summary.json               # Configuration summary
│   ├── curricula/                             # Curriculum definitions
│   └── roles/                                 # Role definitions
│       └── roles.json                         # Job roles data
│
├── output/                                     # Output directory
│   ├── curricula/                            # **Role-integrated curricula output**
│   │   ├── *.json                           # Generated curriculum JSON files
│   │   ├── *.html                           # Interactive HTML curriculum views
│   │   └── *_summary.json                   # Curriculum generation summaries
│   ├── css/                                  # **Curriculum styling files**
│   │   └── curriculum.css                   # Enhanced CSS with color coding & animations
│   ├── js/                                   # **Curriculum JavaScript files**
│   │   └── curriculum.js                    # Interactive features & tab navigation
│   ├── three_tier_profiles/                  # Three-tier profile outputs
│   │   ├── final/                            # Final profiles
│   │   ├── nano_breakdown/                   # Nano credential breakdowns
│   │   ├── integrated_profiles/              # Integrated profiles
│   │   └── curriculum_pathways/              # Curriculum pathways
│   ├── topic_curricula/                      # Topic-specific curricula
│   │   ├── generated/                        # Generated topic curricula
│   │   ├── templates/                        # Curriculum templates
│   │   └── validation/                       # Topic curriculum validation
│   ├── validation_reports/                   # Validation reports
│   │   ├── phase4/                           # Phase 4 validation reports
│   │   ├── t32_review/                       # T3.2 reviewer reports
│   │   ├── t34_review/                       # T3.4 reviewer reports
│   │   └── reviewer_summary/                 # EU reviewer summary reports
│   ├── implementation_plans/                 # Implementation plans
│   └── consolidation_manifest.json          # Output consolidation manifest
│
├── scripts/                                   # Main scripts directory
│   ├── role_integrated_generator.py           # **Enhanced role-integrated curriculum generator**
│   ├── generate_topic_curriculum.py           # Topic-specific curriculum generator
│   ├── nano_spec_compliant_generator_fixed.py # Fixed nano generator
│   ├── nano_spec_validator.py                 # Nano specification validator
│   ├── three_tier_cli_enhanced.py            # Enhanced three-tier CLI
│   ├── integration_test_suite.py             # Integration test suite
│   ├── generate_nano_micro_relationships.py  # Relationship generator
│   ├── generate_micro_module_relationships.py # Module relationship generator
│   ├── create_three_tier_config.py           # Configuration generator
│   ├── comprehensive_validation_suite.py     # Comprehensive validation
│   ├── cleanup_optimization_suite.py         # Cleanup and optimization
│   ├── phase4_complete_runner.py             # Phase 4 complete runner
│   ├── phase4_emergency_fix.py               # Emergency fix script
│   ├── minimal_phase4_runner.py              # Minimal Phase 4 runner
│   │
│   └── validation/                            # EU Reviewer validation scripts
│       ├── T3_2_reviewer_check_suite.py      # T3.2 deliverable validation
│       ├── T3_4_reviewer_check_suite.py      # T3.4 deliverable validation
│       └── run_reviewer_validation.py        # Complete reviewer validation
│
├── tests/                                     # Test directory
│   ├── test_three_tier_integration.py        # Integration tests
│   ├── test_ects_validation.py               # ECTS validation tests
│   └── test_migration_ects.py                # Migration tests
│
├── tools/                                     # Utility tools
│   ├── migration_tools/                      # Migration utilities
│   ├── quality_tools/                        # Quality assurance tools
│   └── data_generators/                      # Data generation tools
│
├── docs/                                      # Documentation
│   ├── api_reference.md                      # API documentation
│   ├── user_guide.md                         # User guide
│   └── architecture_decisions.md             # Architecture decisions
│
├── examples/                                  # Example implementations
│   ├── curriculum_examples/                  # Sample curricula
│   └── configuration_examples/               # Configuration examples
│
├── migration_archive/                         # Archived migration files
├── migration_backup_YYYYMMDD_HHMMSS/        # Migration backups
├── requirements.txt                           # Python dependencies
└── .gitignore                                # Git ignore rules
### **Mathematical Relationships of ECTS Credits**

The framework maintains precise mathematical relationships with configurable nano ECTS, now supporting micro-ECTS down to 0.01:

The value for ECTS credits allocated to nano-credentials learning units can be set by the user. By setting this value the total workload is also set. For instance a nano-credential with an ECTS value of 0.1 corresponds to a workload of 2.5 hours, while 0.01 ECTS corresponds to 15 minutes.

```
With nano_ects = 0.01 (15 minutes):
- Micro credential (1.0 ECTS) → 100 nano credentials
- Learning outcome (0.01 ECTS) → 15 minutes learning time
- Full day training (1.0 ECTS) → 100 micro-learning units

With nano_ects = 0.1 (2.5 hours):
- Micro credential (5.0 ECTS) → 50 nano credentials
- Micro credential (1.67 ECTS) → 17 nano credentials
- Module (180 ECTS) → 1,800 nano credentials

With nano_ects = 0.2:
- Micro credential (5.0 ECTS) → 25 nano credentials
- Micro credential (1.67 ECTS) → 8 nano credentials
- Module (180 ECTS) → 900 nano credentials
```

## Key Features

### 🎯 **New 3-Tier Architecture**
- **Nano credentials**: Atomic learning components with **configurable ECTS** (0.01-0.5 range)
- **Microcredentials**: Modular learning units (1-30 ECTS) built from nano credentials
- **Modules**: Comprehensive programs (30+ ECTS) built from microcredentials

### 🎓 **Topic-Specific Curriculum Generation**
- **Subject-Focused**: Generate curricula for specific digital sustainability topics
- **Micro-ECTS Support**: Support for ultra-granular learning down to 0.01 ECTS (15 minutes)
- **EU EQF Compliance**: Full alignment with European Qualifications Framework levels 4-8
- **Multi-Delivery**: Support for workplace, classroom, blended, online, hybrid, and self-paced delivery
- **Assessment Integration**: EQF-appropriate assessment methods and complexity levels

### ⚙️ **Configurable ECTS System**
- **Parameter-Driven**: Set nano ECTS value as a configuration parameter
- **Micro-Learning Support**: Ultra-granular support down to 0.01 ECTS
- **Mathematical Precision**: Exact calculations ensure perfect tier alignment
- **Standards Compliant**: Adheres to EU micro-credentials framework (0.01-0.5 ECTS range)
- **Migration Flexibility**: Easy adjustment during system migration

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
- **Mathematical Validation**: Automatic ECTS coherence checking

### 🧪 **Production-Ready Features**
- **Enhanced Three-Tier CLI**: Comprehensive framework management and testing
- **Integration Test Suite**: Automated validation of all framework components
- **Live Curriculum Generation**: Real-time curriculum building with configurable parameters
- **Specification Validation**: Full compliance checking against nano-credentials standard
- **Mathematical Coherence Testing**: Automated verification of ECTS relationships

## Installation

### Requirements

- Python 3.8 or higher
- pip package manager
- PyYAML for configuration management (optional)
- Recommended: virtualenv or conda for environment management

### Quick Start Installation

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

4. **Run the complete framework setup:**
```bash
# Generate specification-compliant nano credentials
python3 scripts/nano_spec_compliant_generator_fixed.py input 0.1

# Create relationships
python3 scripts/generate_nano_micro_relationships.py input

# Create configuration files
python3 scripts/create_three_tier_config.py input
```

## Basic Usage

### **Topic-Specific Curriculum Generation**

```bash
# Make the generator executable
chmod +x scripts/generate_topic_curriculum.py

# Generate curriculum for specific sustainability topics
python scripts/generate_topic_curriculum.py \
  --topic "Carbon Footprint Measurement" \
  --eqf-level 6 \
  --ects 15 \
  --delivery-mode "blended" \
  --assessment-type "practical"

# Additional topic examples
python scripts/generate_topic_curriculum.py \
  --topic "Green Software Development" \
  --eqf-level 7 \
  --ects 30 \
  --delivery-mode "online" \
  --assessment-type "project"

python scripts/generate_topic_curriculum.py \
  --topic "Sustainable Data Centers" \
  --eqf-level 5 \
  --ects 10 \
  --delivery-mode "workplace" \
  --assessment-type "practical"

python scripts/generate_topic_curriculum.py \
  --topic "Digital Circular Economy" \
  --eqf-level 6 \
  --ects 20 \
  --delivery-mode "hybrid" \
  --assessment-type "portfolio"

# Micro-learning examples (ultra-granular)
python scripts/generate_topic_curriculum.py \
  --topic "Renewable Energy in IT" \
  --eqf-level 5 \
  --ects 0.5 \
  --delivery-mode "self_paced" \
  --assessment-type "theoretical"

# Ultra-granular nano-learning (15 minutes)
python scripts/generate_topic_curriculum.py \
  --topic "Energy Efficient Coding Practices" \
  --eqf-level 5 \
  --ects 0.01 \
  --delivery-mode "self_paced" \
  --assessment-type "practical"

# Research-level curriculum (EQF 8)
python scripts/generate_topic_curriculum.py \
  --topic "Sustainable AI and Machine Learning" \
  --eqf-level 8 \
  --ects 30 \
  --delivery-mode "hybrid" \
  --assessment-type "research"
```

### **Framework Validation and Statistics**

```bash
# Check framework status and statistics
python3 scripts/three_tier_cli_enhanced.py --statistics

# Validate framework integrity
python3 scripts/three_tier_cli_enhanced.py --validate

# Test curriculum generation
python3 scripts/three_tier_cli_enhanced.py --test-curriculum --target-ects 30 --target-level 6
```

### **Validate Specification Compliance**

```bash
# Validate nano credentials against specification
python3 scripts/nano_spec_validator.py

# Run integration tests
python3 scripts/integration_test_suite.py

# Run comprehensive validation (Phase 4)
python3 scripts/comprehensive_validation_suite.py
```

### **View Framework Content**

```bash
# List all credentials
python3 scripts/three_tier_cli_enhanced.py --list

# List nano credentials only
python3 scripts/three_tier_cli_enhanced.py --list --tier nano --limit 10

# List micro credentials only
python3 scripts/three_tier_cli_enhanced.py --list --tier micro
```

## Architecture Details

### **Tier 1: Nano Credentials (Micro-ECTS Support)**
The most granular level with **micro-ECTS values** supporting ultra-granular learning:

| Granularity Type | Default ECTS | Configurable Range | Learning Time | Typical Use |
|------------------|--------------|-------------------|---------------|-------------|
| **Learning Outcomes** | 0.1 | 0.01-0.2 | 15 min - 5 hours | Single specific learning outcomes |
| **Skill Elements** | 0.1 | 0.01-0.3 | 15 min - 7.5 hours | Individual skill demonstrations |
| **Competency Units** | 0.1 | 0.01-0.5 | 15 min - 12.5 hours | Specific competency elements |
| **Knowledge Units** | 0.1 | 0.01-0.2 | 15 min - 5 hours | Discrete knowledge components |
| **Performance Elements** | 0.1 | 0.01-0.4 | 15 min - 10 hours | Performance demonstrations |
| **Assessment Tasks** | 0.1 | 0.01-0.2 | 15 min - 5 hours | Single assessment activities |

### **Tier 2: Microcredentials (1-30 ECTS)**
Module-level components built from nano credentials:

- **Module Components** (1-5 ECTS): Built from 100-500 nano credentials (at 0.01 ECTS)
- **Full Modules** (5-15 ECTS): Built from 500-1,500 nano credentials (at 0.01 ECTS)
- **Module Clusters** (15-30 ECTS): Built from 1,500-3,000 nano credentials (at 0.01 ECTS)

### **Tier 3: Modules (30+ ECTS)**
Program-level structures built from microcredentials:

- **Specializations** (30-60 ECTS): Built from 3,000-6,000 nano credentials (at 0.01 ECTS)
- **Full Qualifications** (60+ ECTS): Built from 6,000+ nano credentials (at 0.01 ECTS)

## API Usage

### **Python API with Configurable ECTS**

```python
# Basic framework usage
from pathlib import Path
import json

# Load nano credentials
with open('input/nano_credentials/nano_credentials_spec_compliant.json', 'r') as f:
    nano_data = json.load(f)
    if isinstance(nano_data, dict) and 'nano_credentials' in nano_data:
        nano_credentials = nano_data['nano_credentials']
    else:
        nano_credentials = nano_data

print(f"Loaded {len(nano_credentials)} nano credentials")

# Check specification compliance
compliant_count = 0
for nano in nano_credentials:
    if all(field in nano for field in ['learning_outcome', 'ects_credits', 'three_tier_framework_elements']):
        compliant_count += 1

compliance_rate = (compliant_count / len(nano_credentials)) * 100
print(f"Specification compliance: {compliance_rate:.1f}%")
```

## Quality Assurance

### **ECTS-Aware Validation Features**
- **Mathematical Coherence**: Validates exact ECTS calculations across tiers
- **Micro-ECTS Precision**: Supports ultra-granular validation down to 0.01 ECTS
- **Configurable Precision**: Supports different nano ECTS values with validation
- **Tier Alignment**: Ensures perfect mathematical alignment between tiers
- **Standards Compliance**: Validates against EU micro-credentials framework ECTS requirements

### **Enhanced Quality Metrics**
- **ECTS Coherence Score**: Measures mathematical alignment across tiers
- **Nano Distribution Score**: Evaluates optimal nano credential distribution
- **Configuration Compliance**: Validates adherence to ECTS configuration settings
- **Mathematical Precision Score**: Assesses calculation accuracy

## Supported Configurations

| Nano ECTS | Learning Time | Micro (5 ECTS) | Module (60 ECTS) | Use Case |
|-----------|---------------|----------------|------------------|----------|
| **0.01** | 15 minutes | 500 nanos | 6,000 nanos | Ultra-granular micro-learning |
| **0.05** | 1.25 hours | 100 nanos | 1,200 nanos | Micro-learning modules |
| **0.1** | 2.5 hours | 50 nanos | 600 nanos | Maximum granularity |
| **0.15** | 3.75 hours | 33 nanos | 400 nanos | Balanced approach |
| **0.2** | 5 hours | 25 nanos | 300 nanos | Manageable size |
| **0.25** | 6.25 hours | 20 nanos | 240 nanos | Simplified structure |
| **0.5** | 12.5 hours | 10 nanos | 120 nanos | Minimal granularity |

## EU Framework Alignment

### **Additional EU Compliance Arguments**

The Topic-Specific Curriculum Generator includes comprehensive EU framework alignment:

- **Bologna Process Compliance**: Full alignment with European higher education standards
- **Lisbon Recognition Convention**: Cross-border qualification recognition support
- **European Skills Agenda**: Skills development framework alignment
- **Digital Education Action Plan**: EU digital education strategy alignment
- **EU Green Deal**: Environmental sustainability focus alignment
- **WCAG 2.1 AA Accessibility**: EU accessibility requirements compliance
- **European Pillar of Social Rights**: Social inclusion and accessibility support
- **European Education Area**: Cross-border education mobility support

### **EQF Level Descriptors**

Full support for EU EQF levels with appropriate complexity mapping:

| EQF Level | Knowledge | Skills | Autonomy & Responsibility |
|-----------|-----------|--------|---------------------------|
| **4** | Factual and theoretical | Cognitive and practical skills | Self-management with supervision |
| **5** | Comprehensive theoretical | Wide range of cognitive/practical | Management and supervision |
| **6** | Advanced knowledge | Advanced skills with innovation | Complex technical/professional |
| **7** | Highly specialized knowledge | Specialized problem-solving | Strategic decisions & management |
| **8** | Knowledge at forefront | Most advanced skills | Leading complex projects |

## TODO List - Development Roadmap

### 🎯 **Completed Features**

#### ✅ **Topic-Specific Curriculum Generation**
- ✅ **Topic-Specific Curriculum Generator** with full EU EQF compliance
- ✅ **Micro-ECTS Support** down to 0.01 ECTS (15 minutes learning time)
- ✅ **Multi-Delivery Modes** (workplace, classroom, blended, online, hybrid, self-paced)
- ✅ **Assessment Type Integration** (theoretical, practical, project, portfolio, research)
- ✅ **EU Framework Alignment** with Bologna Process, Lisbon Convention, EU Green Deal
- ✅ **Accessibility Compliance** with WCAG 2.1 AA standards

### 📚 **Advanced Features**

#### **Content Developer Support Tools**
- [ ] **Content Development Wizard**
  ```bash
  # Interactive content creation tool
  python scripts/content_developer_wizard.py \
    --role "instructional_designer" \
    --topic "Renewable Energy in IT" \
    --generate-templates
  ```

- [ ] **Learning Outcome Generator**
  - Bloom's taxonomy-aligned outcome generation
  - Action verb suggestions based on EQF level
  - Competency mapping to industry standards
  - Assessment alignment recommendations

#### **Web Interface Development**
- [ ] **React-based Web Dashboard**
  - Visual curriculum design interface
  - Drag-and-drop nano credential composition
  - Real-time ECTS calculation display
  - Interactive relationship mapping

### 📚 **Advanced Features**

#### **API Development**
- [ ] **RESTful API Service**
  ```python
  # Curriculum generation API endpoint
  POST /api/v1/curriculum/generate
  {
    "topic": "Carbon Footprint Measurement",
    "eqf_level": 6,
    "ects": 15,
    "focus_areas": ["measurement", "reporting", "verification"]
  }
  ```

#### **Learning Management System Integration**
- [ ] **LMS API Connectors**
  - Moodle, Canvas, Blackboard integration
  - SCORM package generation
  - xAPI statement tracking
  - Grade passback functionality

## Troubleshooting

### **Common Issues**

**Issue**: Nano credentials validation fails
```bash
# Solution: Check specification compliance
python3 scripts/nano_spec_validator.py
```

**Issue**: Framework statistics show inconsistencies
```bash
# Solution: Verify mathematical relationships
python3 scripts/three_tier_cli_enhanced.py --validate
```

**Issue**: Integration tests failing
```bash
# Solution: Run diagnostic and fix issues
python3 scripts/integration_test_suite.py
python3 scripts/comprehensive_validation_suite.py
```

**Issue**: Topic curriculum generation fails
```bash
# Solution: Check EQF level and ECTS validity
python scripts/generate_topic_curriculum.py --help
```

---
## Role-Integrated Curriculum Generator

A comprehensive Python tool for generating curricula tailored for target groups. The tool is demand-driven, 
it operates on the basis of moduels and facilitates educational profile integration (optione) and offers progression pathway planning.

### Overview

The Role-Integrated Curriculum Generator creates personalized learning pathways by combining:
- **Topic-based module selection** from comprehensive databases
- **Optional role profile integration** for career-focused learning
- **Educational profile generation** on-demand when roles are specified
- **Comprehensive progression pathways** for continued learning
- **EU EQF compliance** with role-specific adaptations

### Key Features

#### 🎯 **Educational Profile Integration**
- Optional argument for role-guided curriculum generation
- On-demand educational profile creation from role data
- Career-focused learning outcomes and assessments
- Role variants support (specialization, organization size, sector, etc.)

#### 📚 **Flexible Curriculum Generation**
- Works with or without role profiles
- Generates micro-credentials (1-5 ECTS) and nano-credentials (0.01-1 ECTS)
- Supports multiple delivery modes and assessment types
- EU EQF levels 4-8 compliance

#### 🚀 **Comprehensive Progression Pathways**
Always provides next-step learning opportunities:
- **Vertical progressions** (higher EQF levels)
- **Horizontal expansions** (related topics)
- **Specialization paths** (deeper expertise)
- **Career-focused routes** (role advancement)

### Installation & Usage

#### Basic Topic-Only Generation
```bash
# Generate curriculum without role integration
python scripts/role_integrated_generator.py \
 --modules-file input/modules/modules_v3.json \
 --topic "Green Software Development" \
 --eqf-level 6 \
 --ects 15 \
 --delivery-mode blended \
 --assessment-type practical
 
# Role-guided generation
python scripts/role_integrated_generator.py \
--modules-file input/modules/modules_v3.json \
--roles-file input/roles/roles.json \
--topic "Carbon Footprint Measurement" \
--eqf-level 6 \
--ects 20 \
--role DSC \
--delivery-mode blended

# Role with specialization variant
python scripts/role_integrated_generator.py \
--modules-file input/modules_v3.json \
--roles-file input/roles.json \
--topic "Sustainable AI" \
--eqf-level 7 \
--ects 30 \
--role DSI \
--specialization data_analytics \
--organization-size enterprise \
--sector manufacturing

 # Topic-only generation
  python scripts/role_integrated_generator.py --modules-file input/modules/modules_v3.json --topic "Green Software Development" --eqf-level 6 --ects 15

  # Role-only generation  
  python scripts/role_integrated_generator.py --modules-file input/modules/modules_v3.json --roles-file input/roles/roles.json --role DSC --eqf-level 6 --ects 180

  # Both topic and role
  python scripts/role

```

---

# PART II - EU REVIEWERS TEST SUITES

## 🏛️ EU Project Reviewer Validation Framework

The Digital Sustainability Curriculum Generator includes comprehensive validation suites specifically designed for **EU project reviewers** to assess compliance with **Task 3.2** (Educational Profiles & Curricula Design) and **Task 3.4** (Micro-Credentials & Certifications) deliverable requirements.

### **EU Project Context**

This framework has been developed to meet the requirements of EU project deliverables focused on:
- **Digital Sustainability Skills** education and training
- **Multi-level curricula** across EQF levels 4-8
- **Modular, stackable credentials** with ECTS compatibility
- **EU recognition** and cross-border certification
- **Industry alignment** with digital sustainability roles

## T3.2 & T3.4 Reviewer Validation Suites

### **Overview of EU Deliverable Requirements**

#### **Task 3.2: Educational Profiles & Curricula Design**
*"Design innovative digital sustainability educational profiles and curricula across multiple EQF levels with modular, ECTS-compatible learning components for flexible delivery and dual education integration."*

**Key Requirements:**
- Multiple EQF levels (4-8) coverage
- Role-based educational profiles
- Modular learning components as building blocks
- ECTS points for program comparability
- High flexibility through modular combinations
- Multiple delivery methodologies (workplace, classroom, blended, online)
- Flexible learning pathways
- Dual education principle support
- Target audience adaptation (students, professionals, managers)
- Upskilling/reskilling focus

#### **Task 3.4: Micro-Credentials & Certifications**
*"Design Digita
