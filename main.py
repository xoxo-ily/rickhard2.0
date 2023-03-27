import json
import discord
from messageProccessing import *

# import sqlite3
# con = sqlite3.connect("users.db")
# cur = con.cursor()

with open("secrets.json", "r") as f:
    info = json.load(f)

token = info["token"]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user}")

@client.event
async def on_message(message: discord.message.Message):
    # print(message.author)
    if message.author == client.user:
        return
    
    print(message.content)
    first = message.content.split()[0]
    if (first == "!close"):
        await client.close()

    await boredCounter(message)
    await userStats(message)
    await getBored(message)
    await eightball(message)
    await nlpAlgorithm(message)
    # await (message.channel.send(content = f"```User: {str(message.author)} \nID: {str(message.author.id)}```", tts = True))
    
client.run(token)
    
