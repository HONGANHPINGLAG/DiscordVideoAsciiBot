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

Setup and code usage: 
Create a bot/application on https://discord.com/developers/applications
Fill in Name, PFP (optional), 
Open Bot and toggle on Presence Intent, Server Members Intent, and Message Content Intent
Also in Bot, copy the token and paste it into DiscordToken.py where the placeholder text is
Open OAuth2 and select Bot in the OAuth2 URL Generator section, then select Administrator in Bot Permissions. Copy the link in the Generated URL at the bottom of the page once Bot and Administrator are selected.
Paste the link into your browser to invite it to your server

Follow instructions at the top of DiscordVideoBot.py

Run DiscordBotVideoDisplay.py to start bot
If you don't want to watch all the way through, press Ctrl+c in the terminal in DiscordBotVideoDisplay.py if using an IDE or stop the program another way, rerun DiscordBotVideoDisplay.py again, then run !reset to delete all hanging files left 
