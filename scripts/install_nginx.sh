#!/usr/bin/env bash

# לצאת אם יש שגיאה
set -e

echo "=== Updating package list (apt update) ==="
sudo apt update -y

echo "=== Installing nginx ==="
sudo apt install -y nginx

echo "=== Checking nginx version ==="
nginx -v

echo "=== nginx installed successfully ==="
