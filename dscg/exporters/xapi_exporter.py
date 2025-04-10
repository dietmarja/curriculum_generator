# xapi_exporter.py

"""
xAPI Exporter for Digital Sustainability Curriculum Generator

This module handles the export of curricula to xAPI statements.
xAPI (Experience API, also known as Tin Can API) is a specification for 
learning technology that enables the collection of data about a wide range 
of learning experiences a person has (online and offline).
"""

import os
import json
import uuid
from datetime import datetime
from typing import Dict, Any, List, Optional, Union

from dscg.models import Curriculum, Module


class XAPIExporter:
    """
    Exports curricula to xAPI statements and creates HTML with embedded xAPI tracking
    """
    
    def __init__(self, lrs_endpoint: str = None, lrs_auth: str = None):
        """
        Initialize the xAPI exporter
        
        Args:
            lrs_endpoint: Endpoint URL of the Learning Record Store (LRS)
            lrs_auth: Authentication token for the LRS (typically Basic Auth)
        """
        self.lrs_endpoint = lrs_endpoint
        self.lrs_auth = lrs_auth
        
        # Default configurations
        self.default_context = {
            "registration": str(uuid.uuid4()),
            "platform": "Digital Sustainability Curriculum Generator",
            "language": "en-US",
            "contextActivities": {
                "category": [{
                    "id": "http://digital4sustainability.eu/curriculum-generator",
                    "definition": {
                        "type": "http://adlnet.gov/expapi/activities/category",
                        "name": {
                            "en-US": "Digital Sustainability Curriculum Generator"
                        }
                    }
                }]
            }
        }
    
    def export(self, curriculum: Curriculum, output_path: str, config: Dict[str, Any] = None) -> str:
        """
        Export a curriculum as HTML with embedded xAPI statements
        
        Args:
            curriculum: The curriculum to export
            output_path: Path to save the output
            config: Additional configuration options
            
        Returns:
            Path to the created output directory
        """
        # Create output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)
        
        # Generate statements for curriculum
        statements = self._generate_curriculum_statements(curriculum)
        
        # Create JSON file with statements
        statements_file = os.path.join(output_path, "xapi_statements.json")
        with open(statements_file, "w", encoding="utf-8") as f:
            json.dump(statements, f, indent=2)
        
        # Create main HTML file
        index_file = os.path.join(output_path, "index.html")
        self._create_index_html(curriculum, index_file)
        
        # Create HTML files for each module
        for module in curriculum.modules:
            module_file = os.path.join(output_path, f"module_{module.id}.html")
            self._create_module_html(module, curriculum, module_file)
        
        # Create CSS file
        css_dir = os.path.join(output_path, "css")
        os.makedirs(css_dir, exist_ok=True)
        self._create_css(os.path.join(css_dir, "styles.css"))
        
        # Create JS files
        js_dir = os.path.join(output_path, "js")
        os.makedirs(js_dir, exist_ok=True)
        self._create_main_js(os.path.join(js_dir, "main.js"))
        self._create_xapi_js(os.path.join(js_dir, "xapi.js"), curriculum)
        
        return output_path
    
    def _generate_curriculum_statements(self, curriculum: Curriculum) -> List[Dict[str, Any]]:
        """
        Generate xAPI statements for a curriculum
        
        Args:
            curriculum: The curriculum to generate statements for
            
        Returns:
            List of xAPI statements
        """
        statements = []
        
        # Generate a unique ID for this curriculum
        curriculum_id = f"http://digital4sustainability.eu/curricula/{curriculum.role.id}_{curriculum.eqf_level}"
        
        # Statement for launching the curriculum
        launch_statement = {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "actor": {
                "objectType": "Agent",
                "name": "Anonymous Learner",
                "account": {
                    "homePage": "http://digital4sustainability.eu",
                    "name": "anonymous"
                }
            },
            "verb": {
                "id": "http://adlnet.gov/expapi/verbs/launched",
                "display": {
                    "en-US": "launched"
                }
            },
            "object": {
                "id": curriculum_id,
                "objectType": "Activity",
                "definition": {
                    "type": "http://adlnet.gov/expapi/activities/course",
                    "name": {
                        "en-US": curriculum.name
                    },
                    "description": {
                        "en-US": curriculum.description
                    }
                }
            },
            "context": self.default_context
        }
        statements.append(launch_statement)
        
        # Statements for completing modules
        for module in curriculum.modules:
            module_id = f"{curriculum_id}/modules/{module.id}"
            
            completed_statement = {
                "id": str(uuid.uuid4()),
                "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                "actor": {
                    "objectType": "Agent",
                    "name": "Anonymous Learner",
                    "account": {
                        "homePage": "http://digital4sustainability.eu",
                        "name": "anonymous"
                    }
                },
                "verb": {
                    "id": "http://adlnet.gov/expapi/verbs/completed",
                    "display": {
                        "en-US": "completed"
                    }
                },
                "object": {
                    "id": module_id,
                    "objectType": "Activity",
                    "definition": {
                        "type": "http://adlnet.gov/expapi/activities/module",
                        "name": {
                            "en-US": module.name
                        },
                        "description": {
                            "en-US": module.description
                        }
                    }
                },
                "result": {
                    "completion": True,
                    "success": True,
                    "duration": "PT30M" # Example duration
                },
                "context": {
                    **self.default_context,
                    "contextActivities": {
                        **self.default_context["contextActivities"],
                        "parent": [{
                            "id": curriculum_id,
                            "definition": {
                                "type": "http://adlnet.gov/expapi/activities/course",
                                "name": {
                                    "en-US": curriculum.name
                                }
                            }
                        }]
                    }
                }
            }
            statements.append(completed_statement)
        
        # Statement for completing the curriculum
        completed_curriculum_statement = {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "actor": {
                "objectType": "Agent",
                "name": "Anonymous Learner",
                "account": {
                    "homePage": "http://digital4sustainability.eu",
                    "name": "anonymous"
                }
            },
            "verb": {
                "id": "http://adlnet.gov/expapi/verbs/completed",
                "display": {
                    "en-US": "completed"
                }
            },
            "object": {
                "id": curriculum_id,
                "objectType": "Activity",
                "definition": {
                    "type": "http://adlnet.gov/expapi/activities/course",
                    "name": {
                        "en-US": curriculum.name
                    },
                    "description": {
                        "en-US": curriculum.description
                    }
                }
            },
            "result": {
                "completion": True,
                "success": True,
                "duration": "PT4H" # Example duration for the whole curriculum
            },
            "context": self.default_context
        }
        statements.append(completed_curriculum_statement)
        
        return statements
    
    def _create_index_html(self, curriculum: Curriculum, output_file: str) -> None:
        """
        Create the main index.html file with xAPI tracking
        
        Args:
            curriculum: The curriculum to export
            output_file: Path to save the file
        """
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{curriculum.name}</title>
    <link rel="stylesheet" href="css/styles.css">
    <script src="https://cdn.jsdelivr.net/npm/xapi-js@2.0.0/dist/xapi.min.js"></script>
    <script src="js/xapi.js"></script>
    <script src="js/main.js"></script>
</head>
<body>
    <header>
        <h1>{curriculum.name}</h1>
    </header>
    
    <main>
        <section class="curriculum-overview">
            <h2>Curriculum Overview</h2>
            <p>{curriculum.description}</p>
            
            <div class="curriculum-details">
                <p><strong>Role:</strong> {curriculum.role.name}</p>
                <p><strong>EQF Level:</strong> {curriculum.eqf_level}</p>
                <p><strong>Total ECTS:</strong> {curriculum.total_ects}</p>
                <p><strong>Work-based Learning:</strong> {curriculum.work_based_percentage:.1f}%</p>
            </div>
            
            <h3>Program Learning Outcomes</h3>
            <ol>
"""
        
        for outcome in curriculum.program_learning_outcomes:
            html_content += f"                <li>{outcome}</li>\n"
        
        html_content += """            </ol>
        </section>
        
        <section class="modules">
            <h2>Modules</h2>
            <table>
                <thead>
                    <tr>
                        <th>Module Code</th>
                        <th>Module Name</th>
                        <th>ECTS</th>
                        <th>Description</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
"""
        
        # Add modules to the table
        if curriculum.modules_by_semester:
            # Sort by semester
            for semester in sorted(curriculum.modules_by_semester.keys()):
                html_content += f"""                    <tr class="semester-header">
                        <td colspan="5">Semester {semester}</td>
                    </tr>
"""
                
                for module in curriculum.modules_by_semester[semester]:
                    html_content += f"""                    <tr>
                        <td>{module.id}</td>
                        <td>{module.name}</td>
                        <td>{module.ects_points}</td>
                        <td>{module.description}</td>
                        <td><a href="module_{module.id}.html" class="btn" data-module-id="{module.id}">View Module</a></td>
                    </tr>
"""
        else:
            # No semester organization
            for module in curriculum.modules:
                html_content += f"""                    <tr>
                        <td>{module.id}</td>
                        <td>{module.name}</td>
                        <td>{module.ects_points}</td>
                        <td>{module.description}</td>
                        <td><a href="module_{module.id}.html" class="btn" data-module-id="{module.id}">View Module</a></td>
                    </tr>
"""
        
        html_content += """                </tbody>
            </table>
        </section>
    </main>
    
    <footer>
        <p>Generated by Digital Sustainability Curriculum Generator</p>
    </footer>
    
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Initialize xAPI tracking
            initXAPI();
            
            // Send curriculum launched statement
            sendStatement('launched', getCurriculumActivity());
            
            // Track module clicks
            document.querySelectorAll('a[data-module-id]').forEach(function(link) {
                link.addEventListener('click', function(e) {
                    const moduleId = this.getAttribute('data-module-id');
                    sendStatement('experienced', getModuleActivity(moduleId));
                });
            });
        });
    </script>
</body>
</html>
"""
        
        # Write the HTML file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_content)
    
    def _create_module_html(self, module: Module, curriculum: Curriculum, output_file: str) -> None:
        """
        Create an HTML file for a module with xAPI tracking
        
        Args:
            module: Module to export
            curriculum: Parent curriculum
            output_file: Path to save the file
        """
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{module.name}</title>
    <link rel="stylesheet" href="css/styles.css">
    <script src="https://cdn.jsdelivr.net/npm/xapi-js@2.0.0/dist/xapi.min.js"></script>
    <script src="js/xapi.js"></script>
    <script src="js/main.js"></script>
</head>
<body>
    <header>
        <h1>{module.name}</h1>
        <p class="module-id">{module.id}</p>
    </header>
    
    <main>
        <nav class="breadcrumb">
            <a href="index.html">Curriculum</a> &gt; {module.name}
        </nav>
        
        <section class="module-details">
            <h2>Module Overview</h2>
            <p>{module.description}</p>
            
            <div class="module-meta">
                <p><strong>EQF Level:</strong> {module.eqf_level}</p>
                <p><strong>ECTS Points:</strong> {module.ects_points}</p>
                <p><strong>Delivery Methods:</strong> {', '.join(method.capitalize() for method in module.delivery_methods)}</p>
                <p><strong>Module Type:</strong> {', '.join(type.capitalize() for type in module.module_type)}</p>
                <p><strong>Work-based:</strong> {'Yes' if module.is_work_based else 'No'}</p>
"""
        
        if module.prerequisites:
            html_content += f"""                <p><strong>Prerequisites:</strong> {', '.join(module.prerequisites)}</p>
"""
        
        html_content += """            </div>
        </section>
        
        <section class="learning-outcomes">
            <h2>Learning Outcomes</h2>
            <p>After completing this module, you will be able to:</p>
            <ul>
"""
        
        for outcome in module.learning_outcomes:
            html_content += f"                <li>{outcome}</li>\n"
        
        html_content += """            </ul>
        </section>
        
        <section class="skills">
            <h2>Skills Covered</h2>
            <ul class="skills-list">
"""
        
        for skill in module.skills:
            html_content += f'                <li data-skill="{skill}">{skill.replace("_", " ").title()}</li>\n'
        
        html_content += """            </ul>
        </section>
        
        <section class="assessment">
            <h2>Assessment Methods</h2>
            <ul>
"""
        
        for method in module.assessment_methods:
            html_content += f"                <li>{method.replace('_', ' ').title()}</li>\n"
        
        html_content