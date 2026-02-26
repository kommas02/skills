# Backend Engineer Documentation

## Overview

This document outlines the backend engineering work for the skills repository.

## Focus Areas

- Python scripts in `scripts/` and `skills/*/scripts/`
- Backend logic improvements
- Script optimization and bug fixes
- API-related code

## Completed Work

### Bug Fix: evaluate_skill.py

**Issue**: Line 95 used `case['id']` which would fail because:
1. Evaluation case JSON files use `name` field, not `id`
2. The `evaluate_case()` function returns `case_id` in the result dict

**Fix**: Changed `case['id']` to `result['case_id']`

**File**: `scripts/evaluate_skill.py:95`

## Scripts Analysis

### Key Scripts Reviewed

1. **scripts/evaluate_skill.py** - Skill evaluation runner
   - Loads evaluation cases from JSON files
   - Validates minimum case count
   - Outputs results in text or JSON format

2. **skills/.system/skill-installer/scripts/** - Skill installation
   - `github_utils.py` - GitHub API helpers
   - `install-skill-from-github.py` - Install skills from GitHub
   - `list-skills.py` - List available skills

3. **skills/.curated/security-ownership-map/scripts/** - Security analysis
   - `build_ownership_map.py` - Build ownership graphs from git history

## Best Practices

- Use `sys.exit()` instead of `exit()` for proper exit codes
- Use `raise SystemExit(main())` pattern for main functions
- Validate JSON input with `.get()` to provide defaults
- Use proper error handling with custom exceptions

## Related Issues

- #5: Add test coverage for skill validation
- #21: Add skill evaluation framework for quality assurance

## Future Improvements

- Add type hints to more scripts
- Add unit tests for evaluation framework
- Improve error messages in scripts
