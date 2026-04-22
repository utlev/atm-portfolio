#!/usr/bin/env bash
# Quick setup for the ATM portfolio repo.
# Usage:  bash setup.sh

set -euo pipefail

echo "▸ Initialising git repository (if not already)…"
if [ ! -d .git ]; then
  git init -b main
fi

echo "▸ Creating virtual environment with uv (falls back to venv)…"
if command -v uv >/dev/null 2>&1; then
  uv venv
  # shellcheck disable=SC1091
  source .venv/bin/activate
  uv pip install -e ".[dev]"
else
  python3 -m venv .venv
  # shellcheck disable=SC1091
  source .venv/bin/activate
  pip install --upgrade pip
  pip install -e ".[dev]"
fi

echo "▸ Installing pre-commit hooks…"
pre-commit install || echo "  (pre-commit not installed yet — run again after first install)"

echo
echo "✓ Done."
echo "  Next steps:"
echo "    1. source .venv/bin/activate"
echo "    2. Create an OpenSky account at https://opensky-network.org/"
echo "    3. Configure traffic credentials — see https://traffic-viz.github.io/installation.html"
echo "    4. jupyter lab"
