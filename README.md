# BOT EDELPA - DISCORD
<i> Eli-ezer Reuven Ramirez Ruiz - ( 19/03/2023 | 26/05/2023 )</i>

<br>

### Introducción
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


### LIBRERIAS
[Discord.py](https://discordpy.readthedocs.io/en/stable/) -> Documentación oficial y Soporte del Bot <br>
[Aioodbc](https://github.com/aio-libs/aioodbc/) -> Documentación oficial y Soporte conector a la base de datos SQLSERVER <br>
[Python-dotenv](https://pypi.org/project/python-dotenv/) -> Documentación oficial y Soporte para variables de entorno <br>
[Quart](https://pgjones.gitlab.io/quart/) -> Documentación oficial y Soporte para servidor web (inspirado en Flask)<br>
### TUTORIALES O DISCUSIONES
[Servidor-corriendo](https://sites.google.com/view/the-home-of-m692/resources/discord-py-bot-hosting/new) -> Tutorial de servidor de bot para que este siempre prendido <br>


<br>

### COMANDOS DISPONIBLES
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

### LIBRERIAS UTILIZADAS
Instalar dependencias
```python
    pip install -r requirements.txt
```