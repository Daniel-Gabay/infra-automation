#!/usr/bin/env bash

# בדיקה אם pydantic כבר מותקן בפייתון
python -c "import pydantic" >/dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "pydantic already installed, skipping."
    exit 0
fi

echo "pydantic not found, installing..."

pip install pydantic
# או pip3 install pydantic אם זה מה שאתה משתמש בו

echo "pydantic installed successfully"
