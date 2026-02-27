## Contributing

### Community values

- **Be kind and inclusive.** Treat others with respect; we follow the [Contributor Covenant](https://www.contributor-covenant.org/).
- **Assume good intent.** Written communication is hard - err on the side of generosity.
- **Teach & learn.** If you spot something confusing, open an issue or PR with improvements.

### Security & responsible AI

Have you discovered a vulnerability or have concerns about model output? Please e-mail **security@openai.com** and we will respond promptly.

---

## Creating Skills

This section guides you through creating a new skill for the OpenAI Skills repository.

### Quick Start

1. **Use the skill-creator skill** - Run `/skill-creator` in Codex for step-by-step guidance
2. **Follow the template** - See [docs/skill-template.md](./docs/skill-template.md) for required sections
3. **Create your skill directory** - Place it in `skills/.curated/` or `skills/.system/`

### Required Files

Every skill must include:

```
skill-name/
├── SKILL.md           # REQUIRED - Main skill definition
├── skill.json         # REQUIRED - Metadata for discovery and versioning
├── LICENSE.txt        # REQUIRED - License file
├── agents/            # RECOMMENDED - Agent-specific instructions
├── assets/            # OPTIONAL - Static assets
└── scripts/           # OPTIONAL - Helper scripts
```

### SKILL.md Requirements

Your `SKILL.md` must include:

- **Frontmatter** with `name` and `description`
- **Core Workflow** - Step-by-step instructions

Example frontmatter:

```yaml
---
name: my-skill
description: A brief description of what this skill does.
---
```

### Resources

- [Skill Template Guide](./docs/skill-template.md) - Detailed template with required, recommended, and optional sections
- [skill-creator skill](./skills/.system/skill-creator/) - Interactive guide for creating skills
- [skill-installer skill](./skills/.system/skill-installer/) - Learn how skills are installed

### Testing Your Skill

Before submitting a PR:

1. Verify `SKILL.md` has proper frontmatter (name, description)
2. Ensure `LICENSE.txt` exists
3. Check that core workflow has clear steps
4. Review against [skill-template.md](./docs/skill-template.md) auditing checklist
