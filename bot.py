import discord
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument, MissingPermissions, RoleNotFound


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all(), application_id=YOUR_APLICATION_ID)

        # Declaration of the cogs
        self.initial_extensions = ["cogs.moderation",
                                   "cogs.others",
                                   "cogs.music",
                                   "cogs.ai",
                                   "cogs.crypto",
                                   "cogs.utils"]

    async def setup_hook(self):
        global synced

        # Load of the cogs
        for ext in self.initial_extensions:
            await self.load_extension(ext)
        synced = await self.tree.sync()

    async def on_ready(self):
        print(f"Logged in as {bot.user} (ID: {bot.user.id})")
        print(f"[Info] Synced {len(synced)} command(s)")
        activity = discord.Activity(type=discord.ActivityType.listening, name="your_discord_name")
        await self.change_presence(status=discord.Status.do_not_disturb, activity=activity)

    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Please type all the command arguments")
        elif isinstance(error, CommandNotFound):
            await ctx.send("The command does not exist")
        elif isinstance(error, MissingPermissions):
            await ctx.send("You don't have permission to use this command")
        elif isinstance(error, RoleNotFound):
            await ctx.send("Invalid role")
        else:
            raise error


bot = MyBot()
bot.run(TOKEN)
