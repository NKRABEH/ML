"""
This script convert a video sequence to frames/images.
Change frameRate to modify the frequency of the extracted frames.
"""
import cv2
import sys
import os
import time

video = 'videos/'+str(sys.argv[1])
classe_name = str(sys.argv[2])
save_dir='./Data_processing/'
#starting point in frames
count=0

# capture image in each frameRate second
frameRate = 0.2 

#starting point in the video
sec = 0

try:
    os.mkdir(save_dir+classe_name)
except: 
    count=len(os.listdir(save_dir+classe_name))


vidcap = cv2.VideoCapture(video)
def getFrame(sec,count):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite(save_dir+'/'+classe_name+'/'+classe_name+'{}.jpg'.format(count), image)     # save frame as JPG file
    return hasFrames

success = getFrame(sec,count)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec,count)
    
print( 'Operation completed.') 