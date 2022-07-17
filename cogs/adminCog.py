from logging import exception
import discord
from discord.ext import commands
import sys
import traceback
import random
from typing import Optional
class Admin(commands.Cog):
    """Admin related commands."""
    __slots__ = ('bot')
    def __init__(self, bot):
        self.bot = bot
    async def __local_check(self, ctx):
        #A local check which applies to all commands in this cog.
        if not ctx.guild:
            raise commands.NoPrivateMessage
        return True
    async def __error(self, ctx, error):
        '''A local error handler'''
        ctx.send(error)
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
    @commands.command(name='embed', aliases=['eb','e'], description="Create an embedded post")
    async def embedMessage_(self,ctx,*,title: Optional[str]='',embedDiscription: Optional[str]='',embedURL: Optional[str]='',message: Optional[str]='',imgURL: Optional[str]='',color: Optional[list]=[0,255,255]):
        """Makes an Embedded Post
        This command attempts to create an embedded post. 
        .e t:'hello world'd:'found this cool link for you'eurl:'https://example.com/'k:'examples programming embedded messages'c:'255,0,127'
        Parameters
        ------------
        title:'str' [Optional] <t:>
            
        embedDiscription:'str' [Optional] <edisc:,ed:,d:>
            
        embedURL: str [Optional] <eurl:>
            
        message: str [Optional] <msg:,m:,keyword:,k:>
            Regular discord message to go with embed link
        color: list [Optional] <colour:,c:>
            R,G,B (0-255) default 0,255,255"""
        await ctx.trigger_typing()
        try:
            embed = discord.Embed(title=title, description=embedDiscription,url=embedURL,  color=discord.Color.from_rgb(color[0],color[1],color[2]))
        except exception as e:
            ctx.send(e)
        embed.set_image(url=imgURL)
        return await ctx.send(message,embed=embed)
    @commands.command(name='roll', aliases=['rl'], description="Rolls Dice")
    async def roll_(self,ctx,dice: str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        embed = discord.Embed(title='Dice Roll',description=result,color=discord.Color.gold())
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Admin(bot))