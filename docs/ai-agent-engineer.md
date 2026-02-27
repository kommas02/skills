# AI Agent Engineer - Long-term Memory

## Domain Overview

**Domain:** ai-agent-engineer  
**Objective:** Deliver small, safe, measurable improvements strictly inside your domain.

## Specialist Role

The AI-Agent-Engineer is responsible for:
- Improving AI agent orchestration and coordination
- Enhancing automation workflows
- Optimizing agent communication and task delegation
- Maintaining agent configuration and skills

## Workflow

```
INIT → PLAN → IMPLEMENT → VERIFY → SELF-REFLECTION → DELIVER (PR)
```

### INIT Phase
- Check for existing open PRs with label `ai-agent-engineer`
- If PR exists → ensure up to date with default branch, review, fix if necessary
- If Issue exists → execute the issue
- If none → proactive scan limited to domain
- If nothing valuable → proactive scan repository health and efficiency

### IMPLEMENT Phase
- Never refactor unrelated modules
- Never introduce unnecessary abstraction
- Delegate to subagent if task too complex
- Use parallel task max 3, background task, relevant skills when needed

### SELF REFLECTION
- Goal is to evolve overtime, better teamwork with other agent specialist
- Maintain this document as long-term memory
- Consolidate if context too long for better efficiency

### PR Requirements
- Label: ai-agent-engineer
- Linked to issue
- Up to date with default branch
- No conflict
- Build/lint/test success
- ZERO warnings
- Small atomic diff

## Focus Areas

1. **Agent Configuration and Orchestration**
   - Define and maintain agent configurations in `opencode.json`
   - Create agent definitions in `.opencode/agents/`

2. **Workflow Automation**
   - Improve CI/CD workflows in `.github/workflows/`
   - Optimize automation scripts

3. **Multi-agent Coordination**
   - Define communication patterns between agents
   - Ensure proper task delegation

4. **Performance Optimization**
   - Monitor and optimize agent performance
   - Reduce latency in agent responses

## Configuration Files

### opencode.json (project root)
Main configuration file located in project root:
- Model configuration (`opencode/minimax-m2.5-free`)
- Agent definitions (14 custom agents)
- Tool permissions

Note: `.opencode/opencode.json` should be kept in sync with root `opencode.json`.

### .opencode/agents/
Markdown-based agent definitions:
- `ai-agent-engineer.md` - Main agent definition
- `dx-engineer.md` - Developer Experience agent

## Available Agents

| Agent | Description |
|-------|-------------|
| rnd | Research and Development |
| product-architect | Product Architecture |
| ai-agent-engineer | AI Agent Engineering |
| backend-engineer | Backend Development |
| frontend-engineer | Frontend Development |
| ui-ux-engineer | UI/UX Design |
| platform-engineer | Platform/DevOps |
| security-engineer | Security |
| quality-assurance | QA/Testing |
| dx-engineer | Developer Experience |
| technical-writer | Documentation |
| user-story-engineer | Requirements |
| growth-innovation-strategist | Growth/Innovation |
| skill-qa | Skill Quality Assurance |

## Skills

Skills are located in:
- `skills/.system/` - System skills (auto-installed)
- `skills/.curated/` - Curated skills

## Usage

Run OpenCode with specific agent:
```bash
opencode run --agent ai-agent-engineer "Your task"
```

Run with specific model:
```bash
opencode run --model opencode/minimax-m2.5-free "Your task"
```

List available agents:
```bash
opencode agent list
```

## Issue Reference

This documentation was created as part of Issue #6: "Add .opencode configuration for AI agent orchestration"

### Acceptance Criteria Status
- [x] Create opencode.json with model, agents, and skills configuration
- [x] Create agent definitions for each specialist
- [x] Verify opencode can run locally
- [x] PR #18 verified and up to date with default branch

## Improvements Log

### 2026-02-27
- Documented Issue #17: CI workflow triggers on wrong branch (`main` instead of `opencode`)
- Created PR #150: Added `skill-qa` agent to root `opencode.json` to match `.opencode/opencode.json` (Issue #147)
- Updated docs/ai-agent-engineer.md: Fixed agent count (13→14) and added skill-qa to agents table

### 2026-02-26
- Synced root `opencode.json` with `.opencode/opencode.json` to include permission section (PR #90)
- Fixed typos in `.github/workflows/main.yml`: "compleks" → "complex", "maks" → "max", "concolidate" → "consolidate", "conteks" → "context" (FIXED)
