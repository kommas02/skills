# Quality Assurance Domain

## Mission
Deliver small, safe, measurable improvements to ensure repository quality through automated validation and testing.

## Current Focus
- Skill validation (SKILL.md structure, YAML validity, Python syntax)
- GitHub Actions workflows for continuous validation

## Implemented Solutions

### validate-skills.yml
Automated validation workflow for all skills in the repository.

**Validates:**
1. YAML syntax for all `agents/openai.yaml` files
2. Required fields in openai.yaml (`interface`, `display_name`, `short_description`, `default_prompt`)
3. Python syntax for all `.py` files
4. SKILL.md frontmatter (required `name` and `description` fields)
5. Markdown link validity

**Scripts:**
- `.github/scripts/validate_openai.py` - Validates openai.yaml structure
- `.github/scripts/validate_skill.py` - Validates SKILL.md frontmatter
- `.github/scripts/validate_python.py` - Validates Python syntax
- `.github/scripts/validate_links.py` - Validates markdown links

**Triggers:**
- On pull requests modifying `skills/**`
- On push to main modifying `skills/**`

## Known Issues
- `skills/.system/skill-installer/agents/openai.yaml` missing `default_prompt` field

## Future Improvements
- Add more comprehensive schema validation
- Consider adding integration tests for skill scripts
