from discord.ext import commands
import discord

class botCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    # @commands.command()
    # @commands.is_owner()
    # async def reload(self, ctx, extension):
    #     await self.bot.reload_extension(f"cogs.{extension}")
    #     embed = discord.Embed(title='Reload', description=f'{extension} successfully reloaded', color=0xff00c8)
    #     await ctx.send(embed=embed)

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def _reload(self, *, module : str):
        try:
            self.bot.unload_extension(module)
            self.bot.load_extension(module)
        except Exception as e:
            await self.bot.say('\N{PISTOL}')
            await self.bot.say('{}: {}'.format(type(e).__name__, e))
        else:
            await self.bot.say('\N{OK HAND SIGN}')

async def setup(bot):
    await bot.add_cog(botCommands(bot))