# UI-UX Engineer Domain Memory

## Repository Context

**Repository:** openai/skills
**Purpose:** Agent Skills repository - folders of instructions, scripts, and resources AI agents can discover and use
**Structure:**
- `skills/.curated/` - Production-ready skills
- `skills/.system/` - System-installed skills
- `skills/.experimental/` - Experimental skills

## Domain Focus

UI/UX engineering in this repository focuses on:
1. Skill documentation quality and clarity
2. User experience of AI agents using skills
3. Consistency in skill structure and metadata
4. Repository documentation and DX

## Prior Work

- 2026-02-25: Established initial domain documentation
- 2026-02-25: Added short-description metadata to all 30 curated skills (previously only 6 had it)
- Previous PRs: Fixed references directory naming (plural)

## Scan Findings

### Opportunities Identified

1. **Documentation Structure**
   - No centralized docs directory exists (FIXED: created docs/ui-ux-engineer.md)
   - No ui-ux-engineer.md memory file (FIXED)
   - contributing.md is minimal - could benefit from more detailed contribution guidelines

2. **Skill Metadata Consistency** (FIXED)
   - Only 6 of 30 curated skills had `metadata.short-description` field
   - Added short-description to all 24 remaining curated skills
   - This improves skill discovery and UX for agents consuming skills

3. **Skill Documentation**
   - Skills follow consistent SKILL.md format with sections: Overview, Prerequisites, Required Workflow, Examples, Best Practices, Common Issues
   - Some skills could benefit from more visual aids (diagrams, screenshots)

4. **Repository Health**
   - Clean structure with well-organized skills
   - Clear README with installation instructions

## Action Items

- [x] Create docs/ui-ux-engineer.md memory file
- [x] Add short-description metadata to all curated skills
- [ ] Create contributing.md enhancements for UI/UX guidelines
- [ ] Consider adding visual documentation templates for skills

## Collaboration Notes

- Coordinate with DX-engineer on documentation improvements
- Coordinate with technical-writer on documentation clarity
