@echo on

rem Eliminar tarea
taskkill /F /IM on_bot.bat

rem Desactivar el ambiente virtual
call .\venv\Scripts\deactivate.bat