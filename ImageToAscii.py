import os
import cv2
from PIL import Image

def FrameGrabber(): 
    vidObj = cv2.VideoCapture("./mp4Files/video.mp4")  
    count = 0
    success = 1
    while success: 
        frameName = './videoFrames/frame' + str(int(count/2)) + '.jpg'
        success, image = vidObj.read() 
        # Only downloads every other frame, reducing framerate by 1/2 for storage and time reasons
        if (count % 2) == 0:
            cv2.imwrite(frameName, image) 
        count += 1

def ImageResizer():
    size = (36, 48)
    dirPath = './videoFrames'
    allFiles = os.listdir(dirPath)
    for frame in allFiles:
        framePath = os.path.join(dirPath, frame.lower())
        oneFrame = Image.open(framePath).convert('L')
        oneFrame.thumbnail(size)
        FrameToAscii(oneFrame, frame, size[0]*2)
    
def FrameToAscii(frame, frameName, lineLength):
        asciiChars = ['░░', '▒▒', '▓▓', '██']
        pixels = frame.getdata()
        asciiStr = ''
        for pixel in pixels:
            asciiStr += asciiChars[pixel//64]
    
        asciiImg = ''
        for i in range(0, len(asciiStr), lineLength):
            asciiImg += asciiStr[i:i+lineLength] + '\n'
        
        newFrameName = frameName.split('/')[-1].split('.')[0]
        textFileName = './asciiFrames/' + newFrameName + '.txt'
        with open(textFileName, 'w') as f:
            f.write(asciiImg)