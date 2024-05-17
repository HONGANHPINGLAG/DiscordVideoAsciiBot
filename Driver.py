import DeleteFlies
import YoutubeToMp4
import ImageToAscii

# link = 'https://youtu.be/9lNZ_Rnr7Jc?si=doHED9zHwVT4Y_Pf'

def Run(link):
    DeleteFlies.DeleteAllFiles()
    
    YoutubeToMp4.DownloadVideo(link)
    print('Finished downloading video')

    ImageToAscii.FrameGrabber()
    print('Finished grabbing frames')
    DeleteFlies.DeleteVideoFile()

    ImageToAscii.ImageResizer()
    print('Finished resizing frames and converting to ascii')
    DeleteFlies.DeleteVideoFrames()

    print('Deleted video and all frames successfully')