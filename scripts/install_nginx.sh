#!/usr/bin/env bash
set -e

apt update -y
apt install -y nginx

nginx -v
echo "nginx installed successfully"
