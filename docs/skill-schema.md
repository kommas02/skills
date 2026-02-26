# Skill Metadata Schema

This document defines the `skill.json` schema for Agent Skills. The metadata file provides standardized information for skill discovery, dependency management, versioning, and quality assurance.

## Schema Definition

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["name", "version", "description", "category"],
  "properties": {
    "name": {
      "type": "string",
      "pattern": "^[a-z0-9-]+$",
      "description": "Unique skill identifier (kebab-case)"
    },
    "version": {
      "type": "string",
      "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+$",
      "description": "Semantic version (semver)"
    },
    "description": {
      "type": "string",
      "minLength": 10,
      "maxLength": 200,
      "description": "Brief description for skill discovery"
    },
    "category": {
      "type": "string",
      "enum": [".system", ".curated", ".experimental"],
      "description": "Skill category determining installation method"
    },
    "author": {
      "type": "object",
      "properties": {
        "name": { "type": "string" },
        "email": { "type": "string", "format": "email" },
        "url": { "type": "string", "format": "uri" }
      }
    },
    "capabilities": {
      "type": "array",
      "items": { "type": "string" },
      "description": "List of specific capabilities this skill provides"
    },
    "dependencies": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Other skills this skill depends on. Use skill names (e.g., ['skill-installer', 'doc']). The skill-installer will automatically install missing dependencies in correct order.",
      "example": ["skill-installer", "doc"]
    },
    "tags": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Keywords for discovery"
    },
    "license": {
      "type": "string",
      "description": "License identifier (reference to LICENSE.txt)"
    },
    "homepage": {
      "type": "string",
      "format": "uri",
      "description": "Documentation URL"
    },
    "repository": {
      "type": "string",
      "format": "uri",
      "description": "Source repository URL"
    },
    "keywords": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Search keywords (alias for tags)"
    }
  }
}
```

## Example

```json
{
  "name": "vercel-deploy",
  "version": "1.0.0",
  "description": "Deploy applications and websites to Vercel with zero configuration",
  "category": ".curated",
  "author": {
    "name": "Codex Team",
    "url": "https://github.com/kommas02/skills"
  },
  "capabilities": [
    "preview-deployment",
    "production-deployment",
    "framework-detection"
  ],
  "dependencies": [],
  "tags": ["deployment", "vercel", "hosting"],
  "license": "MIT",
  "homepage": "https://github.com/kommas02/skills/tree/main/skills/.curated/vercel-deploy",
  "repository": "https://github.com/kommas02/skills"
}
```

## Migration

A migration script (`scripts/migrate-skill-json.js`) generates `skill.json` files for existing skills by extracting metadata from `SKILL.md` frontmatter and `agents/openai.yaml`.

## CI Validation

The skill schema is validated in CI via:
1. `skill-json-validate` - Checks all skills have valid `skill.json`
2. Uses `ajv` for JSON Schema validation
