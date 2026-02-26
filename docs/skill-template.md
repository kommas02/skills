---
title: Skill Template
description: Standardized template for creating skills with required, recommended, and optional sections.
---

# Skill Template

This template defines the **Definition of Done** for creating new skills. Use this template to ensure consistent documentation across all skills.

---

## REQUIRED Sections

These sections **must** be present in every skill.

### 1. Frontmatter

```yaml
---
name: "<skill-name>"
description: "<1-2 sentence description of when to use this skill>"
---
```

**Requirements:**
- `name`: Lowercase, hyphenated, matches directory name
- `description`: Complete sentence explaining use case; includes key tools/frameworks if applicable

---

### 2. When to Use

```markdown
## When to use

- Use this skill when [specific task description]
- Use this skill when [another specific task]
- Prefer this skill over [other skill] when [condition]
```

**Requirements:**
- At least 2 bullet points
- Clearly differentiates from similar skills
- Includes decision criteria

---

### 3. Workflow

```markdown
## Workflow

1. [First step]
2. [Second step]
3. [Third step]
```

**Requirements:**
- Numbered steps
- Action-oriented verbs
- Covers happy path

---

## RECOMMENDED Sections

These sections should be included unless not applicable to the skill.

### 4. Prerequisites

```markdown
## Prerequisites

- [Requirement 1]
- [Requirement 2]
```

**Include when:**
- Authentication is required
- Specific tools must be installed
- Environment setup needed before first use

---

### 5. Dependencies

```markdown
## Dependencies

### Python packages
```
pip install <package>
```

### System tools
```
# macOS
brew install <tool>

# Ubuntu/Debian
sudo apt-get install <tool>
```
```

**Include when:**
- The skill requires specific dependencies
- Installation instructions help users

---

### 6. Environment Variables

```markdown
## Environment

| Variable | Required | Description |
|----------|----------|-------------|
| `VAR_NAME` | Yes | Description of variable |
```

**Include when:**
- The skill requires environment configuration

---

### 7. Temp and Output Conventions

```markdown
## Temp and output conventions

- Use `tmp/<skill>/` for intermediate files
- Write final artifacts under `output/<skill>/`
- Keep filenames stable and descriptive
```

**Include when:**
- The skill produces intermediate or final output files

---

## OPTIONAL Sections

These sections are optional but should be considered for comprehensive skills.

### 8. Examples

```markdown
## Examples

### Example 1: [Title]
[Description of what this example demonstrates]

[Code block or command]

### Example 2: [Title]
[Description]
```

**Include when:**
- Complex workflows benefit from demonstrations
- Common use cases can be illustrated

---

### 9. Quality Expectations

```markdown
## Quality expectations

- [Expectation 1]
- [Expectation 2]
```

**Include when:**
- The skill has specific quality standards
- Delivery criteria exist

---

### 10. Troubleshooting

```markdown
## Troubleshooting

### [Problem 1]
[Solution]

### [Problem 2]
[Solution]
```

**Include when:**
- Common issues are known
- Error messages can be ambiguous

---

### 11. References

```markdown
## References

- [Reference 1](link)
- [Reference 2](link)
```

**Include when:**
- Detailed documentation exists in `references/` subdirectory
- External documentation is available

---

## Directory Structure

A complete skill should follow this structure:

```
<skill-name>/
├── SKILL.md           # REQUIRED: Main documentation
├── LICENSE.txt        # REQUIRED: License file
├── references/        # RECOMMENDED: Detailed reference docs
│   └── ...
├── scripts/           # RECOMMENDED: Helper scripts
│   └── ...
├── agents/            # OPTIONAL: Agent configurations
│   └── ...
├── assets/            # OPTIONAL: Static assets
│   └── ...
└── evaluations/      # OPTIONAL: Evaluation criteria
    └── ...
```

---

## Section Checklist

Use this checklist when creating a new skill:

- [ ] Frontmatter (name, description)
- [ ] When to use
- [ ] Workflow
- [ ] Prerequisites (if applicable)
- [ ] Dependencies (if applicable)
- [ ] Environment variables (if applicable)
- [ ] Temp/output conventions (if applicable)
- [ ] Examples (recommended)
- [ ] Quality expectations (recommended)
- [ ] Troubleshooting (optional)
- [ ] References (if references/ exists)
