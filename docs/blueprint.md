# Architectural Blueprint

This document serves as the architectural constitution for the Agent Skills repository. All contributors must adhere to the conventions defined here.

## Repository Structure

```
skills/
├── .system/       # Automatically installed with Codex
├── .curated/      # Community-verified skills
└── .experimental/ # Early-stage, community-contributed skills
```

## Skill Categories

| Category | Description | Installation |
|----------|-------------|--------------|
| `.system` | Core skills bundled with Codex | Automatic |
| `.curated` | Community-verified, stable skills | `$skill-installer <name>` |
| `.experimental` | Early-stage, may change | Full path required |

## Required Files Per Skill

Every skill must include:

| File | Description |
|------|-------------|
| `SKILL.md` | Skill documentation and usage |
| `LICENSE.txt` | License (NOTICE.txt not supported) |
| `agents/openai.yaml` | Agent configuration |

### Directory Naming Convention

- Use `references/` (plural) for documentation directories
- Do NOT use `reference/` (singular)
- This ensures consistency across all skills

**Correct:** `skills/.curated/my-skill/references/`
**Incorrect:** `skills/.curated/my-skill/reference/`

## Contribution Guidelines

### Adding a New Skill

1. Create skill directory under appropriate category (`.system`, `.curated`, or `.experimental`)
2. Add required files: `SKILL.md`, `LICENSE.txt`, `agents/openai.yaml`
3. Use `references/` (not `reference/`) for any documentation subdirectories
4. Update skill manifest in this document (if applicable)
5. Submit PR with `skill` label

### Skill Structure Example

```
skills/.experimental/my-new-skill/
├── SKILL.md
├── LICENSE.txt
├── agents/
│   └── openai.yaml
└── references/
    └── docs/
```

## Quality Standards

- All skills must have valid `SKILL.md` with clear usage instructions
- License must be present and valid
- Agent configuration must be valid YAML
- No broken internal links
- Consistent naming conventions (always `references/`)

## Maintenance

- Review skills annually for freshness
- Remove deprecated skills after 6 months of inactivity
- Update this blueprint when structural changes occur

## Skill Manifest

*To be populated as skills are added to the repository.*
