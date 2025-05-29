**Digital Sustainability Curriculum Generator (DSCG) v3.1**

A comprehensive, enterprise-ready curriculum generation platform for digital sustainability education with full T3.2 & T3.4 compliance. The system automatically creates modular curricula with Educational Profiles as intermediate data structures, featuring semester breakdowns, micro-credentials, and assessment strategies aligned with European Qualification Framework (EQF) standards.

The DSCG v3.1 implements the complete T3.2/T3.4 workflow: Professional Roles → Educational Profiles → Curricula, providing unprecedented flexibility and compliance with EU educational standards, enhanced with extracted pedagogical profiles for improved maintainability.

**Quick Start**

**Prerequisites**

- Python 3.8+
- Modules data file (JSON format)
- Roles definition file (roles.json)
- Educational profiles configuration (educational_profiles.json)

**Basic Usage**

bash

_\# Interactive mode - full T3.2/T3.4 experience_

./run_refactored_generator.sh

_\# Direct command with role from roles.json_

python3 -m scripts.curriculum_generator.main \\

\--modules-file "input/modules/modules_v5.json" \\

\--role SSD \\

\--topic "Sustainable AI" \\

\--eqf-level 7 \\

\--ects 180

_\# List all available roles_

python3 -m scripts.curriculum_generator.main --list-roles

_\# Generate complete T3.2 & T3.4 deliverables_

python3 scripts/generate_all_deliverables.py

**System Capabilities**

**T3.2 Compliance Features**

- **Educational Profiles**: Role-specific intermediate data structures with extracted pedagogical configurations
- **Modular Design**: Flexible building blocks using comprehensive module database with prerequisite chains
- **Semester Breakdown**: Detailed academic period organization with intelligent module sequencing
- **Work-Based Learning**: Dual principle integration with workplace assessment percentages
- **Multi-EQF Support**: EQF levels 4-8 with appropriate complexity scaling and competency mapping
- **Learning Outcomes**: Tuning formula implementation with sustainability-specific granular outcomes
- **Flexible Pathways**: Multiple progression routes and delivery methods based on role requirements

**T3.4 Compliance Features**

- **Micro-Credentials**: Stackable system with EU recognition framework and module-level credentials
- **ECTS/ECVET Integration**: Full credit transfer and qualification transparency with NQF referencing
- **Competency Mapping**: e-CF, ESCO, and GreenComp framework alignment with detailed outcomes
- **Certification Pathways**: Outcomes-based qualifications framework with professional recognition
- **Quality Assurance**: EQAVET and ESG standards implementation with continuous improvement
- **Cross-Border Recognition**: EU-wide qualification mobility support with institutional partnerships

**Educational Standards**

- **EQF Levels**: 4-8 (Vocational to Doctoral) with appropriate assessment strategies
- **ECTS Integration**: Automatic credit allocation with 25-hour standard and semester balancing
- **Assessment Methods**: Competency-based, workplace, portfolio, project-based evaluation
- **Quality Frameworks**: Built-in validation, stakeholder feedback, and continuous improvement
- **Sustainability-Specific**: Industry-relevant competencies with concrete learning outcomes

**Architecture v3.1**

**Complete File Structure**

```bash
scripts/curriculum_generator/
├── \__init_\_.py
├── main.py                                 # CLI interface with T3.2/T3.4 workflow_
├── core/                                   # Infrastructure services_
│ ├── \__init_\_.py
│ ├── base_generator.py                     # Main orchestrator with Educational Profiles_
│ ├── data_loader.py                         # Module loading & validation_
│ ├── output_manager.py                     # Enhanced JSON/HTML generation_
│ └── standards_manager.py _\# EU standards compliance (T3.3)_
├── domain/ _\# Domain knowledge & profiles_
│ ├── \__init_\_.py
│ ├── knowledge_base.py _\# Digital sustainability expertise_
│ ├── role_manager.py _\# Role definitions from roles.json_
│ ├── educational_profiles.py _\# T3.2 Educational Profiles system_
│ ├── competency_mapper.py _\# Framework mappings_
│ └── topic_relations.py _\# Topic relationships_
├── components/ _\# Specialized processors_
│ ├── __init__.py
│ ├── module_selector.py _\# Intelligent module selection with role relevance_
│ ├── curriculum_builder.py _\# Academic structure with semester planning_
│ ├── pathway_generator.py _\# Learning progression with prerequisites_
│ └── assessment_generator.py _\# Assessment strategies_
├── templates/ _\# Output templates_
│ ├── \__init_\_.py
│ ├── css_generator.py _\# Enhanced styling for HTML outputs_
│ └── js_generator.py _\# Interactive features_
└── utils/ _\# Utilities_
└── \__init_\_.py


input/
├── modules/
│ ├── modules_v5.json _\# Main modules database with prerequisites_
│ ├── modules_test.json _\# Test data_
│ └── core_modules.xlsx _\# Excel source data_
├── roles/
│ └── roles.json _\# Professional role definitions (T3.2)
│ ├── roles_schema.json                           
├── educational_profiles/ _\# NEW: Extracted pedagogical profiles_
│ └── educational_profiles.json _\# Role-specific competencies and outcomes (General informaation)
│ ├── educational_profiles_schema.json 
├── standards/ _\# EU standards definitions_
│ ├── standard_ects.json _\# ECTS framework
│ ├── standard_ecvet.json _\# ECVET framework_
│ ├── standard_eqf.json _\# EQF descriptors_
│ ├── standard_microcredentials.json _\# T3.4 micro-credentials_
│ └── standard_greencomp.json _\# GreenComp framework_
├── micro_credentials/
│ └── nano_credentials.json _\# Nano-level credentials_
└── config/
├── three_tier_config.yaml _\# 3-tier architecture config_
└── validation_rules.yaml _\# Quality validation rules_

output/
├── curricula/ _\# Generated curricula with semester breakdown_
├── educational_profiles/ _\# T3.2 Educational Profiles (JSON + HTML)_
├── micro_credentials/ _\# T3.4 Micro-credential outputs_
├── t32_deliverables/ _\# Complete T3.2 deliverables suite_
│ ├── educational_profiles/ _\# Generated Role-specific profiles with sustainability competencies (depreceated!)
│ ├── core_curricula/ _\# Training curricula with semester structure_
│ └── reports/ _\# Compliance reports (JSON + HTML prose)_
├── t34_deliverables/ _\# Complete T3.4 deliverables suite_
│ ├── micro_credentials/ _\# Stackable credentials by role_
│ ├── certifications/ _\# Professional certifications_

│ ├── qualification_frameworks/ _\# EU recognition frameworks_

│ └── reports/ _\# T3.4 compliance reports_

├── validation_reports/ _\# Quality assurance reports_

└── css/ _\# Generated stylesheets_

**Key Architectural Improvements v3.1**

**Enhanced T3.2 Workflow**

- **Role Definition** → **Educational Profile** → **Curriculum** with extracted pedagogical data
- **Prerequisite-Based Semester Planning**: Modules organized by dependency chains
- **Role-Specific Module Selection**: Using related_modules from roles.json
- **Sustainability-Specific Competencies**: Industry-relevant skills with concrete outcomes
- **Dynamic Topic Extraction**: Topics derived from module database rather than hard-coded

**Extracted Educational Profiles Architecture**

- **Separation of Concerns**: Pedagogical content separated from curriculum logic
- **Maintainable Configuration**: Educational profiles in dedicated JSON for easy updates
- **Role-Specific Competencies**: Detailed sustainability competencies per professional role
- **Industry Context**: Career pathways, employers, and professional recognition
- **Assessment Integration**: Role-appropriate evaluation methods and requirements

**Enhanced Output Generation**

- **Comprehensive HTML Visualizations**: Professional-grade reports for all outputs
- **Semester-Based Curriculum Structure**: Proper academic progression with prerequisites
- **Sustainability-Specific Content**: Industry-relevant competencies and outcomes
- **Professional Recognition**: Certification pathways and continuing education requirements

**Code Examples**

**1\. Basic Role-Based Generation**

```bash
# Data Analyst role with carbon footprint specialization_

python3 -m scripts.curriculum_generator.main \\
--role DAN \\
--topic "Carbon Footprint Measurement" \\
--eqf-level 6 \\
--ects 70

# Software Developer for Sustainability (EQF 5 vocational)_
python3 -m scripts.curriculum_generator.main \\
--role SDD \\
--topic "Green Software Development" \\
--eqf-level 5 \\
--ects 60
```

**2\. Advanced Professional Roles**

```bash
# Digital Sustainability Lead (strategic level)_
python3 -m scripts.curriculum_generator.main \\
\--role DSL \\
\--topic "Digital Circular Economy" \\
\--eqf-level 8 \\
\--ects 80
_\# Data Scientist specializing in Sustainability_

python3 -m scripts.curriculum_generator.main \\
\--role DSI \\
\--topic "Sustainable AI" \\
\--eqf-level 7 \\
\--ects 75
```

** 3\. Complete Deliverables Generation**

```bash
# Generate all T3.2 deliverables (Educational Profiles + Core Curricula)_

python3 scripts/generate_t32_deliverables.py
# Generate all T3.4 deliverables (Micro-Credentials + Certifications)_
python3 scripts/generate_t34_deliverables.py

# Generate complete deliverables suite_
python3 scripts/generate_all_deliverables.py

** 4\. Multi-Role Curriculum Generation**

```bash
_\# Generate curricula for entire sustainability team_
for role in DAN DSE DSM DSC SSD; do
python3 -m scripts.curriculum_generator.main \\
\--role $role \\
\--topic "Carbon Footprint Measurement" \\
\--eqf-level 6 \\
\--ects 70 \\
\--output-dir "output/team_curricula"
```


**Available Professional Roles**

**Data & Analytics Roles**

- **DAN** - Data Analyst (EQF 6-7, 70-75 ECTS)
- **DSE** - Data Engineer (EQF 6-7, 70-75 ECTS) \[Dual Principle\]
- **DSI** - Data Scientist (Sustainability) (EQF 7-8, 70-75 ECTS)

**Management & Strategy Roles**

- **DSL** - Digital Sustainability Lead (EQF 7-8, 75-80 ECTS)
- **DSM** - Digital Sustainability Manager (EQF 6-7, 70-75 ECTS) \[Dual Principle\]
- **DSC** - Digital Sustainability Consultant (EQF 6-7, 70-75 ECTS)

**Technical Implementation Roles**

- **SDD** - Software Developer for Sustainability (EQF 4-6, 60-70 ECTS) \[Dual Principle\]
- **SSD** - Sustainable Solution Designer (EQF 6-7, 70-75 ECTS)
- **STS** - Sustainability Technical Specialist (EQF 4-5, 60-65 ECTS) \[Dual Principle\]

**Analysis & Advisory Roles**

- **SBA** - Sustainability Business Analyst (EQF 6-7, 70-75 ECTS)

**\[Dual Principle\]** = Supports work-based learning integration

**Output Formats & Features v3.1**

**Generated Files Structure**

```bash
output/
├── curricula/
│ ├── SSD_SUSTAINABLE_AI_7_20250529_DSC.json _\# Complete curriculum data_
│ ├── SSD_SUSTAINABLE_AI_7_20250529_DSC.html _\# Interactive web report_
│ └── SSD_SUSTAINABLE_AI_7_20250529_DSC_summary.json _\# Executive summary_
├── educational_profiles/
│ ├── EP_SSD_7_20250529.json _\# T3.2 Educational Profile_
│ └── EP_SSD_7_20250529.html _\# Profile visualization_
└── t32_deliverables/
├── educational_profiles/ _\# All role profiles_
├── core_curricula/ _\# Training curricula_
└── reports/ _\# Compliance reports_
```

**T3.2 Educational Profile Features**

- **Role-Specific Structure**: Derived from roles.json and educational_profiles.json
- **Sustainability Competencies**: Industry-relevant skills with concrete learning outcomes
- **Semester Breakdown**: Detailed academic progression with prerequisite management
- **Work-Based Learning**: Integration percentages and dual principle support
- **Professional Context**: Career pathways, employers, and industry sectors
- **Assessment Strategies**: EQF-appropriate evaluation methods and requirements
- **Professional Recognition**: Certification pathways and continuing education

**T3.4 Micro-Credentials Integration**

- **Stackable Credentials**: Module and semester-level micro-credentials
- **ECTS/ECVET Compliance**: Full credit transfer support with NQF referencing
- **EU Recognition Framework**: Cross-border qualification transparency
- **Certification Pathways**: Professional development routes with industry recognition
- **Quality Indicators**: Performance metrics and outcome validation

**Configuration & Customization v3.1**

**Role-Based Parameters**

Each role in roles.json defines:

- **EQF Levels**: Supported qualification levels with appropriate complexity
- **Default ECTS**: Recommended credit volumes by level
- **Related Modules**: Specific modules with relevance scores (replacing hard-coded topics)
- **Work-Based Components**: WBL integration requirements by EQF level
- **Module Design Preferences**: Delivery methods and pedagogical approaches
- **Dual Principle Capability**: Workplace integration support

**Educational Profiles Configuration**

The educational_profiles.json provides:

- **Sustainability-Specific Competencies**: Detailed skills and learning outcomes per role
- **Industry Context**: Career pathways, typical employers, and professional sectors
- **Entry Requirements**: Academic and professional prerequisites by EQF level
- **Assessment Methods**: Role-appropriate evaluation strategies
- **Professional Recognition**: Certification pathways and continuing education requirements

**Topic Specializations (Dynamic Extraction)**

- **Carbon Footprint Measurement**: Environmental impact assessment and reporting
- **Sustainable AI**: Energy-efficient ML and AI systems with carbon awareness
- **Green Software Development**: Sustainable coding practices and energy optimization
- **Data Center Sustainability**: Green infrastructure and resource optimization
- **Digital Circular Economy**: Circular business models and regenerative design
- **IoT Sustainability**: Low-power device ecosystems and environmental monitoring

**Advanced Features v3.1**

**Enhanced Module Selection**

- **Role Relevance Scoring**: Modules selected based on roles.json related_modules
- **Prerequisite Chain Resolution**: Intelligent semester planning with dependency management
- **ECTS Distribution Optimization**: Balanced workload across academic periods
- **Work-Based Learning Integration**: Workplace components percentage calculation

**Intelligent Semester Planning**

- **Topological Sorting**: Modules organized by prerequisite dependencies
- **Thematic Progression**: Logical flow from foundation through specialization to capstone
- **Assessment Strategy Alignment**: Evaluation methods matched to semester objectives
- **Flexibility Options**: Multiple pathway options for different learning preferences

**Comprehensive Quality Assurance**

- **Coverage Analysis**: Topic-keyword alignment with relevance scoring
- **Competency Validation**: Skills mapping against industry requirements
- **Standards Compliance**: Automated T3.2/T3.4 requirement verification
- **Stakeholder Feedback**: Integration points for continuous improvement

**Testing, Deliverables & Reports v3.1**

**Enhanced Compliance Testing Suite**

```bash
├── tests/
│ ├── run_all_compliance_tests.py
│ ├── t32_compliance_test_suite.py
│ ├── t34_compliance_test_suite.py
│ └── educational_profiles_validation.py _\# NEW: Profile validation tests_
```

**Complete Deliverables Generation**

```bash

├── scripts/
│ ├── generate_all_deliverables.py _\# Enhanced with v3.1 features_
│ ├── generate_t32_deliverables.py _\# Educational profiles + curricula_
│ └── generate_t34_deliverables.py _\# Micro-credentials + certifications_
```

**Enhanced Prose-Style Compliance Reports**

- **Executive Summaries**: Comprehensive overview with quantitative metrics
- **Requirement Analysis**: Detailed T3.2/T3.4 compliance verification
- **Implementation Roadmaps**: Actionable deployment guidance
- **Quality Metrics**: Performance indicators and improvement recommendations
- **Industry Context**: Professional relevance and career pathway analysis

**Future Extensions v3.1**

**Planned Enhancements**

- **Web Interface**: Browser-based curriculum designer with role-based access
- **API Integration**: RESTful services for institutional system connectivity
- **Advanced Analytics**: Machine learning for curriculum optimization
- **Multi-Language Support**: Internationalization for European deployment
- **Blockchain Credentials**: Secure, verifiable micro-credential management

**Research Applications**

- **Digital4Sustainability Integration**: Full project deliverables compliance
- **European Standards Harmonization**: Cross-institutional framework alignment
- **Industry Partnership Development**: Professional recognition and certification
- **Quality Assurance Evolution**: Continuous improvement and validation mechanisms

**Support & Development v3.1**

**Getting Help**

- Check Educational Profiles in output/educational_profiles/ for role-specific visualizations
- Review HTML reports for comprehensive curriculum analysis and semester breakdown
- Use --list-roles for available professional roles with competency details
- Test with modules_test.json for development and validation

**Contributing**

- **Role Definitions**: Updates through roles.json with related_modules specification
- **Educational Profiles**: Enhancements via educational_profiles.json configuration
- **Module Database**: Improvements with prerequisite validation and quality assurance
- **Assessment Strategies**: Refinements aligned with EQF descriptors and industry needs
- **Standards Compliance**: Extensions for emerging EU frameworks and requirements

**Success Metrics v3.1**

The DSCG v3.1 delivers:

- **100% T3.2 Compliance**: Educational Profiles workflow with semester breakdown
- **100% T3.4 Compliance**: Micro-credentials and certification framework
- **Enhanced Maintainability**: Separated pedagogical profiles for easy updates
- **Industry Relevance**: Sustainability-specific competencies with professional context
- **EU Standards Alignment**: EQF/ECTS/ECVET/EQAVET integration with quality assurance
- **Production Readiness**: Enterprise-grade reliability with comprehensive testing

**Technical Evolution v3.1**

The DSCG has evolved from a monolithic script to a comprehensive T3.2/T3.4 compliant system with:

- **Extracted Educational Profiles**: Maintainable separation of pedagogical content
- **Enhanced Module Utilization**: Full leveraging of comprehensive module database
- **Intelligent Semester Planning**: Prerequisite-based academic progression
- **Sustainability-Specific Content**: Industry-relevant competencies and outcomes
- **Professional Recognition**: Career pathways and certification integration

**Quick Reference Commands v3.1**

bash

_\# List all roles with competency details_

python3 -m scripts.curriculum_generator.main --list-roles

_\# Generate with full T3.2/T3.4 compliance and semester breakdown_

python3 -m scripts.curriculum_generator.main \\

\--role SSD --topic "Sustainable AI" --eqf-level 7 --ects 180

_\# Interactive mode with enhanced features_

python3 -m scripts.curriculum_generator.main

_\# Generate complete deliverables suite_

python3 scripts/generate_all_deliverables.py

_\# Generate T3.2 deliverables only_

python3 scripts/generate_t32_deliverables.py

_\# Batch generation with role-specific modules_

for role in DAN DSE DSM SSD; do

python3 -m scripts.curriculum_generator.main \\

\--role $role --eqf-level 6 --ects 70

done

**Status**: Production-ready T3.2/T3.4 compliant curriculum generation platform with extracted educational profiles, enhanced module utilization, intelligent semester planning, and comprehensive EU standards support.
