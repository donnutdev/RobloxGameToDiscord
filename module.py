import discord
from discord.ext import commands

verification_requests = {}

bot = commands.Bot(command_prefix='!', help_command=None, intents=discord.Intents.all())
