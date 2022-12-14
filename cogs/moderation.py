import nextcord 
from nextcord.ext import commands
import datetime
import humanfriendly



class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        
        
    @commands.command()
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member: nextcord.Member, *,reason):
        await member.kick(reason=reason)
        embed = nextcord.Embed()
        embed.set_author(name=f'{member} has been kicked for the following reason: `{reason}`')
        await ctx.send(embed=embed)
        
        
    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member: nextcord.Member, *,reason):
        await member.kick(reason=reason)
        embed = nextcord.Embed()
        embed.set_author(name=f'{member} has been banned for the following reason: `{reason}`')
        await ctx.send(embed=embed)
        
        
    @commands.command()
    @commands.has_guild_permissions(moderate_members=True)
    async def mute(self, ctx, member: nextcord.Member, time):
        time_in_seconds = humanfriendly.parse_timespan(time)
        await member.edit(timeout=datetime.timedelta(seconds=time_in_seconds))
        embed = nextcord.Embed()
        embed.set_author(name=f'{member} has been muted for: `{time}`')
        await ctx.send(embed=embed)
        