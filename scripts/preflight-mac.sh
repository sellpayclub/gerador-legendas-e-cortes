#!/bin/bash
# Verifica/instala pré-requisitos no macOS antes do install.sh
set -euo pipefail

echo "==> Verificando pré-requisitos (Mac)..."

if [[ "$(uname -s)" != "Darwin" ]]; then
  echo "    (preflight-mac ignorado — não é macOS)"
  exit 0
fi

install_brew_pkg() {
  local pkg="$1"
  if brew list "$pkg" &>/dev/null; then
    echo "    $pkg OK"
  else
    echo "    Instalando $pkg..."
    brew install "$pkg"
  fi
}

if ! command -v brew >/dev/null; then
  echo ""
  echo "ERRO: Homebrew não encontrado."
  echo "Instale em https://brew.sh com:"
  echo '  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
  echo ""
  echo "Depois rode novamente: bash install.sh"
  exit 1
fi

install_brew_pkg python@3.13
install_brew_pkg ffmpeg-full

BREW_PREFIX="$(brew --prefix)"
if [[ ! -x "$BREW_PREFIX/opt/python@3.13/bin/python3.13" ]]; then
  echo "ERRO: python3.13 não encontrado após instalar python@3.13."
  echo "Adicione ao PATH: export PATH=\"/opt/homebrew/opt/python@3.13/bin:\$PATH\""
  exit 1
fi

if ! NODE_EXE="$(bash "$(dirname "$0")/find-node-mac.sh")"; then
  if brew list node@22 &>/dev/null; then
    echo "    Reparando Node.js 22..."
    brew reinstall node@22
  else
    install_brew_pkg node@22
  fi
  NODE_EXE="$(bash "$(dirname "$0")/find-node-mac.sh")" || {
    echo "ERRO: Node.js 22+ nao funciona. Reinstale com brew reinstall node@22."
    exit 1
  }
fi
export PATH="$(dirname "$NODE_EXE"):$PATH"

FFMPEG_BIN="$BREW_PREFIX/opt/ffmpeg-full/bin/ffmpeg"
if [[ ! -x "$FFMPEG_BIN" ]]; then
  echo "ERRO: ffmpeg-full não encontrado em $FFMPEG_BIN"
  exit 1
fi

FFMPEG_FILTERS="$("$FFMPEG_BIN" -hide_banner -filters 2>/dev/null)"
if ! grep -q " ass " <<< "$FFMPEG_FILTERS"; then
  echo "ERRO: ffmpeg-full sem filtro ass (libass). Rode: brew reinstall ffmpeg-full"
  exit 1
fi

echo "    python3.13 $("$BREW_PREFIX/opt/python@3.13/bin/python3.13" --version 2>&1 | awk '{print $2}')"
echo "    node $("$NODE_EXE" --version)"
echo "    ffmpeg-full + libass OK"
echo "==> Pré-requisitos OK"
