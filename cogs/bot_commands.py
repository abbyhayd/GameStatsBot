from discord.ext import commands
import discord

class botCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.group(name='reload', hidden=True, invoke_without_command=True)
    async def _reload(self, ctx, *, module: str):
        try:
            await self.bot.reload_extension(module)
        except commands.ExtensionError as e:
            await ctx.send(f'{e.__class__.__name__}: {e}')
        else:
            await ctx.send('\N{OK HAND SIGN}')

async def setup(bot):
    await bot.add_cog(botCommands(bot))