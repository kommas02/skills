# Quality Assurance Documentation

## Overview

This document outlines the quality assurance practices for the skills repository.

## Validation Scripts

The repository includes validation scripts in `.github/scripts/`:
- `.github/scripts/validate_openai.py` - Validates openai.yaml structure
- `.github/scripts/validate_skill.py` - Validates SKILL.md frontmatter
- `.github/scripts/validate_python.py` - Validates Python syntax
- `.github/scripts/validate_links.py` - Validates markdown links

### GitHub Actions Workflow: validate-skills.yml

The repository documents an automated validation workflow at `.github/workflows/validate-skills.yml` (manual setup required - see below).

This workflow runs on:
- Every pull request modifying files in the `skills/` directory
- Every push to opencode branch that modifies files in the `skills/` directory

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

## Running Validation Locally

### Validate YAML Files

```bash
python -c "import yaml; yaml.safe_load(open('path/to/openai.yaml'))"
```

### Validate Python Syntax

```bash
python -m py_compile path/to/script.py
```

### Validate SKILL.md

```bash
# Check frontmatter
head -n 1 SKILL.md  # Should be ---
```

### Run Full Validation

> **Note**: The workflow file requires manual creation (see "Manual Workflow Setup Required" section above).

```bash
# Trigger the workflow manually (after creating the file)
gh workflow run validate-skills.yml
```

## Issue Tracking

Quality assurance issues are tracked with:
- Layer: QA
- Label: QA
- Owner Agent: Quality-Assurance

## Related Issues

- #5: Add test coverage for skill validation (IMPLEMENTED)
- #21: Add skill evaluation framework (IN PROGRESS)
- #51: Missing validate-skills.yml workflow (REQUIRES MANUAL ADD - see below)
- #134: Manual addition: validate-skills.yml workflow (REQUIRES MANUAL ADD - see below)

## Manual Workflow Setup Required

Due to GitHub App permission restrictions, the validate-skills.yml workflow file must be added manually:

**Create `.github/workflows/validate-skills.yml`:**

```yaml
name: Validate Skills

on:
  pull_request:
    paths:
      - 'skills/**'
  push:
    branches:
      - opencode
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
      - name: Install dependencies
        run: pip install pyyaml
      - name: Validate SKILL.md frontmatter
        run: python .github/scripts/validate_skill.py
      - name: Validate openai.yaml files
        run: python .github/scripts/validate_openai.py
      - name: Validate Python syntax
        run: python .github/scripts/validate_python.py
      - name: Validate markdown links
        run: python .github/scripts/validate_links.py
```

## Evaluation Framework

See [evaluation-framework.md](evaluation-framework.md) for the complete evaluation framework documentation.

### Quick Summary

- **Purpose**: Test skill quality, accuracy, and effectiveness
- **Location**: Each skill's `evaluations/` directory
- **Minimum Required**: 2 evaluation cases per skill
- **Runner**: `scripts/evaluate_skill.py` (planned - see issue #21)

### Adding Evaluations

```bash
mkdir -p skills/my-skill/evaluations
# Add case JSON files...
# Add config.json...
```

### Running Evaluations

> **Note**: The `evaluate_skill.py` script is planned as part of issue #21 and is not yet available. Manual evaluation using case JSON files is currently required.

```bash
# Evaluation runner coming soon (issue #21)
```
