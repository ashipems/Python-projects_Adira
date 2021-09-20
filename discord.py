import discord
import random

TOKEN = 'PLACE YOUR TOKEN HERE'

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(username + " : " + user_message + " (" + channel + ")")

    if message.author == client.user:
        return
        
    if message.channel.name == "demo_channel":
        if user_message.lower() == 'hello':
            await message.channel.send("Hello "+username+"!")
            return

        elif user_message.lower() == 'bye':
            await message.channel.send("See you later "+username+"!")
            return

        elif user_message.lower() == 'random':
            await message.channel.send("This is your random number: " + str(random.randrange(1000)) + "!")
            return
        
        elif user_message.lower() == 'photo':
            await message.channel.send(file=discord.File('download.jpg'))
            return

    if user_message.lower() == 'anywhere':
        await message.channel.send("This can be used anywhere!")
        return

client.run(TOKEN)
