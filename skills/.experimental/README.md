# Experimental Skills

This directory contains experimental skills that are in development or testing phase.

## About Experimental Skills

Experimental skills may:
- Be incomplete or subject to breaking changes
- Have limited testing
- Change without notice
- Eventually be promoted to `.curated/` or removed

## Installing Experimental Skills

Use the skill-installer with the experimental path:

```bash
$skill-installer --path skills/.experimental/<skill-name>
```

Or via direct installation:
```bash
scripts/install-skill-from-github.py --repo openai/skills --path skills/.experimental/<skill-name>
```

## Contributing

To add an experimental skill:
1. Create a new folder in `skills/.experimental/<skill-name>/`
2. Add required files: SKILL.md, LICENSE.txt
3. Optionally add agents/openai.yaml for Codex integration
