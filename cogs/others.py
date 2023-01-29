import discord
from discord import app_commands
from discord.ext import tasks, commands


class others(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="ping")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"The average response time is {(self.bot.latency * 1000):.1f}ms")

    @app_commands.command(name="userinfo")
    async def userinfo(self, interaction: discord.Interaction, member: discord.Member):
        embed = discord.Embed(colour=member.colour)

        embed.set_author(name=f'User info - {member}')
        embed.set_thumbnail(url=member.avatar)
        embed.set_footer(text=f'Requested by {interaction.user}', icon_url=interaction.user.avatar)

        embed.add_field(name='ID: ', value=member.id)
        embed.add_field(name='Account name:', value=member)
        embed.add_field(name='Nickname: ', value=member.display_name)
        embed.add_field(name='Status: ', value=member.raw_status)

        embed.add_field(name='Guild name: ', value=member.guild)

        embed.add_field(name='Created at: ', value=member.created_at.strftime('Data: %d/%m/%Y \nTempo: %H:%M:%S'))
        embed.add_field(name='Joined at: ', value=member.joined_at.strftime('Data: %d/%m/%Y \nTempo: %H:%M:%S'))

        embed.add_field(name=f'Roles      nº{len(member.roles)}',
                        value=' '.join([role.mention for role in member.roles]))
        embed.add_field(name='Top role:', value=member.top_role)

        embed.add_field(name='Bot: ', value=member.bot)

        await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(others(bot))
