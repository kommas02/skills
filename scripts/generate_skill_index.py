#!/usr/bin/env python3
"""
Generate skills/index.json manifest with all skills, versions, and metadata.
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml


def extract_frontmatter(skill_md_path):
    """Extract YAML frontmatter from SKILL.md"""
    content = skill_md_path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return None

    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None

    frontmatter_text = match.group(1)
    try:
        return yaml.safe_load(frontmatter_text)
    except yaml.YAMLError:
        return None


def get_license(skill_path):
    """Get license for the skill"""
    license_path = skill_path / "LICENSE.txt"
    if license_path.exists():
        content = license_path.read_text(encoding="utf-8").strip()
        if "Apache License" in content:
            return "Apache-2.0"
        elif "MIT" in content:
            return "MIT"
        elif "GNU" in content:
            return "GPL-3.0"
        return "Custom"
    return None


def scan_skills(root_dir):
    """Scan all skills and extract metadata"""
    skills = []
    root = Path(root_dir)

    for category in [".system", ".curated"]:
        category_path = root / "skills" / category
        if not category_path.exists():
            continue

        for skill_dir in category_path.iterdir():
            if not skill_dir.is_dir():
                continue

            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue

            frontmatter = extract_frontmatter(skill_md)
            if not frontmatter:
                continue

            name = frontmatter.get("name", skill_dir.name)
            description = frontmatter.get("description", "")
            version = frontmatter.get("version", "1.0.0")
            metadata = frontmatter.get("metadata", {})
            allowed_tools = frontmatter.get("allowed-tools", [])
            license_text = get_license(skill_dir)

            skill_info = {
                "name": name,
                "description": description,
                "version": version,
                "category": category.lstrip("."),
                "path": f"skills/{category}/{skill_dir.name}",
                "metadata": metadata,
            }

            if allowed_tools:
                skill_info["allowed-tools"] = allowed_tools
            if license_text:
                skill_info["license"] = license_text

            skills.append(skill_info)

    return skills


def generate_index(skills_root, output_path):
    """Generate the index.json file"""
    skills = scan_skills(skills_root)

    index = {
        "version": "1.0.0",
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "total_skills": len(skills),
        "skills": sorted(skills, key=lambda x: x["name"]),
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Generated {output_path} with {len(skills)} skills")
    return index


if __name__ == "__main__":
    if len(sys.argv) > 1:
        skills_root = Path(sys.argv[1])
    else:
        skills_root = Path(__file__).parent.parent

    output_path = skills_root / "skills" / "index.json"
    generate_index(skills_root, output_path)
