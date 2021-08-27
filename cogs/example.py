import discord
from bot import market
from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.marketplace = market

    @commands.Cog.listener()
    async def on_ready(self):
        print("BOT is ONLINE")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

    # @commands.command()
    # async def meta(self, ctx):
    #     await ctx.send(f'{self.marketplace.name}')

    # @commands.command()
    # async def CreateShop(self, ctx, name, owner):
    #     self.marketplace.add_shop(name, owner)

    # @commands.command()
    # async def CreateTrader(self, ctx, name):
    #     self.marketplace.add_trader(name)


    # @commands.command()
    # async def ListShop(self, ctx):
    #     names = ''
    #     await ctx.send(f'{self.marketplace.list_of_shops()}')

    # @commands.command()
    # async def ListTrader(self, ctx):
    #     await ctx.send(f'{self.marketplace.list_of_traders()}')

    # @commands.command()
    # async def NumberShop(self, ctx):
    #     await ctx.send(f'{self.marketplace.number_of_shops()}')

    # @commands.command()
    # async def NumberTrader(self, ctx):
    #     await ctx.send(f'{self.marketplace.number_of_traders()}')



    # @commands.command()
    # async def ListShopTrader(self, ctx, trader):
    #     await ctx.send(self.marketplace.list_of_shops_of_a_trader(trader))

    # @commands.command()
    # async def ListItemShop(self, ctx, shop):
    #     await ctx.send(self.marketplace.list_of_items_of_a_shop(shop))

    # @commands.command()
    # async def CreateItem(self, ctx, shop, item, price):
    #     self.marketplace.add_item(shop, item, price)

    # @commands.command()
    # async def AssignTo(self, ctx, shop, owner):
    #     self.marketplace.change_owner(shop, owner)


def setup(client):
    client.add_cog(Example(client))