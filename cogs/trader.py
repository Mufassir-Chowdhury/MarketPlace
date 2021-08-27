import discord
from bot import market
from discord.ext import commands

class Trader(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.marketplace = market

    @commands.command()
    async def ListShopTrader(self, ctx, trader):
        await ctx.send(self.marketplace.list_of_shops_of_a_trader(trader))



def setup(client):
    client.add_cog(Trader(client))