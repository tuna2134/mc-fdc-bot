from discord.ext import commands
from discord.ext.fslash import extend_force_slash

from os import listdir
import traceback


class FdcBot(commands.Bot):
    def __init__(self, command_prefix: str, *args, **kwargs):
        self.prefix = command_prefix
        self.debug = kwargs.pop("debug")
        super().__init__(command_prefix, *args, **kwargs)
        extend_force_slash(self)

    def print(self, content: str) -> None:
        if self.debug:
            print(f"[BOT]: {content}")

    async def setup_hook(self) -> None:
        # await self.load_extension("jishaku")
        for name in listdir("./core/cogs"):
            if name.startswith("_"):
                continue
            if name.endswith(".py"):
                try:
                    await self.load_extension("core.cogs." + name[:-3])
                except Exception as _:
                    traceback.print_exc()
                else:
                    self.print(f"Loaded {name}")
        await self.tree.sync()

    async def on_ready(self) -> None:
        print("Bot is ready!")

    async def on_message(self, message):
        await self.process_commands(message)