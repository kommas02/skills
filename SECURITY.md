# Security Policy

## Supported Versions

We actively support and provide security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.x     | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly:

1. **Do NOT** create a public GitHub issue for security vulnerabilities
2. Email security concerns to the maintainers privately
3. Include as much detail as possible:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Any suggested fixes (optional)

## Security Best Practices in This Repository

- No hardcoded secrets - all API keys loaded from environment variables
- GitHub Actions use ephemeral tokens with minimal permissions
- No credentials in YAML configuration files
- Subprocess calls use controlled arguments, not user input

## Third-Party Dependencies

We regularly update dependencies to address known vulnerabilities. If you find a vulnerability in a dependency, please report it following the process above.
