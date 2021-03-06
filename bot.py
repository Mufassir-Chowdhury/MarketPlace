from classes import marketplace
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix = '.')

market = marketplace()

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')



# @client.command()
# async def load(ctx, extension):
#     client.load_extension(f'cogs.{extension}')

# @client.command()
# async def unload(ctx, extension):
#     client.unload_extension(f'cogs.{extension}')

client.run(TOKEN)