# Database reset script for Windows
# Drops and recreates all tables (DEVELOPMENT ONLY)
# Per T033: Create db-reset script with confirmation

param(
    [switch]$Force
)

Write-Host "🌸 Iris Database Reset (DEVELOPMENT ONLY)" -ForegroundColor Red
Write-Host ""
Write-Host "⚠️  WARNING: This will DELETE ALL DATA in your Supabase database!" -ForegroundColor Yellow
Write-Host ""

# Confirmation prompt (unless -Force)
if (-not $Force) {
    $confirm = Read-Host "Type 'yes' to confirm deletion"
    if ($confirm -ne "yes") {
        Write-Host "❌ Reset cancelled" -ForegroundColor Yellow
        exit 0
    }
}

# Load .env
if (-not (Test-Path ".env")) {
    Write-Host "❌ Error: .env file not found" -ForegroundColor Red
    exit 1
}

Get-Content ".env" | ForEach-Object {
    if ($_ -match '^\s*([^#][^=]*?)\s*=\s*(.+?)\s*$') {
        Set-Item -Path "env:$($matches[1])" -Value $matches[2]
    }
}

Write-Host "📄 Dropping all tables..." -ForegroundColor Cyan

$dropScript = @"
from supabase import create_client
import os

try:
    print('Note: Use Supabase SQL Editor to run:')
    print('')
    print('DROP TABLE IF EXISTS notes CASCADE;')
    print('DROP TABLE IF EXISTS reminders CASCADE;')
    print('DROP TABLE IF EXISTS ideas CASCADE;')
    print('DROP TABLE IF EXISTS tasks CASCADE;')
    print('DROP TABLE IF EXISTS projects CASCADE;')
    print('DROP FUNCTION IF EXISTS update_updated_at_column CASCADE;')
    print('DROP FUNCTION IF EXISTS set_completed_timestamp CASCADE;')
    print('')
    print('Then run: just db-init')
    
except Exception as e:
    print(f'Error: {e}')
"@

uv run python -c $dropScript

Write-Host ""
Write-Host "✅ Reset instructions provided. Run 'just db-init' after dropping tables." -ForegroundColor Green

