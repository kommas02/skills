# Epic Breaking Guide

Epics are large features that span multiple sprints. Break them into manageable user stories.

## Identifying Epics

An epic typically:
- Takes more than 1-2 sprints to complete
- Has many acceptance criteria
- Affects multiple parts of the system
- Can be delivered in independent increments

## Breaking Strategies

### 1. By User Journey

Break by the steps a user takes:

**Epic:** "User Checkout"
- Story 1: Guest checkout - enter shipping address
- Story 2: Enter payment information
- Story 3: Review order summary
- Story 4: Order confirmation page

### 2. By Data Layer

Break by backend/frontend/database:

**Epic:** "Product Search"
- Story 1: Create search database schema
- Story 2: Build search API endpoints
- Story 3: Search UI component
- Story 4: Search results display

### 3. By CRUD Operations

Break by create/read/update/delete:

**Epic:** "User Profile Management"
- Story 1: View profile
- Story 2: Edit profile
- Story 3: Upload profile photo
- Story 4: Delete account

### 4. By Happy Path vs Extras

**Epic:** "Advanced Reporting"
- Story 1: Basic report generation (happy path)
- Story 2: Date range filtering
- Story 3: Export to PDF
- Story 4: Scheduled reports
- Story 5: Custom report builder

## Epic Structure in Linear

Create parent issue with:
- Title: Feature name (Epic)
- Label: `epic`
- Description: High-level overview, links to specs
- No estimate (or sum of children)

Create child issues:
- Title: Specific story
- Label: `user-story`
- Parent: Epic issue
- Estimate: Story points

## Validation

After breaking:
- [ ] Each story delivers value independently
- [ ] Stories can be completed in 1 sprint
- [ ] No hard dependencies between stories
- [ ] Each story has clear acceptance criteria
- [ ] Total points fit within sprint capacity

## Anti-Patterns

❌ Breaking by developer (not user value)
✅ Breaking by user outcome

❌ Creating 20+ stories for one feature
✅ Grouping into logical increments

❌ Stories depend on each other strictly
✅ Stories can be done in any order
