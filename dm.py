import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import chalk
import random


client = commands.Bot(command_prefix='!demi')

@client.event
async def on_ready():
                         print("san sang")
                       
@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))
    if message.content.upper().startswith('HELLO'):
        await client.send_message(message.channel, "Xin Chào")

    if message.content.upper().startswith('DUDIME'):
        flit = random.choice(["ukm dudime","uh dudime"])
        await client.send_message(message.channel, (flit))
    if message.content.upper().startswith(':))'):
        flat = random.choice(["vui ko mà cuoi","cuoi gì thê!"])
        await client.send_message(message.channel, (flat))

    if message.content.upper().startswith('!DEMISAY'):
           args = message.content.split(" ")
           await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
    if message.content.upper().startswith('!DEMIPING'):
        ping = random.choice([":ping_pong: Ping!! 999ms",":ping_pong: Ping!!69ms"])
        await client.send_message(message.channel, (ping))


           
@client.command()
async def ping():
    await client.say(':ping_pong: Ping!! 999ms')
    print("asdasd")






client.run("NDkzODI2NjkxMDg1MzY5MzU2.DovNtA.xZLSZQ0DD90r5JrJGCOotaub9Mc")
