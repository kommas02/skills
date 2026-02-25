# Product-Arquitect Domain

## Mission
Deliver small, safe, measurable improvements strictly inside the Product-Arquitect domain.

## Responsibilities
- Architecture integrity
- Repository structure and organization
- Documentation standards (blueprint, conventions)
- Quality standards for skills

## Completed Work

### PR #42: Create architectural blueprint
- Created `docs/blueprint.md` as the architectural constitution
- Documented skill directory structure (.curated, .system, .experimental)
- Documented required files per skill (SKILL.md, LICENSE.txt, agents/openai.yaml)
- Documented naming conventions (kebab-case)
- Documented quality standards (minimum viable skill)
- Added blueprint link to README.md

## Key Findings

### Repository Structure
- Root level: `skills/.curated/` (30 skills), `skills/.system/` (2 skills)
- Nested (to be addressed): `skills/skills/.curated/` (issue #34)
- No `.experimental/` directory yet

### Skill Requirements
- Required: SKILL.md, LICENSE.txt, agents/openai.yaml
- Recommended: references/, scripts/
- Optional: examples/, assets/

## Related Issues
- #2: Create docs/blueprint.md (RESOLVED via PR #42)
- #34: Remove nested skills/skills/ directory (Architecture, Platform-Engineer)
- #35: Add centralized skill registry (Innovation)
- #7: Add skill versioning (Innovation)

## Collaboration Notes
- Coordinate with Technical-Writer for documentation improvements
- Coordinate with Platform-Engineer for structural changes (#34)
- Coordinate with Quality-Assurance for evaluation framework (#21)
