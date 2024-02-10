import discord
from discord import app_commands
from dotenv import load_dotenv
import os
load_dotenv()
#import interaction


#bot = interactions.Client(token = "MTIwNTY3ODc1MDMxNDc5NTAyOQ.Gu7QgF.BuXr1309EkZV6M6Pmx0Wo7cq1Irz3gnwq8zvSc")
intents = discord.Intents.default()
intents.message_content = True
activity=discord.Activity(type=discord.ActivityType.watching, name="your pinterest >:(")
client = discord.Client(command_prefix='/', activity=activity, intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

client.run(os.getenv("TOKEN"))



