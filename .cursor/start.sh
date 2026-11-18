#!/usr/bin/env bash
# Sobe o servidor de desenvolvimento do site. Seguro para rodar de novo.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if curl -fsS -o /dev/null --max-time 2 http://127.0.0.1:1313/; then
  echo "Hugo já responde em http://127.0.0.1:1313"
  exit 0
fi

exec hugo server --bind 0.0.0.0 --port 1313 --baseURL http://127.0.0.1:1313/
