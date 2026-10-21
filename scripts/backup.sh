#!/bin/sh
set -eu

PROJECT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
DB="$PROJECT_DIR/src/nome.sqlite3"
BACKUP_DIR="$PROJECT_DIR/backups"
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"
DEST="$BACKUP_DIR/nome_$TIMESTAMP.sqlite3"

if [ ! -f "$DB" ]; then
    echo "Erro: banco SQLite não encontrado: $DB" >&2
    exit 1
fi

mkdir -p "$BACKUP_DIR"
chmod 700 "$BACKUP_DIR"

sqlite3 "$DB" ".backup '$DEST'"
chmod 600 "$DEST"

if sqlite3 "$DEST" "PRAGMA integrity_check;" | grep -qx 'ok'; then
    echo "Backup concluído: $DEST"
else
    echo "Erro: integridade do backup não confirmada." >&2
    exit 1
fi
