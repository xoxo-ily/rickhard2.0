import discord
import sqlite3
import random

con = sqlite3.connect("users.db")
cur = con.cursor()

printStats = False
boredTrigger = "im bored"

eightball_replies = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes - definitely",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
]

"""
Container:
    contains message proccessing units

    Container.update("message")
        -> pass message to all units
        -> act = Unit.claim("message)
            -> Unit claims message? Proccess message and return True
            -> Unit doesn't claim message? Return False

"""
async def boredCounter(message: discord.message.Message) -> bool:
    if (boredTrigger in message.content.lower()):
        res = cur.execute(f"SELECT id FROM stats WHERE id={message.author.id}")
        result = res.fetchone()

        inDatabase = not result is None
        if not inDatabase:
            # await message.channel.send(content = "Author not in database")
            cur.execute(f"INSERT INTO stats (id, boredCounter) VALUES ({message.author.id}, 0)")
            con.commit()
        
        if inDatabase:
            pass
            # await message.channel.send(content = "Congratulations! You are in our database")


        res = cur.execute(f"SELECT boredCounter FROM stats WHERE id={message.author.id}")
        count = res.fetchone()[0]
        print(count)
        count += 1
        cur.execute(f"UPDATE stats SET boredCounter = {count} WHERE id={message.author.id}")
        con.commit()
        # await message.channel.send(content = f"You have triggered this message {count} times")
        return True
    else:
        return False

async def userStats(message: discord.message.Message) -> bool:
    if printStats:
        await (message.channel.send(content = f"```User: {str(message.author)} \nID: {str(message.author.id)}```", tts = True))
        return True
    else:
        return False

async def getBored(message: discord.message.Message) -> bool:
    first = (message.content.split()[0])
    if (first == "!bored"):
        res = cur.execute(f"SELECT id FROM stats WHERE id={message.author.id}")
        result = res.fetchone()

        inDatabase = not result is None
        if not inDatabase:
            # await message.channel.send(content = "Author not in database")
            cur.execute(f"INSERT INTO stats (id, boredCounter) VALUES ({message.author.id}, 0)")
            con.commit()
        
        if inDatabase:
            pass
            # await message.channel.send(content = "Congratulations! You are in our database")


        res = cur.execute(f"SELECT boredCounter FROM stats WHERE id={message.author.id}")
        count = res.fetchone()[0]
        await message.channel.send(content = (f"You have been bored {count} times"))
        return True
    else:
        return False

async def eightball(message: discord.message.Message) -> bool:
    first = message.content.split()[0]
    if (first == "!eightball"):
        answer = random.choice(eightball_replies)
        await message.reply(content = answer)
        return True
    else:
        return False

async def nlpAlgorithm(message: discord.message.Message):
    if "rickhard" in message.content.lower():
        await message.reply("Hey! I'm Rickhard, but you can call me dick for short")
        return True
    elif "im bored" in message.content.lower() or "i'm bored" in message.content.lower():
            await message.reply("Hi bored! I'm Rickhard, but you can call me dick for short")
            return True
    elif "weed" in message.content.lower():
        await message.reply("I luv weed :)")
        return True
    else:
        return False



    # if ("!bored" in message.content.split()[0])