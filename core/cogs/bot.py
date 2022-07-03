from . import Cog


class Bot_general(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.command()
    async def ping(self, ctx):
        await ctx.send(
            embed=Cog.Embed(title="Pong", description=f"{round(self.bot.latency * 100, 1)}ms")
        )

    @Cog.command()
    async def info(self, ctx):
        pass

async def setup(bot):
    await bot.add_cog(Bot_general(bot))