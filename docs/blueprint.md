# Architectural Constitution

This document serves as the architectural constitution for the Agent Skills repository. It defines the repository structure, skill categories, contribution guidelines, and quality standards.

## Repository Overview

Agent Skills are folders of instructions, scripts, and resources that AI agents can discover and use to perform specific tasks. The repository follows a structured organization with three skill categories.

## Directory Structure

```
skills/
├── .system/          # Auto-installed with Codex
├── .curated/        # Community-curated skills (installable via $skill-installer)
└── .experimental/   # Experimental skills (optional installation)
```

### Skill Categories

#### .system/
Skills automatically installed with Codex. These are foundational skills for skill creation and management.

| Skill | Description |
|-------|-------------|
| skill-creator | Create custom skills in Codex |
| skill-installer | Install and manage skills |

#### .curated/
Community-curated skills available for installation via `$skill-installer`.

| Skill | Description |
|-------|-------------|
| cloudflare-deploy | Deploy applications to Cloudflare |
| develop-web-game | Build web-based games |
| doc | Work with .docx documents |
| figma | Figma design integration |
| figma-implement-design | Implement Figma designs |
| gh-address-comments | Address GitHub comments |
| gh-fix-ci | Fix CI/CD issues |
| imagegen | Image generation |
| jupyter-notebook | Jupyter notebook tasks |
| linear | Linear project management |
| netlify-deploy | Deploy to Netlify |
| notion-knowledge-capture | Capture knowledge in Notion |
| notion-meeting-intelligence | Meeting intelligence in Notion |
| notion-research-documentation | Research documentation in Notion |
| notion-spec-to-implementation | Spec to implementation workflow |
| openai-docs | OpenAI documentation |
| pdf | PDF processing |
| playwright | Playwright testing |
| render-deploy | Deploy to Render |
| screenshot | Screenshot capture |
| security-best-practices | Security best practices |
| security-ownership-map | Security ownership mapping |
| security-threat-model | Threat modeling |
| sentry | Sentry integration |
| sora | Sora video generation |
| speech | Speech/text-to-speech |
| spreadsheet | Spreadsheet operations |
| transcribe | Audio transcription |
| vercel-deploy | Deploy to Vercel |
| yeet | Quick deployment tool |

## Required Files

Every skill must include:

### SKILL.md (Required)
The main skill definition file with frontmatter and instructions.

```yaml
---
name: "skill-name"
description: "Brief description of what this skill does"
---
```

### skill.json (Required)
Metadata file for skill discovery, versioning, and dependency management. See [docs/skill-schema.md](skill-schema.md) for schema definition.

```json
{
  "name": "skill-name",
  "version": "1.0.0",
  "description": "Brief description for skill discovery",
  "category": ".curated",
  "author": { "name": "Author Name" },
  "capabilities": [],
  "dependencies": [],
  "tags": [],
  "license": "MIT"
}
```

### LICENSE.txt (Required)
License file for the skill. Use LICENSE.txt (not NOTICE.txt) for consistency.

### agents/openai.yaml (Required)
Agent configuration for Codex integration.

### Optional Directories
- `references/` - Documentation references (use plural form)
- `scripts/` - Helper scripts
- `assets/` - Static assets
- `examples/` - Example usage
- `evaluations/` - Evaluation criteria

## Naming Conventions

### Directory Names
- Use **plural** form for directories: `references/`, `examples/`, `evaluations/`
- Do NOT use singular form: `reference/`, `example/`, `evaluation/`

## Quality Standards

### skill.json Validation
All skills must have a valid `skill.json` file that passes schema validation:
- `name`: kebab-case identifier
- `version`: semver format (e.g., "1.0.0")
- `description`: 10-200 characters
- `category`: `.system`, `.curated`, or `.experimental`

Run validation with:
```bash
node scripts/validate-skill-json.js
```

## Telemetry (Optional)

Skills may include optional anonymous usage telemetry for quality improvement. This is disabled by default and requires explicit opt-in.

### Schema

The telemetry schema is defined in [docs/skill-telemetry-schema.json](skill-telemetry-schema.json) and supports the following event types:

- `invoked` - Skill was invoked
- `success` - Skill completed successfully
- `failure` - Skill failed
- `feedback_positive` - User gave positive feedback
- `feedback_negative` - User gave negative feedback

### Privacy Principles

- All user IDs must be hashed (SHA-256)
- No PII collected
- Opt-in via `SKILL_TELEMETRY_ENABLED=1` environment variable
- 90-day data retention
- No cross-site tracking

### Providing Feedback

Users can provide feedback via GitHub issues using the [Skill Feedback template](../.github/ISSUE_TEMPLATE/skill-feedback.md).
