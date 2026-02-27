# Growth-Innovation-Strategist

## Domain Overview
Focus: Small, safe, measurable improvements for repository growth, innovation, and strategy.

## Completed Work
- Created growth-innovation-strategist skill in skills/.curated/growth-innovation-strategist/
- Skill provides framework for analyzing repositories for growth/innovation opportunities
- Focus on measurable outcomes, automation, and strategic leverage points
- Created skill-model-compatibility.json - maps all skills to optimal AI model capabilities
- Updated skill-creator template with model requirements guidance
- Added model requirements to top skills: figma, pdf, gh-fix-ci, screenshot, figma-implement-design

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

### Skill Model Requirements Updates (2026-02-26)
- Added Model Requirements section to 5 key skills:
  - figma (requires vision)
  - pdf (may require vision)
  - screenshot (requires vision)
  - figma-implement-design (requires vision)
  - gh-fix-ci (benefits from reasoning)
- Each skill now includes recommended models and references the compatibility matrix
- All modified skills pass quick_validate.py

### Additional Skill Model Requirements Updates
- Extended Model Requirements section to 8 more frequently-used skills:
  - playwright (function calling)
  - cloudflare-deploy (function calling)
  - netlify-deploy (function calling)
  - vercel-deploy (function calling)
  - linear (function calling)
  - notion-knowledge-capture (function calling)
  - imagegen (function calling)
  - jupyter-notebook (function calling)
- Total: 13 skills now document model requirements

### Skill Short-Description Expansion
- Added short-description metadata to 5 more high-value skills:
  - cloudflare-deploy: "Deploy serverless apps to Cloudflare Workers and Pages"
  - netlify-deploy: "Deploy web projects to Netlify with preview URLs"
  - gh-fix-ci: "Debug and fix failing GitHub Actions PR checks"
  - imagegen: "Generate and edit images using OpenAI Image API"
  - jupyter-notebook: "Create and edit Jupyter notebooks for analysis and tutorials"
- Total skills with short-description: 16 (up from 11)

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

## Skill Quality Telemetry System (Issue #30)
- Created docs/skill-telemetry-schema.json with privacy-preserving telemetry schema
- Supports event types: invoked, success, failure, feedback_positive, feedback_negative
- Privacy principles: hashed user IDs, opt-in only, 90-day retention, no PII
- Created .github/ISSUE_TEMPLATE/skill-feedback.md for structured feedback collection
- Updated docs/blueprint.md with telemetry documentation

### Skill Metadata Short-Description Standardization
- Added short-description metadata to 5 high-value curated skills:
  - vercel-deploy: "Deploy web apps to Vercel with preview URLs"
  - playwright: "Automate real browsers for testing and scraping"
  - pdf: "Read, create, and review PDF files with visual checks"
  - figma: "Fetch design context and assets from Figma via MCP"
  - screenshot: "Capture desktop screenshots (full screen, window, or region)"
- Total skills with short-description: 12 (up from 6)
- Improves skill discoverability in AI agent tooling
