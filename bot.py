import nextcord 
from nextcord.ext import commands
import os
import json 

with open('config.json', 'r') as f:
    CONFIG = json.loads(f)




bot = commands.Bot(command_prefix=CONFIG['prefix'], intents=nextcord.Intents.all())
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


@bot.command()
async def ping(ctx):
    await ctx.send(f'My ping is {round(bot.latency * 1000)}')
    
    
    

bot.run(CONFIG['token'])