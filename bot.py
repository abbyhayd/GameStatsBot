import discord
from discord.ext import commands
import fortnite_api
from dotenv import load_dotenv
import os
from cogs.events import *
from cogs.fortnite import *


load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')

class MyBot(commands.Bot):

    def __init__(self, fortnite_client: fortnite_api.Client) -> None:
        super().__init__(
            command_prefix="!",
            intents = discord.Intents.all(),
        )

        self.fortnite_client = fortnite_client

    async def setup_hook(self):
        await self.load_extension("cogs.events")
        await self.load_extension("cogs.fortnite")

    @commands.group(name='reload', hidden=True, invoke_without_command=True)
    async def _reload(self, ctx, *, module: str):
        """Reloads a module."""
        try:
            await self.bot.reload_extension(module)
        except commands.ExtensionError as e:
            await ctx.send(f'{e.__class__.__name__}: {e}')
        else:
            await ctx.send('\N{OK HAND SIGN}')
