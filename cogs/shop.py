import discord
from bot import market
from discord.ext import commands

class Shop(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.marketplace = market

    @commands.command()
    async def ListItemShop(self, ctx, shop):
        await ctx.send(self.marketplace.list_of_items_of_a_shop(shop))

    @commands.command()
    async def CreateItem(self, ctx, shop, item, price):
        self.marketplace.add_item(shop, item, price)


def setup(client):
    client.add_cog(Shop(client))