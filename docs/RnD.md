# RnD Documentation

## Active Improvements

### 2026-02-25
- **Skill structure validation in CI**: Added validation job to `.github/workflows/main.yml` that checks:
  - Each skill has a `SKILL.md` file
  - Each skill has a `LICENSE.txt` file
  - `SKILL.md` has required frontmatter (`name` and `description`)
  - All 30 existing skills pass validation

- **Standardize directory naming**: Renamed `reference/` to `references/` in 4 skills (notion-spec-to-implementation, notion-meeting-intelligence, notion-research-documentation, notion-knowledge-capture) to match the majority convention.

## Notes
- Default branch: `opencode`
- Skills are stored in `.system/` and `.curated/` directories
