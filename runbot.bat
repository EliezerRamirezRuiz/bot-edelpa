@echo on

rem Activar el ambiente
call .\venv\Scripts\activate

rem Ejecutamos el ejecutable
start "Bot corriendo" /wait /B python main.py

