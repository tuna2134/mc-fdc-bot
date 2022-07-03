from discord.ext import commands

import discord


class Embed(discord.Embed):
    def __init__(self, *args, **kwargs):
        kwargs["color"] = 0x05f545
        super().__init__(*args, **kwargs)

class Cog(commands.Cog):
    bot: commands.Bot | None
    command: commands.command

    async def fetch_user(self, user_id: int) -> discord.User:
        return await self.bot.fetch_user(user_id)