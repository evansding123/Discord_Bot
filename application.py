import os

import discord

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#print(GUILD)

client = discord.Client()
@client.event
async def on_ready():
    for guild in client.guilds:

      if guild.name == GUILD:
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )


client.run(TOKEN)



  #@client.event
  #async def on_message(message):
    #if message.author == client.user:
      #return