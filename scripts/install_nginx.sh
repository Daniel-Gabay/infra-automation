#!/bin/bash

# Check if nginx is installed
if ! command -v nginx &> /dev/null; then

    echo "nginx is not installed. Installing..."

    sudo apt update && sudo apt install -y nginx

else

    echo "nginx is already installed."
fi