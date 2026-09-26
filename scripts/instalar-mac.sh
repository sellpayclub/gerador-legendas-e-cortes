#!/bin/bash
# ============================================================
#  Instalador local (macOS) do Gerador de Legendas
#  Deixa a aplicacao sempre online: sobe sozinha no login e
#  reinicia sozinha se cair (via launchd).
#
#  Uso:  bash scripts/instalar-mac.sh
#
#  IMPORTANTE: rode com o projeto FORA da pasta Desktop/Documentos
#  (o macOS bloqueia servicos em background nessas pastas).
#  Local recomendado: ~/legendas-locais
# ============================================================
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LA="$HOME/Library/LaunchAgents"
BREW_PREFIX="$(brew --prefix)"
NODE_BIN="$(dirname "$(bash "$ROOT/scripts/find-node-mac.sh")")"

echo "==> Projeto em: $ROOT"
case "$ROOT" in
  "$HOME/Desktop/"*|"$HOME/Documents/"*|"$HOME/Downloads/"*)
    echo "ERRO: mova o projeto para fora de Desktop/Documents/Downloads (ex: ~/legendas-locais)."
    echo "      O macOS impede servicos em background de rodar nessas pastas."
    exit 1;;
esac

mkdir -p "$ROOT/logs" "$LA"

echo "==> Verificando backend (venv)..."
if [ ! -x "$ROOT/backend/.venv/bin/python" ]; then
  echo "    Criando venv..."
  (cd "$ROOT/backend" && "$BREW_PREFIX/opt/python@3.13/bin/python3.13" -m venv .venv)
fi
(cd "$ROOT/backend" && .venv/bin/python -m pip install -q -e .)

echo "==> Verificando frontend (build de producao)..."
echo "    Compilando frontend..."
(cd "$ROOT/frontend" && export PATH="$NODE_BIN:$PATH" BACKEND_URL="http://127.0.0.1:8000" NEXT_PUBLIC_MULTI_TENANT="false" && npm ci --silent && npm run build)

echo "==> Gerando servicos do macOS..."
cat > "$LA/com.legendas.backend.plist" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key><string>com.legendas.backend</string>
    <key>ProgramArguments</key>
    <array><string>$ROOT/scripts/local-backend.sh</string></array>
    <key>RunAtLoad</key><true/>
    <key>KeepAlive</key><true/>
    <key>StandardOutPath</key><string>$ROOT/logs/backend.log</string>
    <key>StandardErrorPath</key><string>$ROOT/logs/backend.log</string>
</dict>
</plist>
PLIST

cat > "$LA/com.legendas.frontend.plist" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key><string>com.legendas.frontend</string>
    <key>ProgramArguments</key>
    <array><string>$ROOT/scripts/local-frontend.sh</string></array>
    <key>RunAtLoad</key><true/>
    <key>KeepAlive</key><true/>
    <key>StandardOutPath</key><string>$ROOT/logs/frontend.log</string>
    <key>StandardErrorPath</key><string>$ROOT/logs/frontend.log</string>
</dict>
</plist>
PLIST

chmod +x "$ROOT/scripts/local-backend.sh" "$ROOT/scripts/local-frontend.sh" "$ROOT/legendas.sh"

echo "==> Ativando servicos..."
launchctl unload "$LA/com.legendas.backend.plist" 2>/dev/null || true
launchctl unload "$LA/com.legendas.frontend.plist" 2>/dev/null || true
launchctl load -w "$LA/com.legendas.backend.plist"
launchctl load -w "$LA/com.legendas.frontend.plist"

echo "==> Aguardando subir..."
sleep 8
"$ROOT/legendas.sh" status
echo ""
echo "Pronto! A aplicacao agora sobe sozinha sempre que voce ligar o Mac."
echo "Controle:  ./legendas.sh [ligar|desligar|reiniciar|status|atualizar|logs]"
