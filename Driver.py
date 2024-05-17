import os
import DeleteFlies
import YoutubeToMp4
import ImageToAscii

# link = 'https://youtu.be/9lNZ_Rnr7Jc?si=doHED9zHwVT4Y_Pf'

def Run(link):
    mp4Dir = './mp4Files'
    videoFrameDir = './videoFrames'
    asciiFrameDir = './asciiFrames'
    os.makedirs(mp4Dir, exist_ok=True)
    os.makedirs(videoFrameDir, exist_ok=True)
    os.makedirs(asciiFrameDir, exist_ok=True)
    
    DeleteFlies.DeleteAllFiles()
    
    YoutubeToMp4.DownloadVideo(link, mp4Dir)
    print('Finished downloading video')

    ImageToAscii.FrameGrabber(mp4Dir, videoFrameDir)
    print('Finished grabbing frames')
    DeleteFlies.DeleteVideoFile()

    ImageToAscii.ImageResizer(videoFrameDir, asciiFrameDir)
    print('Finished resizing frames and converting to ascii')
    DeleteFlies.DeleteVideoFrames()

    print('Deleted video and all frames successfully')