# RnD Documentation

## Active Improvements

### 2026-02-25
- **Skill structure validation in CI**: Added validation workflow `.github/workflows/skill-validation.yml` that checks:
  - Each skill has a `SKILL.md` file
  - Each skill has a `LICENSE.txt` file
  - `SKILL.md` has required frontmatter (`name` and `description`)
  - All 30 existing skills pass validation

## Notes
- Default branch: `opencode`
- Skills are stored in `.curated/` directory
