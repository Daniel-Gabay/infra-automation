#!/usr/bin/env bash

if command -v nginx >/dev/null 2>&1; then
    echo "nginx already installed"
    exit 0


fi

echo "nginx not found, installing."

sudo yum update -y
sudo yum install nginx -y

sudo systemctl enable nginx
sudo systemctl start nginx

echo "nginx installed successfully"