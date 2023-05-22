@echo off

rem Activar el ambiente
call .\venv\Scripts\activate.bat

rem Ejecutamos el ejecutable
start /B /C python main.py

