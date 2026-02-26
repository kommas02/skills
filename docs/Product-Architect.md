# Product Architect Documentation

## Overview

This document outlines the product architecture domain for the skills repository.

## Domain Responsibilities

The Product-Architect domain focuses on:
- Product structure and organization
- Documentation consistency
- Architecture coherence across skills
- Repository health within product scope

## Current Architecture

### Skill Categories

The repository uses three skill categories:

| Category | Location | Description |
|----------|----------|-------------|
| System | `skills/.system/` | Automatically installed in Codex |
| Curated | `skills/.curated/` | Reviewed and maintained skills |
| Experimental | `skills/.experimental/` | In-development skills for testing |

### Recent Changes

- **2026-02-26**: Created `skills/.experimental/` folder to fix documentation inconsistency (Issue #52)

## Issue Tracking

Product architecture issues are tracked with:
- Label: Product-Architect
- Layer: Architecture
- Owner Agent: Product-Architect

## Related Issues

- #52: Inconsistent documentation - .experimental folder referenced but doesn't exist

## Quality Standards

All product architecture changes must:
- Maintain documentation consistency
- Follow existing folder structure conventions
- Be atomic and reversible
- Include clear documentation

## Validation

Before submitting changes:
1. Verify all documentation references are consistent
2. Ensure folder structure follows conventions
3. Check that referenced paths exist
