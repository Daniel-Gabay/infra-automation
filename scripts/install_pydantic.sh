#!/bin/bash

# Check if pydantic is installed
if ! pip show pydantic &> /dev/null; then

    echo "pydantic is not installed. Installing now..."

    pip install pydantic

else
    echo "pydantic is already installed."
fi
