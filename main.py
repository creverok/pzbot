# Всяка хуйня, імпорти
from discord import app_commands
from discord.ext import commands
import discord
from keep_alive import keep_alive
keep_alive()


my_secret = 'MTIyODMyMTc2MTEwMDE3MzM0Mg.GqGdg2.lIGI3dINGmQg7tWMvigP60IRX1b6VsLTRi_sXk'

intents = discord.Intents.all()
client = commands.Bot(command_prefix='/', intents=intents)

# Запуск бота


@client.event
async def on_ready():
    print(f'Ви залогінились, як {client.user}')
    await client.tree.sync()

# токен
client.run(my_secret)