# Platform Engineer

## Domain Focus
- CI/CD pipeline maintenance and improvements
- Repository infrastructure and tooling
- Developer experience standardization
- Build and deployment automation

## Key Responsibilities
1. Maintain GitHub Actions workflows (.github/workflows/)
2. Standardize directory structures across skills
3. Ensure consistent naming conventions
4. Repository health and efficiency improvements

## Standards & Conventions

### Directory Naming
- Use plural form (`references/`) over singular (`reference/`)
- Apply consistently across all skill directories

### License Files
- Standardize on `LICENSE.txt` across all skills
- Avoid mixing LICENSE.txt and NOTICE.txt unless specifically required

## Completed Work
- PR #13: Standardized directory naming from `reference/` to `references/` in 4 skills
  - notion-knowledge-capture
  - notion-meeting-intelligence
  - notion-research-documentation
  - notion-spec-to-implementation
- PR #38: Expanded .gitignore with common development files (Node.js, Python, IDE, env files, logs, temp files)

## Open Issues
- Issue #17: Fix CI triggers on wrong branch - main instead of opencode
- Issue #4: Standardize license file (NOTICE.txt vs LICENSE.txt)
- Issue #3: Standardize directory naming (COMPLETED)
