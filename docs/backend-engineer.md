# Backend Engineer Documentation

## Domain Focus
Backend improvements for the skills repository, focusing on Python scripts and utilities.

## Past Improvements

### 2026-02-25: HTTP Request Timeout
- **File**: `skills/.system/skill-installer/scripts/github_utils.py`
- **Change**: Added configurable timeout (default 30s) to HTTP requests
- **Reason**: Prevent indefinite hanging on network issues
- **Env Variable**: `GITHUB_REQUEST_TIMEOUT` (optional, defaults to 30)
- **Impact**: Used by `install-skill-from-github.py` and `list-skills.py`

## Code Standards
- Use type hints where possible
- Handle exceptions with custom exception classes
- Use argparse for CLI tools
- Add retry logic for transient failures
- Always set timeouts on network requests
