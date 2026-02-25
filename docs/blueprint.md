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

### Current Inconsistencies
The following skills use singular `reference/` (should be `references/`):
- notion-knowledge-capture
- notion-meeting-intelligence
- notion-research-documentation
- notion-spec-to-implementation

### License Files
- Use `LICENSE.txt` consistently
- Do NOT use `NOTICE.txt` (currently used by playwright skill - needs standardization)

### Skill Names
- Use lowercase
- Use hyphens for multi-word names: `skill-name`
- Avoid underscores: use `skill-name` not `skill_name`

## Quality Standards

### SKILL.md Requirements
1. Frontmatter must include `name` and `description`
2. Include "When to use" section
3. Include workflow/procedures
4. Document dependencies
 variables if needed
6.5. Document environment Include quality expectations

### Code Quality
- Clean, readable code
- Proper error handling
- No hardcoded secrets
- Follow language conventions

### Documentation
- Clear, concise instructions
- Working examples where applicable
- Update documentation with code changes

## Contribution Guidelines

See [contributing.md](../contributing.md) for general guidelines.

### Adding a New Skill

1. Create directory under appropriate category:
   - `.system/` - For foundational skills
   - `.curated/` - For community skills
   - `.experimental/` - For experimental features

2. Add required files:
   - `SKILL.md` with frontmatter
   - `LICENSE.txt`
   - `agents/openai.yaml`

3. Add optional directories as needed:
   - `references/`
   - `scripts/`
   - `assets/`

4. Test skill integration with Codex

### Updating Existing Skills

1. Update relevant files
2. Ensure backward compatibility
3. Update SKILL.md version if needed
4. Test changes

## Architecture Decisions

### Skill Discovery
Skills are discovered by Codex through the `.system/`, `.curated/`, and `.experimental/` directories. Each skill must have a valid `SKILL.md` file.

### Skill Installation
- System skills are auto-installed
- Curated skills installable via `$skill-installer <skill-name>`
- Experimental skills require full GitHub path

### Agent Integration
Each skill can define agent behavior through `agents/openai.yaml` for Codex integration.

## References

- [Using skills in Codex](https://developers.openai.com/codex/skills)
- [Create custom skills in Codex](https://developers.openai.com/codex/skills/create-skill)
- [Agent Skills open standard](https://agentskills.io)

## Version

Last updated: 2026-02-25
