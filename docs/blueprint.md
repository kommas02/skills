# Architectural Blueprint

This document serves as the architectural constitution for the Agent Skills repository.

## Repository Structure

```
skills/
├── .curated/          # Community-vetted skills, ready for production use
├── .system/          # Built-in skills (skill-creator, skill-installer)
├── .experimental/    # Experimental skills (optional, not yet implemented)
└── skills/           # DEPRECATED: Nested directory - to be removed (see Issue #34)
    └── .curated/     # Legacy location - migrate to root skills/.curated/
```

### Directory Categories

| Category | Purpose | Installation |
|----------|---------|--------------|
| `.system/` | Core skills bundled with Codex | Auto-installed |
| `.curated/` | Community-vetted, production-ready | Via `$skill-installer` |
| `.experimental/` | In testing/feedback phase | Manual install only |

## Skill Structure

Each skill must follow this structure:

```
skill-name/
├── SKILL.md          # REQUIRED: Primary skill definition
├── LICENSE.txt      # REQUIRED: License for the skill
├── agents/          # REQUIRED: Agent configurations
│   └── openai.yaml  # REQUIRED: OpenAI agent config
├── references/      # RECOMMENDED: Documentation links
├── scripts/         # OPTIONAL: Helper scripts
├── examples/        # OPTIONAL: Usage examples
└── assets/          # OPTIONAL: Static assets
```

### Required Files

| File | Purpose | Schema |
|------|---------|--------|
| `SKILL.md` | Skill definition with frontmatter | See [SKILL.md Schema](#skillmd-schema) |
| `LICENSE.txt` | License text | Plain text |
| `agents/openai.yaml` | Agent configuration | OpenAI Skills spec |

## SKILL.md Schema

```yaml
---
name: <skill-name>
description: <1-2 sentence description>
metadata:
  short-description: <short description for UI>
---
```

## Naming Conventions

- **Skill names**: kebab-case (e.g., `gh-address-comments`, not `ghAddressComments`)
- **Directories**: Lowercase with hyphens
- **Files**: Follow language conventions (e.g., `SKILL.md`, `LICENSE.txt`)

## Quality Standards

### Minimum Viable Skill

- [ ] `SKILL.md` with name, description in frontmatter
- [ ] Clear usage instructions in body
- [ ] `LICENSE.txt` present
- [ ] `agents/openai.yaml` present

### Recommended Additions

- [ ] `references/` with relevant docs
- [ ] `scripts/` with helper utilities
- [ ] Version field in frontmatter (semver)

## Contribution Guidelines

1. Create skill in appropriate directory (`.curated/` for production)
2. Follow skill structure above
3. Ensure all required files present
4. Submit PR for review

## Known Issues

- **Nested directory**: `skills/skills/` exists and should be migrated to root (Issue #34)
- **No .experimental/**: Experimental category not yet created

## Future Considerations

- Skill versioning system (Issue #7)
- Centralized skill registry/index (Issue #35)
- Skill evaluation framework (Issue #21)
- Quality telemetry (Issue #30)
