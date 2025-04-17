# generate_curriculum.py

"""
Flexible Curriculum Generator - Command Line Interface

Usage:
    python generate_curriculum.py --role CSO --eqf 6 --output curriculum.html
    python generate_curriculum.py --role DSL --eqf 6 --skills "esg_reporting,data_analytics" --output curriculum.json
    python generate_curriculum.py --list-areas
    python generate_curriculum.py --area cybersecurity --list-roles
"""

import os
import sys
import json
import argparse
from typing import List


# Add the project root directory to the Python path
# This allows Python to find the dscg package regardless of where the script is run from
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now import the modules
from dscg.package.models import Module, Role, Curriculum, CurriculumGenerator
# Import the new functions
from dscg.package.enhancements import integrate_all_improvements
from dscg.package.models import CurriculumGenerator, Curriculum










# Fix the import statement to match your actual directory structure
# The models.py file is in dscg/package/models.py
# from dscg.package.models import Module, Role, Curriculum, CurriculumGenerator



def setup_argparse() -> argparse.ArgumentParser:
    """Set up argument parser for command line interface"""
    parser = argparse.ArgumentParser(
        description="Flexible Curriculum Generator"
    )
    
    # Information commands
    info_group = parser.add_argument_group('Information')
    info_group.add_argument(
        "--list-areas", 
        action="store_true",
        help="List all available thematic areas"
    )
    
    info_group.add_argument(
        "--area", 
        type=str, 
        help="Specify thematic area for listing roles"
    )
    
    info_group.add_argument(
        "--list-roles", 
        action="store_true",
        help="List all roles for specified thematic area"
    )
    
    # Generation commands
    gen_group = parser.add_argument_group('Curriculum Generation')
    gen_group.add_argument(
        "--role", 
        type=str, 
        help="Role ID (e.g., DSL for Digital Sustainability Lead, CSO for Chief Security Officer)"
    )
    
    gen_group.add_argument(
        "--eqf", 
        type=int, 
        help="EQF level (4-8)"
    )
    
    # Optional arguments
    gen_group.add_argument(
        "--skills", 
        type=str, 
        help="Target skills for specialized curriculum, comma-separated"
    )
    
    gen_group.add_argument(
        "--full", 
        action="store_true",
        default=True,
        help="Generate a full curriculum (default)"
    )
    
    gen_group.add_argument(
        "--specialized", 
        action="store_true",
        help="Generate a specialized curriculum instead of full"
    )
    
    gen_group.add_argument(
        "--output", 
        type=str, 
        help="Output file path (required for curriculum generation)"
    )
    
    gen_group.add_argument(
        "--format", 
        type=str, 
        choices=["html", "json"],
        help="Output format (default: based on file extension)"
    )
    
    # Common arguments
    parser.add_argument(
        "--data-dir", 
        type=str, 
        default="data",
        help="Directory containing data files"
    )
    
    return parser


def load_generator(data_dir: str) -> CurriculumGenerator:
    """Load data and initialize curriculum generator"""
    modules_path = os.path.join(data_dir, "modules.json")
    roles_path = os.path.join(data_dir, "roles.json")
    
    # Check if data files exist
    if not os.path.exists(modules_path):
        print(f"Error: Module data file not found at {modules_path}")
        sys.exit(1)
    
    if not os.path.exists(roles_path):
        print(f"Error: Role data file not found at {roles_path}")
        sys.exit(1)
    
    # Initialize curriculum generator
    generator = CurriculumGenerator()
    
    # Load data
    generator.load_modules_from_json(modules_path)
    generator.load_roles_from_json(roles_path)
    
    return generator


def list_thematic_areas(generator: CurriculumGenerator) -> None:
    """List all available thematic areas"""
    areas = generator.get_thematic_areas()
    
    print("\nAvailable thematic areas:")
    for area in areas:
        print(f"- {area.capitalize()}")
    
    print(f"\nTotal: {len(areas)} thematic areas")


def list_roles_by_area(generator: CurriculumGenerator, area: str) -> None:
    """List all roles for a specific thematic area"""
    roles = generator.get_roles_by_thematic_area(area)
    
    if not roles:
        print(f"No roles found for thematic area: {area}")
        return
    
    print(f"\nRoles in thematic area '{area.capitalize()}':")
    for role in roles:
        print(f"- {role.id}: {role.name} (EQF levels: {', '.join(map(str, role.eqf_levels))})")
    
    print(f"\nTotal: {len(roles)} roles")


def generate_curriculum(generator: CurriculumGenerator, args: argparse.Namespace) -> None:
    """Generate a curriculum based on command-line arguments"""
    # Check required arguments
    if not args.role:
        print("Error: Role ID is required for curriculum generation. Use --role to specify a role.")
        sys.exit(1)
    
    if not args.eqf:
        print("Error: EQF level is required for curriculum generation. Use --eqf to specify a level.")
        sys.exit(1)
    
    if not args.output:
        print("Error: Output file path is required for curriculum generation. Use --output to specify a path.")
        sys.exit(1)
    
    # Determine if generating full or specialized curriculum
    is_full_curriculum = not args.specialized
    
    # Parse target skills if provided
    target_skills = None
    if args.skills:
        target_skills = args.skills.split(",")
    
    # Generate curriculum
    curriculum = generator.generate_curriculum(
        role_id=args.role,
        eqf_level=args.eqf,
        is_full_curriculum=is_full_curriculum,
        target_skills=target_skills
    )
    
    if not curriculum:
        print("Failed to generate curriculum. Check your parameters.")
        sys.exit(1)
    
    # Determine output format
    output_format = args.format
    if not output_format:
        if args.output.lower().endswith(".json"):
            output_format = "json"
        else:
            output_format = "html"
    
    # Export curriculum
    if output_format == "json":
        curriculum.export_as_json(args.output)
    else:  # Default to HTML
        curriculum.export_as_html(args.output)
    
    print(f"\nCurriculum generated successfully for {curriculum.role.name} (EQF Level {curriculum.eqf_level})")
    print(f"Thematic area: {curriculum.thematic_area.capitalize()}")
    print(f"Total ECTS: {curriculum.total_ects}")
    print(f"Work-based learning: {curriculum.work_based_percentage:.1f}%")
    print(f"Output saved to: {args.output}")


def main() -> None:
    """Main function for the curriculum generator script"""
    # Parse command line arguments
    parser = setup_argparse()
    args = parser.parse_args()
    
    # Load the curriculum generator
    generator = load_generator(args.data_dir)
    
    # Determine what action to take
    if args.list_areas:
        list_thematic_areas(generator)
    elif args.area and args.list_roles:
        list_roles_by_area(generator, args.area)
    elif args.role:
        generate_curriculum(generator, args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()