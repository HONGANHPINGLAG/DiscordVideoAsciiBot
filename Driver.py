import os
import time
import DeleteFlies
import YoutubeToMp4
import ImageToAscii

# link = 'https://youtu.be/9lNZ_Rnr7Jc?si=doHED9zHwVT4Y_Pf'

mp4Dir = './mp4Files'
videoFrameDir = './videoFrames'
asciiFrameDir = './asciiFrames'
os.makedirs(mp4Dir, exist_ok=True)
os.makedirs(videoFrameDir, exist_ok=True)
os.makedirs(asciiFrameDir, exist_ok=True)

def Run(link):
    DeleteFlies.DeleteAllFiles()
    
    YoutubeToMp4.DownloadVideo(link, mp4Dir)
    print('Finished downloading video')

    ImageToAscii.FrameGrabber(mp4Dir, videoFrameDir)
    time.sleep(0.25)
    print('Finished grabbing frames')
    DeleteFlies.DeleteVideoFile()

    ImageToAscii.ImageResizer(videoFrameDir, asciiFrameDir)
    time.sleep(0.25)
    print('Finished resizing frames and converting to ascii')
    DeleteFlies.DeleteVideoFrames()

    print('Deleted video and all frames successfully')