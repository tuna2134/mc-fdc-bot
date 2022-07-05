from discord.ext import commands

import discord


class Embed(discord.Embed):
    def __init__(self, *args, **kwargs):
        kwargs["color"] = 0x05f545
        super().__init__(*args, **kwargs)

class Cog(commands.Cog):
    Embed: Embed = Embed
    bot: commands.Bot | None
    command: commands.command

    async def fetch_user(self, user_id: int) -> discord.User:
        return await self.bot.fetch_user(user_id)

    @classmethod
    def command(cls, *args, **kwargs):
        return commands.command(*args, **kwargs)

    @classmethod
    def group(cls, *args, **kwargs):
        return commands.group(*args, **kwargs)