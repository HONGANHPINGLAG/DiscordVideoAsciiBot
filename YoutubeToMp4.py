# Allows you to insert the Youtube link of the video that you want to run the bot with
from pytube import YouTube

def DownloadVideo(link, outputPath):
    yt = YouTube(link)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').get_by_resolution('360p')
    yt.download(filename='video.mp4', output_path=outputPath)
    