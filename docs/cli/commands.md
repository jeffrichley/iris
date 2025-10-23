# Iris CLI Commands Documentation

## Overview

The Iris CLI provides a comprehensive set of commands for managing your project management system. All commands are built with Rich formatting for beautiful output and comprehensive error handling.

## Installation and Setup

### Prerequisites

- Python 3.12+
- Iris package installed (`pip install -e .`)

### Environment Setup

```bash
# Set environment (optional, defaults to development)
export IRIS_ENV=development

# Create .env file (optional)
cp .env.example .env
```

## Command Structure

All CLI commands follow the pattern:
```bash
iris <command> [options] [arguments]
```

## Database Commands

### `iris db migrate`

Run database migrations to update the schema.

```bash
# Run all pending migrations
iris db migrate

# Run migrations with verbose output
iris db migrate --verbose

# Force migration without confirmation
iris db migrate --force

# Show what would be migrated (dry run)
iris db migrate --dry-run
```

**Options:**
- `--verbose, -v`: Enable verbose output
- `--force, -f`: Force migration without confirmation
- `--dry-run`: Show what would be migrated without applying

**Examples:**
```bash
# Standard migration
iris db migrate

# Verbose migration with confirmation
iris db migrate --verbose

# Force migration for automated scripts
iris db migrate --force

# Preview changes before applying
iris db migrate --dry-run
```

### `iris db test-connection`

Test database connection and verify connectivity.

```bash
# Test connection with default timeout
iris db test-connection

# Test connection with custom timeout
iris db test-connection --timeout 10

# Test connection with verbose output
iris db test-connection --verbose
```

**Options:**
- `--timeout, -t`: Connection timeout in seconds (default: 5)
- `--verbose, -v`: Enable verbose output

**Examples:**
```bash
# Quick connection test
iris db test-connection

# Extended timeout for slow connections
iris db test-connection --timeout 30

# Verbose connection test
iris db test-connection --verbose
```

### `iris db health-check`

Check database health and performance metrics.

```bash
# Basic health check
iris db health-check

# Detailed health information
iris db health-check --detailed

# Health check with verbose output
iris db health-check --verbose
```

**Options:**
- `--detailed, -d`: Show detailed health information
- `--verbose, -v`: Enable verbose output

**Examples:**
```bash
# Basic health check
iris db health-check

# Detailed health metrics
iris db health-check --detailed

# Verbose health check
iris db health-check --verbose
```

### `iris db status`

Show database status and configuration information.

```bash
# Show database status
iris db status
```

**Output includes:**
- Database connection information
- Configuration settings
- Migration status
- Performance metrics

### `iris db reset`

Reset database (WARNING: This will delete all data).

```bash
# Reset database with confirmation
iris db reset

# Reset database without confirmation
iris db reset --confirm

# Force reset without confirmation
iris db reset --force
```

**Options:**
- `--confirm, -y`: Skip confirmation prompt
- `--force, -f`: Force reset without confirmation

**Examples:**
```bash
# Reset with confirmation prompt
iris db reset

# Reset without confirmation (for scripts)
iris db reset --confirm

# Force reset (for automated scripts)
iris db reset --force
```

### `iris db backup`

Create database backup.

```bash
# Create backup with auto-generated filename
iris db backup

# Create backup to specific file
iris db backup --output backup.db

# Create compressed backup
iris db backup --compress

# Create compressed backup to specific file
iris db backup --output backup.db --compress
```

**Options:**
- `--output, -o`: Output file path
- `--compress, -c`: Compress backup file

**Examples:**
```bash
# Auto-generated backup
iris db backup

# Custom backup file
iris db backup --output my_backup.db

# Compressed backup
iris db backup --compress

# Compressed backup to specific file
iris db backup --output backup.db.gz --compress
```

### `iris db restore`

Restore database from backup.

```bash
# Restore from backup with confirmation
iris db restore backup.db

# Restore without confirmation
iris db restore backup.db --force
```

**Arguments:**
- `input_file`: Input backup file path

**Options:**
- `--force, -f`: Force restore without confirmation

**Examples:**
```bash
# Restore with confirmation
iris db restore backup.db

# Restore without confirmation
iris db restore backup.db --force
```

## Project Commands

### `iris project create`

Create a new project.

```bash
# Create project with required name
iris project create "My Project"

# Create project with description
iris project create "My Project" --description "Project description"

# Create project with specific status
iris project create "My Project" --status active
```

**Arguments:**
- `name`: Project name

**Options:**
- `--description`: Project description
- `--status`: Project status (active, completed, paused)

**Examples:**
```bash
# Basic project creation
iris project create "Website Redesign"

# Project with description
iris project create "Mobile App" --description "iOS and Android app development"

# Project with specific status
iris project create "Legacy Project" --status paused
```

### `iris project list`

List all projects.

```bash
# List all projects
iris project list

# List projects with specific status
iris project list --status active

# List projects with detailed information
iris project list --detailed
```

**Options:**
- `--status`: Filter by project status
- `--detailed`: Show detailed information

**Examples:**
```bash
# List all projects
iris project list

# List only active projects
iris project list --status active

# List with detailed information
iris project list --detailed
```

### `iris project show`

Show project details.

```bash
# Show project by ID
iris project show 1

# Show project by name
iris project show "My Project"
```

**Arguments:**
- `project`: Project ID or name

**Examples:**
```bash
# Show project by ID
iris project show 1

# Show project by name
iris project show "Website Redesign"
```

### `iris project update`

Update project information.

```bash
# Update project name
iris project update 1 --name "Updated Project Name"

# Update project status
iris project update 1 --status completed

# Update project description
iris project update 1 --description "Updated description"
```

**Arguments:**
- `project`: Project ID or name

**Options:**
- `--name`: New project name
- `--description`: New project description
- `--status`: New project status

**Examples:**
```bash
# Update project name
iris project update 1 --name "New Project Name"

# Update project status
iris project update "Old Project" --status completed

# Update multiple fields
iris project update 1 --name "New Name" --status active --description "New description"
```

### `iris project delete`

Delete a project.

```bash
# Delete project with confirmation
iris project delete 1

# Delete project without confirmation
iris project delete 1 --force
```

**Arguments:**
- `project`: Project ID or name

**Options:**
- `--force, -f`: Force deletion without confirmation

**Examples:**
```bash
# Delete with confirmation
iris project delete 1

# Delete without confirmation
iris project delete "Old Project" --force
```

## Task Commands

### `iris task create`

Create a new task.

```bash
# Create task with required fields
iris task create --project 1 --title "Complete feature"

# Create task with all options
iris task create --project 1 --title "Complete feature" --priority high --due-date 2024-12-31 --notes "Important task"
```

**Options:**
- `--project`: Project ID or name
- `--title`: Task title
- `--priority`: Task priority (low, medium, high, urgent)
- `--due-date`: Task due date (YYYY-MM-DD)
- `--notes`: Task notes

**Examples:**
```bash
# Basic task creation
iris task create --project 1 --title "Fix bug"

# Task with all options
iris task create --project "Website Redesign" --title "Update CSS" --priority high --due-date 2024-12-31 --notes "Update responsive design"
```

### `iris task list`

List tasks.

```bash
# List all tasks
iris task list

# List tasks for specific project
iris task list --project 1

# List tasks by status
iris task list --completed false

# List tasks by priority
iris task list --priority high
```

**Options:**
- `--project`: Filter by project ID or name
- `--completed`: Filter by completion status
- `--priority`: Filter by priority
- `--due-date`: Filter by due date

**Examples:**
```bash
# List all tasks
iris task list

# List tasks for specific project
iris task list --project "Website Redesign"

# List incomplete tasks
iris task list --completed false

# List high priority tasks
iris task list --priority high
```

### `iris task show`

Show task details.

```bash
# Show task by ID
iris task show 1
```

**Arguments:**
- `task`: Task ID

**Examples:**
```bash
# Show task details
iris task show 1
```

### `iris task update`

Update task information.

```bash
# Mark task as completed
iris task update 1 --completed

# Update task title
iris task update 1 --title "Updated task title"

# Update task priority
iris task update 1 --priority urgent
```

**Arguments:**
- `task`: Task ID

**Options:**
- `--title`: New task title
- `--priority`: New task priority
- `--due-date`: New task due date
- `--notes`: New task notes
- `--completed`: Mark task as completed
- `--incomplete`: Mark task as incomplete

**Examples:**
```bash
# Mark task as completed
iris task update 1 --completed

# Update task title
iris task update 1 --title "New task title"

# Update multiple fields
iris task update 1 --title "Updated title" --priority high --completed
```

### `iris task delete`

Delete a task.

```bash
# Delete task with confirmation
iris task delete 1

# Delete task without confirmation
iris task delete 1 --force
```

**Arguments:**
- `task`: Task ID

**Options:**
- `--force, -f`: Force deletion without confirmation

**Examples:**
```bash
# Delete with confirmation
iris task delete 1

# Delete without confirmation
iris task delete 1 --force
```

## Idea Commands

### `iris idea create`

Create a new idea.

```bash
# Create idea with title
iris idea create --title "Great idea"

# Create idea with description
iris idea create --title "Great idea" --description "Detailed description"

# Create idea associated with project
iris idea create --title "Great idea" --project 1
```

**Options:**
- `--title`: Idea title
- `--description`: Idea description
- `--project`: Associated project ID or name

**Examples:**
```bash
# Basic idea creation
iris idea create --title "Mobile app idea"

# Idea with description
iris idea create --title "Feature idea" --description "Add dark mode support"

# Idea associated with project
iris idea create --title "Enhancement idea" --project "Website Redesign"
```

### `iris idea list`

List ideas.

```bash
# List all ideas
iris idea list

# List ideas for specific project
iris idea list --project 1

# List promoted ideas
iris idea list --promoted
```

**Options:**
- `--project`: Filter by project ID or name
- `--promoted`: Filter by promotion status

**Examples:**
```bash
# List all ideas
iris idea list

# List ideas for specific project
iris idea list --project "Website Redesign"

# List promoted ideas
iris idea list --promoted
```

### `iris idea promote`

Promote an idea to a project.

```bash
# Promote idea to project
iris idea promote 1
```

**Arguments:**
- `idea`: Idea ID

**Examples:**
```bash
# Promote idea to project
iris idea promote 1
```

## Reminder Commands

### `iris reminder create`

Create a new reminder.

```bash
# Create reminder for project
iris reminder create --project 1 --message "Don't forget!" --due-time "2024-12-25 10:00"

# Create reminder for task
iris reminder create --task 1 --message "Review code" --due-time "2024-12-25 10:00"
```

**Options:**
- `--project`: Associated project ID or name
- `--task`: Associated task ID
- `--message`: Reminder message
- `--due-time`: Reminder due time (YYYY-MM-DD HH:MM)

**Examples:**
```bash
# Project reminder
iris reminder create --project "Website Redesign" --message "Check progress" --due-time "2024-12-25 10:00"

# Task reminder
iris reminder create --task 1 --message "Submit code review" --due-time "2024-12-25 14:00"
```

### `iris reminder list`

List reminders.

```bash
# List all reminders
iris reminder list

# List reminders for specific project
iris reminder list --project 1

# List upcoming reminders
iris reminder list --upcoming
```

**Options:**
- `--project`: Filter by project ID or name
- `--task`: Filter by task ID
- `--upcoming`: Show upcoming reminders

**Examples:**
```bash
# List all reminders
iris reminder list

# List project reminders
iris reminder list --project "Website Redesign"

# List upcoming reminders
iris reminder list --upcoming
```

## Note Commands

### `iris note create`

Create a new note.

```bash
# Create note with content
iris note create --content "Important notes"

# Create note associated with project
iris note create --content "Project notes" --project 1
```

**Options:**
- `--content`: Note content
- `--project`: Associated project ID or name

**Examples:**
```bash
# Basic note creation
iris note create --content "Meeting notes from today"

# Project note
iris note create --content "Design decisions" --project "Website Redesign"
```

### `iris note list`

List notes.

```bash
# List all notes
iris note list

# List notes for specific project
iris note list --project 1
```

**Options:**
- `--project`: Filter by project ID or name

**Examples:**
```bash
# List all notes
iris note list

# List project notes
iris note list --project "Website Redesign"
```

## Global Options

### Verbose Output

Most commands support verbose output:

```bash
# Enable verbose output
iris db migrate --verbose
iris project list --verbose
iris task create --project 1 --title "Task" --verbose
```

### Help

Get help for any command:

```bash
# General help
iris --help

# Command help
iris db --help
iris db migrate --help
iris project create --help
```

### Configuration

Commands respect environment variables and configuration files:

```bash
# Set environment
export IRIS_ENV=production

# Use custom config file
iris db migrate --config custom.ini
```

## Output Formatting

### Rich Output

All commands use Rich formatting for beautiful output:

- **Colors**: Different colors for different types of information
- **Tables**: Formatted tables for lists
- **Progress**: Progress bars for long operations
- **Panels**: Highlighted information panels
- **Icons**: Emoji icons for visual clarity

### Error Handling

Comprehensive error handling with:

- **Clear error messages**: Descriptive error messages
- **Suggestions**: Actionable suggestions for fixing errors
- **Context**: Additional context for debugging
- **Recovery**: Automatic retry for transient errors

## Examples

### Complete Workflow

```bash
# Initialize database
iris db migrate

# Create a project
iris project create "Website Redesign" --description "Redesign company website"

# Create tasks
iris task create --project "Website Redesign" --title "Design mockups" --priority high
iris task create --project "Website Redesign" --title "Implement responsive design" --priority medium

# Create an idea
iris idea create --title "Add dark mode" --description "Implement dark mode toggle"

# Create a reminder
iris reminder create --project "Website Redesign" --message "Review design" --due-time "2024-12-25 10:00"

# Create a note
iris note create --content "Client feedback: prefer blue color scheme" --project "Website Redesign"

# Check status
iris db status
iris project list
iris task list --project "Website Redesign"
```

### Database Management

```bash
# Test connection
iris db test-connection

# Check health
iris db health-check --detailed

# Create backup
iris db backup --output website_backup.db

# Run migrations
iris db migrate --verbose

# Reset database (if needed)
iris db reset --confirm
```

### Project Management

```bash
# Create multiple projects
iris project create "Frontend Development" --status active
iris project create "Backend Development" --status active
iris project create "Testing" --status paused

# List projects
iris project list --detailed

# Update project
iris project update "Frontend Development" --status completed

# Show project details
iris project show "Backend Development"
```

## Troubleshooting

### Common Issues

1. **Database connection errors**: Check database file permissions and location
2. **Migration errors**: Verify Alembic configuration and migration files
3. **Permission errors**: Check file system permissions
4. **Configuration errors**: Verify environment variables and config files

### Debug Mode

Enable debug mode for detailed logging:

```bash
# Set debug environment
export IRIS_DEBUG=true

# Run command with debug output
iris db migrate --verbose
```

### Getting Help

```bash
# Command help
iris <command> --help

# Verbose output
iris <command> --verbose

# Debug mode
IRIS_DEBUG=true iris <command>
```
