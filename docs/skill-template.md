# Skill Template

This document defines the standard structure for skills in the repository. It serves as the "Definition of Done" for creating new skills.

## Section Types

### REQUIRED Sections

These sections MUST be present in every skill:

#### 1. SKILL.md (Required)

The main entry point for every skill. Must include YAML frontmatter with required fields:

```yaml
---
name: skill-name
description: Clear, concise description of when to use this skill and what it does
metadata:
  short-description: A brief one-line description for UI display
---
```

**Frontmatter Fields:**
- `name` (required): Lowercase, hyphen-separated identifier (e.g., `gh-address-comments`)
- `description` (required): 1-2 sentence description explaining when to use this skill
- `metadata.short-description` (recommended): Brief description for skill store UI

**Content Structure:**
1. Title/Overview: What the skill does
2. Prerequisites: What users need before starting (tools, auth, etc.)
3. Usage/Workflow: Step-by-step instructions
4. Examples (optional but recommended)

**Example:**
```markdown
---
name: my-skill
description: Do something useful when the user needs help with X
metadata:
  short-description: Brief description for UI
---

# My Skill

A longer description of what this skill accomplishes.

## Prerequisites

- Tool X installed
- Authentication configured

## Usage

1. First step
2. Second step

## Examples

### Example 1
Description of example...
```

### 2. agents/openai.yaml (Required for UI Display)

UI metadata for skill stores:

```yaml
version: "openai/v1"
name: skill-name
description: Description shown in UI
metadata:
  color: #HEXCODE
  category: category-name
```

---

### RECOMMENDED Sections

These sections should be included for comprehensive skills:

#### 3. references/

Supporting documentation for context loading. Files here are loaded when the skill is used.

**Common files:**
- `references/overview.md` - Skill overview and concepts
- `references/configuration.md` - Configuration options
- `references/troubleshooting.md` - Common issues and solutions

**Naming Convention:** Use kebab-case (e.g., `spec-parsing.md`, `quick-start.md`)

#### 4. examples/

End-to-end walkthroughs showing the skill in action.

**Common files:**
- `examples/example-name.md` - Detailed walkthrough
- Include: scenario, steps, expected outcome

#### 5. scripts/

Executable code (Python, Bash, etc.)

**Requirements:**
- Must have proper shebang
- Should be executable (`chmod +x`)
- Include help/usage documentation

---

### OPTIONAL Sections

These sections are optional but add value:

#### 6. evaluations/

Test cases for skill quality assurance.

**Structure:**
```
evaluations/
├── config.json      # Evaluation configuration
└── cases/          # Test case files
    └── case-1.json
```

See [docs/evaluation-framework.md](evaluation-framework.md) for details.

#### 7. assets/

Static files used by the skill (images, templates, etc.)

#### 8. LICENSE.txt

License for the skill (recommended for curated skills)

---

## Quick Reference

| Section | Type | Required |
|---------|------|----------|
| SKILL.md | File | ✅ Yes |
| agents/openai.yaml | File | For UI |
| references/ | Directory | Recommended |
| examples/ | Directory | Recommended |
| scripts/ | Directory | If applicable |
| evaluations/ | Directory | Optional |
| assets/ | Directory | Optional |
| LICENSE.txt | File | Optional |

---

## Creating a New Skill

1. Create directory: `skills/.curated/my-new-skill/`
2. Add `SKILL.md` with frontmatter
3. Add `agents/openai.yaml` for UI (optional but recommended)
4. Add supporting directories as needed:
   - `references/` for documentation
   - `examples/` for walkthroughs
   - `scripts/` for code
5. Run validation: `python scripts/evaluate_skill.py skills/my-new-skill`

---

## Validation

Skills are validated by the `validate-skills.yml` workflow:

- YAML syntax checks
- Python syntax checks  
- SKILL.md frontmatter validation
- Markdown link validation

Run locally:
```bash
gh workflow run validate-skills.yml
```
