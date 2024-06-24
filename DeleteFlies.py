import os
    
def deleteFiles(dirPath):
    allframes = os.listdir(dirPath)
    if len(allframes) > 0:
        for eachFrame in allframes:
            framePath = os.path.join(dirPath, eachFrame)
            os.remove(framePath)

def DeleteAllFiles():
    print('\nDeleting all files')
    
    # Removing source video.mp4 file
    videoPath = './mp4Files/video.mp4'
    if os.path.isfile(videoPath): 
        os.remove(videoPath)
    
    # Removing all of the files from the videoFrames, resizedFrames, and asciiFrames folders
    framePaths = ['./videoFrames', './asciiFrames']
    for path in framePaths:
        deleteFiles(path)
    
    print('Successfully deleted all files\n')


def DeleteVideoFile():
    videoPath = os.path.join('./mp4Files', 'video.mp4')
    os.remove(videoPath)
    print('Removed video file\n')
    

def DeleteVideoFrames():
    deleteFiles('./videoFrames')
    print('Removed video frames\n')

def DeleteAsciiFrames():
    deleteFiles('./asciiFrames')
    print('Removed ascii frames\n')