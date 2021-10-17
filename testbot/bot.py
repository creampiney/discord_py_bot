import discord
import math
import random
import json
import os
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get
import youtube_dl
from functools import partial
import asyncio
from async_timeout import timeout
from songs import songAPI       # songs.py

prefix = "-"

with open('config.json') as json_file:
    TOKEN = json.load(json_file)['DISCORD_TOKEN']
bot = commands.Bot(command_prefix=prefix, help_command=None)

random.seed(1111)

songsInstance = songAPI()


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.change_presence(activity=discord.Game(name="เบื่อ TT"))

# @bot.event
# async def on_message(message):
#    msg = message.content
#    uid = message.author.id
#    if msg.startswith('.welcome'):
#        channel = client.get_channel(id)
#        await message.channel.send("Welcome Muang!")
#        # await message.author.send("Welcome Muang!")
#
#    elif msg.startswith('.answer'):
#        submit_answer(uid, " ".join(msg.split()[1:]), exam_info)
#        info = get_student_info(uid, exam_info)
#        for i in range(len(info[3])):
#            await message.author.send(info[2][i] + " --> " + info[3][i])
#        question = get_question(uid, exam_info, all_questions)
#        if question != "end":
#            question += " -->"
#        await message.author.send(question)


@bot.command()
async def help(ctx):
    emBed = discord.Embed(title="ยินดีต้อนรับสู่บอท "+bot.user.name+"!", color=0x977fd7)
    emBed.add_field(name="help", value="แสดงคำสั่งทุกคำสั่งของบอทนี้", inline=False)
    emBed.add_field(name="play / p", value="Format : `"+prefix+"play/p <url/song_name>`\nคำสั่งใช้เล่นเพลงหรือเพิ่มเพลงในคิว", inline=False)
    emBed.add_field(name="queue / q", value="แสดงเพลงที่อยู่ในคิวและจำนวนเพลงที่อยู่ในคิว", inline=False)
    emBed.add_field(name="stop", value="ใช้เพื่อหยุดเพลงและลบเพลงนั้น", inline=False)
    emBed.add_field(name="pause", value="ใช้เพื่อหยุดเพลงชั่วคราว", inline=False)
    emBed.add_field(name="resume", value="ใช่เพื่อเล่นเพลงต่อ (ใช้คู่กับ pause)", inline=False)
    await ctx.channel.send(embed=emBed)


@bot.command()
async def play(ctx, *, search: str):
    await songsInstance.play(ctx, search)


@bot.command()
async def p(ctx, *, search: str):
    await songsInstance.play(ctx, search)


@bot.command()
async def stop(ctx):
    await songsInstance.stop(ctx)


@bot.command()
async def pause(ctx):
    await songsInstance.pause(ctx)


@bot.command()
async def resume(ctx):
    await songsInstance.resume(ctx)


@bot.command()
async def leave(ctx):
    await songsInstance.leave(ctx)


@bot.command()
async def queue(ctx):
    await songsInstance.queueList(ctx)


@bot.command()
async def q(ctx):
    await songsInstance.queueList(ctx)


@bot.command()
async def skip(ctx):
    await songsInstance.skip(ctx)


@bot.command()
async def quit(ctx, msg):
    if msg == "1234":
        await bot.logout()


bot.run(TOKEN)
