#!/bin/bash
set -euo pipefail

for candidate in "$(command -v node 2>/dev/null || true)" \
  /usr/local/bin/node /opt/homebrew/bin/node \
  /opt/homebrew/opt/node@22/bin/node /usr/local/opt/node@22/bin/node; do
  if [ -n "$candidate" ] && [ -x "$candidate" ] && \
     "$candidate" -e 'process.exit(Number(process.versions.node.split(".")[0]) >= 22 ? 0 : 1)' >/dev/null 2>&1; then
    printf '%s\n' "$candidate"
    exit 0
  fi
done
exit 1
