import discord
from keep_alive import keep_alive
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

reply_text = """:love4you:
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
        await message.reply(reply_text)

keep_alive()

TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)
