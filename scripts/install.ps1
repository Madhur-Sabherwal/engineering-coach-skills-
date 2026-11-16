# Copies every skill in ./skills into your Claude Code skills folder.
# Usage: powershell -ExecutionPolicy Bypass -File scripts/install.ps1 [-Only coach-data-engineering,coach-robotics]
param([string[]]$Only)
$src = Join-Path (Split-Path $PSScriptRoot -Parent) "skills"
$dst = Join-Path $HOME ".claude/skills"
New-Item -ItemType Directory -Force $dst | Out-Null
Get-ChildItem $src -Directory | Where-Object { -not $Only -or $Only -contains $_.Name } | ForEach-Object {
    Copy-Item $_.FullName -Destination $dst -Recurse -Force
    Write-Host "Installed $($_.Name)"
}
