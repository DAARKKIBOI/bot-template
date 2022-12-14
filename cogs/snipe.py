import nextcord 
from nextcord.ext import commands
import datetime


class Snipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        self.snipes = {}
        
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        self.snipes[message.channel.id] = (message.content, message.author, datetime.datetime.now(), message.attachments)
        
        
    @commands.command(aliases=['s'])#u can add more aliases if u want 
    async def snipe(self, ctx):
        try:
            content, author, time, attachments = self.snipes[ctx.channel.id]
        except KeyError:
            await ctx.send('There are no messages to snipe!')
            
        embed = nextcord.Embed(title='Deleted Message', description=content, color=nextcord.Color.random(), timestamp=time)
        embed.set_thumbnail(url=author.avatar.url)
        embed.set_footer(text=f'Delted in {ctx.channel}')
        await ctx.send(embed=embed)
        
        
        
        
        
def setup(bot):
    bot.add_cog(Snipe(bot))