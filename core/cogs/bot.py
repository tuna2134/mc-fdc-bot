from . import Cog

from discord.ext import commands


class Bot_general(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Ping command")
    async def ping(self, ctx):
        await ctx.reply(
            embed=Cog.Embed(title="Pong", description=f"{round(self.bot.latency * 100, 1)}ms")
        )

    @commands.command()
    async def info(self, ctx):
        pass

async def setup(bot):
    await bot.add_cog(Bot_general(bot))