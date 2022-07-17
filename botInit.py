# ________   ________  ___       ___  _______   ________  ________  _________   
#|\   ___  \|\   __  \|\  \     |\  \|\  ___ \ |\   __  \|\   __  \|\___   ___\ 
#\ \  \\ \  \ \  \|\  \ \  \    \ \  \ \   __/|\ \  \|\ /\ \  \|\  \|___ \  \_| 
# \ \  \\ \  \ \  \\\  \ \  \    \ \  \ \  \_|/_\ \   __  \ \  \\\  \   \ \  \  
#  \ \  \\ \  \ \  \\\  \ \  \____\ \  \ \  \_|\ \ \  \|\  \ \  \\\  \   \ \  \ 
#   \ \__\\ \__\ \_______\ \_______\ \__\ \_______\ \_______\ \_______\   \ \__\
#    \|__| \|__|\|_______|\|_______|\|__|\|_______|\|_______|\|_______|    \|__|
# Created By  : Nolan Peet
# Created Date: 14-07-2022
# version ='1.0'
# ---------------------------------------------------------------------------
#     Just a lil bot i wanted to make for my discord servers.
#     Special thanks to https://stackoverflow.com/users/14940355/aditya-tomar
#     for https://stackoverflow.com/a/66669004. helped w/ ytdl streaming!
#     https://github.com/Rapptz/discord.py/blob/master/examples/basic_voice.py
# ---------------------------------------------------------------------------
#     Module check (hopefully this is correct, idk for sure)
import os
try:
  import discord
except ImportError:
  print("Trying to Install required module: discord, pyNaCl\n")
  os.system('python -m pip install discord.py')
  os.system('python -m pip install pynacl')
try:
  from discord.ext import commands
except ImportError:
  print("Trying to Install required module: discord.ext\n")
  os.system('python -m pip install discord.ext')
try:
  import dotenv
except ImportError:
  print("Trying to Install required module: dotenv\n")
  os.system('python -m pip install python-dotenv')
try:
  import asyncio
except ImportError:
  print("Trying to Install required module: asyncio\n")
  os.system('python -m pip install asyncio')
try:
  import youtube_dl
except ImportError:
  print("Trying to Install required module: youtube_dl\n")
  os.system('python -m pip install youtube_dl')
try:
  from requests import get
except ImportError:
  print("Trying to Install required module: requests\n")
  os.system('python -m pip install requests')
from discord.ext import commands
from dotenv import load_dotenv
# ---------------------------------------------------------------------------
#     COGS initilization
extensions = ['cogs.musicCog',
              'cogs.adminCog']
# ---------------------------------------------------------------------------
#     Start the bot
bot = commands.Bot(command_prefix='.')
for extention in extensions:
    bot.load_extension(extention)
@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}({bot.user.id}) in:')
    for guild in bot.guilds:
        print(f'{guild}: {guild.member_count} members')
projectPath = os.path.dirname(os.path.realpath(__file__))
if os.path.exists(os.path.join(projectPath,".env")):
  with open(os.path.join(projectPath,".env"),'r') as f:
    token = str(f.read())
    f.close()
else:
  token = input('What is your discord bot token:')
  with open(os.path.join(projectPath,".env"),'w') as f:
    f.write(token)
    f.close()
bot.run(token)