import base64
import asyncio
import discord
from discord import app_commands
import aiohttp
from io import BytesIO
import time
from discord.ext import tasks, commands


class ai(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="imagine")
    async def generate_image(self, ctx: commands.Context, *, prompt: str):
        ETA = int(time.time() + 60)
        msg = await ctx.send(f"Generating the images... ETA: <t:{ETA}:R>")
        async with aiohttp.request("POST", "https://backend.craiyon.com/generate", json={"prompt": prompt}) as resp:
            r = await resp.json()
            images = r['images']
            image = BytesIO(base64.decodebytes(images[0].encode("utf-8")))
            file = discord.File(image, "image.png")
            return await ctx.send(content="Generated using craiyon.com", file=file)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ai(bot))
