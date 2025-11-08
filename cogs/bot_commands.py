from discord.ext import commands
import discord
import sys
import importlib

class botCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, extension):
        sys.modules[f'./cogs/{extension}.py'] = importlib.reload(sys.modules[f'./cogs/{extension}.py'])
        await self.bot.reload_extension(f"cogs.{extension}")
        embed = discord.Embed(title='Reload', description=f'{extension} successfully reloaded', color=0xff00c8)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(botCommands(bot))