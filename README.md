# Agent Skills

Agent Skills are folders of instructions, scripts, and resources that AI agents can discover and use to perform at specific tasks. Write once, use everywhere.

Codex uses skills to help package capabilities that teams and individuals can use to complete specific tasks in a repeatable way. This repository catalogs skills for use and distribution with Codex.

Learn more:
- [Using skills in Codex](https://developers.openai.com/codex/skills)
- [Create custom skills in Codex](https://developers.openai.com/codex/skills/create-skill)
- [Agent Skills open standard](https://agentskills.io)

## Directory Structure

```
skills/
├── .system/        # System skills (auto-installed in Codex)
├── .curated/       # Production-ready skills (installable via $skill-installer)
└── .experimental/  # Skills in development or testing
```

## Skill Categories

### System Skills (`.system/`)
Automatically available in the latest version of Codex. Includes:
- `skill-creator` - Interactive guide for creating new skills
- `skill-installer` - Handles skill installation and discovery

### Curated Skills (`.curated/`)
Production-ready skills that can be installed on-demand:
- Deployment skills (cloudflare-deploy, netlify-deploy, render-deploy, vercel-deploy)
- Development skills (develop-web-game, figma, figma-implement-design, playwright)
- Productivity skills (linear, notion-*, gh-address-comments, gh-fix-ci)
- And more...

### Experimental Skills (`.experimental/`)
Skills in development or testing. May have breaking changes.

## Installing a skill

### System Skills
Already installed in Codex. Run `/skill-creator` or `/skill-installer` to use.

### Curated Skills
Use `$skill-installer` inside Codex:

[Curated](skills/.curated/) skills are tested and stable.

[Experimental](skills/.experimental/) skills are in development and may have breaking changes.

To install [curated](skills/.curated/) skills, you can use the `$skill-installer` inside Codex.

Curated skills can be installed by name:

```
$skill-installer gh-address-comments
```

After installing a skill, restart Codex to pick up new skills.

### Experimental Skills
Use the skill-installer with the path flag:

```
$skill-installer --path skills/.experimental/<skill-name>
```

## License

The license of an individual skill can be found directly inside the skill's directory inside the `LICENSE.txt` file.
