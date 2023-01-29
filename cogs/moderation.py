import discord
from discord import app_commands
from discord.ext import commands
import asyncio


class moderation(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="clear")
    async def delete_message(self, interaction: discord.Interaction, amount: int):
        await interaction.response.defer()
        await asyncio.sleep(0.1)
        await interaction.followup.send(f"{amount} message(s) have been deleted.")
        await interaction.channel.purge(limit=amount + 1)

    @app_commands.command(name="kick")
    async def kick(self, interaction: discord.Interaction, member: discord.Member, *, reason: str):
        await member.kick(reason=reason)
        embed = discord.Embed(title='KICK',
                              description=f'{member.mention} got kicked from the sever',
                              color=discord.Color.red())
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="ban")
    async def ban(self, interaction: discord.Interaction, member: discord.Member, *, reason: str):
        await member.ban(reason=reason)
        embed = discord.Embed(title='BAN',
                              description=f'{member.mention} got banned from the sever',
                              color=discord.Color.red())
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="mute")
    async def mute(self, interaction: discord.Interaction, member: discord.Member):
        await member.edit(mute=True)
        embed = discord.Embed(title="User Muted!",
                              description=f"{member} was muted",
                              color=discord.Color.red())
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="tempmute")
    async def temp_mute(self, interaction: discord.Interaction, member: discord.Member, time: int):
        await member.edit(mute=True)
        embed = discord.Embed(title="User Muted!",
                              description=f"{member} was muted for {time}s",
                              color=discord.Color.red())
        await interaction.response.send_message(embed=embed, ephemeral=True)
        await asyncio.sleep(time)
        await member.edit(mute=False)

    @app_commands.command(name="unmute")
    async def unmute(self, interaction: discord.Interaction, member: discord.Member):
        await member.edit(mute=False)
        embed = discord.Embed(title="User Unmuted!",
                              description=f"{member} was unmuted",
                              color=discord.Color.green())
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="deafen")
    async def mute(self, interaction: discord.Interaction, member: discord.Member):
        await member.edit(deafen=True)
        embed = discord.Embed(title="User Deafen!",
                              description=f"{member} was deafen",
                              color=discord.Color.red())
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="tempdeafen")
    async def temp_deafen(self, interaction: discord.Interaction, member: discord.Member, time: int):
        await member.edit(mute=True)
        embed = discord.Embed(title="User Deafen!",
                              description=f"{member} was deafen for {time}s",
                              color=discord.Color.red())
        await interaction.response.send_message(embed=embed, ephemeral=True)
        await asyncio.sleep(time)
        await member.edit(mute=False)

    @app_commands.command(name="undeafen")
    async def mute(self, interaction: discord.Interaction, member: discord.Member):
        await member.edit(deafen=False)
        embed = discord.Embed(title="User Undeafen!",
                              description=f"{member} was undeafen",
                              color=discord.Color.green())
        await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(moderation(bot))
