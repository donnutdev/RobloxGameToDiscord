import discord
import os
import requests
from module import verification_requests, bot
from webserver import keep_alive
from replit import db
from discord.ext import commands

@bot.event
async def on_ready():
    print("I'm alive!")


@bot.command(name='verify')
async def _verify(ctx):
  await ctx.send(f"Redirected prompt to your DMs.")
  msg1 = await ctx.author.send(f"Hello {ctx.author.mention}! Please mention your roblox username.")
  username = await bot.wait_for('message', check=lambda m: m.channel == msg1.channel, timeout=600.0)
  roblox_check = requests.get(f'https://api.roblox.com/users/get-by-username?username={username.content}').json()
  if roblox_check.get('success', True) == False:
    return await ctx.author.send("I couldn't find your user, please try again.")
  await ctx.author.send(f"Please join this game to complete your verification.")
  verification_requests[roblox_check.get('Id')] = {'success':True, 'discordId':str(ctx.author.id), 'robloxUser':roblox_check.get('Username'), 'discordTag':ctx.author.name+"#"+ctx.author.discriminator}
  print(verification_requests)

keep_alive()
bot.run(os.environ['TOKEN'])