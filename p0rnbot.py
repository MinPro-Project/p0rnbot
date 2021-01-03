from discord.ext import commands
from discord.utils import get
import discord.member
import discord.mentions

import discord
import asyncio
import os
import re

filter_default = ['http', 'www.', 'https', '://', '.com', '.gg', '.xyz', '.one', '.io', '.net', '.shop', '.site', '.한국', '.biz', '.company', '.tv', '.link', '.id', '.kr', '.co', '.me', '.cn', '.jp', '.ai', '.us', '.tw', '.id', '.hk', '.uk', '.cc', '.sg', '.in', '.eu', '.ac', '.am', '.닷컴', '.company', '.cafe', '.life', '.network']
link_filter = filter_default



try:
    game = discord.Game("Welcome P0rn Server")
    bot = commands.Bot(command_prefix='~',Status=discord.Status.online,activity=game)

    client = discord.Client()

    msg_nl = "\n"

    def box(msg):
        return "@everyone" + msg_nl + msg

    @bot.event
    async def on_ready():
        print("login...")
        print(bot.user.name)
        print(bot.user.id)
        print("ready!")
        print("----------------")

    @bot.event
    async def on_message(message):
        if message.author.bot:
            return None
        did = message.author.id
        dname = message.author.name
        dmention = message.author.mention
        channel = message.channel
        for i in link_filter:
            if i in message.content:
                if message.author.guild_permissions.manage_guild == True:
                    print(f"Link Passed : {dname} 서버 관리자 메세지")
                    break
                else:
                    await message.delete()
                    await channel.send(f"{dmention}님 링크를 올리실수 없습니다.")
                    print(f"Id : {did}\n{dname}가 올린 링크 삭제조치 완료")
                    break
        await bot.process_commands(message)
    
    token = os.environ["BOT_TOKEN"]
    print("Token_key : ", token)
    # bot.loop.create_task(my_background_task())
    bot.run(token)
except Exception as e:
    print(e)
