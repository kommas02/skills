# Example: Simple Feature Story

## Scenario

User says: "I want users to be able to reset their password"

## Step 1: Identify the user role

The user role is: **Platform user** (someone with an account who forgot their password)

## Step 2: Define the goal

Instead of "reset password" (too vague), make it specific:
"I want to request a password reset via email"

## Step 3: Define the benefit

Why does the user need this?
"So that I can regain access to my account if I forget my password"

## Step 4: Complete user story

```
As a registered platform user,
I want to request a password reset via email,
so that I can regain access to my account if I forget my password.
```

## Step 5: Write acceptance criteria

- [ ] "Forgot password" link appears on login page
- [ ] Clicking link shows email input form
- [ ] Valid email submits successfully
- [ ] Invalid email shows error message
- [ ] Success message confirms email sent
- [ ] Reset email arrives within 2 minutes
- [ ] Reset link expires after 24 hours
- [ ] Link directs to new password entry page
- [ ] New password must meet complexity requirements
- [ ] Confirmation password must match
- [ ] Successful reset shows login redirect

## Step 6: Estimate story points

This involves:
- Email delivery integration
- Token generation/storage
- Frontend form
- Backend API endpoints
- Token validation

**Estimate: 5 points** (complex, some unknowns)

## Step 7: Create in Linear

```python
# Using Linear MCP
linear:create_issue(
  title="Password reset feature",
  description="""## User Story
As a registered platform user,
I want to request a password reset via email,
so that I can regain access to my account if I forget my password.

## Acceptance Criteria
- [ ] "Forgot password" link appears on login page
- [ ] Clicking link shows email input form
- [ ] Valid email submits successfully
- [ ] Invalid email shows error message
- [ ] Success message confirms email sent
- [ ] Reset email arrives within 2 minutes
- [ ] Reset link expires after 24 hours
- [ ] Link directs to new password entry page
- [ ] New password must meet complexity requirements
- [ ] Confirmation password must match
- [ ] Successful reset shows login redirect""",
  labels=["user-story", "security"],
  estimate=5,
  priority=2
)
```
