# Digital Sustainability Curriculum Generator (DSCG) v3.1

A comprehensive, enterprise-ready curriculum generation platform for digital sustainability education with full T3.2 & T3.4 compliance. The system automatically creates modular curricula with Educational Profiles as intermediate data structures, featuring semester breakdowns, micro-credentials, and assessment strategies aligned with European Qualification Framework (EQF) standards.

## 🌟 Key Features

### T3.2 Compliance Features
- **Educational Profiles**: Role-specific intermediate data structures with extracted pedagogical configurations
- **Modular Design**: Flexible building blocks using comprehensive module database with prerequisite chains
- **Semester Breakdown**: Detailed academic period organization with intelligent module sequencing
- **Work-Based Learning**: Dual principle integration with workplace assessment percentages
- **Multi-EQF Support**: EQF levels 4-8 with appropriate complexity scaling and competency mapping
- **Learning Outcomes**: Tuning formula implementation with sustainability-specific granular outcomes

### T3.4 Compliance Features
- **Micro-Credentials**: Stackable system with EU recognition framework and module-level credentials
- **ECTS/ECVET Integration**: Full credit transfer and qualification transparency with NQF referencing
- **Competency Mapping**: e-CF, ESCO, and GreenComp framework alignment with detailed outcomes
- **Certification Pathways**: Outcomes-based qualifications framework with professional recognition
- **Quality Assurance**: EQAVET and ESG standards implementation with continuous improvement
- **Cross-Border Recognition**: EU-wide qualification mobility support with institutional partnerships

## 🚀 Quick Start

### Prerequisites
```bash
# System Requirements
- Python 3.8+
- Git (for version control)
- 4GB+ RAM recommended
- 2GB+ disk space for outputs

# Required Files
- input/modules/modules_v5.json (Module database)
- input/roles/roles.json (Role definitions)
- input/educational_profiles/educational_profiles.json (Enhanced profiles)
Installation
bash# Clone the repository
git clone <repository-url>
cd digital-sustainability-curriculum-generator

# Verify file structure
ls -la input/modules/
ls -la input/roles/
ls -la input/educational_profiles/

# Test basic functionality
python3 -m scripts.curriculum_generator.main --list-roles
📋 Basic Usage Examples
1. Interactive Mode (Recommended for First-Time Users)
bash# Launch interactive curriculum generator
./run_refactored_generator.sh

# OR using Python directly
python3 -m scripts.curriculum_generator.main

# Follow the prompts:
# 1. Select role (e.g., SSD - Sustainable Solution Designer)
# 2. Choose topic (e.g., "Sustainable AI")
# 3. Set EQF level (e.g., 7)
# 4. Define ECTS (e.g., 180)
2. Direct Command Examples
bash# Data Analyst role with carbon footprint specialization
python3 -m scripts.curriculum_generator.main \
  --modules-file "input/modules/modules_v5.json" \
  --role DAN \
  --topic "Carbon Footprint Measurement" \
  --eqf-level 6 \
  --ects 70

# Software Developer for Sustainability (EQF 5 vocational)
python3 -m scripts.curriculum_generator.main \
  --modules-file "input/modules/modules_v5.json" \
  --role SDD \
  --topic "Green Software Development" \
  --eqf-level 5 \
  --ects 60

# Digital Sustainability Lead (strategic level)
python3 -m scripts.curriculum_generator.main \
  --modules-file "input/modules/modules_v5.json" \
  --role DSL \
  --topic "Digital Circular Economy" \
  --eqf-level 8 \
  --ects 80
3. List Available Options
bash# List all available roles with details
python3 -m scripts.curriculum_generator.main --list-roles

# Expected output:
# 📋 Available Professional Roles:
# 
# 🎯 DAN: Data Analyst
#    📚 Main Area: Data & Analytics
#    📊 EQF Levels: [6, 7]
#    
# 🎯 DSE: Data Engineer
#    📚 Main Area: Data & Analytics  
#    📊 EQF Levels: [6, 7]
🏗️ Advanced Usage Examples
4. Batch Generation for Entire Teams
bash# Generate curricula for entire sustainability team
for role in DAN DSE DSM DSC SSD; do
  python3 -m scripts.curriculum_generator.main \
    --role $role \
    --topic "Carbon Footprint Measurement" \
    --eqf-level 6 \
    --ects 70 \
    --output-dir "output/team_curricula"
done

# Generate role-specific topics automatically
declare -A role_topics=(
  ["SSD"]="Sustainable AI"
  ["DSM"]="Digital Circular Economy" 
  ["DAN"]="Data Center Sustainability"
  ["SDD"]="Green Software Development"
  ["DSE"]="IoT Sustainability"
)

for role in "${!role_topics[@]}"; do
  topic="${role_topics[$role]}"
  python3 -m scripts.curriculum_generator.main \
    --role "$role" \
    --topic "$topic" \
    --eqf-level 7 \
    --ects 75
done
5. Custom Output Directory Management
bash# Organize outputs by date and purpose
DATE=$(date +%Y%m%d)
OUTPUT_BASE="output/production_${DATE}"

# Create organized structure
mkdir -p "${OUTPUT_BASE}"/{curricula,profiles,reports}

# Generate with custom output locations
python3 -m scripts.curriculum_generator.main \
  --role SSD \
  --topic "Sustainable AI" \
  --eqf-level 7 \
  --ects 180 \
  --output-dir "${OUTPUT_BASE}/curricula"

# Verify outputs
ls -la "${OUTPUT_BASE}/curricula/"
📚 T3.2 & T3.4 Deliverables Generation
Complete Deliverables Suite
bash# Generate ALL T3.2 and T3.4 deliverables
python3 scripts/generate_all_deliverables.py

# Expected output structure:
# output/
# ├── t32_deliverables/
# │   ├── educational_profiles/
# │   ├── core_curricula/
# │   └── reports/
# └── t34_deliverables/
#     ├── micro_credentials/
#     ├── certifications/
#     ├── qualification_frameworks/
#     └── reports/
T3.2 Deliverables Only
bash# Generate T3.2 deliverables (Educational Profiles + Core Curricula)
python3 scripts/generate_t32_deliverables.py

# Verify T3.2 outputs
ls -la output/t32_deliverables/educational_profiles/
ls -la output/t32_deliverables/core_curricula/
ls -la output/t32_deliverables/reports/

# Check T3.2 compliance report
open output/t32_deliverables/reports/T32_Compliance_Report_*.html
T3.4 Deliverables Only
bash# Generate T3.4 deliverables (Micro-Credentials + Certifications)
python3 scripts/generate_t34_deliverables.py

# Verify T3.4 outputs
ls -la output/t34_deliverables/micro_credentials/
ls -la output/t34_deliverables/certifications/
ls -la output/t34_deliverables/qualification_frameworks/

# Review T3.4 compliance report
open output/t34_deliverables/reports/T34_Compliance_Report_*.html
Educational Profiles Bulk Generation
bash# Generate educational profiles for ALL roles and ALL EQF levels
python3 scripts/generate_all_educational_profiles.py

# Generate for specific role only
python3 scripts/generate_all_educational_profiles.py --role STS

# Generate for specific EQF level across all roles
python3 scripts/generate_all_educational_profiles.py --eqf-level 6

# Generate for specific role and EQF level combination
python3 scripts/generate_all_educational_profiles.py --role DSC --eqf-level 7

# List all available roles and their supported EQF levels
python3 scripts/generate_all_educational_profiles.py --list-roles
🎯 Professional Roles and Specializations
Data & Analytics Roles
bash# Data Analyst - Carbon footprint analysis specialization
python3 -m scripts.curriculum_generator.main \
  --role DAN \
  --topic "Carbon Footprint Measurement" \
  --eqf-level 6 \
  --ects 70

# Data Engineer - IoT sustainability systems  
python3 -m scripts.curriculum_generator.main \
  --role DSE \
  --topic "IoT Sustainability" \
  --eqf-level 7 \
  --ects 75

# Data Scientist - AI for sustainability applications
python3 -m scripts.curriculum_generator.main \
  --role DSI \
  --topic "Sustainable AI" \
  --eqf-level 7 \
  --ects 75
Management & Strategy Roles
bash# Digital Sustainability Manager - Circular economy focus
python3 -m scripts.curriculum_generator.main \
  --role DSM \
  --topic "Digital Circular Economy" \
  --eqf-level 7 \
  --ects 75

# Digital Sustainability Lead - Strategic level
python3 -m scripts.curriculum_generator.main \
  --role DSL \
  --topic "Digital Circular Economy" \
  --eqf-level 8 \
  --ects 80

# Digital Sustainability Consultant - Multi-sector approach
python3 -m scripts.curriculum_generator.main \
  --role DSC \
  --topic "Digital Ethics & Governance" \
  --eqf-level 7 \
  --ects 70
Technical Implementation Roles
bash# Software Developer - Green coding practices
python3 -m scripts.curriculum_generator.main \
  --role SDD \
  --topic "Green Software Development" \
  --eqf-level 5 \
  --ects 60

# Sustainable Solution Designer - AI systems design
python3 -m scripts.curriculum_generator.main \
  --role SSD \
  --topic "Sustainable AI" \
  --eqf-level 7 \
  --ects 70

# Sustainability Technical Specialist - Infrastructure focus
python3 -m scripts.curriculum_generator.main \
  --role STS \
  --topic "Data Center Sustainability" \
  --eqf-level 5 \
  --ects 65
🌐 Web Interface (Coming Soon)
Development Setup
bash# Install Flask dependencies (when web interface is ready)
pip install flask flask-socketio flask-cors gunicorn

# Development server (localhost)
python3 web/app.py

# Production deployment preparation
gunicorn --bind 0.0.0.0:8000 web.app:app
API Endpoints (Planned)
bash# Curriculum generation API
curl -X POST http://localhost:5000/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "role": "SSD",
    "topic": "Sustainable AI", 
    "eqf_level": 7,
    "ects": 180
  }'

# Role information API
curl http://localhost:5000/api/roles

# Educational profiles API
curl http://localhost:5000/api/profiles/SSD/7

# File download API
curl http://localhost:5000/api/download/curriculum/{id}
🔧 Configuration and Customization
Environment Variables
bash# Set custom configuration
export DSCG_MODULES_FILE="input/modules/modules_v5.json"
export DSCG_ROLES_FILE="input/roles/roles.json"
export DSCG_OUTPUT_DIR="output"
export DSCG_LOG_LEVEL="INFO"

# Use custom configuration
python3 -m scripts.curriculum_generator.main \
  --role SSD \
  --topic "Sustainable AI" \
  --eqf-level 7 \
  --ects 180
Custom Module Files
bash# Use test modules for development
python3 -m scripts.curriculum_generator.main \
  --modules-file "input/modules/modules_test.json" \
  --role STS \
  --topic "Green Technology" \
  --eqf-level 5 \
  --ects 60

# Use custom output directory
python3 -m scripts.curriculum_generator.main \
  --role DAN \
  --topic "Data Analytics" \
  --eqf-level 6 \
  --ects 70 \
  --output-dir "custom_output/$(date +%Y%m%d)"
📊 Quality Assurance and Testing
Validation Commands
bash# Test all roles with standard configuration
for role in DAN DSE DSI DSL DSM DSC SDD SSD STS SBA; do
  echo "Testing role: $role"
  python3 -m scripts.curriculum_generator.main \
    --role "$role" \
    --topic "Digital Sustainability" \
    --eqf-level 6 \
    --ects 70 \
    --output-dir "test_output/role_tests"
done

# Validate generated outputs
find output/ -name "*.json" -exec python3 -m json.tool {} \; > /dev/null
echo "JSON validation completed"

# Check HTML generation
find output/ -name "*.html" | wc -l
echo "HTML files generated"
Compliance Testing
bash# Run T3.2 compliance tests
python3 tests/t32_compliance_test_suite.py

# Run T3.4 compliance tests  
python3 tests/t34_compliance_test_suite.py

# Run all compliance tests
python3 tests/run_all_compliance_tests.py

# Educational profiles validation
python3 tests/educational_profiles_validation.py
📁 File Structure and Outputs
Input File Structure
input/
├── modules/
│   ├── modules_v5.json          # Main modules database
│   ├── modules_test.json        # Test data
│   └── core_modules.xlsx        # Excel source data
├── roles/
│   ├── roles.json               # Professional role definitions
│   └── roles_schema.json        # Role validation schema
├── educational_profiles/
│   ├── educational_profiles.json # Enhanced competency profiles
│   └── educational_profiles_schema.json # Profile validation schema
└── standards/
    ├── standard_ects.json       # ECTS framework
    ├── standard_ecvet.json      # ECVET framework
    ├── standard_eqf.json        # EQF descriptors
    └── standard_microcredentials.json # Micro-credentials framework
Output File Structure
output/
├── curricula/                   # Individual curriculum outputs
│   ├── SSD_SUSTAINABLE_AI_7_*.json
│   ├── SSD_SUSTAINABLE_AI_7_*.html
│   └── SSD_SUSTAINABLE_AI_7_*_summary.json
├── educational_profiles/        # Educational profile outputs
│   ├── EP_SSD_7_*.json
│   └── EP_SSD_7_*.html
├── t32_deliverables/           # Complete T3.2 deliverables
│   ├── educational_profiles/
│   ├── core_curricula/
│   └── reports/
└── t34_deliverables/           # Complete T3.4 deliverables
    ├── micro_credentials/
    ├── certifications/
    ├── qualification_frameworks/
    └── reports/
🚨 Troubleshooting
Common Issues and Solutions
Issue: "No roles found in roles.json"
bash# Check file exists
ls -la input/roles/roles.json

# Validate JSON format
python3 -m json.tool input/roles/roles.json

# Check file permissions
chmod 644 input/roles/roles.json
Issue: "Module database not found"
bash# Verify modules file location
ls -la input/modules/modules_v5.json

# Use alternative modules file
python3 -m scripts.curriculum_generator.main \
  --modules-file "input/modules/modules_test.json" \
  --role STS

# Check file size (should be > 100KB)
du -h input/modules/modules_v5.json
Issue: "Educational profile generation failed"
bash# Check educational profiles file
ls -la input/educational_profiles/educational_profiles.json

# Validate profiles JSON
python3 -m json.tool input/educational_profiles/educational_profiles.json

# Generate with fallback profile
python3 -m scripts.curriculum_generator.main \
  --role UNKNOWN_ROLE \
  --topic "Test Topic" \
  --eqf-level 6 \
  --ects 60
Issue: "Permission denied" errors
bash# Fix file permissions
chmod +x run_refactored_generator.sh
chmod 644 input/**/*.json

# Create output directories
mkdir -p output/{curricula,educational_profiles,t32_deliverables,t34_deliverables}
chmod 755 output/ -R
Debug Mode
bash# Enable verbose logging
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
export DSCG_DEBUG=1

# Run with detailed output
python3 -v -m scripts.curriculum_generator.main \
  --role SSD \
  --topic "Sustainable AI" \
  --eqf-level 7 \
  --ects 180

# Check logs
tail -f logs/dscg.log  # (if logging is configured)
🔬 Development and Testing
Development Environment Setup
bash# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Run development server (when web interface is ready)
export FLASK_ENV=development
export FLASK_DEBUG=1
python3 web/app.py
Testing Procedures
bash# Unit tests
python3 -m pytest tests/unit/

# Integration tests
python3 -m pytest tests/integration/

# Full test suite
python3 -m pytest tests/

# Performance testing
python3 tests/performance_tests.py

# Memory usage testing
python3 -c "
import tracemalloc
tracemalloc.start()
# Run curriculum generation
from scripts.curriculum_generator.main import main
main()
print(tracemalloc.get_traced_memory())
"
Code Quality
bash# Code formatting
black scripts/ tests/

# Linting
flake8 scripts/ tests/

# Type checking
mypy scripts/curriculum_generator/

# Security scanning
bandit -r scripts/
🌍 Deployment Options
Local Development
bash# Direct Python execution
python3 scripts/generate_all_deliverables.py

# Using shell wrapper
./run_refactored_generator.sh
Docker Deployment (Future)
bash# Build container
docker build -t dscg:v3.1 .

# Run container
docker run -v $(pwd)/input:/app/input \
           -v $(pwd)/output:/app/output \
           dscg:v3.1

# Docker Compose for web interface
docker-compose up -d
Production Server (Future)
bash# Using Gunicorn
gunicorn --bind 0.0.0.0:8000 \
         --workers 4 \
         --timeout 300 \
         web.app:app

# Using systemd service
sudo systemctl start dscg-web
sudo systemctl enable dscg-web

# Nginx reverse proxy configuration
# /etc/nginx/sites-available/dscg
server {
    listen 80;
    server_name your-domain.com;
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
🤝 Contributing
Development Workflow
bash# Fork and clone repository
git clone https://github.com/yourusername/dscg.git
cd dscg

# Create feature branch
git checkout -b feature/your-feature-name

# Make changes and test
python3 scripts/generate_all_deliverables.py

# Run tests
python3 -m pytest tests/

# Commit changes
git add .
git commit -m "Add: Your feature description"

# Push and create pull request
git push origin feature/your-feature-name
Adding New Roles
bash# Edit roles.json
vim input/roles/roles.json

# Add role entry:
{
  "NEW": {
    "name": "New Role Name",
    "eqf_levels": [5, 6, 7],
    "default_ects": {
      "5": 60,
      "6": 70, 
      "7": 75
    },
    "related_modules": {
      "M10": 85,
      "M15": 90
    },
    "core_skills": ["skill1", "skill2"],
    "main_area": "Technical"
  }
}

# Test new role
python3 -m scripts.curriculum_generator.main \
  --role NEW \
  --topic "Test Topic" \
  --eqf-level 6 \
  --ects 70
Adding New Modules
bash# Edit modules database
vim input/modules/modules_v5.json

# Add module entry following schema
# Test module integration
python3 scripts/validate_modules.py
📖 Documentation
API Documentation

T3.2 Educational Profiles Schema
T3.4 Micro-Credentials Schema
Role Configuration Guide
Module Database Schema

Architecture Documentation

System Architecture
Database Design
Workflow Diagrams
Integration Guide

📞 Support and Resources
Getting Help

Documentation: Check the docs/ directory
Examples: Review the examples in this README
Issues: Create GitHub issues for bugs
Discussions: Use GitHub discussions for questions

Useful Resources

European Qualifications Framework (EQF)
ECTS User Guide
ECVET Framework
Digital4Sustainability Project

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
🏆 Acknowledgments

Digital4Sustainability Project Consortium
European Commission Erasmus+ Programme
Contributing institutions and industry partners
Open source community and contributors


Status: Production-ready T3.2/T3.4 compliant curriculum generation platform with extracted educational profiles, enhanced module utilization, intelligent semester planning, and comprehensive EU standards support.
Version: 3.1.0
Last Updated: 2025-01-31
Compatibility: Python 3.8+, EU Educational Standards 2025
