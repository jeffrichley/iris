# 🏛️ Iris Development Constitution

## Purpose

This document establishes the foundational principles and standards for developing Iris — a personal project management assistant. All contributors, AI agents, and automated systems must adhere to these principles to ensure consistency, quality, and maintainability.

---

## 🎯 Core Tenets

### 1. **Local-First Forever**

- User data MUST reside locally first (SQLite)
- Cloud sync is enhancement, not requirement
- Offline functionality is non-negotiable
- No feature should fail without internet connectivity

### 2. **Zero Data Loss**

- All state changes MUST be durable
- Crashes cannot lose unsaved work
- Sync conflicts must be resolved transparently
- User actions must be recoverable

### 3. **Privacy by Design**

- User data stays local by default
- Opt-in for cloud features
- No telemetry without explicit consent
- Sensitive logs excluded from error reporting

### 4. **Performance is Feature**

- Responsiveness equals trust
- Every millisecond counts
- Measure first, optimize second
- Performance regressions block releases

---

## 💎 Code Quality Standards

### Principle 1: Type Safety First

**Rules:**

- ✅ All Python code MUST use type hints (no `Any` allowed)
- ✅ All TypeScript code MUST enable strict mode
- ✅ Enums for static values; no magic strings
- ✅ Pydantic for configuration and data validation
- ❌ No implicit type coercion
- ❌ No `typing.Any` without documented justification

**Example (Python):**

```python
# ❌ BAD
def process_task(data: dict) -> Any:
    status = data["status"]  # magic string
    return do_something(status)

# ✅ GOOD
from enum import Enum
from pydantic import BaseModel

class TaskStatus(str, Enum):
    TODO = "todo"
    DOING = "doing"
    REVIEW = "review"
    DONE = "done"

class Task(BaseModel):
    title: str
    status: TaskStatus

def process_task(task: Task) -> ProcessResult:
    status_handlers: dict[TaskStatus, Callable] = {
        TaskStatus.TODO: handle_todo,
        TaskStatus.DOING: handle_doing,
        # ...
    }
    return status_handlers[task.status](task)
```

### Principle 2: Explicit Over Implicit

**Rules:**

- Function signatures MUST document intent clearly
- Side effects MUST be documented
- Dependencies MUST be injected, not imported globally
- Configuration MUST be centralized in dedicated packages

**Example:**

```python
# ❌ BAD
def save_task():
    db = get_global_db()  # hidden dependency
    db.save()  # implicit side effect

# ✅ GOOD
def save_task(task: Task, db: Database) -> SaveResult:
    """Save task to database.

    Side effects: Writes to database, triggers sync event
    """
    result = db.save(task)
    emit_sync_event(task.id)
    return result
```

### Principle 3: Modular Architecture

**Rules:**

- One responsibility per module
- Clear boundaries between layers (UI / API / Data)
- Dependency inversion for testability
- No circular dependencies

**Layer Structure:**

```
Frontend (React/Tauri) → API Layer (FastAPI) → Business Logic → Data Layer (SQLite/Supabase)
```

### Principle 4: Error Handling

**Rules:**

- MUST use rich library for colored logging
- Errors MUST be specific, never generic
- User-facing errors MUST be actionable
- System errors MUST be logged with context

**Example:**

```python
from rich.console import Console
from rich.panel import Panel

console = Console()

try:
    result = sync_to_cloud(task)
except NetworkError as e:
    console.print(Panel(
        f"[bold red]Sync Failed[/bold red]\n"
        f"Cannot reach cloud server. Your data is safe locally.\n"
        f"Will retry automatically when connection restores.",
        title="❌ Sync Error",
        border_style="red"
    ))
    queue_retry(task)
except ValidationError as e:
    console.print(Panel(
        f"[bold yellow]Invalid Task Data[/bold yellow]\n"
        f"Field '{e.field}': {e.message}\n"
        f"Please correct and try again.",
        title="⚠️ Validation Error",
        border_style="yellow"
    ))
```

### Principle 5: Documentation Standards

**Rules:**

- Public APIs MUST have docstrings
- Complex logic MUST have inline comments
- Architecture decisions MUST be documented
- Breaking changes MUST update CHANGELOG

**Format:**

```python
def sync_differential(
    local: SQLiteDB,
    remote: SupabaseDB,
    strategy: SyncStrategy = SyncStrategy.TIMESTAMP
) -> SyncResult:
    """Perform differential sync between local and remote databases.

    This function implements a timestamp-based differential sync algorithm
    that minimizes data transfer by only syncing changed records.

    Args:
        local: Local SQLite database instance
        remote: Remote Supabase database instance
        strategy: Sync strategy (TIMESTAMP or HASH)

    Returns:
        SyncResult containing counts of pushed, pulled, and conflicted records

    Raises:
        SyncConflictError: When conflicts cannot be auto-resolved
        NetworkError: When remote is unreachable

    Example:
        >>> result = sync_differential(local_db, supabase_db)
        >>> print(f"Synced {result.pushed} local → cloud")
    """
    # Implementation...
```

---

## 🧪 Testing Standards

### Principle 6: Test Pyramid

**Rules:**

- Unit tests: 70% (fast, isolated, no I/O)
- Integration tests: 20% (API + DB)
- E2E tests: 10% (full user workflows)
- All tests MUST use `pytest.mark.unit` / `integration` / `e2e` decorators explicitly

**Coverage Requirements:**

- Core business logic: 90% minimum
- API endpoints: 85% minimum
- Utilities: 80% minimum
- UI components: 70% minimum

### Principle 7: Test Quality

**Rules:**

- ✅ Tests MUST be deterministic (no flaky tests)
- ✅ Tests MUST be isolated (no shared state)
- ✅ Tests MUST be fast (unit tests < 50ms each)
- ✅ Tests MUST use descriptive names
- ❌ Never disable warnings (`--disable-warnings`)
- ❌ No test pollution in source code (use `tests/system/`)

**Example:**

```python
import pytest
from iris.tasks import TaskService, Task, TaskStatus

@pytest.mark.unit
def test_task_service_marks_task_as_complete():
    """TaskService.complete() should update status and set completion time."""
    # Arrange
    service = TaskService(db=MockDatabase())
    task = Task(id="t1", title="Test", status=TaskStatus.DOING)

    # Act
    result = service.complete(task)

    # Assert
    assert result.status == TaskStatus.DONE
    assert result.completed_at is not None
    assert result.completed_at > task.created_at

@pytest.mark.integration
def test_task_service_persists_completion_to_database(real_db):
    """TaskService.complete() should persist changes to database."""
    # Arrange
    service = TaskService(db=real_db)
    task = service.create(Task(title="Test Task"))

    # Act
    service.complete(task)

    # Assert
    persisted = real_db.get_task(task.id)
    assert persisted.status == TaskStatus.DONE
```

### Principle 8: Test Execution

**Command:**

```bash
just test  # Always use this; never invoke pytest directly
```

**CI Requirements:**

- All tests MUST pass before merge
- Coverage reports MUST be generated
- Performance benchmarks MUST be tracked

---

## 🎨 User Experience Consistency

### Principle 9: Design System

**Rules:**

- MUST use shadcn/ui components only
- MUST follow Tailwind conventions
- MUST maintain dark theme first (light optional)
- MUST use Iris brand colors consistently

**Brand Colors:**

```css
--iris-primary: #6c63ff; /* Iris Blue */
--iris-bg-dark: #0f0f1a; /* Background */
--iris-surface: #1a1a2e; /* Cards/Panels */
--iris-success: #00d9a3; /* Success states */
--iris-warning: #ffb547; /* Warning states */
--iris-error: #ff6b6b; /* Error states */
--iris-text: #e4e4e7; /* Primary text */
--iris-text-muted: #a1a1aa; /* Secondary text */
```

**Typography:**

```css
--font-body: "Inter", sans-serif;
--font-display: "DM Sans", sans-serif;
--font-mono: "Fira Code", monospace;
```

### Principle 10: Interaction Patterns

**Rules:**

- Keyboard shortcuts for all primary actions
- Loading states for operations > 100ms
- Optimistic UI updates with rollback
- Animations MUST be smooth (60fps minimum)
- Toast notifications for async confirmations

**Keyboard Shortcuts Standard:**

```typescript
// Primary actions
Ctrl+N / Cmd+N        → New Task
Ctrl+K / Cmd+K        → Quick Command
Ctrl+F / Cmd+F        → Search
Ctrl+, / Cmd+,        → Settings
Esc                   → Close/Cancel

// Navigation
Ctrl+1-9 / Cmd+1-9    → Tab switching
Ctrl+B / Cmd+B        → Toggle Sidebar
```

### Principle 11: Accessibility

**Rules:**

- WCAG 2.1 AA compliance minimum
- Semantic HTML structure
- ARIA labels on interactive elements
- Focus visible on all controls
- Screen reader tested

### Principle 12: Feedback & Status

**Rules:**

- User actions MUST provide immediate feedback
- Loading states MUST be visible
- Error messages MUST be actionable
- Success confirmations MUST be clear
- Progress indicators for long operations

**Feedback Patterns:**

```typescript
// ❌ BAD
async function saveTask(task: Task) {
  await api.save(task);
}

// ✅ GOOD
async function saveTask(task: Task) {
  // Immediate optimistic update
  updateLocalState(task);
  toast.loading("Saving task...");

  try {
    await api.save(task);
    toast.success("Task saved successfully");
  } catch (error) {
    // Rollback optimistic update
    revertLocalState();
    toast.error("Failed to save task", {
      action: { label: "Retry", onClick: () => saveTask(task) },
    });
  }
}
```

---

## ⚡ Performance Requirements

### Principle 13: Response Time Targets

**Hard Limits:**
| Operation | Target | Maximum | Measurement |
|-----------|--------|---------|-------------|
| UI interaction response | < 50ms | 100ms | Time to first paint update |
| Dashboard load | < 100ms | 150ms | Time to interactive |
| CRUD operations | < 100ms | 200ms | API round-trip |
| Search results | < 200ms | 500ms | First result displayed |
| Sync operation | < 500ms | 2s | Background, user-visible completion |
| Voice recognition | < 300ms | 1s | Speech → text latency |
| TTS generation | < 500ms | 1.5s | Text → audio playback |

**Enforcement:**

- Performance budgets tracked in CI
- Regressions > 10% block deployment
- Real-world metrics collected via telemetry (opt-in)

### Principle 14: Resource Management

**Rules:**

- Bundle size: Frontend < 500KB gzipped
- Memory: Peak usage < 200MB for base app
- Database queries: < 10ms for indexed lookups
- Batch operations: Max 50 items per transaction
- WebSocket messages: < 1KB per message

**Monitoring:**

```python
from iris.telemetry import measure_performance

@measure_performance(threshold_ms=150)
async def load_dashboard(user_id: str) -> Dashboard:
    """Load user dashboard with performance monitoring."""
    # Implementation...
```

### Principle 15: Optimization Strategy

**Priority Order:**

1. **Correctness** — Never sacrifice data integrity
2. **Perceived Performance** — Optimistic updates, loading states
3. **Actual Performance** — Caching, indexing, lazy loading
4. **Resource Efficiency** — Memory, CPU, battery optimization

**Caching Strategy:**

```typescript
// API responses cached with TTL
const { data, isLoading } = useQuery({
  queryKey: ["tasks", filters],
  queryFn: fetchTasks,
  staleTime: 30_000, // 30s
  cacheTime: 300_000, // 5m
});
```

### Principle 16: Scalability Boundaries

**System Limits:**

- Projects: 1,000 per user
- Tasks: 10,000 per project
- Ideas: Unlimited (archived after 6 months inactive)
- Notes: 100MB total per user
- Reminders: 1,000 active per user

**Graceful Degradation:**

- Pagination for lists > 50 items
- Virtual scrolling for lists > 100 items
- Lazy loading for embedded content
- Background sync queue with retry logic

---

## 🔧 Development Workflow

### Principle 17: Version Control

**Rules:**

- Conventional commits required
- Feature branches from `main`
- PR required for all changes
- Squash merge to main
- Semantic versioning strictly enforced

**Commit Format:**

```
type(scope): description

[optional body]

[optional footer]
```

**Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`

### Principle 18: Code Review

**Requirements:**

- All PRs require review
- No self-merge allowed
- CI must pass
- Coverage must not decrease
- Changelog updated for user-facing changes

**Review Checklist:**

- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] Performance impact assessed
- [ ] Breaking changes noted
- [ ] Accessibility verified

### Principle 19: Tooling Compliance

**Commands (MUST use these):**

```bash
just test          # Run tests (never pytest directly)
just lint          # Run linting
just format        # Format code
just build         # Build project
uv sync            # Sync dependencies (never pip)
```

**Never:**

- Reference `.venv` directly
- Use `pip` instead of `uv`
- Disable pre-commit hooks
- Skip CI checks

---

## 🚀 Release Standards

### Principle 20: Deployment Safety

**Pre-release Checklist:**

- [ ] All tests passing
- [ ] Performance benchmarks met
- [ ] Security audit passed
- [ ] Breaking changes documented
- [ ] Migration guide provided (if applicable)
- [ ] Rollback plan documented

**Release Process:**

1. Version bump (semantic versioning)
2. Changelog generation
3. Tag creation
4. CI build & test
5. GitHub Release
6. Auto-update deployment

---

## 🎓 Learning & Evolution

### Principle 21: Continuous Improvement

**Rules:**

- Retrospectives after each milestone
- Performance metrics reviewed monthly
- User feedback triaged weekly
- Technical debt addressed quarterly

### Principle 22: Constitutional Amendments

**Process:**

- Proposals require documented rationale
- Team discussion required
- Approval by project owner
- Update date and version tracked

---

## 📝 Governance

### Authority

- **Project Owner:** Jeff Richley (final decision authority)
- **AI Secretary:** Iris (proposes improvements, enforces standards)
- **Contributors:** Must follow all principles

### Enforcement

- Pre-commit hooks enforce formatting
- CI enforces tests and coverage
- Code review enforces architecture
- Performance budgets enforced automatically

### Exceptions

- Must be documented with rationale
- Require explicit approval
- Tracked in `EXCEPTIONS.md`
- Time-boxed with removal plan

---

## 📊 Metrics & Success

### Quality Metrics

- Test coverage: ≥ 85%
- Type coverage: 100%
- Performance budget compliance: 100%
- Zero critical security vulnerabilities

### User Experience Metrics

- Dashboard load time: < 150ms (p95)
- Crash rate: < 0.1%
- Data loss incidents: 0
- User satisfaction: "I trust Iris" (qualitative)

---

## 🌟 Philosophy

> "Iris is built on trust. Users trust us with their most important tasks and ideas. We honor that trust through:
>
> - Uncompromising quality
> - Radical transparency
> - Privacy by default
> - Performance as feature
> - Empathy in design"

---

**Version:** 1.0.0
**Last Updated:** October 20, 2025
**Next Review:** January 2026

---

_This constitution is a living document. All suggestions for improvement are welcome through the standard PR process._
