#!/bin/bash
# Setup script for wechat-article-reader skill
set -e

SKILL_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Setting up wechat-article-reader in: $SKILL_DIR"

# Create virtualenv
python3 -m venv "$SKILL_DIR/.venv"

# Install dependencies
"$SKILL_DIR/.venv/bin/pip" install -q -r "$SKILL_DIR/requirements.txt"

echo "Done. You can now use the skill in Claude Code."
