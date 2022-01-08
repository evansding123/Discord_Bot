import os

import discord
import logging
import random


from dotenv import load_dotenv

from discord.ext import commands

logging.basicConfig(level=logging.INFO)

intents = discord.Intents().all()
intents.members = True
intents.presences = True
bot = discord.Client(intents=intents)

bot = commands.Bot(command_prefix="$")


load_dotenv()

class Commands:
  urls = ['1', '2', '3', 'you suck']

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


#print(bot)





@bot.command()
async def ping(ctx):
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

  await bot.process_commands(message)

@bot.event
async def on_member_update(before, after):
  print(before)
  if str(before.status) == "online" and str(after.status) == "offline":
      #await after.create_dm()
      #await after.dm_channel.send('status change')
      #channel = bot.get_channel(ID)
      await after.channel.send(f'{before.name} changed status to {after.status}')

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