import discord
from discord import app_commands
from discord.ext import tasks, commands
import requests


class crypto(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="price")
    async def price(self, interaction: discord.Interaction, coin: str, base: str):
        try:
            response = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}')
            data = response.json()
            price = data.get('price')
            price = float(price)

            if price:
                await interaction.response.send_message(f'The Value of the pair {coin.upper()}/{base.upper()} is {price:.4f}',
                                                        ephemeral=True)
            else:
                await interaction.response.send_message(f'The pair {coin.upper()}/{base.upper()} is invalid.', ephemeral=True)
        except Exception as error:
            await interaction.response.send_message('Something went wrong')
            print(f'[ ERROR ] {error}')


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(crypto(bot))
