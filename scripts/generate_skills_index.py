#!/usr/bin/env python3
"""
Skills Index Generator - Generates skills/index.json manifest

Usage:
    generate_skills_index.py [--path <skills-dir>] [--output <output-file>]

Outputs a JSON manifest of all skills with their metadata.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from datetime import datetime, timezone


def parse_skill_md(skill_path: Path) -> dict | None:
    """Parse SKILL.md frontmatter to extract metadata."""
    try:
        content = skill_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"[WARN] Could not read {skill_path}: {e}")
        return None

    frontmatter_pattern = r"^---\s*\n(.*?)\n---"
    match = re.match(frontmatter_pattern, content, re.DOTALL)

    if not match:
        print(f"[WARN] No frontmatter found in {skill_path}")
        return None

    frontmatter_text = match.group(1)
    metadata = {}

    for line in frontmatter_text.split("\n"):
        line = line.strip()
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            
            metadata[key] = value

    return metadata


def get_agents_metadata(skill_path: Path) -> dict:
    """Read agents/openai.yaml for additional UI metadata."""
    yaml_path = skill_path / "agents" / "openai.yaml"
    if not yaml_path.exists():
        return {}

    try:
        content = yaml_path.read_text(encoding="utf-8")
        metadata = {}
        
        for line in content.split("\n"):
            line = line.strip()
            if ":" in line:
                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip()
                
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                
                if key in ("display_name", "short_description", "default_prompt", "icon"):
                    metadata[key] = value
        
        return metadata
    except Exception as e:
        print(f"[WARN] Could not read {yaml_path}: {e}")
        return {}


def discover_skills(skills_root: Path) -> list[dict]:
    """Discover all skills in the skills directory."""
    skills = []

    for category in (".system", ".curated"):
        category_path = skills_root / category
        if not category_path.exists():
            continue

        for skill_dir in sorted(category_path.iterdir()):
            if not skill_dir.is_dir():
                continue
            
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue

            skill_metadata = parse_skill_md(skill_md)
            if not skill_metadata:
                continue

            agents_metadata = get_agents_metadata(skill_dir)

            skill_info = {
                "name": skill_metadata.get("name", skill_dir.name),
                "version": skill_metadata.get("version", "1.0.0"),
                "description": skill_metadata.get("description", ""),
                "category": category.lstrip("."),
                "path": str(skill_dir.relative_to(skills_root)),
            }

            if agents_metadata:
                skill_info["display_name"] = agents_metadata.get("display_name", "")
                skill_info["short_description"] = agents_metadata.get("short_description", "")
                skill_info["default_prompt"] = agents_metadata.get("default_prompt", "")
                if agents_metadata.get("icon"):
                    skill_info["icon"] = agents_metadata["icon"]

            skills.append(skill_info)

    return skills


def generate_index(skills_root: Path, output_path: Path | None = None):
    """Generate the skills index.json."""
    skills = discover_skills(skills_root)

    index = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_skills": len(skills),
        "skills": skills,
    }

    json_output = json.dumps(index, indent=2, ensure_ascii=False)

    if output_path:
        output_path.write_text(json_output + "\n", encoding="utf-8")
        print(f"[OK] Generated {output_path} with {len(skills)} skills")
    else:
        print(json_output)

    return index


def main():
    parser = argparse.ArgumentParser(
        description="Generate skills/index.json manifest from SKILL.md files."
    )
    parser.add_argument(
        "--path",
        default="skills",
        help="Path to skills directory (default: skills)",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Output file path (default: stdout)",
    )
    args = parser.parse_args()

    skills_root = Path(args.path).resolve()
    if not skills_root.exists():
        print(f"[ERROR] Skills directory not found: {skills_root}")
        sys.exit(1)

    output_path = Path(args.output).resolve() if args.output else None
    generate_index(skills_root, output_path)


if __name__ == "__main__":
    main()
