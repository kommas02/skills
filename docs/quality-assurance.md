# Quality Assurance Documentation

## Overview

This document outlines the quality assurance practices for the skills repository.

## Validation Pipeline

### GitHub Actions Workflow: validate-skills.yml

The repository includes an automated validation workflow that runs on:
- Every pull request modifying files in the `skills/` directory
- Every push to main branch that modifies files in the `skills/` directory

#### Validation Steps

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

### Yamllint Configuration

The repository uses `.yamllint` configuration with the following rules:
- Maximum line length: 120 characters (warning level)
- Indentation: 2 spaces
- Document start marker: not required
- Colons: max 0 spaces before, max 1 space after

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

```bash
# Trigger the workflow manually
gh workflow run validate-skills.yml
```

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
