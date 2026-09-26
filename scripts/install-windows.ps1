$ErrorActionPreference = "Stop"
$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
Set-Location $projectRoot

function Refresh-Path {
  $env:Path = [Environment]::GetEnvironmentVariable("Path", "Machine") + ";" +
    [Environment]::GetEnvironmentVariable("Path", "User") + ";" + $env:Path
}

function Ensure-Command([string]$command, [string]$package, [string]$download) {
  if (Get-Command $command -ErrorAction SilentlyContinue) { return }
  if (Get-Command winget -ErrorAction SilentlyContinue) {
    Write-Host "Instalando $package..."
    & winget install --id $package --exact --source winget --accept-package-agreements --accept-source-agreements
    if ($LASTEXITCODE -ne 0) { throw "Falha ao instalar $package. Instale em $download e execute novamente." }
    Refresh-Path
  }
  if (-not (Get-Command $command -ErrorAction SilentlyContinue)) {
    throw "$command nao encontrado. Instale em $download, abra um novo terminal e execute Instalar-Windows.cmd novamente."
  }
}

Ensure-Command "py" "Python.Python.3.13" "https://www.python.org/downloads/"
Ensure-Command "node" "OpenJS.NodeJS.LTS" "https://nodejs.org/"
Ensure-Command "ffmpeg" "Gyan.FFmpeg" "https://www.gyan.dev/ffmpeg/builds/"

$pythonVersion = & py -3.13 --version 2>&1
if ($LASTEXITCODE -ne 0) { throw "Python 3.13 nao disponivel: $pythonVersion" }
$nodeVersion = & node --version
$nodeMajor = [int]($nodeVersion.TrimStart('v').Split('.')[0])
if ($nodeMajor -lt 22) {
  if (Get-Command winget -ErrorAction SilentlyContinue) {
    & winget upgrade --id OpenJS.NodeJS.LTS --exact --source winget --accept-package-agreements --accept-source-agreements
    Refresh-Path
    $nodeVersion = & node --version
    $nodeMajor = [int]($nodeVersion.TrimStart('v').Split('.')[0])
  }
  if ($nodeMajor -lt 22) { throw "Node.js 22 ou superior e necessario. Atualize em https://nodejs.org/ e execute novamente." }
}
if (-not (Get-Command ffprobe -ErrorAction SilentlyContinue)) { throw "ffprobe nao encontrado. Instale a versao full do FFmpeg." }
$ffmpegFilters = & ffmpeg -hide_banner -filters 2>&1 | Out-String
if ($LASTEXITCODE -ne 0 -or $ffmpegFilters -notmatch '(?m)^\s*\S+\s+ass\s') {
  throw "FFmpeg precisa incluir o filtro ass (libass). Instale a versao full do FFmpeg e tente novamente."
}
Write-Host "Python $pythonVersion, Node $nodeVersion, FFmpeg com libass: OK"

$venvPython = Join-Path $projectRoot "backend\.venv\Scripts\python.exe"
if (-not (Test-Path $venvPython)) {
  & py -3.13 -m venv (Join-Path $projectRoot "backend\.venv")
  if ($LASTEXITCODE -ne 0) { throw "Nao foi possivel criar o ambiente Python." }
}
Push-Location (Join-Path $projectRoot "backend")
try {
  & $venvPython -m pip install -e .
  if ($LASTEXITCODE -ne 0) { throw "Falha ao instalar o backend." }
} finally { Pop-Location }

Push-Location (Join-Path $projectRoot "frontend")
try {
  $env:BACKEND_URL = "http://127.0.0.1:8000"
  $env:NEXT_PUBLIC_MULTI_TENANT = "false"
  & npm.cmd ci
  if ($LASTEXITCODE -ne 0) { throw "Falha ao instalar o frontend." }
  & npm.cmd run build
  if ($LASTEXITCODE -ne 0) { throw "Falha ao compilar o frontend." }
} finally { Pop-Location }

Write-Host "Instalacao concluida. Abrindo o app local..."
$startup = [Environment]::GetFolderPath("Startup")
$shortcutPath = Join-Path $startup "Gerador de Legendas.lnk"
$shell = New-Object -ComObject WScript.Shell
$shortcut = $shell.CreateShortcut($shortcutPath)
$shortcut.TargetPath = (Get-Command powershell.exe -ErrorAction Stop).Source
$shortcut.Arguments = "-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File `"$PSScriptRoot\start-windows.ps1`" -NoBrowser"
$shortcut.WorkingDirectory = $projectRoot
$shortcut.Description = "Inicia o Gerador de Legendas ao entrar no Windows"
$shortcut.Save()
& (Join-Path $PSScriptRoot "start-windows.ps1")
