from google import genai
from dotenv import load_dotenv
import os

import discord
from discord.ext import commands

import asyncio
import fortnite_api

from bot import *

async def main() -> None:
    fortnite_client = fortnite_api.Client(api_key = os.getenv('FORTNITE_KEY'))

    bot = MyBot(fortnite_client=fortnite_client)

    async with fortnite_client, bot:
        await bot.start(os.getenv('DISCORD_TOKEN'))

    @bot.command()
    @commands.is_owner()
    async def reload(ctx, extension):
        bot.reload_extension(f"cogs.{extension}")
        embed = discord.Embed(title='Reload', description=f'{extension} successfully reloaded', color=0xff00c8)
        await ctx.send(embed=embed)


if __name__ == "__main__":
    asyncio.run(main())