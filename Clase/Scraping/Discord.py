
import asyncio
import discord
import PrimerObjetivo

# Obtener el valor del token de acceso
TOKEN = 'MTE2ODk0Njc0NjA1NTk4MzEyNA.G39xzZ.F5Ki61ijivkF_fWdt2McyKsJzR94EeuOTHaLlE'
GUILD = '1169654918639001761'
CHANNEL = 1169668971532922950
async def esperar_segundos():
    while True:
        await asyncio.sleep(3)  # Espera 3 segundos


def ejecutar():



    # Definir los intents que necesita tu bot
    intents = discord.Intents.default()
    intents.typing = False  # Puedes ajustar estos según las necesidades de tu bot
    intents.presences = False

    client = discord.Client(intents=intents)


    @client.event
    async def on_ready():
        for guild in client.guilds:
            if guild.name == GUILD:
                break

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

        # Obtener el canal en el que deseas enviar el mensaje
        channel = client.get_channel(CHANNEL)

        if channel:

            peliculas=PrimerObjetivo.ejecutar('1')
            if len(peliculas) > 2000:
                peliculas = peliculas[:1800]  # Recorta la cadena a los primeros 2000 caracteres

            message = peliculas
            await channel.send("Buenos dias, aqui tienes el listado diario de peliculas ordenado por puntuacion:\n\n"+message)


    client.run(TOKEN)