import os
import time
import Driver
import discord
import DeleteFlies
# Uncomment line 6 and delete line 7
# import DiscordToken 
import DiscordTokenReal
from discord.ext import commands
# Uncomment line 11 and delete line 12
# token = DiscordToken.token
token = DiscordTokenReal.token

prefix = '!'
bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

@bot.command(name='run')
async def runCommand(command, *, link:str = None):
    if link is None:
        await command.send('The link must be filled!')
        
    else:
        print('\nStarting up')
        message = await command.send('Starting Up!')
        await command.message.delete()
       
        Driver.Run(link)
        time.sleep(1)
        if 'https://youtu.be/FtutLA63Cp8?si=CnKngncrljco9EWP' in link:     
            await message.edit(content='Bad Apple, but played in ascii by a Discord bot')
        
        asciiPath = './asciiFrames'
        allFiles = os.listdir(asciiPath)
        fileCount = len(allFiles)
        time.sleep(5)
        
        count = 0
        while count < fileCount:
            asciiPicture = ''
            frameName = 'frame' + str(count) + '.txt'
            framePath = os.path.join(asciiPath, frameName)
            with open (framePath, 'r', encoding='utf-8') as file:
                for line in file:
                    asciiPicture += line
                    
            count += 1
            
            time.sleep(0.8)
            await message.edit(content=asciiPicture)
            print('Frame', count, '/', fileCount)
        
        await message.delete()   
        DeleteFlies.DeleteAsciiFrames()  
        print('All Finished!')
    
@bot.command(name='reset')
async def resetFiles(command):
    paths = ['./mp4Files', './asciiFrames', './videoFrames']
    for path in paths: 
        DeleteFlies.deleteFiles(path)
    await command.message.delete()
    await command.send('Files reset!')

@bot.command(name='del')
async def deleteMessage(command, *, amount:int = None):
    if amount is None:
        messages = []
        async for message in command.channel.history(limit=2):
            messages.append(message)
        for message in messages:
            await message.delete()
    else:
        await command.channel.purge(limit=amount + 1)
        finishedMessage = 'Finished deleting ' + str(amount) + ' messages!'
        print(finishedMessage)
        await command.send(finishedMessage)
                

bot.run(token)