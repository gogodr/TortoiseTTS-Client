if [[ "$OSTYPE" == "msys" ]]; then
    .venv/Scripts/python.exe index.py
else
    .venv/bin/python index.py
fi