git submodule update --init --recursive
python -m venv .venv
if [[ "$OSTYPE" == "msys" ]]; then
    . .venv/Scripts/activate
else
    . .venv/bin/activate
fi
export DS_BUILD_AIO=0
export DS_BUILD_SPARSE_ATTN=0
export DS_BUILD_OPS=0
pip install -r requirements_cuda.txt
pip install -r requirements.txt
cd tts
python setup.py install
cd ..
