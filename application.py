import os

import discord

from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix="$")
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

@bot.event
async def on_typing(channel, user, when):
  #print(user.id)
  await channel.send('hello there you are typing')

bot.run(TOKEN)



  #@client.event
  #async def on_message(message):
    #if message.author == client.user:
      #return