import os

import discord
import logging
import random
import searchStuff



from dotenv import load_dotenv

from discord.ext import commands

#logging.basicConfig(level=logging.INFO)

#intents permissions
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

search_youtube = searchStuff.SearchWeb('https://www.google.com/search?q=youtube')

#@bot.command(pass_context=True)
#async def music(ctx, term):
  #message_content = term.lower()
  #print(message_content)

  #key_words, search_words = search_youtube.key_words_search_words(message_content)
  #links = search_youtube.search(key_words)
  #print(links)
  #author = ctx.message.author
  #voice_channel = author.voice_channel
  #vc = await bot.join_voice_channel(voice_channel)
  #player = await vc.create_ytdl_player(links)
  #player.start()


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
async def on_message(message):
  if message.author == bot.user:
    return
  message_content = message.content.lower()
  if message_content.startswith(f'$hello'):
    await message.channel.send(f'Hello {message.author}')

  if message_content.startswith(f'$search'):
    key_words, search_words = search_youtube.key_words_search_words(message_content)
    links = search_youtube.search(key_words)
    print(links)
    await message.channel.send(f'found this for you {message.author}! \n{links}')

  #await bot.process_commands(message)

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



