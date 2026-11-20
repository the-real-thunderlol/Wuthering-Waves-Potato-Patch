REM python -m nuitka --onefile --enable-plugin=tk-inter --windows-console-mode=disable --windows-icon-from-ico=ico/app.ico --output-filename=wuwa-potato-patch-v1.0.exe main.py
python -m PyInstaller --windowed --contents-directory=lib --icon=ico/app.ico --name=wuwa-potato-patch-v1.0 main.py
