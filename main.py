import discord
import tasks
import asyncio
from discord import Intents
from discord.ext import commands
from discord.ext import tasks
from discord.ext import commands 
from config import owner,token,prefix,activty


case_insensitive = True

intents = Intents.default()
intents.members = True

client = commands.Bot(command_prefix=(prefix), intents=intents)

intents = discord.Intents.default() 

@client.event
async def on_command_error(msg, error):
    print(error)
    print(type(error))

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{activty}"))
    print(f'bot is online in {len(client.guilds)} servers!')

@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))


@client.command()
async def ping(ctx):
        """Ping of your bot"""
        embedVar = discord.Embed(title="Current ping", color=0x00ff00)
        embedVar.add_field(name="PİNG", value=f'**{round(client.latency * 1000)} ms**', inline=False)  
        await ctx.send(embed=embedVar)


client.run(token)