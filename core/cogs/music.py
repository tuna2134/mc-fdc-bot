from . import Cog
import discord

import yt_dlp as ytdlp


ytdl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "%(extractor)s-%(id)s-%(title)s.%(ext)s",
    "restrictfilenames": True,
    "noplaylist": True,
    "nocheckcertificate": True,
    "ignoreerrors": False,
    "logtostderr": False,
    "quiet": True,
    "no_warnings": True,
    "default_search": "auto",
    "source_address": "0.0.0.0"
}

ytdl = ytdlp.YoutubeDL(ytdl_opts)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source)
        self.volume = volume
        self.data = data

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        data = await loop.run_in_executor(None, lambda: ytdlp.extract_info(url, download=not stream))
        if "entries" in data:
            data = data["entries"][0]
        filename = data["url"]
        return cls(discord.FFmpegPCMAudio(filename, before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"), data=data)

class Music(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.group()
    async def music(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("No subcommand passed")

    @music.command()
    async def join(self, ctx):
        m = await ctx.reply("Joining voice channel")
        await ctx.author.voice.channel.connect()
        await m.edit(content="Joined voice channel")

    @music.command()
    async def leave(self, ctx):
        m = await ctx.reply("Leaving voice channel")
        await ctx.author.voice.channel.disconnect()
        await m.edit(content="Left voice channel")

    @music.command()
    async def play(self, ctx, *, url):
        m = await ctx.reply("Playing song")
        player = await YTDLSource.from_url(url, loop=self.bot.loop)
        ctx.voice_client.play(player, after=lambda: m.edit(content="Song finished"))


async def setup(bot):
    await bot.add_cog(Music(bot))