# Technical Writer Domain Knowledge

## Overview
Domain focused on documentation standardization, skill template creation, and documentation quality for the skills repository.

## Key Learnings

### Skill Structure Patterns
- **SKILL.md**: Primary documentation file with frontmatter (name, description)
- **references/**: Subdirectory for detailed reference docs
- **scripts/**: Automation scripts
- **assets/**: Static assets
- **agents/**: Agent-specific instructions
- **LICENSE.txt**: Required license file

### Template Standards (from docs/skill-template.md)
- **REQUIRED**: Frontmatter (name, description), Title, Description, When to Use
- **RECOMMENDED**: Prerequisites, Quick Start, Usage, Examples, References, Scripts, Assets
- **OPTIONAL**: Configuration, Troubleshooting, Evaluations, Benchmarks

### Documentation Patterns
- Use frontmatter with `name` (kebab-case) and `description` (one-liner)
- Clear "When to use" / "When NOT to use" guidance
- Include prerequisites and setup requirements
- Provide concrete examples with code blocks
- Troubleshooting section for common issues

## Active Issues
- Issue #37: Create skill template with required sections standardization

## Notes
- Repository has nested skills/skills/ structure (related to issue #34)
- Skills are in .curated and .system subdirectories
