# scorm_exporter.py

"""
SCORM Exporter for Digital Sustainability Curriculum Generator

This module handles the export of curricula to SCORM-compliant packages.
SCORM (Shareable Content Object Reference Model) is a standard for
e-learning content that ensures interoperability between learning
management systems (LMS).

The module supports SCORM 1.2 and SCORM 2004 formats.
"""

import os
import shutil
import json
import xml.etree.ElementTree as ET
from xml.dom import minidom
import zipfile
import uuid
from datetime import datetime
from typing import Dict, Any, List, Optional

from dscg.models import Curriculum, Module


class SCORMExporter:
    """
    Exports curricula to SCORM-compliant packages
    """
    
    def __init__(self, version: str = "1.2", temp_dir: str = None):
        """
        Initialize the SCORM exporter
        
        Args:
            version: SCORM version ("1.2" or "2004")
            temp_dir: Temporary directory for package preparation
        """
        if version not in ["1.2", "2004"]:
            raise ValueError("SCORM version must be '1.2' or '2004'")
        
        self.version = version
        self.temp_dir = temp_dir or os.path.join("output", "temp")
        
        # Create temporary directory if it doesn't exist
        os.makedirs(self.temp_dir, exist_ok=True)
    
    def export(self, curriculum: Curriculum, output_path: str, config: Dict[str, Any] = None) -> str:
        """
        Export a curriculum as a SCORM package
        
        Args:
            curriculum: The curriculum to export
            output_path: Path to save the SCORM package
            config: Additional configuration options
            
        Returns:
            Path to the created SCORM package
        """
        # Create a unique ID for this package
        package_id = f"dscg_{curriculum.role.id}_{curriculum.eqf_level}_{uuid.uuid4().hex[:8]}"
        
        # Create package directory
        package_dir = os.path.join(self.temp_dir, package_id)
        os.makedirs(package_dir, exist_ok=True)
        
        # Create curriculum content
        self._create_content(curriculum, package_dir)
        
        # Create SCORM manifest
        self._create_manifest(curriculum, package_dir, package_id)
        
        # Create SCORM package (ZIP file)
        zip_path = self._create_package(package_dir, output_path)
        
        # Clean up temporary files
        shutil.rmtree(package_dir)
        
        return zip_path
    
    def _create_content(self, curriculum: Curriculum, package_dir: str) -> None:
        """
        Create the curriculum content files
        
        Args:
            curriculum: The curriculum to export
            package_dir: Directory to save the content
        """
        # Create main content directory
        content_dir = os.path.join(package_dir, "content")
        os.makedirs(content_dir, exist_ok=True)
        
        # Create index.html (main entry point)
        self._create_index_html(curriculum, content_dir)
        
        # Create a page for each module
        for module in curriculum.modules:
            self._create_module_html(module, content_dir)
        
        # Create CSS directory and file
        css_dir = os.path.join(content_dir, "css")
        os.makedirs(css_dir, exist_ok=True)
        self._create_css(css_dir)
        
        # Create JS directory and file
        js_dir = os.path.join(content_dir, "js")
        os.makedirs(js_dir, exist_ok=True)
        self._create_js(js_dir)
        
        # Create SCORM API adapter
        self._create_scorm_api(js_dir)
    
    def _create_index_html(self, curriculum: Curriculum, content_dir: str) -> None:
        """
        Create the main index.html file
        
        Args:
            curriculum: The curriculum to export
            content_dir: Directory to save the file
        """
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{curriculum.name}</title>
    <link rel="stylesheet" href="css/styles.css">
    <script src="js/scorm_api_{self.version}.js"></script>
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
                        <td><a href="module_{module.id}.html" class="btn">View Module</a></td>
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
                        <td><a href="module_{module.id}.html" class="btn">View Module</a></td>
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
            // Initialize SCORM
            initializeSCORM();
            
            // Set course status to incomplete
            setValue('cmi.core.lesson_status', 'incomplete');
            
            // Record start time
            setValue('cmi.core.session_time', '00:00:00');
        });
    </script>
</body>
</html>
"""
        
        # Write the HTML file
        with open(os.path.join(content_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_content)
    
    def _create_module_html(self, module: Module, content_dir: str) -> None:
        """
        Create an HTML file for a module
        
        Args:
            module: Module to export
            content_dir: Directory to save the file
        """
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{module.name}</title>
    <link rel="stylesheet" href="css/styles.css">
    <script src="js/scorm_api_{self.version}.js"></script>
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
            html_content += f"                <li>{skill.replace('_', ' ').title()}</li>\n"
        
        html_content += """            </ul>
        </section>
        
        <section class="assessment">
            <h2>Assessment Methods</h2>
            <ul>
"""
        
        for method in module.assessment_methods:
            html_content += f"                <li>{method.replace('_', ' ').title()}</li>\n"
        
        html_content += """            </ul>
        </section>
        
        <div class="navigation-buttons">
            <a href="index.html" class="btn">Back to Curriculum</a>
            <button id="mark-complete" class="btn btn-primary">Mark as Complete</button>
        </div>
    </main>
    
    <footer>
        <p>Generated by Digital Sustainability Curriculum Generator</p>
    </footer>
    
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Initialize SCORM
            initializeSCORM();
            
            // Handle "Mark as Complete" button
            document.getElementById('mark-complete').addEventListener('click', function() {
                // Set module status to completed
                setValue('cmi.core.lesson_status', 'completed');
                
                // Calculate time spent
                // In a real implementation, this would track actual time spent
                setValue('cmi.core.session_time', '00:05:00');
                
                // Save data
                commit();
                
                // Update UI
                this.textContent = 'Completed';
                this.disabled = true;
                this.classList.add('btn-success');
                
                alert('Module marked as complete!');
            });
        });
    </script>
</body>
</html>
"""
        
        # Write the HTML file
        with open(os.path.join(content_dir, f"module_{module.id}.html"), "w", encoding="utf-8") as f:
            f.write(html_content)
    
    def _create_css(self, css_dir: str) -> None:
        """
        Create CSS file for styling
        
        Args:
            css_dir: Directory to save the CSS file
        """
        css_content = """/* Digital Sustainability Curriculum Generator - SCORM Package Styles */

/* Basic reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f5f5f5;
    margin: 0;
    padding: 0;
}

header {
    background-color: #2c3e50;
    color: #fff;
    padding: 1.5rem;
    text-align: center;
}

header h1 {
    margin: 0;
}

.module-id {
    font-size: 1rem;
    color: #ecf0f1;
    margin-top: 0.5rem;
}

main {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
}

.breadcrumb {
    margin-bottom: 2rem;
    padding: 0.5rem 0;
    border-bottom: 1px solid #ddd;
}

section {
    margin-bottom: 2rem;
    background-color: #fff;
    padding: 1.5rem;
    border-radius: 5px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

h2 {
    color: #2c3e50;
    margin-bottom: 1rem;
    border-bottom: 2px solid #3498db;
    padding-bottom: 0.5rem;
}

h3 {
    color: #2c3e50;
    margin: 1.5rem 0 1rem;
}

p {
    margin-bottom: 1rem;
}

ul, ol {
    margin-left: 2rem;
    margin-bottom: 1rem;
}

li {
    margin-bottom: 0.5rem;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 1rem;
}

table th, table td {
    padding: 0.75rem;
    text-align: left;
    border: 1px solid #ddd;
}

table th {
    background-color: #f2f2f2;
    font-weight: bold;
}

.semester-header {
    background-color: #eaf2f8;
    font-weight: bold;
    text-align: center;
}

.btn {
    display: inline-block;
    padding: 0.5rem 1rem;
    background-color: #3498db;
    color: #fff;
    text-decoration: none;
    border-radius: 4px;
    border: none;
    cursor: pointer;
    font-size: 0.9rem;
    transition: background-color 0.3s;
}

.btn:hover {
    background-color: #2980b9;
}

.btn-primary {
    background-color: #2ecc71;
}

.btn-primary:hover {
    background-color: #27ae60;
}

.btn-success {
    background-color: #27ae60;
}

.navigation-buttons {
    display: flex;
    justify-content: space-between;
    margin-top: 2rem;
}

.skills-list {
    display: flex;
    flex-wrap: wrap;
    list-style: none;
    margin-left: 0;
}

.skills-list li {
    background-color: #e8f4fc;
    padding: 0.5rem 1rem;
    margin: 0 0.5rem 0.5rem 0;
    border-radius: 20px;
    font-size: 0.9rem;
}

.curriculum-details {
    background-color: #f8f9fa;
    padding: 1rem;
    border-radius: 5px;
    margin: 1rem 0;
}

.module-meta {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1rem;
    background-color: #f8f9fa;
    padding: 1rem;
    border-radius: 5px;
    margin: 1rem 0;
}

footer {
    background-color: #2c3e50;
    color: #fff;
    text-align: center;
    padding: 1rem;
    margin-top: 2rem;
}
"""
        
        # Write the CSS file
        with open(os.path.join(css_dir, "styles.css"), "w", encoding="utf-8") as f:
            f.write(css_content)
    
    def _create_js(self, js_dir: str) -> None:
        """
        Create JavaScript file for interactivity
        
        Args:
            js_dir: Directory to save the JS file
        """
        js_content = """/* Digital Sustainability Curriculum Generator - SCORM Package JavaScript */

// General utilities for the SCORM package
function initializeSCORM() {
    console.log("Initializing SCORM API...");
    
    // Find SCORM API
    var API = findAPI(window);
    
    if (API) {
        // Initialize communication with the LMS
        var result = API.LMSInitialize("");
        console.log("SCORM API Initialization: " + (result ? "Successful" : "Failed"));
        
        // Get learner name if available
        var learnerName = getValue("cmi.core.student_name");
        if (learnerName) {
            console.log("Learner: " + learnerName);
            // Could use this to personalize the content
        }
    } else {
        console.warn("SCORM API not found. Running in standalone mode.");
    }
}

// Set a SCORM data model element value
function setValue(element, value) {
    var API = findAPI(window);
    if (API) {
        var result = API.LMSSetValue(element, value);
        if (!result) {
            console.error("Failed to set " + element + " to " + value);
            console.error("Error: " + API.LMSGetLastError());
        }
        return result;
    }
    return false;
}

// Get a SCORM data model element value
function getValue(element) {
    var API = findAPI(window);
    if (API) {
        return API.LMSGetValue(element);
    }
    return null;
}

// Commit changes to the LMS
function commit() {
    var API = findAPI(window);
    if (API) {
        return API.LMSCommit("");
    }
    return false;
}

// Terminate the SCORM session
function terminateSession() {
    var API = findAPI(window);
    if (API) {
        commit();
        return API.LMSFinish("");
    }
    return false;
}

// Handle page unload - ensure data is saved
window.addEventListener('beforeunload', function() {
    commit();
});
"""
        
        # Write the JS file
        with open(os.path.join(js_dir, "main.js"), "w", encoding="utf-8") as f:
            f.write(js_content)
    
    def _create_scorm_api(self, js_dir: str) -> None:
        """
        Create SCORM API adapter based on version
        
        Args:
            js_dir: Directory to save the API JS file
        """
        if self.version == "1.2":
            self._create_scorm_1_2_api(js_dir)
        else:  # SCORM 2004
            self._create_scorm_2004_api(js_dir)
    
    def _create_scorm_1_2_api(self, js_dir: str) -> None:
        """
        Create SCORM 1.2 API adapter
        
        Args:
            js_dir: Directory to save the API JS file
        """
        js_content = """/* SCORM 1.2 API Implementation */

// Find the SCORM API in parent windows
function findAPI(win) {
    var findAPITries = 0;
    var maxTries = 10;
    
    // Check if the current window has the API
    if (win.API) {
        return win.API;
    }
    
    // Look in parent windows
    while ((win.parent != null) && (win.parent != win) && (findAPITries < maxTries)) {
        findAPITries++;
        win = win.parent;
        
        if (win.API) {
            return win.API;
        }
    }
    
    // If we're in a frameset, look in opener window
    if (win.opener != null && typeof(win.opener) != "undefined" && !win.opener.closed) {
        // Look in opener
        if (win.opener.API) {
            return win.opener.API;
        }
        
        // Look in opener's parent
        if (win.opener.parent && win.opener.parent.API) {
            return win.opener.parent.API;
        }
    }
    
    // Not found
    return null;
}

// Stand-alone implementation for testing without LMS
if (typeof(window.API) == "undefined") {
    window.API = {
        _data: {
            "cmi.core.student_name": "Test Learner",
            "cmi.core.student_id": "12345",
            "cmi.core.lesson_status": "not attempted",
            "cmi.core.session_time": "00:00:00",
            "cmi.core.score.raw": "0"
        },
        
        LMSInitialize: function() {
            console.log("[SCORM 1.2] LMSInitialize called");
            return "true";
        },
        
        LMSFinish: function() {
            console.log("[SCORM 1.2] LMSFinish called");
            return "true";
        },
        
        LMSGetValue: function(element) {
            console.log("[SCORM 1.2] LMSGetValue called for: " + element);
            return this._data[element] || "";
        },
        
        LMSSetValue: function(element, value) {
            console.log("[SCORM 1.2] LMSSetValue called for: " + element + " with value: " + value);
            this._data[element] = value;
            return "true";
        },
        
        LMSCommit: function() {
            console.log("[SCORM 1.2] LMSCommit called");
            return "true";
        },
        
        LMSGetLastError: function() {
            return "0";
        },
        
        LMSGetErrorString: function(errorCode) {
            return "No error";
        },
        
        LMSGetDiagnostic: function(errorCode) {
            return "No diagnostic information";
        }
    };
    
    console.log("[SCORM 1.2] Using stand-alone API implementation for testing");
}
"""
        
        # Write the SCORM 1.2 API JS file
        with open(os.path.join(js_dir, "scorm_api_1.2.js"), "w", encoding="utf-8") as f:
            f.write(js_content)
    
    def _create_scorm_2004_api(self, js_dir: str) -> None:
        """
        Create SCORM 2004 API adapter
        
        Args:
            js_dir: Directory to save the API JS file
        """
        js_content = """/* SCORM 2004 API Implementation */

// Find the SCORM API in parent windows
function findAPI(win) {
    var findAPITries = 0;
    var maxTries = 10;
    
    // Check if the current window has the API_1484_11
    if (win.API_1484_11) {
        return win.API_1484_11;
    }
    
    // Look in parent windows
    while ((win.parent != null) && (win.parent != win) && (findAPITries < maxTries)) {
        findAPITries++;
        win = win.parent;
        
        if (win.API_1484_11) {
            return win.API_1484_11;
        }
    }
    
    // If we're in a frameset, look in opener window
    if (win.opener != null && typeof(win.opener) != "undefined" && !win.opener.closed) {
        // Look in opener
        if (win.opener.API_1484_11) {
            return win.opener.API_1484_11;
        }
        
        // Look in opener's parent
        if (win.opener.parent && win.opener.parent.API_1484_11) {
            return win.opener.parent.API_1484_11;
        }
    }
    
    // Not found
    return null;
}

// Stand-alone implementation for testing without LMS
if (typeof(window.API_1484_11) == "undefined") {
    window.API_1484_11 = {
        _data: {
            "cmi.learner_name": "Test Learner",
            "cmi.learner_id": "12345",
            "cmi.completion_status": "not attempted",
            "cmi.session_time": "PT0H0M0S",
            "cmi.score.raw": "0",
            "cmi.success_status": "unknown"
        },
        
        Initialize: function() {
            console.log("[SCORM 2004] Initialize called");
            return "true";
        },
        
        Terminate: function() {
            console.log("[SCORM 2004] Terminate called");
            return "true";
        },
        
        GetValue: function(element) {
            console.log("[SCORM 2004] GetValue called for: " + element);
            return this._data[element] || "";
        },
        
        SetValue: function(element, value) {
            console.log("[SCORM 2004] SetValue called for: " + element + " with value: " + value);
            this._data[element] = value;
            return "true";
        },
        
        Commit: function() {
            console.log("[SCORM 2004] Commit called");
            return "true";
        },
        
        GetLastError: function() {
            return "0";
        },
        
        GetErrorString: function(errorCode) {
            return "No error";
        },
        
        GetDiagnostic: function(errorCode) {
            return "No diagnostic information";
        }
    };
    
    console.log("[SCORM 2004] Using stand-alone API implementation for testing");
}
"""
        
        # Write the SCORM 2004 API JS file
        with open(os.path.join(js_dir, "scorm_api_2004.js"), "w", encoding="utf-8") as f:
            f.write(js_content)
    
    def _create_manifest(self, curriculum: Curriculum, package_dir: str, package_id: str) -> None:
        """
        Create the SCORM manifest file (imsmanifest.xml)
        
        Args:
            curriculum: The curriculum to export
            package_dir: Directory to save the manifest
            package_id: Unique ID for this package
        """
        # Create the root element
        if self.version == "1.2":
            root = self._create_scorm_1_2_manifest(curriculum, package_id)
        else:
            root = self._create_scorm_2004_manifest(curriculum, package_id)
        
        # Format the XML with proper indentation
        xml_str = ET.tostring(root, encoding="utf-8")
        dom = minidom.parseString(xml_str)
        pretty_xml = dom.toprettyxml(indent="  ")
        
        # Write the manifest file
        with open(os.path.join(package_dir, "imsmanifest.xml"), "w", encoding="utf-8") as f:
            f.write(pretty_xml)
    
    def _create_scorm_1_2_manifest(self, curriculum: Curriculum, package_id: str) -> ET.Element:
        """
        Create a SCORM 1.2 manifest
        
        Args:
            curriculum: The curriculum to export
            package_id: Unique ID for this package
            
        Returns:
            XML root element for the manifest
        """
        # Create the root element
        manifest = ET.Element("manifest")
        manifest.set("identifier", package_id)
        manifest.set("version", "1.0")
        manifest.set("xmlns", "http://www.imsproject.org/xsd/imscp_rootv1p1p2")
        manifest.set("xmlns:adlcp", "http://www.adlnet.org/xsd/adlcp_rootv1p2")
        manifest.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        manifest.set("xsi:schemaLocation", "http://www.imsproject.org/xsd/imscp_rootv1p1p2 imscp_rootv1p1p2.xsd http://www.imsglobal.org/xsd/imsmd_rootv1p2p1 imsmd_rootv1p2p1.xsd http://www.adlnet.org/xsd/adlcp_rootv1p2 adlcp_rootv1p2.xsd")
        
        # Create metadata
        metadata = ET.SubElement(manifest, "metadata")
        
        schema = ET.SubElement(metadata, "schema")
        schema.text = "ADL SCORM"
        
        schemaversion = ET.SubElement(metadata, "schemaversion")
        schemaversion.text = "1.2"
        
        # Create organizations
        organizations = ET.SubElement(manifest, "organizations")
        organizations.set("default", "default_org")
        
        organization = ET.SubElement(organizations, "organization")
        organization.set("identifier", "default_org")
        
        title = ET.SubElement(organization, "title")
        title.text = curriculum.name
        
        # Create items for each module
        for i, module in enumerate(curriculum.modules):
            item = ET.SubElement(organization, "item")
            item.set("identifier", f"item_{module.id}")
            item.set("identifierref", f"resource_{module.id}")
            
            item_title = ET.SubElement(item, "title")
            item_title.text = module.name
            
            # Add metadata for the item
            item_metadata = ET.SubElement(item, "metadata")
            
            # Add prerequisites if any
            if module.prerequisites:
                prerequisites = ET.SubElement(item, "adlcp:prerequisites")
                prerequisites.text = ",".join(module.prerequisites)
                prerequisites.set("type", "aicc_script")
        
        # Create resources
        resources = ET.SubElement(manifest, "resources")
        
        # Add resource for main curriculum page
        resource_main = ET.SubElement(resources, "resource")
        resource_main.set("identifier", "resource_main")
        resource_main.set("type", "webcontent")
        resource_main.set("href", "content/index.html")
        resource_main.set("adlcp:scormtype", "sco")
        
        file_main = ET.SubElement(resource_main, "file")
        file_main.set("href", "content/index.html")
        
        # Add resources for each module
        for module in curriculum.modules:
            resource = ET.SubElement(resources, "resource")
            resource.set("identifier", f"resource_{module.id}")
            resource.set("type", "webcontent")
            resource.set("href", f"content/module_{module.id}.html")
            resource.set("adlcp:scormtype", "sco")
            
            file = ET.SubElement(resource, "file")
            file.set("href", f"content/module_{module.id}.html")
        
        # Add dependency on CSS and JS
        dependencies = ET.SubElement(resource_main, "dependency")
        dependencies.set("identifierref", "resource_css")
        
        dependencies = ET.SubElement(resource_main, "dependency")
        dependencies.set("identifierref", "resource_js")
        
        # Add CSS resource
        resource_css = ET.SubElement(resources, "resource")
        resource_css.set("identifier", "resource_css")
        resource_css.set("type", "webcontent")
        resource_css.set("href", "content/css/styles.css")
        
        file_css = ET.SubElement(resource_css, "file")
        file_css.set("href", "content/css/styles.css")
        
        # Add JS resource
        resource_js = ET.SubElement(resources, "resource")
        resource_js.set("identifier", "resource_js")
        resource_js.set("type", "webcontent")
        resource_js.set("href", "content/js/main.js")
        
        file_js1 = ET.SubElement(resource_js, "file")
        file_js1.set("href", "content/js/main.js")
        
        file_js2 = ET.SubElement(resource_js, "file")
        file_js2.set("href", f"content/js/scorm_api_{self.version}.js")
        
        return manifest
    
    def _create_scorm_2004_manifest(self, curriculum: Curriculum, package_id: str) -> ET.Element:
        """
        Create a SCORM 2004 manifest
        
        Args:
            curriculum: The curriculum to export
            package_id: Unique ID for this package
            
        Returns:
            XML root element for the manifest
        """
        # Create the root element
        manifest = ET.Element("manifest")
        manifest.set("identifier", package_id)
        manifest.set("version", "1.0")
        manifest.set("xmlns", "http://www.imsglobal.org/xsd/imscp_v1p1")
        manifest.set("xmlns:adlcp", "http://www.adlnet.org/xsd/adlcp_v1p3")
        manifest.set("xmlns:adlseq", "http://www.adlnet.org/xsd/adlseq_v1p3")
        manifest.set("xmlns:adlnav", "http://www.adlnet.org/xsd/adlnav_v1p3")
        manifest.set("xmlns:imsss", "http://www.imsglobal.org/xsd/imsss")
        manifest.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        manifest.set("xsi:schemaLocation", "http://www.imsglobal.org/xsd/imscp_v1p1 imscp_v1p1.xsd http://www.adlnet.org/xsd/adlcp_v1p3 adlcp_v1p3.xsd http://www.adlnet.org/xsd/adlseq_v1p3 adlseq_v1p3.xsd http://www.adlnet.org/xsd/adlnav_v1p3 adlnav_v1p3.xsd http://www.imsglobal.org/xsd/imsss imsss_v1p0.xsd")
        
        # Create metadata
        metadata = ET.SubElement(manifest, "metadata")
        
        schema = ET.SubElement(metadata, "schema")
        schema.text = "ADL SCORM"
        
        schemaversion = ET.SubElement(metadata, "schemaversion")
        schemaversion.text = "2004 4th Edition"
        
        # Create organizations
        organizations = ET.SubElement(manifest, "organizations")
        organizations.set("default", "default_org")
        
        organization = ET.SubElement(organizations, "organization")
        organization.set("identifier", "default_org")
        
        title = ET.SubElement(organization, "title")
        title.text = curriculum.name
        
        # Create items for each module
        for i, module in enumerate(curriculum.modules):
            item = ET.SubElement(organization, "item")
            item.set("identifier", f"item_{module.id}")
            item.set("identifierref", f"resource_{module.id}")
            
            item_title = ET.SubElement(item, "title")
            item_title.text = module.name
            
            # Add prerequisites if any
            if module.prerequisites:
                # In SCORM 2004, prerequisites are handled through sequencing
                sequencing = ET.SubElement(item, "imsss:sequencing")
                
                precondition_rule = ET.SubElement(sequencing, "imsss:preconditionRule")
                precondition_rule.set("action", "skip")
                
                rule_conditions = ET.SubElement(precondition_rule, "imsss:ruleConditions")
                rule_conditions.set("conditionCombination", "all")
                
                for prereq in module.prerequisites:
                    condition = ET.SubElement(rule_conditions, "imsss:ruleCondition")
                    condition.set("referencedObjective", f"item_{prereq}")
                    condition.set("operator", "not")
                    condition.set("condition", "satisfied")
        
        # Create resources
        resources = ET.SubElement(manifest, "resources")
        
        # Add resource for main curriculum page
        resource_main = ET.SubElement(resources, "resource")
        resource_main.set("identifier", "resource_main")
        resource_main.set("type", "webcontent")
        resource_main.set("href", "content/index.html")
        resource_main.set("adlcp:scormType", "sco")
        
        file_main = ET.SubElement(resource_main, "file")
        file_main.set("href", "content/index.html")
        
        # Add resources for each module
        for module in curriculum.modules:
            resource = ET.SubElement(resources, "resource")
            resource.set("identifier", f"resource_{module.id}")
            resource.set("type", "webcontent")
            resource.set("href", f"content/module_{module.id}.html")
            resource.set("adlcp:scormType", "sco")
            
            file = ET.SubElement(resource, "file")
            file.set("href", f"content/module_{module.id}.html")
        
        # Add dependency on CSS and JS
        dependencies = ET.SubElement(resource_main, "dependency")
        dependencies.set("identifierref", "resource_css")
        
        dependencies = ET.SubElement(resource_main, "dependency")
        dependencies.set("identifierref", "resource_js")
        
        # Add CSS resource
        resource_css = ET.SubElement(resources, "resource")
        resource_css.set("identifier", "resource_css")
        resource_css.set("type", "webcontent")
        resource_css.set("href", "content/css/styles.css")
        
        file_css = ET.SubElement(resource_css, "file")
        file_css.set("href", "content/css/styles.css")
        
        # Add JS resource
        resource_js = ET.SubElement(resources, "resource")
        resource_js.set("identifier", "resource_js")
        resource_js.set("type", "webcontent")
        resource_js.set("href", "content/js/main.js")
        
        file_js1 = ET.SubElement(resource_js, "file")
        file_js1.set("href", "content/js/main.js")
        
        file_js2 = ET.SubElement(resource_js, "file")
        file_js2.set("href", f"content/js/scorm_api_{self.version}.js")
        
        return manifest
    
    def _create_package(self, package_dir: str, output_path: str) -> str:
        """
        Create a ZIP package of the SCORM content
        
        Args:
            package_dir: Directory containing the package content
            output_path: Path to save the ZIP file
            
        Returns:
            Path to the created ZIP file
        """
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Create ZIP file
        with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            # Add all files in the package directory
            for root, _, files in os.walk(package_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arc_name = os.path.relpath(file_path, package_dir)
                    zipf.write(file_path, arc_name)
        
        return output_path