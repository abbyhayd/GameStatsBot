from dotenv import load_dotenv
from discord.ext import commands
import fortnite_api

class FortniteCog(commands.Cog):

    @commands.command(name="stats", description="Get requested player stats")
    async def player_stats(self, ctx) -> None:
        pass

    @commands.hybrid_command(
        name="total-cosmetics",
        description="Get the total number of cosmetics in Fortnite.",
    )
    async def total_cosmetics(self, ctx) -> None:
        async with ctx.typing():
            bot = ctx.bot
            fortnite_client : fortnite_api.Client = bot.fortnite_client

            all_cosmetics = await fortnite_client.fetch_cosmetics_all()

            total_cosmetics = len(all_cosmetics)

            await ctx.send(
                f"The total number of cosmetics in Fortnite is: {total_cosmetics}",
                ephemeral=True,
            )