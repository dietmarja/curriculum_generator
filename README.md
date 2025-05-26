# Digital Sustainability Curriculum Generator (DSCG) - 3-Tier Framework

A comprehensive toolkit for generating, analyzing, and evaluating modular, outcome-based curricula for digital sustainability education. The DSCG now supports a new **3-tier architecture** with Nano credentials, Microcredentials, and Modules, providing unprecedented granularity and flexibility in curriculum design across EQF levels 4-8.

## 🆕 Latest Updates

### **Configurable Nano Credential ECTS**
- **Adaptable ECTS Values**: Nano credentials learnng units now support configurable ECTS values (default: 0.1, range: 0.1-0.5)
- **Mathematical Precision**: Exact ECTS calculations ensure  alignment across all tiers
- **Parameter-Driven Generation**: Set values for nano ECTS per nano credentials learning units as a variable. The default is 0.1 ECTS
- **Standards Compliance**: Full compliance with EU micro-credentials framework recommendations

### **Enhanced Migration System**
- **Proper Generation Logic**: ECTS values set correctly from the start, not as post-processing fixes
- **Robust Error Handling**: Handles missing or insufficient learning outcomes gracefully
- **Backward Compatibility**: Seamless migration from existing 2-tier systems
- **Validation Framework**: Built-in validation ensures mathematical coherence

## Overview

The enhanced 3-Tier Curriculum Framework provides a sophisticated approach to curriculum design and management, allowing for atomic-level control over educational content while maintaining coherence across different levels of learning complexity. This framework supports both full educational programs and specific micro-credential pathways with seamless integration across all three tiers.

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
│ Tier 1: NANO CREDENTIALS (Configurable ECTS)               │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ • Learning Outcomes (default: 0.1 ECTS)                │ │
│ │ • Skill Elements (default: 0.1 ECTS)                   │ │
│ │ • Competency Units (default: 0.1 ECTS)                 │ │
│ │ • Knowledge Units (default: 0.1 ECTS)                  │ │
│ │ • Performance Elements (default: 0.1 ECTS)             │ │
│ │ • Assessment Tasks (default: 0.1 ECTS)                 │ │
│ │                                                         │ │
│ │ 📊 Configurable Range: 0.1-0.5 ECTS per nano           │ │
│ └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

### **Mathematical Relationships**

The framework maintains precise mathematical relationships with configurable nano ECTS:

```
With nano_ects = 0.1:
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
- **Nano credentials**: Atomic learning components with **configurable ECTS** (0.1-0.5 range)
- **Microcredentials**: Modular learning units (1-30 ECTS) built from nano credentials
- **Modules**: Comprehensive programs (30+ ECTS) built from microcredentials

### ⚙️ **Configurable ECTS System**
- **Parameter-Driven**: Set nano ECTS value as a configuration parameter
- **Mathematical Precision**: Exact calculations ensure perfect tier alignment
- **Standards Compliant**: Adheres to EU micro-credentials framework (0.1-0.5 ECTS range)
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

## Installation

### Requirements

- Python 3.8 or higher
- pip package manager
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

4. **Run the migration with configurable nano ECTS:**
```bash
# Default 0.1 ECTS per nano credential
./run_proper_migration.sh

# Or specify custom nano ECTS value (e.g., 0.15 ECTS)
./run_proper_migration.sh 0.15

# Or use 0.2 ECTS per nano credential
./run_proper_migration.sh 0.2
```

## Usage

### **3-Tier Framework CLI with Configurable ECTS**

#### **Migration with Custom Nano ECTS**
```bash
# Migrate with default 0.1 ECTS per nano credential
./run_proper_migration.sh

# Migrate with 0.15 ECTS per nano credential
./run_proper_migration.sh 0.15

# Migrate with 0.2 ECTS per nano credential
./run_proper_migration.sh 0.2

# Migrate with maximum allowed 0.5 ECTS per nano credential
./run_proper_migration.sh 0.5
```

#### **Basic 3-Tier Operations**
```bash
# List all credentials across all tiers
python scripts/three_tier_cli_fixed.py --list

# List only nano credentials
python scripts/three_tier_cli_fixed.py --list --tier nano

# Show framework statistics with ECTS breakdown
python scripts/three_tier_cli_fixed.py --statistics

# Show specific credential details
python scripts/three_tier_cli_fixed.py --show M1_n_01
```

#### **Creating Credentials with Configurable ECTS**

**Create Nano Credentials:**
```bash
# Create nano credentials during migration (automated)
./run_proper_migration.sh 0.1  # 0.1 ECTS each

# View generated nano credentials
python scripts/three_tier_cli_fixed.py --list --tier nano --limit 10
```

**Mathematical Verification:**
```bash
# Check ECTS alignment across tiers
python scripts/three_tier_cli_fixed.py --statistics

# Expected output shows perfect mathematical alignment:
# Nano ECTS total ≈ Micro ECTS total
```

### **Advanced Configuration**

#### **Environment-Specific ECTS Settings**
Create configuration files for different environments:

```yaml
# development_config.yaml
nano_config:
  ects_per_credential: 0.1
  granularity_precision: "high"

# production_config.yaml  
nano_config:
  ects_per_credential: 0.2
  granularity_precision: "standard"
```

#### **Validation Commands**
```bash
# Validate ECTS coherence across tiers
python scripts/validate_ects_coherence.py --nano-ects 0.1

# Check mathematical relationships
python scripts/verify_tier_mathematics.py

# Generate quality assurance report
python scripts/generate_qa_report.py --include-ects-analysis
```

## Architecture Details

### **Tier 1: Nano Credentials (Configurable ECTS)**
The most granular level with **configurable ECTS values**:

| Granularity Type | Default ECTS | Configurable Range | Typical Use |
|------------------|--------------|-------------------|-------------|
| **Learning Outcomes** | 0.1 | 0.1-0.2 | Single specific learning outcomes |
| **Skill Elements** | 0.1 | 0.1-0.3 | Individual skill demonstrations |
| **Competency Units** | 0.1 | 0.1-0.5 | Specific competency elements |
| **Knowledge Units** | 0.1 | 0.1-0.2 | Discrete knowledge components |
| **Performance Elements** | 0.1 | 0.1-0.4 | Performance demonstrations |
| **Assessment Tasks** | 0.1 | 0.1-0.2 | Single assessment activities |

### **Tier 2: Microcredentials (1-30 ECTS)**
Module-level components built from nano credentials:

- **Module Components** (1-5 ECTS): Built from 10-50 nano credentials
- **Full Modules** (5-15 ECTS): Built from 50-150 nano credentials
- **Module Clusters** (15-30 ECTS): Built from 150-300 nano credentials

### **Tier 3: Modules (30+ ECTS)**
Program-level structures built from microcredentials:

- **Specializations** (30-60 ECTS): Built from 300-600 nano credentials
- **Full Qualifications** (60+ ECTS): Built from 600+ nano credentials

## Configuration

### **Main Configuration with Configurable ECTS**

```yaml
# input/config/three_tier_config.yaml
nano_config:
  # Configurable ECTS value (key new feature)
  default_ects: 0.1
  min_ects: 0.1
  max_ects: 0.5
  
  # ECTS options for different granularities
  ects_options:
    learning_outcome: [0.1, 0.15, 0.2]
    skill_element: [0.1, 0.15, 0.2, 0.25, 0.3]
    competency_unit: [0.1, 0.2, 0.3, 0.4, 0.5]
    knowledge_unit: [0.1, 0.15, 0.2]
    performance_element: [0.1, 0.2, 0.3, 0.4]
    assessment_task: [0.1, 0.15, 0.2]

micro_config:
  min_ects: 1.0
  max_ects: 30.0
  constituent_nano_calculation: "micro_ects / nano_ects"

module_config:
  min_ects: 30.0
  max_ects: 240.0
  constituent_calculation: "module_ects / micro_ects"

# Mathematical validation rules
validation_rules:
  enforce_ects_coherence: true
  ects_tolerance: 0.1
  require_exact_nano_count: true
  validate_tier_mathematics: true
```

### **ECTS Calculation Examples**

```yaml
# Example calculations with different nano ECTS values:
calculation_examples:
  nano_ects_0_1:
    micro_5_ects: "50 nano credentials"
    micro_1_67_ects: "17 nano credentials" 
    module_180_ects: "1,800 nano credentials"
    
  nano_ects_0_2:
    micro_5_ects: "25 nano credentials"
    micro_1_67_ects: "8 nano credentials"
    module_180_ects: "900 nano credentials"
    
  nano_ects_0_15:
    micro_5_ects: "33 nano credentials"
    micro_1_67_ects: "11 nano credentials"
    module_180_ects: "1,200 nano credentials"
```

## CLI Reference

### **Migration Commands with ECTS Configuration**
```bash
# Migrate with different nano ECTS values
./run_proper_migration.sh 0.1    # Default: 100 nanos per 10 ECTS micro
./run_proper_migration.sh 0.15   # 67 nanos per 10 ECTS micro
./run_proper_migration.sh 0.2    # 50 nanos per 10 ECTS micro
./run_proper_migration.sh 0.25   # 40 nanos per 10 ECTS micro

# Advanced migration with validation
python scripts/proper_migration.py --nano-ects 0.1 --validate --verbose
```

### **Analysis Commands**
```bash
# View statistics with ECTS breakdown
python scripts/three_tier_cli_fixed.py --statistics

# Verify mathematical relationships
python scripts/verify_nano_mathematics.py --nano-ects 0.1

# Export framework data with ECTS configuration
python scripts/export_three_tier_data.py --include-ects-config
```

### **Quality Assurance Commands**
```bash
# Validate ECTS coherence across all tiers
python scripts/validate_ects_coherence.py

# Check nano credential distribution
python scripts/analyze_nano_distribution.py

# Generate compliance report
python scripts/generate_compliance_report.py --include-ects-analysis
```

## API Usage

### **Python API with Configurable ECTS**

```python
from dscg.package.three_tier_manager import ThreeTierManager

# Initialize framework with custom nano ECTS
manager = ThreeTierManager("input", nano_ects=0.15)

# Generate curriculum with specific ECTS configuration
curriculum = manager.build_complete_curriculum(
    target_ects=60,
    eqf_level=6,
    nano_ects=0.1,  # Override default
    focus_areas=["sustainability", "software"]
)

# Validate ECTS coherence
is_coherent, report = manager.validate_ects_coherence()

# Get ECTS distribution statistics
stats = manager.get_ects_distribution_stats()
```

### **Configuration API**
```python
from dscg.core.three_tier_config import ThreeTierConfigManager

# Load configuration with ECTS settings
config = ThreeTierConfigManager("input/config", nano_ects=0.2)

# Validate ECTS configuration
is_valid = config.validate_nano_ects_setting(0.15)

# Calculate expected nano count
nano_count = config.calculate_nano_count(micro_ects=5.0, nano_ects=0.1)
# Result: 50 nano credentials
```

## Migration from 2-Tier System

### **Enhanced Migration with ECTS Configuration**

```bash
# Step 1: Analyze existing data
python tools/migration_tools/analyze_existing_data.py

# Step 2: Configure nano ECTS value
# Choose: 0.1 (precise), 0.15 (balanced), 0.2 (manageable)

# Step 3: Execute migration with chosen ECTS value
./run_proper_migration.sh 0.1

# Step 4: Verify mathematical coherence
python scripts/three_tier_cli_fixed.py --statistics
```

### **Migration Validation**
```bash
# Verify ECTS alignment
python tools/validate_migration_ects.py --nano-ects 0.1

# Check nano credential distribution
python tools/analyze_nano_distribution.py

# Generate migration report
python tools/generate_migration_report.py --include-ects-analysis
```

## Quality Assurance

### **ECTS-Aware Validation Features**
- **Mathematical Coherence**: Validates exact ECTS calculations across tiers
- **Configurable Precision**: Supports different nano ECTS values with validation
- **Tier Alignment**: Ensures perfect mathematical alignment between tiers
- **Standards Compliance**: Validates against EU micro-credentials framework ECTS requirements

### **Enhanced Quality Metrics**
- **ECTS Coherence Score**: Measures mathematical alignment across tiers
- **Nano Distribution Score**: Evaluates optimal nano credential distribution
- **Configuration Compliance**: Validates adherence to ECTS configuration settings
- **Mathematical Precision Score**: Assesses calculation accuracy

## Supported Configurations

| Nano ECTS | Micro (5 ECTS) | Module (60 ECTS) | Use Case |
|-----------|----------------|------------------|----------|
| **0.1** | 50 nanos | 600 nanos | Maximum granularity |
| **0.15** | 33 nanos | 400 nanos | Balanced approach |
| **0.2** | 25 nanos | 300 nanos | Manageable size |
| **0.25** | 20 nanos | 240 nanos | Simplified structure |
| **0.5** | 10 nanos | 120 nanos | Minimal granularity |

## Testing Commands

### **Quick Test Suite**
```bash
# Test nano generation with different ECTS values
./test_nano_generation.sh 0.1
./test_nano_generation.sh 0.2

# Test CLI functionality
python scripts/three_tier_cli_fixed.py --statistics
python scripts/three_tier_cli_fixed.py --list --tier nano --limit 5

# Verify mathematical relationships
python scripts/verify_ects_mathematics.py
```

### **Integration Tests**
```bash
# Full framework test
python -m pytest tests/test_three_tier_integration.py

# ECTS validation tests  
python -m pytest tests/test_ects_validation.py

# Migration tests
python -m pytest tests/test_migration_ects.py
```

## Troubleshooting

### **Common ECTS Configuration Issues**

**Issue**: Nano ECTS value outside valid range
```bash
# Solution: Use values between 0.1 and 0.5
./run_proper_migration.sh 0.15  # ✅ Valid
./run_proper_migration.sh 0.05  # ❌ Too small
./run_proper_migration.sh 0.6   # ❌ Too large
```

**Issue**: ECTS coherence validation fails
```bash
# Solution: Regenerate with correct nano ECTS
python scripts/working_nano_fix.py
python scripts/three_tier_cli_fixed.py --statistics
```

**Issue**: Mathematical relationships incorrect
```bash
# Solution: Verify and fix ECTS calculations
python scripts/verify_ects_mathematics.py --fix
```

## Contributing

### **Development Guidelines for ECTS Features**
- Always validate ECTS calculations in tests
- Support configurable nano ECTS in new features
- Maintain mathematical precision in all tier relationships
- Include ECTS validation in quality assurance checks

### **Testing ECTS Features**
```bash
# Test with multiple ECTS configurations
for ects in 0.1 0.15 0.2; do
    ./run_proper_migration.sh $ects
    python scripts/verify_ects_mathematics.py --nano-ects $ects
done
```

## License

[Specify license information]

## Changelog

### **Version 3.1.0 (Configurable ECTS)**
- ✅ **Added configurable nano ECTS** (0.1-0.5 range)
- ✅ **Enhanced migration system** with parameter-driven generation
- ✅ **Mathematical precision validation** across all tiers
- ✅ **Proper generation logic** (no post-processing fixes)
- ✅ **Robust error handling** for edge cases
- ✅ **Standards compliance** with EU micro-credentials framework

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
