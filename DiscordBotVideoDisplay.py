import os
import discord
# Uncomment line below and delete DiscordTokenReal line
# import DiscordToken 
import DiscordTokenReal
from discord.ext import commands
from discord.ext.commands.bot import Bot

token = DiscordTokenReal.token
prefix = '!'
bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

@bot.command(name='test')
async def testMessage(ctx):
    print('Entered test scenario')
    response = 'Hello, test worked!'
    await ctx.send(response)
    
    
bot.run(token)