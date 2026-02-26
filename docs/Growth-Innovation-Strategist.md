# Growth-Innovation-Strategist

## Domain Overview
Focus: Small, safe, measurable improvements for repository growth, innovation, and strategy.

## Completed Work
- Created growth-innovation-strategist skill in skills/.curated/growth-innovation-strategist/
- Skill provides framework for analyzing repositories for growth/innovation opportunities
- Focus on measurable outcomes, automation, and strategic leverage points
- Created skill-model-compatibility.json - maps all skills to optimal AI model capabilities
- Updated skill-creator template with model requirements guidance

## Implementation Details
### Skill Versioning System (Issue #7)
- Added version field to SKILL.md frontmatter template in skill-creator
- Updated quick_validate.py to allow 'version' as valid frontmatter property
- Created scripts/generate_skill_index.py to generate skills/index.json
- Created .github/workflows/update-skill-index.yml for auto-updates
- Documented versioning guidelines in .opencode/README.md

#### Version Format
- MAJOR (1.0.0 → 2.0.0): Breaking changes
- MINOR (1.0.0 → 1.1.0): New features, backward compatible
- PATCH (1.0.0 → 1.0.1): Bug fixes

#### Auto-Generated Index
- skills/index.json contains all 33 skills with metadata
- Auto-updated via GitHub Actions on SKILL.md or LICENSE.txt changes
- Includes: name, description, version, category, path, metadata, license

### skill-model-compatibility.json
- Maps all 33 skills to required model capabilities (vision, function_calling, reasoning, large_context)
- Documents recommended/fallback models for each skill
- Includes use case recommendations (general_coding, complex_reasoning, vision_tasks, etc.)
- Machine-readable format for tool integration

### Skill Template Updates
- Added "Model Requirements" section to skill-creator SKILL.md
- Documents common capability requirements with examples
- References compatibility matrix for full details

## Insights & Patterns
- Repository benefits from dedicated growth/innovation skill
- Skills repository can serve as foundation for agent-specialist workflows
- Small, atomic additions provide more value than large rewrites
- PR-based workflow enables incremental improvements with review
- Clear domain boundaries help specialist agents collaborate effectively

## Collaboration Notes
- When PR exists, review for issues (duplicate content, style consistency) before merge
- Fix minor issues directly and push to keep PRs atomic and ready

## Future Opportunities
- Expand skill with repository-specific metrics
- Add integration with existing CI/CD tooling
- Develop scoring system for opportunity prioritization
