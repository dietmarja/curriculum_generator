# models.py

"""
Flexible Curriculum Generator - Core Classes

This module contains core classes for generating curricula across different thematic domains,
including but not limited to digital sustainability, business, computer security, etc.
"""

import json
import os
from typing import List, Dict, Any, Set, Optional

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
                 is_work_based: bool = False) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.eqf_level = eqf_level
        self.ects_points = ects_points
        self.thematic_area = thematic_area  # e.g., "sustainability", "cybersecurity", "business"
        self.prerequisites = prerequisites or []
        self.delivery_methods = delivery_methods or ["classroom"]
        self.module_type = module_type or ["theoretical"]
        self.skills = skills or []
        self.role_relevance = role_relevance or {}
        self.is_work_based = is_work_based
    
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
            "is_work_based": self.is_work_based
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
            is_work_based=data.get("is_work_based", False)
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
                 default_ects: Dict[int, int] = None) -> None:
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
            "default_ects": self.default_ects
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
            })
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
            "thematic_area": self.thematic_area
        }
    
    def get_covered_skills(self) -> Set[str]:
        """Get set of all skills covered by this curriculum"""
        skills = set()
        for module in self.modules:
            skills.update(module.skills)
        return skills
    
    def export_as_html(self, output_file: str) -> None:
        """Export curriculum as HTML"""
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>{self.name}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                h1, h2, h3 {{ color: #2c3e50; }}
                table {{ border-collapse: collapse; width: 100%; margin-bottom: 20px; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #f2f2f2; }}
                tr:nth-child(even) {{ background-color: #f9f9f9; }}
            </style>
        </head>
        <body>
            <h1>{self.name}</h1>
            <p>{self.description}</p>
            
            <h2>Program Overview</h2>
            <ul>
                <li><strong>Role:</strong> {self.role.name}</li>
                <li><strong>Thematic Area:</strong> {self.thematic_area.capitalize()}</li>
                <li><strong>EQF Level:</strong> {self.eqf_level}</li>
                <li><strong>Total ECTS:</strong> {self.total_ects}</li>
                <li><strong>Work-based Learning:</strong> {self.work_based_percentage:.1f}%</li>
            </ul>
            
            <h2>Modules</h2>
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
        
        for module in self.modules:
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
            
            <h2>Skills Coverage</h2>
            <ul>
        """
        
        for skill in sorted(self.get_covered_skills()):
            html_content += f"<li>{skill.replace('_', ' ').title()}</li>\n"
        
        html_content += """
            </ul>
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
    def __init__(self, modules: List[Module] = None, roles: List[Role] = None) -> None:
        self.modules = modules or []
        self.roles = roles or []
    
    def load_modules_from_json(self, json_file: str) -> None:
        """Load modules from a JSON file"""
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
            
            self.modules = [Module.from_dict(module_data) for module_data in data]
        except FileNotFoundError:
            print(f"Module file {json_file} not found.")
        except json.JSONDecodeError:
            print(f"Error decoding {json_file}. Make sure it's valid JSON.")
    
    def load_roles_from_json(self, json_file: str) -> None:
        """Load roles from a JSON file"""
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
            
            self.roles = [Role.from_dict(role_data) for role_data in data]
        except FileNotFoundError:
            print(f"Role file {json_file} not found.")
        except json.JSONDecodeError:
            print(f"Error decoding {json_file}. Make sure it's valid JSON.")
    
    def get_role(self, role_id: str) -> Optional[Role]:
        """Get a role by ID"""
        for role in self.roles:
            if role.id == role_id:
                return role
        return None
    
    def filter_modules(self, 
                       eqf_level: int = None, 
                       role_id: str = None,
                       thematic_area: str = None,
                       min_relevance: float = 0) -> List[Module]:
        """Filter modules based on criteria"""
        filtered = self.modules
        
        if eqf_level is not None:
            filtered = [m for m in filtered if m.eqf_level == eqf_level]
        
        if thematic_area is not None:
            filtered = [m for m in filtered if m.thematic_area == thematic_area]
        
        if role_id is not None:
            filtered = [m for m in filtered if role_id in m.role_relevance and 
                      m.role_relevance[role_id] >= min_relevance]
        
        return filtered
    
    def generate_curriculum(self, 
                           role_id: str, 
                           eqf_level: int,
                           is_full_curriculum: bool = True,
                           target_skills: List[str] = None,
                           min_module_relevance: float = 50,
                           name: str = None,
                           description: str = None) -> Optional[Curriculum]:
        """Generate a curriculum for a specific role and EQF level"""
        role = self.get_role(role_id)
        if role is None:
            print(f"Role with ID {role_id} not found")
            return None
        
        if eqf_level not in role.eqf_levels:
            print(f"EQF level {eqf_level} is not applicable for role {role.name}")
            return None
        
        # Filter modules by EQF level, thematic area, and role relevance
        eligible_modules = self.filter_modules(
            eqf_level=eqf_level,
            thematic_area=role.thematic_area,
            role_id=role_id,
            min_relevance=min_module_relevance
        )
        
        if not eligible_modules:
            print(f"No eligible modules found for role {role.name} at EQF level {eqf_level}")
            return None
        
        # Sort by relevance to the role
        eligible_modules.sort(key=lambda m: m.role_relevance.get(role_id, 0), reverse=True)
        
        # Select modules based on parameters
        target_ects = role.default_ects.get(eqf_level, 60)
        selected_modules = []
        current_ects = 0
        
        # For a full curriculum
        if is_full_curriculum:
            # First include highly relevant modules
            for module in eligible_modules:
                if module.role_relevance.get(role_id, 0) >= 80 and current_ects + module.ects_points <= target_ects:
                    selected_modules.append(module)
                    current_ects += module.ects_points
            
            # Then add modules that cover core skills for the role
            if role.core_skills:
                remaining_modules = [m for m in eligible_modules if m not in selected_modules]
                for module in remaining_modules:
                    if any(skill in role.core_skills for skill in module.skills) and current_ects + module.ects_points <= target_ects:
                        selected_modules.append(module)
                        current_ects += module.ects_points
            
            # Fill in with other modules to reach target ECTS
            remaining_modules = [m for m in eligible_modules if m not in selected_modules]
            for module in remaining_modules:
                if current_ects + module.ects_points <= target_ects:
                    selected_modules.append(module)
                    current_ects += module.ects_points
                
                if current_ects >= target_ects:
                    break
        
        # For specialized curriculum focusing on specific skills
        else:
            if target_skills:
                # Prioritize modules that cover target skills
                modules_with_target_skills = {}
                for module in eligible_modules:
                    skill_count = sum(1 for skill in module.skills if skill in target_skills)
                    if skill_count > 0:
                        modules_with_target_skills[module] = skill_count
                
                # Sort modules by number of target skills covered
                skill_coverage_modules = sorted(
                    modules_with_target_skills.keys(),
                    key=lambda m: modules_with_target_skills[m],
                    reverse=True
                )
                
                # Add modules until we reach target ECTS (capped at original target)
                for module in skill_coverage_modules:
                    if current_ects + module.ects_points <= target_ects:
                        selected_modules.append(module)
                        current_ects += module.ects_points
                    
                    if current_ects >= target_ects:
                        break
            else:
                # Without target skills, just use most relevant modules
                for module in eligible_modules:
                    if current_ects + module.ects_points <= target_ects:
                        selected_modules.append(module)
                        current_ects += module.ects_points
                    
                    if current_ects >= target_ects:
                        break
        
        # Create curriculum with selected modules
        return Curriculum(
            role=role,
            eqf_level=eqf_level,
            modules=selected_modules,
            name=name,
            description=description
        )
        
    def get_thematic_areas(self) -> List[str]:
        """Get a list of available thematic areas"""
        areas = set()
        for role in self.roles:
            areas.add(role.thematic_area)
        return sorted(list(areas))
    
    def get_roles_by_thematic_area(self, thematic_area: str) -> List[Role]:
        """Get roles for a specific thematic area"""
        return [role for role in self.roles if role.thematic_area == thematic_area]