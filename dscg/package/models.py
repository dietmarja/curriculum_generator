import json
import os
from typing import List, Dict, Any, Set, Optional, Tuple

class Module:
    """Represents a learning module in a curriculum"""
    def __init__(self,
                 id: str,
                 name: str,
                 description: str,
                 eqf_level: int,
                 ects_points: int,
                 thematic_area: str,
                 prerequisites: List[str] = None,
                 delivery_methods: List[str] = None,
                 module_type: List[str] = None,
                 skills: List[str] = None,
                 role_relevance: Dict[str, float] = None,
                 is_work_based: bool = False,
                 learning_outcomes: List[str] = None,
                 assessment_methods: List[str] = None,
                 content_topics: List[str] = None,
                 semester: int = None) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.eqf_level = eqf_level
        self.ects_points = ects_points
        self.thematic_area = thematic_area
        self.prerequisites = prerequisites or []
        self.delivery_methods = delivery_methods or ["classroom"]
        self.module_type = module_type or ["theoretical"]
        self.skills = skills or []
        self.role_relevance = role_relevance or {}
        self.is_work_based = is_work_based
        self.learning_outcomes = learning_outcomes or []
        self.assessment_methods = assessment_methods or []
        self.content_topics = content_topics or []
        self.semester = semester

    def to_dict(self) -> Dict[str, Any]:
        """Convert module to dictionary representation"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "eqf_level": self.eqf_level,
            "ects_points": self.ects_points,
            "thematic_area": self.thematic_area,
            "prerequisites": self.prerequisites,
            "delivery_methods": self.delivery_methods,
            "module_type": self.module_type,
            "skills": self.skills,
            "role_relevance": self.role_relevance,
            "is_work_based": self.is_work_based,
            "learning_outcomes": self.learning_outcomes,
            "assessment_methods": self.assessment_methods,
            "content_topics": self.content_topics,
            "semester": self.semester
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Module':
        """Create module from dictionary representation"""
        return cls(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            eqf_level=data["eqf_level"],
            ects_points=data["ects_points"],
            thematic_area=data.get("thematic_area", "general"),
            prerequisites=data.get("prerequisites", []),
            delivery_methods=data.get("delivery_methods", ["classroom"]),
            module_type=data.get("module_type", ["theoretical"]),
            skills=data.get("skills", []),
            role_relevance=data.get("role_relevance", {}),
            is_work_based=data.get("is_work_based", False),
            learning_outcomes=data.get("learning_outcomes", []),
            assessment_methods=data.get("assessment_methods", []),
            content_topics=data.get("content_topics", []),
            semester=data.get("semester")
        )

class Role:
    """Represents a professional role"""
    def __init__(self,
                 id: str,
                 name: str,
                 description: str,
                 main_area: str,
                 thematic_area: str,
                 eqf_levels: List[int] = None,
                 core_skills: List[str] = None,
                 default_ects: Dict[int, int] = None,
                 career_paths: List[str] = None,
                 program_duration: Dict[int, int] = None,
                 program_learning_outcomes: Dict[int, List[str]] = None,
                 assessment_methods: List[Dict[str, Any]] = None,
                 work_based_learning: Dict[int, int] = None) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.main_area = main_area
        self.thematic_area = thematic_area  # e.g., "sustainability", "cybersecurity", "business"
        self.eqf_levels = eqf_levels or [5, 6, 7]
        self.core_skills = core_skills or []
        self.default_ects = default_ects or {
            4: 60,
            5: 120,
            6: 180,
            7: 120,
            8: 180
        }
        self.career_paths = career_paths or []
        # Duration in semesters for each EQF level
        self.program_duration = program_duration or {
            4: 2,  # 1 year (2 semesters)
            5: 4,  # 2 years (4 semesters)
            6: 6,  # 3 years (6 semesters)
            7: 4,  # 2 years (4 semesters)
            8: 6   # 3 years (6 semesters)
        }
        # Learning outcomes by EQF level
        self.program_learning_outcomes = program_learning_outcomes or {}
        # Assessment methods with weights
        self.assessment_methods = assessment_methods or [
            {"name": "Written exams", "weight": 30},
            {"name": "Project work", "weight": 30},
            {"name": "Presentations", "weight": 20},
            {"name": "Participation", "weight": 20}
        ]
        # Work-based learning percentage by EQF level
        self.work_based_learning = work_based_learning or {
            4: 50,  # 50% work-based for EQF 4
            5: 40,  # 40% work-based for EQF 5
            6: 30,  # 30% work-based for EQF 6
            7: 20,  # 20% work-based for EQF 7
            8: 10   # 10% work-based for EQF 8
        }

    def to_dict(self) -> Dict[str, Any]:
        """Convert role to dictionary representation"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "main_area": self.main_area,
            "thematic_area": self.thematic_area,
            "eqf_levels": self.eqf_levels,
            "core_skills": self.core_skills,
            "default_ects": self.default_ects,
            "career_paths": self.career_paths,
            "program_duration": self.program_duration,
            "program_learning_outcomes": self.program_learning_outcomes,
            "assessment_methods": self.assessment_methods,
            "work_based_learning": self.work_based_learning
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Role':
        """Create role from dictionary representation"""
        return cls(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            main_area=data["main_area"],
            thematic_area=data.get("thematic_area", "general"),
            eqf_levels=data.get("eqf_levels", [5, 6, 7]),
            core_skills=data.get("core_skills", []),
            default_ects=data.get("default_ects", {
                4: 60,
                5: 120,
                6: 180,
                7: 120,
                8: 180
            }),
            career_paths=data.get("career_paths", []),
            program_duration=data.get("program_duration"),
            program_learning_outcomes=data.get("program_learning_outcomes", {}),
            assessment_methods=data.get("assessment_methods"),
            work_based_learning=data.get("work_based_learning")
        )

class Curriculum:
    """Represents a curriculum for a specific role and EQF level"""
    def __init__(self,
                 role: Role,
                 eqf_level: int,
                 modules: List[Module],
                 name: str = None,
                 description: str = None) -> None:
        self.role = role
        self.eqf_level = eqf_level
        self.modules = modules
        self.name = name or f"{role.name} Curriculum (EQF Level {eqf_level})"
        self.description = description or f"Curriculum for {role.name} at EQF Level {eqf_level}"

        # Calculate total ECTS
        self.total_ects = sum(module.ects_points for module in modules)

        # Calculate percentage of work-based learning
        work_based_ects = sum(module.ects_points for module in modules if module.is_work_based)
        self.work_based_percentage = (work_based_ects / self.total_ects * 100) if self.total_ects > 0 else 0

        # Extract thematic area from role
        self.thematic_area = role.thematic_area

        # Program duration in semesters
        self.program_duration = role.program_duration.get(eqf_level, 6)

        # Get program learning outcomes for this specific EQF level
        self.program_learning_outcomes = role.program_learning_outcomes.get(
            eqf_level,
            ["Apply knowledge and skills in " + self.thematic_area]
        )

        # Program assessment methods
        self.assessment_methods = role.assessment_methods

        # Organize modules by semester
        self.modules_by_semester = self._organize_modules_by_semester()

        # Career pathways
        self.career_paths = role.career_paths

        # Skills categorization
        self.skills_by_category = self._categorize_skills()

    def to_dict(self) -> Dict[str, Any]:
        """Convert curriculum to dictionary representation"""
        return {
            "name": self.name,
            "description": self.description,
            "role": self.role.to_dict(),
            "eqf_level": self.eqf_level,
            "modules": [module.to_dict() for module in self.modules],
            "total_ects": self.total_ects,
            "work_based_percentage": self.work_based_percentage,
            "thematic_area": self.thematic_area,
            "program_duration": self.program_duration,
            "program_learning_outcomes": self.program_learning_outcomes,
            "assessment_methods": self.assessment_methods,
            "career_paths": self.career_paths,
            "skills_by_category": self.skills_by_category
        }

    def get_covered_skills(self) -> Set[str]:
        """Get set of all skills covered by this curriculum"""
        skills = set()
        for module in self.modules:
            skills.update(module.skills)
        return skills

    def _organize_modules_by_semester(self) -> Dict[int, List[Module]]:
        """Organize modules by semester"""
        modules_by_semester = {}

        # First, use existing semester assignments
        for module in self.modules:
            if module.semester is not None:
                if module.semester not in modules_by_semester:
                    modules_by_semester[module.semester] = []
                modules_by_semester[module.semester].append(module)

        # If no semester assignments, organize them logically
        if not modules_by_semester:
            # Create a dependency graph
            dependencies = {}
            for module in self.modules:
                dependencies[module.id] = module.prerequisites

            # Assign semesters based on dependencies
            semesters = {}
            self._assign_semesters_recursive(dependencies, semesters)

            # Distribute modules to semesters
            for module in self.modules:
                semester = semesters.get(module.id, 1)
                if semester > self.program_duration:
                    semester = self.program_duration
                if semester not in modules_by_semester:
                    modules_by_semester[semester] = []
                modules_by_semester[semester].append(module)

            # Balance semesters if needed
            modules_by_semester = self._balance_semesters(modules_by_semester)

        return modules_by_semester

    def _assign_semesters_recursive(self, dependencies: Dict[str, List[str]], semesters: Dict[str, int], module_id: str = None, visited: Set[str] = None) -> int:
        """Recursively assign semesters based on dependencies"""
        if visited is None:
            visited = set()

        # If no specific module is provided, process all modules
        if module_id is None:
            max_semester = 1
            for module_id in dependencies:
                if module_id not in visited:
                    semester = self._assign_semesters_recursive(dependencies, semesters, module_id, visited)
                    max_semester = max(max_semester, semester)
            return max_semester

        # Skip if already visited
        if module_id in visited:
            return semesters.get(module_id, 1)

        # Mark as visited
        visited.add(module_id)

        # If no prerequisites, assign to semester 1
        prereqs = dependencies.get(module_id, [])
        if not prereqs:
            semesters[module_id] = 1
            return 1

        # Process prerequisites and assign to the semester after the latest prerequisite
        max_prereq_semester = 0
        for prereq in prereqs:
            # Skip if prerequisite doesn't exist (might be from outside the current module set)
            if prereq not in dependencies:
                continue
            prereq_semester = self._assign_semesters_recursive(dependencies, semesters, prereq, visited)
            max_prereq_semester = max(max_prereq_semester, prereq_semester)

        # Assign to semester after prerequisites
        semesters[module_id] = max_prereq_semester + 1
        return semesters[module_id]

    def _balance_semesters(self, modules_by_semester: Dict[int, List[Module]]) -> Dict[int, List[Module]]:
        """Balance modules across semesters"""
        # Get total ECTS per semester
        ects_by_semester = {}
        for semester, modules in modules_by_semester.items():
            ects_by_semester[semester] = sum(module.ects_points for module in modules)

        # Calculate average ECTS per semester
        target_ects = self.total_ects / self.program_duration

        # Try to balance semesters (simple approach)
        for current_semester in range(1, self.program_duration):
            if current_semester not in ects_by_semester:
                continue

            current_ects = ects_by_semester.get(current_semester, 0)

            # Skip if already balanced
            if abs(current_ects - target_ects) <= 5:
                continue

            # Get movable modules (those without others depending on them)
            movable_modules = []
            for module in modules_by_semester.get(current_semester, []):
                if not any(module.id in m.prerequisites for m in self.modules):
                    movable_modules.append(module)

            # Sort by ECTS points (smallest first)
            movable_modules.sort(key=lambda m: m.ects_points)

            # Try to move modules to next semester if overloaded
            if current_ects > target_ects and movable_modules:
                next_semester = current_semester + 1
                if next_semester not in modules_by_semester:
                    modules_by_semester[next_semester] = []

                for module in movable_modules:
                    if current_ects - module.ects_points >= target_ects - 5:
                        modules_by_semester[current_semester].remove(module)
                        modules_by_semester[next_semester].append(module)
                        current_ects -= module.ects_points
                        ects_by_semester[current_semester] = current_ects
                        ects_by_semester[next_semester] = ects_by_semester.get(next_semester, 0) + module.ects_points
                    else:
                        break

        return modules_by_semester

    def _categorize_skills(self) -> Dict[str, List[str]]:
        """Categorize skills into technical, domain-specific, and transversal"""
        all_skills = self.get_covered_skills()

        # Define categories based on thematic area
        if self.thematic_area == "sustainability":
            categories = {
                "technical": [
                    "data_analytics", "digital_technology", "software_development",
                    "system_architecture", "cloud_computing", "iot", "blockchain"
                ],
                "green": [
                    "sustainability_basics", "esg_reporting", "circular_economy",
                    "impact_measurement", "carbon_footprint", "sustainable_it"
                ],
                "transversal": [
                    "leadership", "communication", "critical_thinking", "team_management",
                    "project_management", "strategic_thinking", "problem_solving"
                ]
            }
        elif self.thematic_area == "cybersecurity":
            categories = {
                "technical": [
                    "network_security", "encryption", "secure_coding", "penetration_testing",
                    "forensics", "vulnerability_assessment", "security_architecture"
                ],
                "domain": [
                    "security_basics", "risk_assessment", "compliance", "incident_response",
                    "security_governance", "threat_intelligence", "security_operations"
                ],
                "transversal": [
                    "leadership", "communication", "critical_thinking", "team_management",
                    "project_management", "strategic_thinking", "problem_solving"
                ]
            }
        else:
            # Generic categories for other domains
            categories = {
                "technical": [],
                "domain": [],
                "transversal": [
                    "leadership", "communication", "critical_thinking", "team_management",
                    "project_management", "strategic_thinking", "problem_solving"
                ]
            }

        # Categorize skills
        categorized_skills = {
            "technical": [],
            "domain": [],
            "transversal": []
        }

        for skill in all_skills:
            if skill in categories.get("technical", []):
                categorized_skills["technical"].append(skill)
            elif skill in categories.get("green", []) or skill in categories.get("domain", []):
                categorized_skills["domain"].append(skill)
            elif skill in categories.get("transversal", []):
                categorized_skills["transversal"].append(skill)
            else:
                # Place in most appropriate category based on name
                if any(tech in skill for tech in ["data", "software", "system", "tech", "digital", "code"]):
                    categorized_skills["technical"].append(skill)
                elif any(trans in skill for trans in ["manage", "communicate", "think", "lead", "solve"]):
                    categorized_skills["transversal"].append(skill)
                else:
                    categorized_skills["domain"].append(skill)

        # Rename domain to appropriate name based on thematic area
        if self.thematic_area == "sustainability":
            categorized_skills["green"] = categorized_skills.pop("domain")
        else:
            categorized_skills[self.thematic_area] = categorized_skills.pop("domain")

        return categorized_skills

    def export_as_html(self, output_file: str) -> None:
        """Export curriculum as HTML with enhanced details"""
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>{self.name}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; line-height: 1.6; }}
                h1, h2, h3 {{ color: #2c3e50; }}
                h1 {{ border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
                h2 {{ border-bottom: 1px solid #3498db; padding-bottom: 5px; margin-top: 30px; }}
                table {{ border-collapse: collapse; width: 100%; margin-bottom: 20px; }}
                th, td {{ border: 1px solid #ddd; padding: 12px 8px; text-align: left; }}
                th {{ background-color: #f2f2f2; }}
                tr:nth-child(even) {{ background-color: #f9f9f9; }}
                .section {{ margin-bottom: 30px; }}
                .overview-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; margin: 20px 0; }}
                .overview-item {{ background-color: #f8f9fa; padding: 15px; border-radius: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
                .overview-item h3 {{ margin-top: 0; color: #3498db; }}
                .assessment-bar {{ display: flex; margin-bottom: 15px; }}
                .assessment-item {{ background-color: #3498db; color: white; padding: 10px; margin-right: 5px; text-align: center; }}
                .skill-category {{ margin-bottom: 20px; }}
                .skill-list {{ display: flex; flex-wrap: wrap; gap: 10px; }}
                .skill-tag {{ background-color: #e8f4fc; padding: 8px 15px; border-radius: 20px; font-size: 0.9em; }}
                .career-item {{ background-color: #f0f8ff; padding: 10px 15px; margin-bottom: 10px; border-left: 4px solid #3498db; }}
                .semester-header {{ background-color: #eaf2f8; font-weight: bold; }}
            </style>
        </head>
        <body>
            <h1>{self.name}</h1>
            <p class="section">{self.description}</p>

            <h2>Program Overview</h2>
            <div class="overview-grid">
                <div class="overview-item">
                    <h3>Role</h3>
                    <p>{self.role.name}</p>
                </div>
                <div class="overview-item">
                    <h3>Thematic Area</h3>
                    <p>{self.thematic_area.capitalize()}</p>
                </div>
                <div class="overview-item">
                    <h3>EQF Level</h3>
                    <p>{self.eqf_level}</p>
                </div>
                <div class="overview-item">
                    <h3>Total ECTS</h3>
                    <p>{self.total_ects}</p>
                </div>
                <div class="overview-item">
                    <h3>Duration</h3>
                    <p>{self.program_duration} semesters ({self.program_duration//2} years)</p>
                </div>
                <div class="overview-item">
                    <h3>Work-based Learning</h3>
                    <p>{self.work_based_percentage:.1f}% ({int(self.total_ects * self.work_based_percentage / 100)} ECTS)</p>
                </div>
            </div>

            <h2>Program Learning Outcomes</h2>
            <p>Upon successful completion of this program, graduates will be able to:</p>
            <ol>
        """

        for outcome in self.program_learning_outcomes:
            html_content += f"                <li>{outcome}</li>\n"

        html_content += """
            </ol>

            <h2>Assessment Methods</h2>
            <div class="assessment-bar">
        """

        for method in self.assessment_methods:
            html_content += f"""
                <div class="assessment-item" style="width: {method['weight']}%">
                    {method['name']} ({method['weight']}%)
                </div>"""

        html_content += """
            </div>
        """

        # Add modules by semester
        html_content += """
            <h2>Curriculum Structure</h2>
        """

        for semester in sorted(self.modules_by_semester.keys()):
            html_content += f"""
            <h3>Semester {semester}</h3>
            <table>
                <tr>
                    <th>Module Code</th>
                    <th>Module Name</th>
                    <th>ECTS</th>
                    <th>Type</th>
                    <th>Delivery</th>
                    <th>Description</th>
                </tr>
            """

            for module in self.modules_by_semester[semester]:
                module_type = "/".join(module.module_type)
                delivery = "/".join(module.delivery_methods)

                html_content += f"""
                <tr>
                    <td>{module.id}</td>
                    <td>{module.name}</td>
                    <td>{module.ects_points}</td>
                    <td>{module_type}</td>
                    <td>{delivery}</td>
                    <td>{module.description}</td>
                </tr>
                """

            html_content += """
            </table>
            """

        # Add module details
        html_content += """
            <h2>Module Details</h2>
        """

        for semester in sorted(self.modules_by_semester.keys()):
            for module in self.modules_by_semester[semester]:
                html_content += f"""
                <h3>{module.name} ({module.id})</h3>
                <div class="overview-grid">
                    <div class="overview-item">
                        <h4>ECTS</h4>
                        <p>{module.ects_points}</p>
                    </div>
                    <div class="overview-item">
                        <h4>Semester</h4>
                        <p>{semester}</p>
                    </div>
                    <div class="overview-item">
                        <h4>Type</h4>
                        <p>{'/'.join(module.module_type)}</p>
                    </div>
                    <div class="overview-item">
                        <h4>Delivery</h4>
                        <p>{'/'.join(module.delivery_methods)}</p>
                    </div>
                    <div class="overview-item">
                        <h4>Work-based</h4>
                        <p>{'Yes' if module.is_work_based else 'No'}</p>
                    </div>
                """

                if module.prerequisites:
                    html_content += f"""
                    <div class="overview-item">
                        <h4>Prerequisites</h4>
                        <p>{', '.join(module.prerequisites)}</p>
                    </div>
                    """

                html_content += """
                </div>
                """

                html_content += f"""
                <p><strong>Description:</strong> {module.description}</p>
                """

                if module.learning_outcomes:
                    html_content += """
                    <p><strong>Learning Outcomes:</strong></p>
                    <ul>
                    """
                    for outcome in module.learning_outcomes:
                        html_content += f"    <li>{outcome}</li>\n"
                    html_content += "</ul>\n"

                if module.content_topics:
                    html_content += """
                    <p><strong>Content Topics:</strong></p>
                    <ul>
                    """
                    for topic in module.content_topics:
                        html_content += f"    <li>{topic}</li>\n"
                    html_content += "</ul>\n"

                if module.assessment_methods:
                    html_content += """
                    <p><strong>Assessment Methods:</strong></p>
                    <ul>
                    """
                    for method in module.assessment_methods:
                        html_content += f"    <li>{method.replace('_', ' ').title()}</li>\n"
                    html_content += "</ul>\n"

        # Add skills section
        html_content += """
            <h2>Skills Coverage</h2>
        """

        for category, skills in self.skills_by_category.items():
            if skills:
                html_content += f"""
                <div class="skill-category">
                    <h3>{category.capitalize()} Skills</h3>
                    <div class="skill-list">
                """

                for skill in sorted(skills):
                    html_content += f'<span class="skill-tag">{skill.replace("_", " ").title()}</span>\n'

                html_content += """
                    </div>
                </div>
                """

        # Add career paths
        if self.career_paths:
            html_content += """
            <h2>Career Pathways</h2>
            <p>Graduates of this program can pursue careers as:</p>
            """

            for path in self.career_paths:
                html_content += f'<div class="career-item">{path}</div>\n'

        html_content += """
        </body>
        </html>
        """

        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Write HTML file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_content)

    def export_as_json(self, output_file: str) -> None:
        """Export curriculum as JSON"""
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Write JSON file
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2)

class CurriculumGenerator:
    """Curriculum generator for various thematic areas"""
    def __init__(self):
        """Initialize the curriculum generator"""
        self.modules = []
        self.roles = []

    def load_modules_from_json(self, json_file):
        """Load modules from a JSON file"""
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            print(f"Successfully loaded {len(data)} modules from {json_file}")
            self.modules = [Module.from_dict(module_data) for module_data in data]
        except FileNotFoundError:
            print(f"Module file {json_file} not found.")
        except json.JSONDecodeError as e:
            print(f"Error decoding {json_file}: {e}")
            print("Make sure it's valid JSON.")
        except Exception as e:
            print(f"Unexpected error loading {json_file}: {e}")

    def load_roles_from_json(self, json_file):
        """Load roles from a JSON file"""
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            print(f"Successfully loaded {len(data)} roles from {json_file}")
            self.roles = [Role.from_dict(role_data) for role_data in data]
        except FileNotFoundError:
            print(f"Role file {json_file} not found.")
        except json.JSONDecodeError as e:
            print(f"Error decoding {json_file}: {e}")
            print("Make sure it's valid JSON.")
        except Exception as e:
            print(f"Unexpected error loading {json_file}: {e}")

    def get_role(self, role_id):
        """Get a role by ID"""
        for role in self.roles:
            if role.id == role_id:
                return role
        return None

    def generate_curriculum(self, role_id, eqf_level, is_full_curriculum=True, target_skills=None):
        """Generate a basic curriculum"""
        # Create a simple sample role if none exists
        role = self.get_role(role_id)
        if not role:
            role = Role(
                id=role_id,
                name="Digital Sustainability Lead",
                description="Drives digital sustainability initiatives within organizations",
                main_area="Management & Consultancy",
                thematic_area="sustainability"
            )

        # Create sample modules if none exist
        if not self.modules:
            modules = [
                Module(
                    id="DSL601",
                    name="Introduction to Digital Sustainability",
                    description="Fundamentals of digital sustainability concepts and principles",
                    eqf_level=eqf_level,
                    ects_points=5,
                    thematic_area="sustainability",
                    prerequisites=[],
                    delivery_methods=["classroom", "online"],
                    module_type=["theoretical"],
                    skills=["sustainability_basics", "critical_thinking"],
                    semester=1
                ),
                Module(
                    id="DSL602",
                    name="Sustainability Frameworks and Standards",
                    description="Overview of major sustainability frameworks, regulations, and standards",
                    eqf_level=eqf_level,
                    ects_points=5,
                    thematic_area="sustainability",
                    prerequisites=["DSL601"],
                    delivery_methods=["classroom", "online"],
                    module_type=["theoretical"],
                    skills=["sustainability_regulations", "esg_reporting"],
                    semester=1
                ),
                Module(
                    id="DSL603",
                    name="Digital Technologies for Sustainability",
                    description="Survey of digital technologies that enable sustainability initiatives",
                    eqf_level=eqf_level,
                    ects_points=5,
                    thematic_area="sustainability",
                    prerequisites=["DSL601"],
                    delivery_methods=["classroom", "blended"],
                    module_type=["theoretical", "practical"],
                    skills=["digital_technology", "sustainable_it"],
                    semester=1
                )
            ]
        else:
            # Use the existing modules that match the EQF level
            modules = [m for m in self.modules if m.eqf_level == eqf_level]

            # If still no modules, create default ones
            if not modules:
                modules = [
                    Module(
                        id="DSL601",
                        name="Introduction to Digital Sustainability",
                        description="Fundamentals of digital sustainability concepts and principles",
                        eqf_level=eqf_level,
                        ects_points=5,
                        thematic_area="sustainability",
                        prerequisites=[],
                        delivery_methods=["classroom", "online"],
                        module_type=["theoretical"],
                        skills=["sustainability_basics", "critical_thinking"],
                        semester=1
                    )
                ]

        # Create and return a curriculum
        return Curriculum(
            role=role,
            eqf_level=eqf_level,
            modules=modules
        )
