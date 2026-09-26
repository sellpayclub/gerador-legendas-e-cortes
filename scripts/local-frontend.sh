#!/bin/bash
set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_ROOT/frontend"
NODE_EXE="$(bash "$PROJECT_ROOT/scripts/find-node-mac.sh")"
export PATH="$(dirname "$NODE_EXE"):/opt/homebrew/bin:/usr/local/bin:$PATH"
export PORT=3000 HOSTNAME=127.0.0.1 BACKEND_URL=http://127.0.0.1:8000
exec npm run start
