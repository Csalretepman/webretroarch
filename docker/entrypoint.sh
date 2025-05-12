#!/bin/bash
set -e

# Генерация nes.html перед стартом nginx
python3 /generate-nes-html.py

# Запуск nginx
nginx -g "daemon off;"
