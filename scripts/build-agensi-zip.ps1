# Builds the Agensi upload package: dist/photoshop-design-coach.zip
# Contents: one top-level folder photoshop-design-coach/ with SKILL.md, references/, scripts/design_calc.py and CHANGELOG.md only.
# Not included on purpose: README.md, LICENSE (MIT conflicts with the Agensi buyer licence), LISTING.md, evals/, tests/, scripts/build-agensi-zip.ps1.
# Usage (from anywhere): pwsh ./scripts/build-agensi-zip.ps1

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

$root    = Split-Path -Parent $PSScriptRoot
$name    = 'photoshop-design-coach'
$distDir = Join-Path $root 'dist'
$zipPath = Join-Path $distDir "$name.zip"
$include = @('SKILL.md', 'references', 'scripts/design_calc.py', 'CHANGELOG.md')

New-Item -ItemType Directory -Force -Path $distDir | Out-Null
if (Test-Path $zipPath) { Remove-Item $zipPath -Force }

$zip = [System.IO.Compression.ZipFile]::Open($zipPath, [System.IO.Compression.ZipArchiveMode]::Create)
try {
    foreach ($item in $include) {
        $src = Join-Path $root $item
        if (-not (Test-Path $src)) { throw "Missing required item: $item" }
        $files = if ((Get-Item $src).PSIsContainer) { Get-ChildItem -Path $src -Recurse -File } else { @(Get-Item $src) }
        foreach ($f in $files) {
            $rel   = $f.FullName.Substring($root.Length).TrimStart('\', '/').Replace('\', '/')
            $entry = "$name/$rel"
            [System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, $f.FullName, $entry, [System.IO.Compression.CompressionLevel]::Optimal) | Out-Null
        }
    }
}
finally {
    $zip.Dispose()
}

$check = [System.IO.Compression.ZipFile]::OpenRead($zipPath)
try {
    Write-Host "Built $zipPath"
    $check.Entries | ForEach-Object { Write-Host ("  {0}  ({1} bytes)" -f $_.FullName, $_.Length) }
}
finally {
    $check.Dispose()
}
