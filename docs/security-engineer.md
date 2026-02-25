# Security Engineer - Repository Memory

## Current Security Posture

### ✅ Strengths
- **No hardcoded secrets**: All API keys/tokens loaded from environment variables only
- **Proper secret handling**: GitHub Actions workflow uses `secrets.GITHUB_TOKEN`, `secrets.GEMINI_API_KEY`, etc.
- **No command injection**: Subprocess calls use controlled arguments, not user input
- **YAML files clean**: No credentials in `.yaml`/`.yml` configuration files

### Security Skills Available
- `security-ownership-map`: Maps code ownership for security accountability
- `security-threat-model`: Threat modeling documentation
- `security-best-practices`: Web framework security references (Django, Flask, FastAPI, Express, Next.js, Vue, React)

### Areas to Monitor
1. **Third-party scripts**: Review any new Python scripts for subprocess usage
2. **Environment variables**: Ensure no secrets are accidentally committed
3. **GitHub workflow permissions**: Review periodically - current broad permissions (contents, issues, pull-requests, actions, id-token) needed for AI agent automation

### Past Security Scans
| Date | Status | Notes |
|------|--------|-------|
| 2026-02-25 | ✅ Pass | Initial scan - No vulnerabilities found |
| 2026-02-25 | ✅ Pass | Rebase scan - No vulnerabilities found |

## Workflow Integration
- Label all PRs with `security-engineer`
- Link PRs to issues
- Ensure build/lint/test success before merge
