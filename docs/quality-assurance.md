# Quality Assurance Documentation

## Overview

This document outlines the quality assurance practices for the skills repository.

## Validation Scripts

The repository includes validation scripts in `.github/scripts/`:
- `.github/scripts/validate_openai.py` - Validates openai.yaml structure
- `.github/scripts/validate_skill.py` - Validates SKILL.md frontmatter

### GitHub Actions Workflow: validate-skills.yml (NOT YET IMPLEMENTED)

The repository needs an automated validation workflow that runs on:
- Every pull request modifying files in the `skills/` directory
- Every push to main branch that modifies files in the `skills/` directory

#### Required Validation Steps

1. **YAML Syntax Validation**
   - Validates all `agents/openai.yaml` files for proper YAML syntax
   - Ensures YAML files can be parsed without errors

2. **Python Syntax Validation**
   - Validates all `.py` files for correct Python syntax
   - Uses Python's built-in `py_compile` module

3. **SKILL.md Frontmatter Validation**
   - Ensures every skill has a `SKILL.md` file
   - Validates required frontmatter fields:
     - `name`: The skill name
     - `description`: The skill description
   - Checks for proper YAML frontmatter format (--- delimiters)

4. **Markdown Link Validation**
   - Checks for broken relative links in markdown files
   - Validates that linked resources exist

### Running Validation Locally

```bash
# Validate SKILL.md files
python .github/scripts/validate_skill.py

# Validate openai.yaml files
python .github/scripts/validate_openai.py

# Validate YAML syntax
python -c "import yaml; yaml.safe_load(open('path/to/openai.yaml'))"

# Validate Python syntax
python -m py_compile path/to/script.py
```

### Creating the validate-skills.yml workflow

Create `.github/workflows/validate-skills.yml`:

```yaml
name: Validate Skills
on:
  pull_request:
    paths:
      - 'skills/**'
  push:
    branches:
      - main
    paths:
      - 'skills/**'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.x'
      - run: pip install pyyaml
      - run: python .github/scripts/validate_skill.py
      - run: python .github/scripts/validate_openai.py
```

## Skill Structure Requirements

### Required Files

Every skill must include:
- `SKILL.md` - Main skill definition with YAML frontmatter

### Recommended Files

- `agents/openai.yaml` - UI metadata for skill displays

### Optional Files

- `scripts/` - Executable code
- `references/` - Documentation for context loading
- `assets/` - Files used in output

### SKILL.md Frontmatter Format

```yaml
---
name: skill-name
description: Description of when to use this skill
---
```

Required fields:
- `name`: Lowercase, hyphen-separated skill identifier
- `description`: Clear explanation of skill purpose and trigger conditions

## Self-Reflection

### What Worked
- Created validation scripts that can run locally and in CI
- Updated documentation to be accurate about current state
- Found that skill-installer is missing default_prompt field in openai.yaml

### What Didn't Work
- GitHub App token lacks "workflows" permission - cannot push workflow files directly
- Could not create validate-skills.yml workflow file due to permission restriction
- Workaround: Added scripts that can be called manually or via other means

### Teamwork Notes
- Coordination with DX-engineer needed for workflow automation
- Consider adding QA workflow permission to GitHub App
- Validation scripts provide foundation for future CI/CD

### Next Steps
1. Request GitHub App workflow permission
2. Create validate-skills.yml using provided template
3. Add evaluation framework (issue #21)
4. Fix skill-installer missing field

## Issue Tracking

Quality assurance issues are tracked with:
- Layer: QA
- Label: QA
- Owner Agent: Quality-Assurance

## Related Issues

- #5: Add test coverage for skill validation
- #21: Add skill evaluation framework for quality assurance

## Evaluation Framework

See [docs/evaluation-framework.md](evaluation-framework.md) for the complete evaluation framework documentation.

### Quick Summary

- **Purpose**: Test skill quality, accuracy, and effectiveness
- **Location**: Each skill's `evaluation/` directory
- **Minimum Required**: 2 evaluation cases per skill
- **Runner**: `scripts/evaluate_skill.py`

### Adding Evaluations

```bash
mkdir -p skills/my-skill/evaluation/cases
# Add case JSON files...
# Add config.json...
```

### Running Evaluations

```bash
# Evaluate specific skill
python scripts/evaluate_skill.py skills/skill-name

# Evaluate all skills
python scripts/evaluate_skill.py --all
```
