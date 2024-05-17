import os
import cv2
from PIL import Image

def FrameGrabber(mp4Dir, videoFrameDir): 
    vidObj = cv2.VideoCapture(os.path.join(mp4Dir, 'video.mp4'))  
    count = 0
    success = 1
    while success: 
        success, image = vidObj.read() 
        if not success:
            break
        
        frameName = os.path.join(videoFrameDir, 'frame' + str(int(count/2)) + '.jpg')        
        # Only downloads every other frame, reducing framerate by 1/2 for storage and time reasons
        if (count % 2) == 0:
            cv2.imwrite(frameName, image) 
        count += 1

def ImageResizer(videoFrameDir, asciiFrameDir):
    size = (36, 48)
    allFiles = os.listdir(videoFrameDir)
    for frame in allFiles:
        framePath = os.path.join(videoFrameDir, frame.lower())
        oneFrame = Image.open(framePath).convert('L')
        oneFrame.thumbnail(size)
        FrameToAscii(oneFrame, frame, size[0]*2, asciiFrameDir)
    
def FrameToAscii(frame, frameName, lineLength, asciiFrameDir):
        asciiChars = ['░░', '▒▒', '▓▓', '██']
        pixels = frame.getdata()
        asciiStr = ''
        for pixel in pixels:
            asciiStr += asciiChars[pixel//64]
    
        asciiImg = ''
        for i in range(0, len(asciiStr), lineLength):
            asciiImg += asciiStr[i:i+lineLength] + '\n'
        
        newFrameName = frameName.split('/')[-1].split('.')[0] + '.txt'
        textFileName = os.path.join(asciiFrameDir, newFrameName)
        with open(textFileName, 'w') as f:
            f.write(asciiImg)