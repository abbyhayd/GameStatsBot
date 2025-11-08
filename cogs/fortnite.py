from dotenv import load_dotenv
from discord.ext import commands
import fortnite_api

def get_total_wins(stats: fortnite_api.BrPlayerStats, game_type) -> int:
        all_inputs = stats.inputs and stats.inputs.all
        if all_inputs is None:
            return 0
        
        total_wins = 0
        
        match game_type:
            case "solo":
                total_wins = all_inputs.solo
            case "duos":
                total_wins = all_inputs.duo
            case "trios":
                total_wins = all_inputs.trio
            case "squads":
                total_wins = all_inputs.squad
        if total_wins is None:
            total_wins = 0

        return total_wins.wins

class FortniteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="fortnite-stats", description="Get game stats for player")
    async def player_stats(self, ctx, user, game_type) -> None:        
        bot = ctx.bot
        fortnite_client : fortnite_api.Client = bot.fortnite_client

        if game_type not in ["solo", "duos", "trios", "squads"]:
            await ctx.send("Provide valid game type (solo, duos, trios, squads)")
            return

        #put in player not found exception

        player_info = await fortnite_client.fetch_br_stats(name=user)

        total_wins = get_total_wins(player_info, game_type)

        await ctx.send(
            f"The Battle Royal Stats for {user} in {game_type}: \n"
            f"Total wins: {total_wins}"
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