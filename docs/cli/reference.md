# Iris CLI Reference

## Command Reference

This reference provides detailed information about all Iris CLI commands, their options, and usage examples.

## Global Options

All commands support these global options:

- `--help, -h`: Show help message
- `--verbose, -v`: Enable verbose output
- `--version`: Show version information

## Database Commands

### `iris db migrate`

Run database migrations to update the schema.

**Usage:**
```bash
iris db migrate [OPTIONS]
```

**Options:**
- `--verbose, -v`: Enable verbose output
- `--force, -f`: Force migration without confirmation
- `--dry-run`: Show what would be migrated without applying

**Examples:**
```bash
iris db migrate
iris db migrate --verbose
iris db migrate --force
iris db migrate --dry-run
```

**Description:**
Runs all pending database migrations to update the schema to the latest version. This command is safe to run multiple times and will only apply new migrations.

### `iris db test-connection`

Test database connection and verify connectivity.

**Usage:**
```bash
iris db test-connection [OPTIONS]
```

**Options:**
- `--timeout, -t INTEGER`: Connection timeout in seconds (default: 5)
- `--verbose, -v`: Enable verbose output

**Examples:**
```bash
iris db test-connection
iris db test-connection --timeout 10
iris db test-connection --verbose
```

**Description:**
Tests the database connection to ensure it's working properly. Useful for troubleshooting connection issues.

### `iris db health-check`

Check database health and performance metrics.

**Usage:**
```bash
iris db health-check [OPTIONS]
```

**Options:**
- `--detailed, -d`: Show detailed health information
- `--verbose, -v`: Enable verbose output

**Examples:**
```bash
iris db health-check
iris db health-check --detailed
iris db health-check --verbose
```

**Description:**
Performs a comprehensive health check of the database, including connection status, performance metrics, and system information.

### `iris db status`

Show database status and configuration information.

**Usage:**
```bash
iris db status
```

**Examples:**
```bash
iris db status
```

**Description:**
Displays current database status, configuration settings, and migration information.

### `iris db reset`

Reset database (WARNING: This will delete all data).

**Usage:**
```bash
iris db reset [OPTIONS]
```

**Options:**
- `--confirm, -y`: Skip confirmation prompt
- `--force, -f`: Force reset without confirmation

**Examples:**
```bash
iris db reset
iris db reset --confirm
iris db reset --force
```

**Description:**
Resets the database to its initial state, deleting all data. Use with caution as this action cannot be undone.

### `iris db backup`

Create database backup.

**Usage:**
```bash
iris db backup [OPTIONS]
```

**Options:**
- `--output, -o TEXT`: Output file path
- `--compress, -c`: Compress backup file

**Examples:**
```bash
iris db backup
iris db backup --output backup.db
iris db backup --compress
iris db backup --output backup.db --compress
```

**Description:**
Creates a backup of the database. If no output file is specified, a timestamped filename is generated automatically.

### `iris db restore`

Restore database from backup.

**Usage:**
```bash
iris db restore INPUT_FILE [OPTIONS]
```

**Arguments:**
- `INPUT_FILE`: Input backup file path

**Options:**
- `--force, -f`: Force restore without confirmation

**Examples:**
```bash
iris db restore backup.db
iris db restore backup.db --force
```

**Description:**
Restores the database from a backup file. This will replace all current data with the backup data.

## Project Commands

### `iris project create`

Create a new project.

**Usage:**
```bash
iris project create NAME [OPTIONS]
```

**Arguments:**
- `NAME`: Project name

**Options:**
- `--description TEXT`: Project description
- `--status [active|completed|paused]`: Project status (default: active)

**Examples:**
```bash
iris project create "My Project"
iris project create "My Project" --description "Project description"
iris project create "My Project" --status active
```

**Description:**
Creates a new project with the specified name and optional description and status.

### `iris project list`

List all projects.

**Usage:**
```bash
iris project list [OPTIONS]
```

**Options:**
- `--status [active|completed|paused]`: Filter by project status
- `--detailed`: Show detailed information

**Examples:**
```bash
iris project list
iris project list --status active
iris project list --detailed
```

**Description:**
Lists all projects, optionally filtered by status. Use `--detailed` for additional information.

### `iris project show`

Show project details.

**Usage:**
```bash
iris project show PROJECT
```

**Arguments:**
- `PROJECT`: Project ID or name

**Examples:**
```bash
iris project show 1
iris project show "My Project"
```

**Description:**
Shows detailed information about a specific project, including associated tasks, ideas, reminders, and notes.

### `iris project update`

Update project information.

**Usage:**
```bash
iris project update PROJECT [OPTIONS]
```

**Arguments:**
- `PROJECT`: Project ID or name

**Options:**
- `--name TEXT`: New project name
- `--description TEXT`: New project description
- `--status [active|completed|paused]`: New project status

**Examples:**
```bash
iris project update 1 --name "Updated Project"
iris project update "My Project" --status completed
iris project update 1 --description "Updated description"
```

**Description:**
Updates project information. You can update the name, description, or status.

### `iris project delete`

Delete a project.

**Usage:**
```bash
iris project delete PROJECT [OPTIONS]
```

**Arguments:**
- `PROJECT`: Project ID or name

**Options:**
- `--force, -f`: Force deletion without confirmation

**Examples:**
```bash
iris project delete 1
iris project delete "My Project" --force
```

**Description:**
Deletes a project and all associated tasks, ideas, reminders, and notes. This action cannot be undone.

## Task Commands

### `iris task create`

Create a new task.

**Usage:**
```bash
iris task create [OPTIONS]
```

**Options:**
- `--project TEXT`: Project ID or name
- `--title TEXT`: Task title
- `--priority [low|medium|high|urgent]`: Task priority (default: medium)
- `--due-date DATE`: Task due date (YYYY-MM-DD)
- `--notes TEXT`: Task notes

**Examples:**
```bash
iris task create --project 1 --title "Complete feature"
iris task create --project "My Project" --title "Fix bug" --priority high
iris task create --project 1 --title "Review code" --due-date 2024-12-31 --notes "Important task"
```

**Description:**
Creates a new task associated with a project. The project must exist before creating the task.

### `iris task list`

List tasks.

**Usage:**
```bash
iris task list [OPTIONS]
```

**Options:**
- `--project TEXT`: Filter by project ID or name
- `--completed BOOLEAN`: Filter by completion status
- `--priority [low|medium|high|urgent]`: Filter by priority
- `--due-date DATE`: Filter by due date (YYYY-MM-DD)

**Examples:**
```bash
iris task list
iris task list --project "My Project"
iris task list --completed false
iris task list --priority high
```

**Description:**
Lists tasks, optionally filtered by project, completion status, priority, or due date.

### `iris task show`

Show task details.

**Usage:**
```bash
iris task show TASK
```

**Arguments:**
- `TASK`: Task ID

**Examples:**
```bash
iris task show 1
```

**Description:**
Shows detailed information about a specific task, including its project, priority, due date, and notes.

### `iris task update`

Update task information.

**Usage:**
```bash
iris task update TASK [OPTIONS]
```

**Arguments:**
- `TASK`: Task ID

**Options:**
- `--title TEXT`: New task title
- `--priority [low|medium|high|urgent]`: New task priority
- `--due-date DATE`: New task due date (YYYY-MM-DD)
- `--notes TEXT`: New task notes
- `--completed`: Mark task as completed
- `--incomplete`: Mark task as incomplete

**Examples:**
```bash
iris task update 1 --completed
iris task update 1 --title "Updated task"
iris task update 1 --priority high --completed
```

**Description:**
Updates task information. You can update the title, priority, due date, notes, or completion status.

### `iris task delete`

Delete a task.

**Usage:**
```bash
iris task delete TASK [OPTIONS]
```

**Arguments:**
- `TASK`: Task ID

**Options:**
- `--force, -f`: Force deletion without confirmation

**Examples:**
```bash
iris task delete 1
iris task delete 1 --force
```

**Description:**
Deletes a task. This action cannot be undone.

## Idea Commands

### `iris idea create`

Create a new idea.

**Usage:**
```bash
iris idea create [OPTIONS]
```

**Options:**
- `--title TEXT`: Idea title
- `--description TEXT`: Idea description
- `--project TEXT`: Associated project ID or name

**Examples:**
```bash
iris idea create --title "Great idea"
iris idea create --title "Feature idea" --description "Add dark mode"
iris idea create --title "Enhancement" --project "My Project"
```

**Description:**
Creates a new idea. Ideas can be standalone or associated with a project.

### `iris idea list`

List ideas.

**Usage:**
```bash
iris idea list [OPTIONS]
```

**Options:**
- `--project TEXT`: Filter by project ID or name
- `--promoted`: Filter by promotion status

**Examples:**
```bash
iris idea list
iris idea list --project "My Project"
iris idea list --promoted
```

**Description:**
Lists ideas, optionally filtered by project or promotion status.

### `iris idea promote`

Promote an idea to a project.

**Usage:**
```bash
iris idea promote IDEA
```

**Arguments:**
- `IDEA`: Idea ID

**Examples:**
```bash
iris idea promote 1
```

**Description:**
Promotes an idea to a full project. The idea's title becomes the project name, and the description becomes the project description.

## Reminder Commands

### `iris reminder create`

Create a new reminder.

**Usage:**
```bash
iris reminder create [OPTIONS]
```

**Options:**
- `--project TEXT`: Associated project ID or name
- `--task INTEGER`: Associated task ID
- `--message TEXT`: Reminder message
- `--due-time DATETIME`: Reminder due time (YYYY-MM-DD HH:MM)

**Examples:**
```bash
iris reminder create --project "My Project" --message "Don't forget!" --due-time "2024-12-25 10:00"
iris reminder create --task 1 --message "Review code" --due-time "2024-12-25 14:00"
```

**Description:**
Creates a new reminder. Reminders can be associated with either a project or a task.

### `iris reminder list`

List reminders.

**Usage:**
```bash
iris reminder list [OPTIONS]
```

**Options:**
- `--project TEXT`: Filter by project ID or name
- `--task INTEGER`: Filter by task ID
- `--upcoming`: Show upcoming reminders

**Examples:**
```bash
iris reminder list
iris reminder list --project "My Project"
iris reminder list --upcoming
```

**Description:**
Lists reminders, optionally filtered by project, task, or showing only upcoming reminders.

## Note Commands

### `iris note create`

Create a new note.

**Usage:**
```bash
iris note create [OPTIONS]
```

**Options:**
- `--content TEXT`: Note content
- `--project TEXT`: Associated project ID or name

**Examples:**
```bash
iris note create --content "Important notes"
iris note create --content "Project notes" --project "My Project"
```

**Description:**
Creates a new note. Notes can be standalone or associated with a project.

### `iris note list`

List notes.

**Usage:**
```bash
iris note list [OPTIONS]
```

**Options:**
- `--project TEXT`: Filter by project ID or name

**Examples:**
```bash
iris note list
iris note list --project "My Project"
```

**Description:**
Lists notes, optionally filtered by project.

## Environment Variables

The following environment variables can be used to configure Iris:

- `IRIS_ENV`: Application environment (development, staging, production)
- `IRIS_DEBUG`: Enable debug mode (true/false)
- `IRIS_DATABASE_URL`: Database connection URL
- `IRIS_LOG_LEVEL`: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- `IRIS_LOG_FILE`: Log file path

## Configuration Files

Iris supports configuration through:

- `.env` file in the project root
- `alembic.ini` for database migrations
- Environment variables
- Command-line options

## Exit Codes

Iris uses the following exit codes:

- `0`: Success
- `1`: General error
- `2`: Invalid command or option
- `3`: Database error
- `4`: Configuration error
- `5`: Permission error

## Output Formats

Iris uses Rich formatting for beautiful output:

- **Tables**: Formatted tables for lists
- **Progress**: Progress bars for long operations
- **Panels**: Highlighted information panels
- **Colors**: Different colors for different types of information
- **Icons**: Emoji icons for visual clarity

## Error Handling

Iris provides comprehensive error handling:

- **Clear error messages**: Descriptive error messages
- **Suggestions**: Actionable suggestions for fixing errors
- **Context**: Additional context for debugging
- **Recovery**: Automatic retry for transient errors

## Performance

Iris is optimized for performance:

- **Connection pooling**: Efficient database connections
- **Batch operations**: Process multiple items efficiently
- **Indexing**: Optimized database queries
- **Caching**: Reduced database access

## Security

Iris implements security best practices:

- **Input validation**: All input is validated
- **SQL injection protection**: Parameterized queries
- **File permissions**: Proper file system permissions
- **Data encryption**: Optional data encryption

## Troubleshooting

### Common Issues

1. **Database connection errors**: Check database file permissions and location
2. **Migration errors**: Verify Alembic configuration and migration files
3. **Permission errors**: Check file system permissions
4. **Configuration errors**: Verify environment variables and config files

### Debug Mode

Enable debug mode for detailed logging:

```bash
export IRIS_DEBUG=true
iris <command> --verbose
```

### Getting Help

```bash
iris --help
iris <command> --help
iris <command> --verbose
```
