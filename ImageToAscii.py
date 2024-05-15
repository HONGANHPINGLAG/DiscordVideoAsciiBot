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
        if (count % 2) == 0:
            # print('Frame', int(count/2))
            cv2.imwrite(frameName, image) 
        count += 1
        
def DeleteFrames():
    dirPath = './videoFrames'
    allFrames = os.listdir(dirPath)     
    for frame in allFrames:
        framePath = os.path.join(dirPath, frame)
        os.remove(framePath)

def ImageResizer():
    # Image has to be 88x66px for discord bot
    size = (88, 66)
    dirPath = './videoFrames'
    allFrames = os.listdir(dirPath)
    for frame in allFrames:
        fileName = './resizedFrames/' + frame.lower()
        framePath = os.path.join(dirPath, frame.lower())
        oneFrame = Image.open(framePath).convert('L')
        oneFrame.thumbnail(size)
        oneFrame.save(fileName)
    
def PixelToAscii(frame):
    asciiChars = ['⬛', '⬜']
    pixels = frame.getdata()
    asciiStr = ''
    for pixel in pixels:
        asciiStr += asciiChars[pixel//130]
    return asciiStr
    
def FrameToAscii():
    dirPath = './resizedFrames'
    allFrames = os.listdir(dirPath)
    imageSize = [88, 66]
    for frame in allFrames:
        filePath = os.path.join(dirPath, frame.lower())
        oneFrame = Image.open(filePath)
        
        asciiStr = PixelToAscii(oneFrame)
        asciiStrLen = len(asciiStr)
        asciiImg = ''
        for i in range(0, asciiStrLen, imageSize[0]):
            asciiImg += asciiStr[i:i+imageSize[0]] + "\n"
        
        textFileName = './asciiFrames/' + frame.split('.')[0] + '.txt'
        with open(textFileName, 'w') as f:
            f.write(asciiImg)
        