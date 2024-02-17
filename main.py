import discord
from discord import app_commands
from dotenv import load_dotenv
import os
import interactions
import requests

load_dotenv()
 
header = {"X-MAL-CLIENT-ID": os.getenv("MAL_TOKEN")}
url = 'https://api.myanimelist.net/v2/' 

button = interactions.Button(
  style = interactions.ButtonStyle.PRIMARY,
  label = ":right_arrow:",
  custom_id = "click me"
)

#response = requests.get(url, headers=header)
#print(response.json()["data"][0]['node']['title'])

intents = discord.Intents.default()
intents.message_content = True
activity=discord.Activity(type=discord.ActivityType.watching, name="your anime list :3")
client = discord.Client(command_prefix='/', activity=activity, intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name="watching", description="shows user's watching list")
async def watching(interaction, username:str):
  user_list_url = url + "users/" + username + "/animelist?status=watching&limit=1000"
  response = requests.get(user_list_url, headers=header)
  watching_num = len(response.json()["data"])
  embed = discord.Embed(title=f"{username}'s Watching List!", description=f"Watching: {watching_num}")
  for i in range(watching_num):
    embed.add_field(name= str(i+1) + ". " + response.json()["data"][i]['node']['title'], value = "", inline=False)
  await interaction.response.send_message(embed=embed)

@tree.command(name="completed", description="shows user's completed list")
async def completed(interaction, username:str):
  user_list_url = url + "users/" + username + "/animelist?status=completed&limit=1000"
  response = requests.get(user_list_url, headers=header)
  completed_num = len(response.json()["data"])
  embed = discord.Embed(title=f"{username}'s Completed List!", description=f"Completed: {completed_num}")
  compani = []
  for i in range(completed_num):
    compani.append(response.json()["data"][i]['node']['title'])

  await interaction.response.send_message(embed=embed)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await tree.sync()


client.run(os.getenv("DC_TOKEN"))



