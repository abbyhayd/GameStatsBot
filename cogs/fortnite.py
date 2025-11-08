from dotenv import load_dotenv
from discord.ext import commands
import fortnite_api

class FortniteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="fortnite-stats", description="Get requested player stats")
    async def player_stats(self, ctx, user) -> None:
        bot = ctx.bot
        fortnite_client : fortnite_api.Client = bot.fortnite_client

        player_info = await fortnite_client.fetch_br_stats(user)

        await ctx.send(
            f"The Battle Royal Stats for {user} are: "
            f"Level: {player_info.data.level}"
        )


    @commands.hybrid_command(
        name="fortnite-total-cosmetics",
        description="Get the total number of cosmetics in Fortnite.",
    )
    async def total_cosmetics(self, ctx) -> None:
        async with ctx.typing():
            bot= ctx.bot
            fortnite_client : fortnite_api.Client = bot.fortnite_client

            all_cosmetics = await fortnite_client.fetch_cosmetics_all()

            total_cosmetics = len(all_cosmetics)

            await ctx.send(
                f"The total number of cosmetics in Fortnite is: {total_cosmetics}",
                ephemeral=True,
            )
    
    async def cog_load(self):
        print(f"{self.__class__.__name__} loaded!")

    async def cog_unload(self):
        print(f"{self.__class__.__name__} unloaded!")

async def setup(bot):
    await bot.add_cog(FortniteCog(bot))