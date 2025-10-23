# Iris CLI User Guide

## Getting Started

The Iris CLI is your command-line interface to the Iris project management system. This guide will help you get started and become productive with the CLI.

## Installation

### Prerequisites

- Python 3.12 or higher
- pip (Python package installer)

### Install Iris

```bash
# Clone the repository
git clone https://github.com/your-username/iris.git
cd iris

# Install in development mode
pip install -e .

# Verify installation
iris --help
```

### First-Time Setup

```bash
# Initialize the database
iris db migrate

# Test the connection
iris db test-connection

# Check system status
iris db status
```

## Basic Concepts

### Projects

Projects are the main organizational unit in Iris. Each project can contain:
- Tasks
- Ideas
- Reminders
- Notes

### Tasks

Tasks are work items that belong to projects. Each task has:
- Title
- Priority (low, medium, high, urgent)
- Due date (optional)
- Completion status
- Notes

### Ideas

Ideas are spontaneous thoughts that may become projects. They can be:
- Standalone ideas
- Associated with existing projects
- Promoted to full projects

### Reminders

Reminders are notifications for projects or tasks. They have:
- Message
- Due time
- Association with project or task

### Notes

Notes are free-form text associated with projects. They're useful for:
- Meeting notes
- Design decisions
- Client feedback
- Documentation

## Common Workflows

### Starting a New Project

1. **Create the project:**
   ```bash
   iris project create "My New Project" --description "Project description"
   ```

2. **Add initial tasks:**
   ```bash
   iris task create --project "My New Project" --title "Setup project" --priority high
   iris task create --project "My New Project" --title "Research requirements" --priority medium
   ```

3. **Set up reminders:**
   ```bash
   iris reminder create --project "My New Project" --message "Check progress" --due-time "2024-12-25 10:00"
   ```

4. **Add notes:**
   ```bash
   iris note create --content "Initial project notes" --project "My New Project"
   ```

### Daily Task Management

1. **Check your tasks:**
   ```bash
   iris task list
   ```

2. **Update task status:**
   ```bash
   iris task update 1 --completed
   ```

3. **Add new tasks:**
   ```bash
   iris task create --project "My Project" --title "New task" --priority medium
   ```

4. **Check reminders:**
   ```bash
   iris reminder list --upcoming
   ```

### Project Review

1. **List all projects:**
   ```bash
   iris project list --detailed
   ```

2. **Check project status:**
   ```bash
   iris project show "My Project"
   ```

3. **Update project status:**
   ```bash
   iris project update "My Project" --status completed
   ```

4. **Review project notes:**
   ```bash
   iris note list --project "My Project"
   ```

## Advanced Usage

### Batch Operations

Create multiple tasks at once:

```bash
# Create several tasks for a project
iris task create --project "Website Redesign" --title "Design homepage" --priority high
iris task create --project "Website Redesign" --title "Design about page" --priority medium
iris task create --project "Website Redesign" --title "Design contact page" --priority low
```

### Project Templates

Create a standard set of tasks for new projects:

```bash
# Create project
iris project create "New Website" --description "Client website project"

# Add standard tasks
iris task create --project "New Website" --title "Requirements gathering" --priority high
iris task create --project "New Website" --title "Design mockups" --priority high
iris task create --project "New Website" --title "Development" --priority medium
iris task create --project "New Website" --title "Testing" --priority medium
iris task create --project "New Website" --title "Deployment" --priority high
```

### Idea Management

Capture and organize ideas:

```bash
# Create standalone ideas
iris idea create --title "Mobile app idea" --description "Fitness tracking app"
iris idea create --title "Website feature" --description "Add search functionality"

# Associate ideas with projects
iris idea create --title "Enhancement idea" --project "Website Redesign" --description "Add dark mode"

# Promote idea to project
iris idea promote 1
```

### Reminder System

Set up reminders for important deadlines:

```bash
# Project reminders
iris reminder create --project "Website Redesign" --message "Client meeting" --due-time "2024-12-25 14:00"
iris reminder create --project "Website Redesign" --message "Submit proposal" --due-time "2024-12-30 17:00"

# Task reminders
iris reminder create --task 1 --message "Review code" --due-time "2024-12-26 10:00"
```

## Productivity Tips

### Use Aliases

Create shell aliases for common commands:

```bash
# Add to your .bashrc or .zshrc
alias iris-list="iris project list"
alias iris-tasks="iris task list"
alias iris-ideas="iris idea list"
alias iris-reminders="iris reminder list --upcoming"
```

### Organize with Status

Use project status to organize your work:

```bash
# Active projects (current work)
iris project list --status active

# Completed projects (finished work)
iris project list --status completed

# Paused projects (on hold)
iris project list --status paused
```

### Priority Management

Use task priorities to focus on important work:

```bash
# High priority tasks (urgent)
iris task list --priority high

# Medium priority tasks (important)
iris task list --priority medium

# Low priority tasks (nice to have)
iris task list --priority low
```

### Due Date Management

Use due dates to manage deadlines:

```bash
# Tasks due today
iris task list --due-date $(date +%Y-%m-%d)

# Tasks due this week
iris task list --due-date $(date -d "+7 days" +%Y-%m-%d)
```

## Data Management

### Backing Up Your Data

Regular backups are important:

```bash
# Create backup
iris db backup --output backup_$(date +%Y%m%d).db

# Create compressed backup
iris db backup --output backup_$(date +%Y%m%d).db --compress
```

### Restoring Data

Restore from backup if needed:

```bash
# Restore from backup
iris db restore backup_20241219.db
```

### Database Maintenance

Keep your database healthy:

```bash
# Check database health
iris db health-check --detailed

# Test connection
iris db test-connection

# Run migrations
iris db migrate
```

## Troubleshooting

### Common Issues

#### Database Connection Errors

```bash
# Check database file exists
ls -la iris.db

# Test connection
iris db test-connection --verbose

# Check permissions
ls -la iris.db
```

#### Migration Errors

```bash
# Check migration status
iris db status

# Run migrations
iris db migrate --verbose

# Check Alembic configuration
cat alembic.ini
```

#### Permission Errors

```bash
# Check file permissions
ls -la iris.db

# Fix permissions if needed
chmod 644 iris.db
```

### Getting Help

```bash
# General help
iris --help

# Command help
iris db --help
iris project --help
iris task --help

# Verbose output
iris <command> --verbose
```

### Debug Mode

Enable debug mode for detailed logging:

```bash
# Set debug environment
export IRIS_DEBUG=true

# Run command with debug output
iris db migrate --verbose
```

## Best Practices

### Project Organization

1. **Use descriptive names**: Clear, descriptive project names
2. **Set appropriate status**: Keep project status up to date
3. **Add descriptions**: Include project descriptions for context
4. **Regular reviews**: Review and update projects regularly

### Task Management

1. **Break down work**: Split large tasks into smaller ones
2. **Set priorities**: Use priority levels to focus on important work
3. **Set due dates**: Use due dates to manage deadlines
4. **Add notes**: Include relevant notes for context

### Idea Capture

1. **Capture quickly**: Record ideas as soon as they come
2. **Add descriptions**: Include detailed descriptions
3. **Associate with projects**: Link ideas to relevant projects
4. **Promote good ideas**: Convert promising ideas to projects

### Reminder System

1. **Set realistic reminders**: Don't over-remind yourself
2. **Use specific messages**: Clear, actionable reminder messages
3. **Set appropriate times**: Choose times when you'll be available
4. **Review regularly**: Check and update reminders regularly

### Data Management

1. **Regular backups**: Backup your data regularly
2. **Test restores**: Verify backup restoration works
3. **Keep migrations current**: Run migrations regularly
4. **Monitor health**: Check database health periodically

## Integration

### Shell Integration

Add Iris commands to your shell profile:

```bash
# Add to .bashrc or .zshrc
alias iris-status="iris db status"
alias iris-health="iris db health-check --detailed"
alias iris-backup="iris db backup --output backup_$(date +%Y%m%d).db"
```

### Scripting

Use Iris in scripts:

```bash
#!/bin/bash
# Daily backup script

# Create backup
iris db backup --output daily_backup_$(date +%Y%m%d).db --compress

# Check health
iris db health-check --detailed

# List today's tasks
iris task list --due-date $(date +%Y-%m-%d)
```

### Automation

Automate common tasks:

```bash
# Cron job for daily backup
0 2 * * * /path/to/iris db backup --output /path/to/backups/backup_$(date +\%Y\%m\%d).db --compress

# Cron job for health check
0 8 * * * /path/to/iris db health-check --detailed
```

## Advanced Features

### Custom Configuration

Create custom configuration:

```bash
# Set environment
export IRIS_ENV=production

# Use custom config
iris db migrate --config custom.ini
```

### Batch Operations

Process multiple items:

```bash
# Create multiple projects
for project in "Frontend" "Backend" "Testing"; do
    iris project create "$project" --description "Development project"
done

# Create multiple tasks
for task in "Setup" "Develop" "Test" "Deploy"; do
    iris task create --project "My Project" --title "$task" --priority medium
done
```

### Data Export

Export data for analysis:

```bash
# List all projects
iris project list > projects.txt

# List all tasks
iris task list > tasks.txt

# List all ideas
iris idea list > ideas.txt
```

## Support

### Getting Help

- **Command help**: `iris <command> --help`
- **Verbose output**: `iris <command> --verbose`
- **Debug mode**: `IRIS_DEBUG=true iris <command>`

### Reporting Issues

When reporting issues, include:
- Command that failed
- Error message
- Verbose output (`--verbose`)
- System information
- Steps to reproduce

### Contributing

- Report bugs and feature requests
- Contribute code improvements
- Improve documentation
- Share your workflows
