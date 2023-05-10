# Bot Edelpa
<i>Eli-ezer Reuven Ramirez Ruiz - 19/03/2023</i>


## Problema dentro de la empresa

"La empresa Edelpa ha solicitado la creacion de un bot para poder mantener en comunicacion <br>
a la empresa de los estado, posibles fallo que presente el robot. Tambien se espera que el <br>
Bot pueda cumplir con otros requerimientos tales como que se conecte a una Base de datos de <br>
SQL Server y pueda consultar stocks y alertas, gracias a eso poder generar respuestas y <br>
notificaciones de forma autonoma."

<br>

## Actualizaciones

"El Bot estaba pensado para realizarse como un bot de whatsapp pero 
<br>debido a las limitantes, se ha replanteado para realizarse en otra 
<br>plataforma digital de comunicacion y la cual se ha llegado a un concenso 
<br>es Discord que nos proporciona <i>[Discord Developer Portal](https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications)</i>"

<br>

## Tecnologias utilizadas

Las librerias utilizadas en este proyecto fueron:
- [Discord.py](https://discordpy.readthedocs.io/en/stable/)
- [Aiohttp](https://docs.aiohttp.org/en/stable/)
- [Aioodbc](https://github.com/aio-libs/aioodbc/)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)

<br>

Links de referencia
https://support.discord.com/hc/es/articles/4644915651095-Permisos-para-comandos
https://discordpy.readthedocs.io/en/stable/ext/commands/extensions.html#reloading
https://www.youtube.com/watch?v=9zl0FT30jvo
https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html?highlight=bot%20get_cog

COMANDOS
- !menu
- !consultar_stock
- !estado_robot
- !alertas_activas
- !alertas_desactivadas

MENU
- Consultar stock
- Estado robot
- Ultimas alertas activas
- Reporte del dia

SLASH
- /menu
- /consultar_stock
