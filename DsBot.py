from settings import settings
import discord
# import * - это тоже самое, что перечислить все файлы
from bot_logic import *



# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send("Hi, how are you?")

    elif message.content.startswith('!bye'):
        await message.channel.send("Bye, I was glad to help")

    elif message.content.startswith('!game'):
        await message.channel.send("I think roblox is a good game.")

    elif message.content.startswith('!flip a coin'):
        await message.channel.send(flip_coin())

    elif message.content.startswith('!who is your creator?'):
        await message.channel.send("My creator: Retmeh")
    
    elif message.content.startswith('!help'):
        await message.channel.send("!hello")
        await message.channel.send("!bye") 
        await message.channel.send("!game") 
        await message.channel.send('!flip a coin')
        await message.channel.send('!who is your creator?')

    elif message.content.startswith('!smile'):
        await message.channel.send(gen_emodji())

    elif message.content.startswith('!pass'):
        await message.channel.send(gen_pass(10))
        

    else:
        await message.channel.send("#Error#")

 

client.run(settings["TOKEN"])
