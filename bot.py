import discord

# НАСТРОЙКА INTENTS — ЭТА ЧАСТЬ У ВАС ПРАВИЛЬНАЯ
intents = discord.Intents.default()
intents.message_content = True  # Читаем содержимое сообщений

client = discord.Client(intents=intents)

reply_text = """<:love4you:1487554540545773608>
[https://discord.com/channels/1484523161935544471/1487097535217799249/1487105935271923874]"""

keywords = ["release", "demo", "playtest", "price", "when"]

@client.event
async def on_ready():
    print(f"✅ Бот {client.user} запущен!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot:
        return
    
    content = message.content.lower()
    
    if any(word in content for word in keywords):
        await message.channel.send(reply_text)
        print(f"📨 Ответ отправлен!")

TOKEN = "MTQ5MzI2ODUzODQzNjIyNzExMg.GgG8or.fyReoGWVnUmyTmE7ulwy8q_CYNyn9NQQvi_e_s"

client.run("MTQ5MzI2ODUzODQzNjIyNzExMg.GgG8or.fyReoGWVnUmyTmE7ulwy8q_CYNyn9NQQvi_e_s")