import discord
from discord.ext import commands
import fortnite_api
from dotenv import load_dotenv
import os
from cogs.bot_commands import *
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
        await self.load_extension("cogs.fortnite")
        await self.load_extension("cogs.bot_commands")


