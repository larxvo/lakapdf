@echo off
cd /d "%~dp0"
py -3.12 -m pip install -r requirements-build.txt || exit /b 1
py -3.12 -m unittest discover -s tests -v || exit /b 1
py -3.12 -m PyInstaller --clean LakaPDF.spec || exit /b 1
"%ProgramFiles(x86)%\Inno Setup 6\ISCC.exe" installer\LakaPDF.iss || exit /b 1
