from dotenv import load_dotenv
from discord.ext import commands
import fortnite_api


class FortniteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def in_target_channel(ctx):
        return ctx.channel.id == 1436644620238061670

    @commands.command(
            name="fortnite-stats", 
            brief="Get game stats for player", 
            description="Gets the overall stats for a player given their username")
    @commands.check(in_target_channel)
    async def player_stats(self, ctx, username) -> None:        
        bot = ctx.bot
        fortnite_client : fortnite_api.Client = bot.fortnite_client

        try:
            player_info : fortnite_api.BrPlayerStats = await fortnite_client.fetch_br_stats(name=username)

        except fortnite_api.NotFound:
            await ctx.send("Username not found")

        else:
            stats = player_info.inputs and player_info.inputs.all

            total_wins = stats.overall.wins
            total_kills = stats.overall.kills
            total_deaths = stats.overall.deaths
            total_matches = stats.overall.matches

            await ctx.send(
                f"The overall Battle Royal Stats for {username}: \n"
                f":trophy: Total wins: {total_wins}\n"
                f":drop_of_blood: Total kills: {total_kills}\n"
                f":skull_crossbones: Total deaths: {total_deaths}\n"
                f":video_game: Total matches: {total_matches}\n"
            )

    @commands.hybrid_command(
        name="fortnite-total-cosmetics",
        brief="Get total number of cosmetics",
        description="Gets the total number of cosmetics in the Fortnite shop"
    )
    @commands.check(in_target_channel)
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