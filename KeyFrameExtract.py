#!/bin/python3
# Made by YHJ
# Code & ETC reference writed in README.md file

import sys, os
import cv2
from matplotlib import pyplot as plt
import numpy as np
import glob
## init settings
# set variable
# check enviroment
outputFolderName = "resultFolder"
videoFileName = sys.argv[1]
## openCV variable set
OPENCV_METHODS = (
    (cv2.HISTCMP_CORREL ),
    (cv2.HISTCMP_CHISQR),
    (cv2.HISTCMP_INTERSECT), 
    (cv2.HISTCMP_BHATTACHARYYA)
)
def Initialize():
    if ( len(sys.argv) != 2 ):
        print("** ERROR arg")
        print("you have to use like this__")
        print("python KeyFrameExtract.py sample.mp4")
        exit()
    if ( not os.path.exists(outputFolderName) ):
        os.makedirs(outputFolderName)
    if ( not os.listdir(outputFolderName) ):
        print("** ERROR Result Directory is not empty so you should be backup or delete data in resultFolder")
        exit()

def Extraction():
    print("video file extraction running...")
    video = cv2.VideoCapture(videoFileName)
    frame_list = []
    cframe = 0
    while(True):
        ret, frame = video.read()
        filename = "${outputFolderName}/{0}.jpg".format(str(cframe))
        cv2.imwrite(filename, frame)
        frame_list.append(frame)
        cframe += 1
        if not ret:
            break
    images = {}
    index = {}
    for imagePath in glob.glob('./${outputFolderName}/*.jpg'):
        filename = imagePath[imagePath.rfind("/") + 1:]
        image = cv2.imread(imagePath,1)
        images[filename] = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        hist = cv2.calcHist([image],[0,1,2],None,[8,8,8],[0,256,0,256,0,256])
        hist = cv2.normalize(hist,None).flatten()
        index[filename] = hist

    for method in OPENCV_METHODS:
        results = {}
        reverse = False
        if method in (cv2.HISTCMP_CORREL, cv2.HISTCMP_INTERSECT ):
            reverse = True
    
    for (k, hist) in index.items():
            d = cv2.compareHist(index[k], hist, cv2.HISTCMP_INTERSECT)
            results[k] = d
            print(d)
        
    for (k,hist) in index.items():
        mean__ = np.mean(index[k], dtype=np.float64)

    for (k,hist) in index.items():
        variance = np.var(index[k], dtype=np.float64)

    print("variance", variance)
            
    standard_deviation = np.sqrt(variance)
    th = mean__ + standard_deviation + 3
    print("threshold value", th)

    try:
        if not os.path.exists('keyframes'):
            os.makedirs('keyframes')
    except OSError:
        print("Error cant make directories")

    cframe1=0
    for (k,hist) in index.items():
            d = cv2.compareHist(index[k], hist, cv2.HISTCMP_INTERSECT)
            ret, keyframe = video.read()
            if not ret:
                    break
            if (d > th):
                    name = './keyframes/' + str(cframe1) + '.jpg'
                    print("creating" +name)
                    cv2.imwrite(name, keyframe )
                    cframe1+=1

if __name__ == "main":
    print("Extraction KeyFrame from video" + videoFileName )
    Initialize()
    Extraction()