git submodule update --init --recursive
python -m venv .venv
if [[ "$OSTYPE" == "msys" ]]; then
    . .venv/Scripts/activate
else
    . .venv/bin/activate
fi
pip install -r requirements_cuda.txt
pip install -r requirements.txt
cd tts
python setup.py install
cd ..
