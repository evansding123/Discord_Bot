import os

import discord

import random

from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()

class Commands:
  urls = ['1', '2', '3', 'you suck']

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix="$")
#print(bot)

intents = discord.Intents().all()
client = discord.Client(intents=intents)

@bot.command()
async def ping(ctx, args):
  await ctx.channel.send('pong')

#print(GUILD)

#client = discord.Client()
@bot.event
async def on_ready():
    for guild in bot.guilds:

      if guild.name == GUILD:
        print(
            f'{bot.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

#@bot.event
#async def on_typing(channel, user, when):

  #await channel.send(f'{user} has chosen {random.choice(Commands.urls)}')

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  if message.content.startswith(f'$hello'):
    await message.channel.send(f'Hello {message.author}')

@bot.event
async def on_member_update(before, after):
  print(before.status)
  if str(before.status == 'online'):
    if(str(after.status == 'offline')):


      await bot.channel.send(f'{before.name} changed status to {after.status}')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

bot.run(TOKEN)



  #@client.event
  #async def on_message(message):
    #if message.author == client.user:
      #return