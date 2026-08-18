#!/usr/bin/env bash
set -Eeuo pipefail

# Ontolith Codespaces bootstrap
# Usage:
#   bash bootstrap-codespace.sh /workspaces/enterprise-ontology-graph-full.zip
#   START_DEV=0 bash bootstrap-codespace.sh /workspaces/enterprise-ontology-graph-full.zip

ARCHIVE_PATH="${1:-enterprise-ontology-graph-full.zip}"
TARGET_DIR="${2:-$PWD/enterprise-ontology-graph}"
START_DEV="${START_DEV:-1}"

if [[ ! -f "$ARCHIVE_PATH" ]]; then
  echo "Archive not found: $ARCHIVE_PATH" >&2
  echo "Upload the project ZIP to Codespaces, then pass its path as the first argument." >&2
  exit 1
fi

if [[ -e "$TARGET_DIR" ]] && [[ -n "$(find "$TARGET_DIR" -mindepth 1 -maxdepth 1 -print -quit 2>/dev/null)" ]]; then
  echo "Target directory is not empty: $TARGET_DIR" >&2
  echo "Choose another target directory or remove the existing directory first." >&2
  exit 1
fi

command -v unzip >/dev/null 2>&1 || { echo "unzip is required in the Codespace image." >&2; exit 1; }
command -v node >/dev/null 2>&1 || { echo "Node.js is required in the Codespace image." >&2; exit 1; }

WORK_DIR="$(mktemp -d)"
cleanup() { rm -rf "$WORK_DIR"; }
trap cleanup EXIT

printf '%s\n' "Checking archive integrity..."
unzip -t "$ARCHIVE_PATH" >/dev/null

printf '%s\n' "Extracting project..."
unzip -q "$ARCHIVE_PATH" -d "$WORK_DIR"

SOURCE_DIR=""
if [[ -d "$WORK_DIR/enterprise-ontology-graph" ]]; then
  SOURCE_DIR="$WORK_DIR/enterprise-ontology-graph"
else
  SOURCE_DIR="$(find "$WORK_DIR" -mindepth 1 -maxdepth 1 -type d -print -quit)"
fi

if [[ -z "$SOURCE_DIR" || ! -f "$SOURCE_DIR/package.json" ]]; then
  echo "Could not find a project directory containing package.json in the archive." >&2
  exit 1
fi

mkdir -p "$TARGET_DIR"
cp -a "$SOURCE_DIR"/. "$TARGET_DIR"/
cd "$TARGET_DIR"

if ! command -v pnpm >/dev/null 2>&1; then
  echo "pnpm was not found; enabling it through Corepack..."
  if command -v corepack >/dev/null 2>&1; then
    corepack enable
    corepack prepare pnpm@10.4.1 --activate
  else
    npm install --global pnpm@10.4.1
  fi
fi

printf '%s\n' "Installing dependencies..."
pnpm install

printf '%s\n' "Running TypeScript checks..."
pnpm check

printf '%s\n' "Running tests..."
pnpm test

printf '%s\n' "Project setup completed successfully."
printf '%s\n' "Project directory: $TARGET_DIR"
printf '%s\n' "Start manually with: pnpm dev"

if [[ "$START_DEV" == "1" ]]; then
  exec pnpm dev
fi
