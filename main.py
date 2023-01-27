import discord, asyncio
from discord import app_commands
from discord.ext import commands
import asyncio

MY_GUILD_ID = "GUILD_ID"
MY_GUILD = discord.Object(id=MY_GUILD_ID)


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.default()
bot = MyClient(intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    synced = await bot.tree.sync()
    print(f"[Info] Synced {len(synced)} command(s)")


@bot.tree.command(name="ping")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"The average response time is {(bot.latency * 1000):.1f}ms")


@bot.tree.command(name="clear")
async def delete_message(interaction: discord.Interaction, amount: int):
    await interaction.response.defer()
    await asyncio.sleep(0.1)
    await interaction.followup.send(f"{amount} message(s) have been deleted.")
    await interaction.channel.purge(limit=amount + 1)


@bot.tree.command(name="kick")
async def kick(interaction: discord.Interaction, member: discord.Member, *, reason: str):
    await member.kick(reason=reason)
    embed = discord.Embed(title='KICK',
                          description=f'{member.mention} got kicked from the sever',
                          color=discord.Color.red())
    await interaction.response.send_message(embed=embed, ephemeral=True)


@bot.tree.command(name="ban")
async def ban(interaction: discord.Interaction, member: discord.Member, *, reason: str):
    await member.ban(reason=reason)
    embed = discord.Embed(title='BAN',
                          description=f'{member.mention} got banned from the sever',
                          color=discord.Color.red())
    await interaction.response.send_message(embed=embed, ephemeral=True)


@bot.tree.command(name="mute")
async def mute(interaction: discord.Interaction, member: discord.Member):
    await member.edit(mute=True)
    embed = discord.Embed(title="User Muted!",
                          description=f"{member} was muted",
                          color=discord.Color.red())
    await interaction.response.send_message(embed=embed, ephemeral=True)


@bot.tree.command(name="tempmute")
async def tempmute(interaction: discord.Interaction, member: discord.Member, time: int):
    await member.edit(mute=True)
    embed = discord.Embed(title="User Muted!",
                          description=f"{member} was muted for {time}s",
                          color=discord.Color.red())
    await interaction.response.send_message(embed=embed, ephemeral=True)
    await asyncio.sleep(time)
    await member.edit(mute=False)


@bot.tree.command(name="unmute")
async def unmute(interaction: discord.Interaction, member: discord.Member):
    await member.edit(mute=False)
    embed = discord.Embed(title="User Unmuted!",
                          description=f"{member} was unmuted",
                          color=discord.Color.green())
    await interaction.response.send_message(embed=embed, ephemeral=True)


@bot.tree.command(name="deafen")
async def mute(interaction: discord.Interaction, member: discord.Member):
    await member.edit(deafen=True)
    embed = discord.Embed(title="User Deaden!",
                          description=f"{member} was deaden",
                          color=discord.Color.red())
    await interaction.response.send_message(embed=embed, ephemeral=True)


@bot.tree.command(name="tempdeafen")
async def tempdeafen(interaction: discord.Interaction, member: discord.Member, time: int):
    await member.edit(mute=True)
    embed = discord.Embed(title="User Deafen!",
                          description=f"{member} was deafen for {time}s",
                          color=discord.Color.red())
    await interaction.response.send_message(embed=embed, ephemeral=True)
    await asyncio.sleep(time)
    await member.edit(mute=False)


@bot.tree.command(name="undeafen")
async def mute(interaction: discord.Interaction, member: discord.Member):
    await member.edit(deafen=False)
    embed = discord.Embed(title="User Undeaden!",
                          description=f"{member} was undeaden",
                          color=discord.Color.green())
    await interaction.response.send_message(embed=embed, ephemeral=True)


bot.run("TOKEN")
