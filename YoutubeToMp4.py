# Allows you to insert the Youtube link of the video that you want to run the bot with
# Solution found from https://stackoverflow.com/a/74275320
from pytube import YouTube
import os
import time

def DownloadVideo(link):
    yt = YouTube(link)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').get_by_resolution('360p')
    yt.download(filename='video.mp4', output_path='./mp4Files')
    
def DeleteVideo():
    time.sleep(10)
    os.remove('./mp4Files/video.mp4')
    # print('Deleted video')