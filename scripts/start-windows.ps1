param([switch]$NoBrowser)

$ErrorActionPreference = "Stop"
$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$backend = Join-Path $projectRoot "backend"
$frontend = Join-Path $projectRoot "frontend"
$python = Join-Path $backend ".venv\Scripts\python.exe"
$server = Join-Path $frontend ".next\standalone\server.js"
$logs = Join-Path $projectRoot "logs"
New-Item -ItemType Directory -Force -Path $logs | Out-Null
if (-not (Test-Path $python) -or -not (Test-Path $server)) {
  throw "Instalacao incompleta. Execute Instalar-Windows.cmd primeiro."
}

function Is-Ready([string]$url) {
  try { return (Invoke-WebRequest -Uri $url -UseBasicParsing -TimeoutSec 3).StatusCode -eq 200 }
  catch { return $false }
}

$env:BACKEND_URL = "http://127.0.0.1:8000"
$env:NEXT_PUBLIC_MULTI_TENANT = "false"
$env:PORT = "3000"
$env:HOSTNAME = "127.0.0.1"
$env:NODE_ENV = "production"

if (-not (Is-Ready "http://127.0.0.1:8000/api/health")) {
  Start-Process -FilePath $python -ArgumentList @("-m", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000") -WorkingDirectory $backend -WindowStyle Minimized -RedirectStandardOutput (Join-Path $logs "backend-windows.log") -RedirectStandardError (Join-Path $logs "backend-windows-error.log") | Out-Null
}
if (-not (Is-Ready "http://127.0.0.1:3000/")) {
  $node = (Get-Command node -ErrorAction Stop).Source
  Start-Process -FilePath $node -ArgumentList "`"$server`"" -WorkingDirectory $frontend -WindowStyle Minimized -RedirectStandardOutput (Join-Path $logs "frontend-windows.log") -RedirectStandardError (Join-Path $logs "frontend-windows-error.log") | Out-Null
}

for ($attempt = 0; $attempt -lt 30; $attempt++) {
  if ((Is-Ready "http://127.0.0.1:8000/api/health") -and (Is-Ready "http://127.0.0.1:3000/")) {
    Write-Host "Pronto: http://127.0.0.1:3000"
    if (-not $NoBrowser) { Start-Process "http://127.0.0.1:3000" }
    exit 0
  }
  Start-Sleep -Seconds 2
}
throw "O app nao respondeu nas portas 3000/8000. Veja os arquivos em logs\ e execute Iniciar-Windows.cmd novamente."
