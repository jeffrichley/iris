## Description

<!-- Provide a brief description of the changes in this PR -->

## Type of Change

<!-- Mark the relevant option with an 'x' -->

- [ ] `feat`: New feature
- [ ] `fix`: Bug fix
- [ ] `docs`: Documentation update
- [ ] `style`: Code style change (formatting, no logic change)
- [ ] `refactor`: Code refactoring
- [ ] `perf`: Performance improvement
- [ ] `test`: Adding or updating tests
- [ ] `chore`: Build process, tooling, dependencies
- [ ] `ci`: CI configuration changes

## Related Issues

<!-- Link related issues: Fixes #123, Closes #456 -->

## Changes Made

<!-- List the specific changes made in this PR -->

- 
- 
- 

## Testing

<!-- Describe how you tested these changes -->

- [ ] Tested locally with `just ci`
- [ ] Pre-commit hooks passing
- [ ] Added/updated tests
- [ ] All tests passing
- [ ] Coverage maintained/improved (>= 80%)

## Screenshots (if applicable)

<!-- Add screenshots for UI changes -->

## Checklist

### Code Quality

- [ ] Code follows project style guide (enforced by ruff/prettier)
- [ ] Type hints added for new Python code (mypy strict)
- [ ] TypeScript strict mode compliance
- [ ] No linting errors (`just lint`)
- [ ] No type checking errors (`just type-check`)
- [ ] All tests pass (`just test`)
- [ ] Coverage is >= 80%

### Documentation

- [ ] Updated README.md (if user-facing changes)
- [ ] Updated relevant documentation in docs/
- [ ] Added inline code comments for complex logic
- [ ] Updated CHANGELOG.md (if applicable)

### Security

- [ ] No hardcoded secrets or credentials
- [ ] No new HIGH/CRITICAL security vulnerabilities
- [ ] Sensitive data properly handled
- [ ] Input validation added where needed

### Performance

- [ ] No performance regressions
- [ ] Optimized for efficiency where possible
- [ ] Resource usage considered (memory, CPU)

### Breaking Changes

- [ ] No breaking changes
- [ ] OR: Breaking changes documented and justified
- [ ] OR: Migration guide provided

## CI Status

<!-- Wait for CI to complete before requesting review -->

All CI checks must pass before merge:

**Matrix Tests**: 
- [ ] All 12 matrix jobs passing (6 OS × 2 Python)

**Security**:
- [ ] Security scan passing
- [ ] CodeQL analysis passing
- [ ] No HIGH/CRITICAL vulnerabilities

**Coverage**:
- [ ] Code coverage >= 80%
- [ ] Coverage report uploaded to Codecov

## Reviewer Notes

<!-- Any specific areas you want reviewers to focus on? -->

## Post-Merge

<!-- Will this trigger a version bump? -->

- [ ] This is a `feat` commit (MINOR version bump)
- [ ] This is a `fix`/`perf` commit (PATCH version bump)
- [ ] This is `docs`/`chore` (no version bump)

---

**PR Author Checklist**: 
- Read the checklist above
- Mark applicable items
- Wait for CI to pass
- Request review when ready

**Reviewer Checklist**:
- Verify all checklist items marked
- Check CI passing
- Review code quality
- Approve or request changes

