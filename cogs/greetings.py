import discord
from discord import app_commands
from discord.ext import tasks, commands
import datetime


class greetings(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.WELLCOME_CHANNEL = "channel_id"
        self.GOODBYE_CHANNEL = "channel_id"

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        role = discord.utils.get(member.guild.roles, name="user")
        await member.add_roles(role)

        channel = self.bot.get_channel(WELLCOME_CHANNEL)

        time = datetime.datetime.utcnow()
        time = time.strftime('Date: %d/%m/%Y Time: %H:%M:%S')

        embed = discord.Embed(title=f'Welcome!',
                              description=f'{member.mention}, welcome to {member.guild}\nMember count: {member.guild.member_count}')
        embed.set_author(name=member.guild, icon_url=member.avatar)
        embed.set_thumbnail(url=member.avatar)
        embed.set_footer(text=f'User ID: {member.id}                   {time}')

        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        channel = self.bot.get_channel(GOODBYE_CHANNEL)

        time = datetime.datetime.now()
        time = time.strftime('Date: %d/%m/%Y Time: %H:%M:%S')

        embed = discord.Embed(title=f'{member}, just left the server')
        embed.set_author(name=member.guild, icon_url=member.avatar)
        embed.set_thumbnail(url=member.avatar)
        embed.set_footer(text=f'User ID: {member.id}                   {time}')

        await channel.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(greetings(bot))
