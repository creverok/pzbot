# Всяка хуйня, імпорти
from discord import app_commands
from discord.ext import commands
import discord
import crv
from keep_alive import keep_alive
keep_alive()


my_secret = 'MTIyODMyMTc2MTEwMDE3MzM0Mg.GqGdg2.lIGI3dINGmQg7tWMvigP60IRX1b6VsLTRi_sXk'

intents = discord.Intents.all()
client = commands.Bot(command_prefix='/', intents=intents)

# Запуск бота


@client.event
async def on_ready():
    crv.create_table()
    print(f'Ви залогінились, як {client.user}')
    await client.tree.sync()

@client.tree.command(name='додати_книгу',
                     description='Додає книгу до нашої бібліотеки')
@app_commands.choices(книга=[
    app_commands.Choice(name="Будівництво/Строительство Том 1", value="Будівництво/Строительство Том 1"),
    app_commands.Choice(name="Будівництво/Строительство Том 2", value="Будівництво/Строительство Том 2"),
    app_commands.Choice(name="Будівництво/Строительство Том 3", value="Будівництво/Строительство Том 3"),
    app_commands.Choice(name="Будівництво/Строительство Том 4", value="Будівництво/Строительство Том 4"),
    app_commands.Choice(name="Будівництво/Строительство Том 5", value="Будівництво/Строительство Том 5"),

    app_commands.Choice(name="Кулінарія/Кулинария Том 1", value="Кулінарія/Кулинария Том 1"),
    app_commands.Choice(name="Кулінарія/Кулинария Том 2", value="Кулінарія/Кулинария Том 2"),
    app_commands.Choice(name="Кулінарія/Кулинария Том 3", value="Кулінарія/Кулинария Том 3"),
    app_commands.Choice(name="Кулінарія/Кулинария Том 4", value="Кулінарія/Кулинария Том 4"),
    app_commands.Choice(name="Кулінарія/Кулинария Том 5", value="Кулінарія/Кулинария Том 5"),

    app_commands.Choice(name="Електроніка/Електроника Том 1", value="Електроніка/Електроника Том 1"),
    app_commands.Choice(name="Електроніка/Електроника Том 2", value="Електроніка/Електроника Том 2"),
    app_commands.Choice(name="Електроніка/Електроника Том 3", value="Електроніка/Електроника Том 3"),
    app_commands.Choice(name="Електроніка/Електроника Том 4", value="Електроніка/Електроника Том 4"),
    app_commands.Choice(name="Електроніка/Електроника Том 5", value="Електроніка/Електроника Том 5"),

    app_commands.Choice(name="Фермерство Том 1", value="Фермерство Том 1"),
    app_commands.Choice(name="Фермерство Том 2", value="Фермерство Том 2"),
    app_commands.Choice(name="Фермерство Том 3", value="Фермерство Том 3"),
    app_commands.Choice(name="Фермерство Том 4", value="Фермерство Том 4"),
    app_commands.Choice(name="Фермерство Том 5", value="Фермерство Том 5"),

    app_commands.Choice(name="Перша допомога/Первая помощь Том 1", value="Перша допомога/Первая помощь Том 1"),
    app_commands.Choice(name="Перша допомога/Первая помощь Том 2", value="Перша допомога/Первая помощь Том 2"),
    app_commands.Choice(name="Перша допомога/Первая помощь Том 3", value="Перша допомога/Первая помощь Том 3"),
    app_commands.Choice(name="Перша допомога/Первая помощь Том 4", value="Перша допомога/Первая помощь Том 4"),
    app_commands.Choice(name="Перша допомога/Первая помощь Том 5", value="Перша допомога/Первая помощь Том 5"),
])
async def додати_книгу(Interaction: discord.Interaction, книга: app_commands.Choice[str]):
    книга1=книга.name
    print(книга1)
    s=crv.add_book(книга1)
    embed = discord.Embed(title="Бібліотека PZ",
                          description="",
                          colour=discord.Colour.dark_blue())
    embed.add_field(name=f"{s}", value='')
    await Interaction.response.send_message(embed=embed)


@client.tree.command(name='додати_книгу_2',
                     description='Додає книгу до нашої бібліотеки')
@app_commands.choices(книга=[
    app_commands.Choice(name="Рибальство/Рыболовство Том 1", value="Рибальство/Рыболовство Том 1"),
    app_commands.Choice(name="Рибальство/Рыболовство Том 2", value="Рибальство/Рыболовство Том 2"),
    app_commands.Choice(name="Рибальство/Рыболовство Том 3", value="Рибальство/Рыболовство Том 3"),
    app_commands.Choice(name="Рибальство/Рыболовство Том 4", value="Рибальство/Рыболовство Том 4"),
    app_commands.Choice(name="Рибальство/Рыболовство Том 5", value="Рибальство/Рыболовство Том 5"),

    app_commands.Choice(name="Збиральництво/Собирательство Том 1", value="Збиральництво/Собирательство Том 1"),
    app_commands.Choice(name="Збиральництво/Собирательство Том 2", value="Збиральництво/Собирательство Том 2"),
    app_commands.Choice(name="Збиральництво/Собирательство Том 3", value="Збиральництво/Собирательство Том 3"),
    app_commands.Choice(name="Збиральництво/Собирательство Том 4", value="Збиральництво/Собирательство Том 4"),
    app_commands.Choice(name="Збиральництво/Собирательство Том 5", value="Збиральництво/Собирательство Том 5"),

    app_commands.Choice(name="Автомеханіка/Автомеханика Том 1", value="Автомеханіка/Автомеханика Том 1"),
    app_commands.Choice(name="Автомеханіка/Автомеханика Том 2", value="Автомеханіка/Автомеханика Том 2"),
    app_commands.Choice(name="Автомеханіка/Автомеханика Том 3", value="Автомеханіка/Автомеханика Том 3"),
    app_commands.Choice(name="Автомеханіка/Автомеханика Том 4", value="Автомеханіка/Автомеханика Том 4"),
    app_commands.Choice(name="Автомеханіка/Автомеханика Том 5", value="Автомеханіка/Автомеханика Том 5"),

    app_commands.Choice(name="Газосварка/Металлообработка Том 1", value="Газосварка/Металлообработка Том 1"),
    app_commands.Choice(name="Газосварка/Металлообработка Том 2", value="Газосварка/Металлообработка Том 2"),
    app_commands.Choice(name="Газосварка/Металлообработка Том 3", value="Газосварка/Металлообработка Том 3"),
    app_commands.Choice(name="Газосварка/Металлообработка Том 4", value="Газосварка/Металлообработка Том 4"),
    app_commands.Choice(name="Газосварка/Металлообработка Том 5", value="Газосварка/Металлообработка Том 5"),

    app_commands.Choice(name="Шиття/Шитьё Том 1", value="Шиття/Шитьё Том 1"),
    app_commands.Choice(name="Шиття/Шитьё Том 2", value="Шиття/Шитьё Том 2"),
    app_commands.Choice(name="Шиття/Шитьё Том 3", value="Шиття/Шитьё Том 3"),
    app_commands.Choice(name="Шиття/Шитьё Том 4", value="Шиття/Шитьё Том 4"),
    app_commands.Choice(name="Шиття/Шитьё Том 5", value="Шиття/Шитьё Том 5"),
])
async def додати_книгу_2(Interaction: discord.Interaction, книга: app_commands.Choice[str]):
    книга1=книга.name
    print(книга1)
    s=crv.add_book(книга1)
    embed = discord.Embed(title="Бібліотека PZ",
                          description="",
                          colour=discord.Colour.dark_blue())
    embed.add_field(name=f"{s}", value='')
    await Interaction.response.send_message(embed=embed)


@client.tree.command(name='додати_книгу_3',
                     description='Додає книгу до нашої бібліотеки')
@app_commands.choices(книга=[
    app_commands.Choice(name="Звіроловство/Звероловство Том 1", value="Звіроловство/Звероловство Том 1"),
    app_commands.Choice(name="Звіроловство/Звероловство Том 2", value="Звіроловство/Звероловство Том 2"),
    app_commands.Choice(name="Звіроловство/Звероловство Том 3", value="Звіроловство/Звероловство Том 3"),
    app_commands.Choice(name="Звіроловство/Звероловство Том 4", value="Звіроловство/Звероловство Том 4"),
    app_commands.Choice(name="Звіроловство/Звероловство Том 5", value="Звіроловство/Звероловство Том 5"),
])
async def додати_книгу_3(Interaction: discord.Interaction, книга: app_commands.Choice[str]):
    книга1=книга.name
    print(книга1)
    s=crv.add_book(книга1)
    embed = discord.Embed(title="Бібліотека PZ",
                          description="",
                          colour=discord.Colour.dark_blue())
    embed.add_field(name=f"{s}", value='')
    await Interaction.response.send_message(embed=embed)




@client.tree.command(name='видалити_книгу',
                     description='Видаляє книгу з нашої бібліотеки')
async def видалити_книгу(Interaction: discord.Interaction, книга: str):
    s=crv.remove_book(книга)
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