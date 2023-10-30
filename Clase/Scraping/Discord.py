import discord
from discord.ext import commands

TOKEN = 'tu_token_de_discord'
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

@bot.command()
async def ejecutar(ctx, *, codigo: str):
    try:
        resultado = exec(codigo)
        await ctx.send(f'Resultado: {resultado}')
    except Exception as e:
        await ctx.send(f'Error: {e}')

bot.run(TOKEN)
