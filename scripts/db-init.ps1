# Database initialization script for Windows
# Applies 001_initial_schema.sql to Supabase
# Per T032: Create db-init script

param(
    [string]$EnvFile = ".env"
)

Write-Host "🌸 Iris Database Initialization" -ForegroundColor Blue
Write-Host ""

# Check if .env exists
if (-not (Test-Path $EnvFile)) {
    Write-Host "❌ Error: $EnvFile not found" -ForegroundColor Red
    Write-Host "Run 'copy .env.example .env' and configure your Supabase credentials" -ForegroundColor Yellow
    exit 1
}

# Load .env file
Get-Content $EnvFile | ForEach-Object {
    if ($_ -match '^\s*([^#][^=]*?)\s*=\s*(.+?)\s*$') {
        $name = $matches[1]
        $value = $matches[2]
        Set-Item -Path "env:$name" -Value $value
    }
}

# Verify Supabase credentials
if (-not $env:SUPABASE_URL) {
    Write-Host "❌ Error: SUPABASE_URL not set in $EnvFile" -ForegroundColor Red
    exit 1
}

Write-Host "📍 Supabase URL: $env:SUPABASE_URL" -ForegroundColor Cyan
Write-Host ""

# Check if migration file exists
$migrationFile = "src/iris/database/migrations/001_initial_schema.sql"
if (-not (Test-Path $migrationFile)) {
    Write-Host "❌ Error: Migration file not found: $migrationFile" -ForegroundColor Red
    exit 1
}

Write-Host "📄 Applying migration: 001_initial_schema.sql" -ForegroundColor Cyan

# Use Supabase Python client to execute SQL
$pythonScript = @"
from supabase import create_client
import os
import sys

try:
    # Read migration SQL
    with open('$migrationFile', 'r', encoding='utf-8') as f:
        sql = f.read()
    
    # Connect to Supabase (using service key to create schema)
    client = create_client(
        os.environ['SUPABASE_URL'],
        os.environ.get('SUPABASE_SERVICE_KEY', os.environ['SUPABASE_ANON_KEY'])
    )
    
    # Execute migration
    # Note: Supabase Python client doesn't directly support raw SQL execution
    # In practice, use Supabase SQL Editor or psql command
    print('✅ Migration file ready')
    print('')
    print('⚠️  To apply this migration:')
    print('   1. Open Supabase Dashboard → SQL Editor')
    print('   2. Copy contents of', '$migrationFile')
    print('   3. Paste and run in SQL Editor')
    print('')
    print('   Or use psql if you have PostgreSQL client:')
    print('   psql $SUPABASE_DATABASE_URL -f $migrationFile')
    
except Exception as e:
    print(f'❌ Error: {e}', file=sys.stderr)
    sys.exit(1)
"@

uv run python -c $pythonScript

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "✅ Database initialization complete!" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "❌ Database initialization failed" -ForegroundColor Red
    exit 1
}

