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
    
    # Size tuning
    testFrameName = os.path.join(videoFrameDir, allFiles[0].lower())
    testFrame = Image.open(testFrameName).convert('L')
    newFrameSize = getCharAmount(testFrame)
    if newFrameSize[1] > size[1]:
        size = newFrameSize
        
    for frame in allFiles:
        framePath = os.path.join(videoFrameDir, frame.lower())
        oneFrame = Image.open(framePath).convert('L')
        oneFrame.thumbnail(size)
        FrameToAscii(oneFrame, frame, size[0]*2, asciiFrameDir)
        
        
def getCharAmount(frame):
    aspectRatioSizes = [(36, 48), (37, 49), (38, 50), (38, 51), (39, 52)]
    asciiChars = ['░░', '▒▒', '▓▓', '██']
    maxStrSize = 2000
    asciiStrLen = 0
    
    count = 0
    for newSize in aspectRatioSizes:
        asciiStr = ''
        
        testFrame = frame.copy()
        testFrame.thumbnail(newSize)
        
        pixelCount = 0
        pixels = testFrame.getdata()
        for pixel in pixels:
            asciiStr += asciiChars[pixel//64]
            pixelCount += 1
        
        # print('NewSize:', newSize, 'with asciiStr length:', pixelCount*2)

        if len(asciiStr) > maxStrSize:
            print('Size:', aspectRatioSizes[count-1], 'with char count of', str(asciiStrLen))
            return aspectRatioSizes[count-1]
        asciiStrLen = len(asciiStr)
        count += 1  
    print('All aspect ratios did not exceed 2000 characters')
    return aspectRatioSizes[count-1]

    
def FrameToAscii(frame, frameName, lineLength, asciiFrameDir):
    asciiChars = ['░░', '▒▒', '▓▓', '██']
    pixels = frame.getdata()
    asciiStr = ''
    for pixel in pixels:
        asciiStr += asciiChars[pixel//64]
    # print('AsciiStrLen:', len(asciiStr))
    asciiImg = ''
    # print('ASCII STRING SIZE:', str(len(asciiStr)))
    for i in range(0, len(asciiStr), lineLength):
        asciiImg += asciiStr[i:i+lineLength] + '\n'
    
    newFrameName = frameName.split('/')[-1].split('.')[0] + '.txt'
    textFileName = os.path.join(asciiFrameDir, newFrameName)
    with open(textFileName, 'w', encoding='utf-8') as f:
        f.write(asciiImg)