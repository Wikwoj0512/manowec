from threading import *
import requests
import asyncio
import discord
import time
import requests
from commands import *


client = discord.Client()

prefix=">"

name=f"[{prefix}]manowiec"


@client.event
async def on_ready():
    game = discord.Game("Work in progress")
    name = f"[{prefix}]manowiec"
    await client.user.edit(username=name)
    await client.change_presence(status=discord.Status.idle, activity=game)
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    global prefix
    if message.author==client:
        return
    mes=message.content
    if message.author.bot:
        if message.channel.id==536242178343567362:
                await message.delete()
    if mes=="co?":
        await message.channel.send("Chujów sto")
    command="prefix "
    if mes.startswith(prefix+command):
        if message.author.top_role >= findrole(message.channel.guild.roles, 'mod'):
            prefix=mes[len(prefix+command):]
            name=f"[{prefix}]manowiec"
            await client.user.edit(username = name)
            await message.channel.send(f"Prefix zmieniony na {prefix}")

    command="purge "
    if mes.startswith(prefix+command):
        if message.author.top_role >= findrole(message.channel.guild.roles,'mod'):
            try:
                num = mes[len(prefix + command):]
                num=int(num)+1
                await message.channel.purge(limit=num)
            except ValueError:
                await message.channel.send("we sie opie ogarnij")

    command="spam "
    if mes.startswith(prefix+command):
        if message.author.top_role >= findrole(message.channel.guild.roles,'mod'):
            num=int(mes[len(prefix+command):])
            for i in range(1,num+1):
                await message.channel.send(i)

    command='verify'
    if mes.startswith(prefix+command):
        if findrole(message.channel.guild.roles,'weryfikator') in message.author.roles:
            await verify(message)

    command = "purgeuser"
    if mes.startswith(prefix + command):
        print(1)
        if message.author.top_role >= findrole(message.channel.guild.roles,'mod'):

            try:
                if len(message.mentions)==1:
                    user = message.mentions[0]
                    num = int(mes[mes.find("|") + 1:])+1

                    if not user:
                        await message.channel.send("Nie ma takiego użytkownika")
                        return
                    print(num)
                    deleted = 0
                    while deleted < num:
                        mess = await message.channel.history().get(author__name=user.name)
                        if mess:
                            print(mess)
                            await mess.delete()
                            deleted += 1
                        else:
                            break

            except ValueError:
                await message.channel.send("we sie opie ogarnij")
        await message.delete()

    if mes==">endmysuffering":
        await client.close()
        quit()


if __name__=="__main__":
    client.run('NjAyMTExMzUwMDI5OTQyNzk0.XTMGFg.wonQQkCyc5M6-_gYm0SMWWsV2NA')