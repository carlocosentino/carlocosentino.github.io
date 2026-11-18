#!/usr/bin/env bash
# Instala o Hugo Extended na versão de hugoblox.yaml e as dependências npm.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

HUGO_VERSION="$(python3 - <<'PY'
import re
from pathlib import Path

text = Path("hugoblox.yaml").read_text()
match = re.search(r"hugo_version:\s*['\"]?([0-9]+\.[0-9]+\.[0-9]+)", text)
if not match:
    raise SystemExit("hugo_version ausente em hugoblox.yaml")
print(match.group(1))
PY
)"

install_hugo() {
  local archive
  archive="$(mktemp)"
  curl -fsSL \
    "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz" \
    -o "$archive"
  sudo tar -xzf "$archive" -C /usr/local/bin hugo
  sudo chmod 755 /usr/local/bin/hugo
  rm -f "$archive"
}

current=""
if command -v hugo >/dev/null 2>&1; then
  current="$(hugo version 2>/dev/null || true)"
fi

if [[ "$current" != *"v${HUGO_VERSION}"* || "$current" != *"extended"* ]]; then
  install_hugo
fi

npm ci
# Baixa os módulos do tema sem alterar go.mod.
hugo mod graph >/dev/null
hugo version
