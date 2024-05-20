# DiscordVideoAsciiBot

Packages/dependencies: 
pytube: pip install pytube
discord: pip install discord.py
cv2: pip install opencv-python
PIL: pip install pillow

Bot usage: 
!run <link> will download the link to an mp4, resize, convert to ascii, then play in Discord in the channel the bot was called

!reset will clear the folders of files if the program gets interrupted, breaks, or stopped midway

!del will delete the command message and the message before it
!del <number> will delete the command message and the number of messages specified before the call

Code usage: 
Run DiscordBotVideoDisplay.py to start bot
If you don't want to watch all the way through, press Ctrl+c in the terminal in DiscordBotVideoDisplay.py, rerun the bot again, then run !reset to delete all hanging files left
