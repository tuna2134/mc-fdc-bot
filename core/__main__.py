from .client import FdcBot
from argparse import ArgumentParser
import platform
from inspect import cleandoc
from data import DATA

import discord

import asyncio
try:
    import uvloop
except ImportError:
    NO_UVLOOP = True
else:
    NO_UVLOOP = False


def main():
    parser = ArgumentParser(description="About mc_fdc bot")
    parser.add_argument("--debug", help="Start with debug mode", action="store_true")
    parser.add_argument("--version", help="Print version", action="store_true")

    args = parser.parse_args()

    if args.version:
        print(cleandoc(f"""
        mc-fdc bot version monitor:
          - Version: {DATA['version']}
          - Discord.py: {discord.__version__}
            - pkg_resources: {discord.version_info}
          - Platform: {platform.version()}
          - Python: {platform.python_version()}
        """))
        return

    debug = args.debug
    
    bot = FdcBot(
        command_prefix=DATA["discord"]["prefix"],
        debug=debug, intents=discord.Intents.all()
    )
    if not debug:
        if not NO_UVLOOP:
            uvloop.install()
    async def run():
        async with bot:
            await bot.start(DATA["discord"]["token"])
    asyncio.run(run())

if __name__ == "__main__":
    main()