@echo off
if not "%1"=="STDOUT_TO_FILE"  %0 STDOUT_TO_FILE %*  >log.txt 2>&1
shift /1

if not exist "tortoise-tts-client" (
    mkdir tortoise-tts-client
)
cd tortoise-tts-client
cls
if not exist "TortoiseTTS-Client" (
    if not exist "git/bin/git.exe" (
        if not exist "7z.exe" (
            echo Downloading 7zip
            powershell -c "Invoke-WebRequest -OutFile 7z.exe -Uri https://www.7-zip.org/a/7zr.exe"
        )
        cls
        if not exist "git.zip" (
            cls
            echo Downloading Git
            powershell -c "Invoke-WebRequest -OutFile git.zip -Uri https://github.com/git-for-windows/git/releases/download/v2.41.0.windows.3/PortableGit-2.41.0.3-64-bit.7z.exe"
            cls
        )
        echo Extracting Git
        7z.exe x git.zip -ogit
    )
    cls
    echo Download TortoiseTTS-Client
    .\git\bin\git.exe clone --recursive https://github.com/gogodr/TortoiseTTS-Client.git
)
cls
if not exist ".venv" (    
    echo Extracting Python Virtual Environment
    python -m venv .venv
)
echo Install Python Cuda requirements
.\.venv\Scripts\pip.exe install -r TortoiseTTS-Client\requirements_cuda.txt
cls
echo Install Python requirements
.\.venv\Scripts\pip.exe install -r TortoiseTTS-Client\requirements.txt
echo Install Tortoise TTS
cd TortoiseTTS-Client\tts
..\..\.venv\Scripts\python.exe .\setup.py install
cd ..
cd ..
cls
echo Install Pyinstaller
.\.venv\Scripts\pip.exe install pyinstaller
cls
.\.venv\Scripts\pyinstaller.exe TortoiseTTS-Client\TortoiseTTSClientDebug.spec