# Skill Template

This template defines the required, recommended, and optional sections for OpenAI Skills. Use this as the "Definition of Done" when creating or auditing skills.

## Directory Structure

```
skill-name/
├── SKILL.md           # REQUIRED - Main skill definition
├── skill.json         # REQUIRED - Metadata for discovery and versioning
├── LICENSE.txt        # REQUIRED - License file
├── agents/            # RECOMMENDED - Agent-specific instructions
├── assets/            # OPTIONAL - Static assets
├── references/        # RECOMMENDED - Detailed references
├── scripts/           # OPTIONAL - Helper scripts
├── examples/          # OPTIONAL - Usage examples
└── evaluations/       # OPTIONAL - Evaluation criteria
```

---

## SKILL.md Structure

### Frontmatter (REQUIRED)

Every SKILL.md must start with YAML frontmatter:

```yaml
---
name: <skill-name>
description: <one-sentence description of what this skill does>
---
```

**Fields:**
- `name`: Lowercase alphanumeric with hyphens (e.g., `cloudflare-deploy`)
- `description**: One-sentence description for skill discovery

---

### Sections

#### REQUIRED Sections

These sections MUST be present in every skill:

| Section | Purpose | Template |
|---------|---------|----------|
| **Name/Title** | Human-readable skill name | `# Skill Name` |
| **Description** | What the skill does and when to use it | `Use when...` |
| **Core Workflow** | Step-by-step instructions | Numbered list or decision tree |

**Example:**

```markdown
# Figma MCP

Use the Figma MCP server for Figma-driven implementation.

## Workflow
1. Run get_design_context first to fetch the structured representation.
2. Download any assets needed and start implementation.
3. Validate against Figma for 1:1 look and behavior.
```

---

#### RECOMMENDED Sections

These sections are highly encouraged for quality skills:

| Section | Purpose |
|---------|---------|
| **Prerequisites** | Requirements before using the skill (tools, env vars, permissions) |
| **References** | Links to detailed reference docs |
| **Troubleshooting** | Common issues and solutions |
| **Environment** | Required environment variables |
| **Dependencies** | Tools or packages needed |

**Example - Prerequisites:**

```markdown
## Prerequisites

- When sandboxing blocks the deployment network calls, rerun with `sandbox_permissions=require_escalated`.
- The deployment might take a few minutes. Use appropriate timeout values.
```

**Example - Dependencies:**

```markdown
## Dependencies

Install required packages:

```bash
uv pip install python-docx pdf2image
```
```

---

#### OPTIONAL Sections

These sections add depth but are not required:

| Section | Purpose |
|---------|---------|
| **Examples** | Concrete usage examples |
| **Quality Expectations** | Standards for deliverable quality |
| **Decision Trees** | Flowcharts for choosing options |
| **Benchmarks** | Performance or quality benchmarks |
| **Temp/Output Conventions** | File naming and location conventions |

---

## Section Templates

### Quick Decision Tree Template

```
## Decision Tree

### " need to [goal]"

```
Need [goal]?
├─ OptionI A → use case A
├─ Option B → use case B
└─ Option C → use case C
```
```

### Product Index Template

```markdown
## Product Index

| Product | Reference |
|---------|-----------|
| Product A | `references/product-a/` |
| Product B | `references/product-b/` |
```

### Reference Link Template

```markdown
## References

- `references/<topic>.md` — Description of what this covers.
- `scripts/<script-name>.py` — Helper script for X task.
```

### Troubleshooting Template

```markdown
## Troubleshooting

### Issue: [Common Problem]

**Symptoms:** [What the user sees]

**Solution:** [How to fix it]
```

---

## Frontmatter Requirements

### Minimum Viable Skill

```yaml
---
name: my-skill
description: A brief description of what this skill does.
---
```

### Complete Frontmatter (for advanced skills)

```yaml
---
name: my-skill
description: A brief description of what this skill does.
---
```

---

## Auditing Checklist

Use this checklist to verify a skill meets minimum requirements:

- [ ] `name` in frontmatter matches directory name
- [ ] `description` is one sentence, starts with action verb
- [ ] SKILL.md exists at root
- [ ] LICENSE.txt exists at root
- [ ] Core workflow has numbered steps
- [ ] Prerequisites section (if skill requires setup)
- [ ] References section (if references/ directory exists)
- [ ] Troubleshooting section (if applicable)

---

## Common Patterns

### Pattern: Prerequisites + Auth

```markdown
## Prerequisites

- Verify authentication before proceeding:
  ```bash
  npx wrangler whoami
  ```

## Authentication

Not authenticated? → See `references/auth.md`
```

### Pattern: Decision Tree

```markdown
## Quick Decision Tree

### "I need to [action]"

```
Need [action]?
├─ [Option A] → [path/to/ref/]
├─ [Option B] → [path/to/ref/]
└─ [Option C] → [path/to/ref/]
```
```

### Pattern: Multi-step Workflow

```markdown
## Workflow

1. **Step One** - Description of what to do
2. **Step Two** - Description of what to do
3. **Step Three** - Validate results

> **Tip:** Add tips or warnings here
```
