import time
import YoutubeToMp4
import ImageToAscii

# link = input('Enter valid Youtube link here: ')
link = 'https://youtu.be/9lNZ_Rnr7Jc?si=doHED9zHwVT4Y_Pf'
YoutubeToMp4.DownloadVideo(link)
print('Finished Downloading')

ImageToAscii.FrameGrabber()
print('Finished grabbing frames')

ImageToAscii.ImageResizer()
print('Finished resizing frames')

ImageToAscii.FrameToAscii()
print('Converted frames to ascii')

time.sleep(30)
YoutubeToMp4.DeleteVideo()
ImageToAscii.DeleteFrames()
print('Deleted video and all frames successfully')