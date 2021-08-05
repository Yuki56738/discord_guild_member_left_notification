#!/usr/bin/python3

import discord
from discord.ext import commands
from return_token import return_token

client = commands.Bot(command_prefix=".")

TOKEN = return_token()
CHANNEL = 768231963890024480
@client.event
async def on_ready():
  print("Logged in as:")
  print(client.user.name)
  print(client.user.id)
  print("Connected to following guild(s):")
  for x in client.guilds:
    print(x)
  print("----------")
  #inf_channel = client.get_channel(CHANNEL)
  #await inf_channel.send("test")

@client.event
async def on_member_remove(member):
  print(f"debug: on_member_remove hitted")
  inf_channel = client.get_channel(CHANNEL)
  await inf_channel.send(f"{member.name}がサーバーから退出しました。")

client.run(TOKEN)
