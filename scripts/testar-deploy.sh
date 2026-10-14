#!/usr/bin/env bash

set -Eeuo pipefail

cd "$(dirname "$0")/.."

echo "======================================"
echo " TESTES DE IMPLANTACAO - PROJETO RONALDO"
echo "======================================"

echo
echo "[1/5] Executando testes automatizados..."
./env/bin/python -m pytest

echo
echo "[2/5] Verificando configuracao do Django..."
./env/bin/python src/manage.py check

echo
echo "[3/5] Verificando migracoes pendentes..."
docker compose exec -T web python manage.py migrate --check

echo
echo "[4/5] Verificando se o container esta em execucao..."
docker compose ps --status running --services | grep -qx web
echo "Container web em execucao."

echo
echo "[5/5] Testando resposta HTTP..."
resposta=$(curl --silent --show-error --fail http://localhost:8000/)

if [[ "$resposta" != "Projeto Ronaldo" ]]; then
    echo "ERRO: resposta HTTP inesperada: $resposta"
    exit 1
fi

echo "Resposta HTTP correta: $resposta"

echo
echo "======================================"
echo " TODOS OS TESTES PASSARAM!"
echo "======================================"
