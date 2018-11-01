:: Check for Python Installation
python --version 2>NUL
if errorlevel 1 goto errorNoPython
SET PYTHONPATH=%~dp0\src
python %~dp0\src\editor\pathfinder_editor.py

goto:eof

:errorNoPython
echo.
echo Error^: Python not installed
