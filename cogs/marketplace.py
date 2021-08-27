import discord
from bot import market
from discord.ext import commands

class MarketPlace(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.marketplace = market

    @commands.command()
    async def meta(self, ctx):
        await ctx.send(f'{self.marketplace.name}')

    @commands.command()
    async def CreateShop(self, ctx, name, owner):
        self.marketplace.add_shop(name, owner)

    @commands.command()
    async def CreateTrader(self, ctx, name):
        self.marketplace.add_trader(name)

    @commands.command()
    async def ListShop(self, ctx):
        names = ''
        await ctx.send(f'{self.marketplace.list_of_shops()}')

    @commands.command()
    async def ListTrader(self, ctx):
        await ctx.send(f'{self.marketplace.list_of_traders()}')

    @commands.command()
    async def AssignTo(self, ctx, shop, owner):
        self.marketplace.change_owner(shop, owner)


def setup(client):
    client.add_cog(MarketPlace(client))