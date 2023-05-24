# DISCORD BOT - EDELPA
<i> Eli-ezer Reuven Ramirez Ruiz - 19/03/2023 </i>

<br>

## Introducción
```txt
El bot surge ante una necesidad de la empresa en automatizar los procesos como:
--> a) Automatizar la consulta de stock.
--> b) Obtener las alertas.
--> c) Verificar el estado del robot.
--> d) Guardar datos en una base de datos.

Enlace del bot para que se pueda unir al servidor:
--> https://discord.com/api/oauth2/authorize?client_id=1087791201639485520&permissions=8&scope=bot%20applications.commands
```

<br>

## DOCUMENTACION DE LIBRERIAS UTILIZADAS
```txt
Aqui se dejara link e informacion de las librerias utilizadas:
```
### LIBRERIAS
[Discord.py](https://discordpy.readthedocs.io/en/stable/) -> Documentación oficial y Soporte del Bot <br>
[Aioodbc](https://github.com/aio-libs/aioodbc/) -> Documentación oficial y Soporte conector a la base de datos SQLSERVER <br>
[Python-dotenv](https://pypi.org/project/python-dotenv/) -> Documentación oficial y Soporte para variables de entorno <br>
[Flask](https://flask.palletsprojects.com/en/2.3.x/) -> Documentación oficial y Soporte para SERVIDOR WEB <br>
### TUTORIALES O DISCUSIONES
[Servidor-corriendo](https://sites.google.com/view/the-home-of-m692/resources/discord-py-bot-hosting/new) -> Tutorial de servidor de bot para que este siempre prendido
[Discución de github syncronizar](https://gist.github.com/Rapptz/c4324f17a80c94776832430007ad40e6#syncing)
https://hdsplus.co/ejecutar-un-script-en-segundo-plano-con-tmux/

<br>

## COMANDOS DISPONIBLES
```txt
COMANDOS (Prefijo de invocación ["!"])
1) !menu (Opciones)
2) !consultar_stock (parametro: codigo[int])
3) !estado_robot (sin parametros)(pendiente)
4) !alertas_activas (sin parametros)
5) !alertas_desactivadas (sin parametros)
6) !sincronizar (Recarga las extensiones)
7) !help

OPCIONES MENU (Comando de invocación ["!menu" | "/menu"])
1) Default  <br>
2) Consultar stock  <br>
3) Estado robot <br>
4) Ultimas alertas activas <br>
5) Ultimas alertas desactivadas <br>
6) Reporte del dia <br>

COMANDOS SLASH (Prefijo de invocación ["/"])
1) /menu <br>
2) /consultar_stock (parametro: codigo[int]) <br>
3) /ultimas_alertas_activas <br>
4) /ultimas_alertas_desactivadas <br>
5) /estado_robot
```

<br>

## LIBRERIAS UTILIZADAS
```requirements.txt
aiohttp==3.8.4
aioodbc==0.4.0
aiosignal==1.3.1
async-timeout==4.0.2
attrs==22.2.0
autopep8==2.0.2
beautifulsoup4==4.12.0
blinker==1.6.2
certifi==2022.12.7
charset-normalizer==3.1.0
click==8.1.3
colorama==0.4.6
discord-py-slash-command==4.2.1
discord.py==2.2.3
Flask==2.3.2
frozenlist==1.3.3
idna==3.4
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.2
MouseInfo==0.1.3
multidict==6.0.4
Pillow==9.4.0
PyAutoGUI==0.9.53
pycodestyle==2.10.0
PyGetWindow==0.0.9
PyMsgBox==1.0.9
pyodbc==4.0.35
pyperclip==1.8.2
PyRect==0.2.0
PyScreeze==0.1.28
python-dotenv==1.0.0
pytweening==1.0.4
requests==2.28.2
soupsieve==2.4
urllib3==1.26.15
Werkzeug==2.3.4
wikipedia==1.4.0
yarl==1.8.2
```

```py

pyinstaller -F -p "C:\Users\eramirezr\OneDrive - Envases del Pacifico S.A\Escritorio\Bot;/bot_discord/src" -p "C:\Users\eramirezr\OneDrive - Envases del Pacifico S.A\Escritorio\Bot;/bot_discord/src/app" -p "C:\Users\eramirezr\OneDrive - Envases del Pacifico S.A\Escritorio\Bot;/bot_discord/src/ayuda" -p "C:\Users\eramirezr\OneDrive - Envases del Pacifico S.A\Escritorio\Bot;/bot_discord/src/comandos" -p "C:\Users\eramirezr\OneDrive - Envases del Pacifico S.A\Escritorio\Bot;/bot_discord/src/componentes" -p "C:\Users\eramirezr\OneDrive - Envases del Pacifico S.A\Escritorio\Bot;/bot_discord/src/config" -p "C:\Users\eramirezr\OneDrive - Envases del Pacifico S.A\Escritorio\Bot;/bot_discord/src/database" -p "C:\Users\eramirezr\OneDrive - Envases del Pacifico S.A\Escritorio\Bot;/bot_discord/src/eventos" -p "C:\Users\eramirezr\OneDrive - Envases del Pacifico S.A\Escritorio\Bot;/bot_discord/src/logger" -p "C:\Users\eramirezr\OneDrive - Envases del Pacifico S.A\Escritorio\Bot;/bot_discord/src/server" -p "C:\Users\eramirezr\OneDrive - Envases del Pacifico S.A\Escritorio\Bot;/bot_discord/src/slash_comandos" -p "C:\Users\eramirezr\OneDrive - Envases del Pacifico S.A\Escritorio\Bot;/bot_discord/src/utils" main.py

```