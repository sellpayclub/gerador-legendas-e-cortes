#!/bin/bash
set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_ROOT/backend"
for BREW_PREFIX in /opt/homebrew /usr/local; do
  if [ -x "$BREW_PREFIX/opt/ffmpeg-full/bin/ffmpeg" ]; then
    export PATH="$BREW_PREFIX/opt/ffmpeg-full/bin:$BREW_PREFIX/bin:$PATH"
    break
  fi
done
exec .venv/bin/python -m uvicorn main:app --port 8000 --host 127.0.0.1
