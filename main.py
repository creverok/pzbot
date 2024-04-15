# Всяка хуйня, імпорти
from discord import app_commands
from discord.ext import commands
import git
import os
import discord
import crv
from keep_alive import keep_alive
keep_alive()


my_secret = 'MTIyODMyMTc2MTEwMDE3MzM0Mg.GqGdg2.lIGI3dINGmQg7tWMvigP60IRX1b6VsLTRi_sXk'

intents = discord.Intents.all()
client = commands.Bot(command_prefix='/', intents=intents)

# Запуск бота

def gitpush():
    repo = git.Repo(os.getcwd())
    repo.index.add("*")
    repo.index.commit("Update db")
    origin = repo.remotes.origin
    origin.push()

@client.event
async def on_ready():
    crv.create_table()
    print(f'Ви залогінились, як {client.user}')
    await client.tree.sync()

@client.tree.command(name='додати_книгу',
                     description='Додає книгу до нашої бібліотеки')
@app_commands.choices(книга=[
    app_commands.Choice(name="Автомеханіка/Автомеханика", value="Автомеханіка/Автомеханика"),
    app_commands.Choice(name="Будівництво/Строительство", value="Будівництво/Строительство"),
   app_commands.Choice(name="Газосварка/Металлообработка", value="Газосварка/Металлообработка"),
    app_commands.Choice(name="Електроніка/Електроника", value="Електроніка/Електроника"),
    app_commands.Choice(name="Збиральництво/Собирательство", value="Збиральництво/Собирательство"),
    app_commands.Choice(name="Звіроловство/Звероловство", value="Звіроловство/Звероловство"),
    app_commands.Choice(name="Кулінарія/Кулинария", value="Кулінарія/Кулинария"),
    app_commands.Choice(name="Перша допомога/Первая помощь", value="Перша допомога/Первая помощь"),
    app_commands.Choice(name="Рибальство/Рыболовство", value="Рибальство/Рыболовство"),
    app_commands.Choice(name="Фермерство", value="Фермерство"),
    app_commands.Choice(name="Шиття/Шитьё", value="Шиття/Шитьё")
]) 
@app_commands.choices(том=[
    app_commands.Choice(name="1", value="Том 1"),
    app_commands.Choice(name="2", value="Том 2"),
    app_commands.Choice(name="3", value="Том 3"),
    app_commands.Choice(name="4", value="Том 4"),
    app_commands.Choice(name="5", value="Том 5")
])
async def додати_книгу(Interaction: discord.Interaction, книга: app_commands.Choice[str], том:app_commands.Choice[str]):
    книга1=f"{книга.name} {том.value}"
    print(книга1)
    s=crv.add_book(книга1)
    gitpush()
    embed = discord.Embed(title="Бібліотека PZ",
                          description="",
                          colour=discord.Colour.dark_blue())
    embed.add_field(name=f"{s}", value='')
    await Interaction.response.send_message(embed=embed)



@client.tree.command(name='видалити_книгу', description='Видаляє книгу з нашої бібліотеки')
async def видалити_книгу(Interaction: discord.Interaction, книга: str):
    s=crv.remove_book(книга)
    gitpush()
    embed = discord.Embed(title="Бібліотека PZ",
                          description="",
                          colour=discord.Colour.dark_blue())
    embed.add_field(name=f"{s}", value='')
    await Interaction.response.send_message(embed=embed)

@client.tree.command(name='показати_всі_книги', description="Демонструє всі книги нашої бібліотеки")
async def показати_всі_книги(Interaction: discord.Interaction):
    s=crv.show_all_books()
    embed=discord.Embed(title="Бібліотека PZ", description="", colour=discord.Colour.dark_blue())
    embed.add_field(name=f"{s}", value='')
    await Interaction.response.send_message(embed=embed)

# токен
client.run(my_secret)