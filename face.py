#!/usr/bin/python
import Image
import sys
import cv2.cv as cv
import string
from random import randrange
data = sys.stdin.read()

imgarray = ("/home/spy/facedetect-and-replace/images/comeon.png", "/home/spy/facedetect-and-replace/images/foreveralone.png", "/home/spy/facedetect-and-replace/images/happysmile.png", "/home/spy/facedetect-and-replace/images/herpderp.png", "/home/spy/facedetect-and-replace/images/lol.png", "/home/spy/facedetect-and-replace/images/megusta.png", "/home/spy/facedetect-and-replace/images/okay.png", "/home/spy/facedetect-and-replace/images/pokerface.png", "/home/spy/facedetect-and-replace/images/troll.png")
im = cv.LoadImageM(data)
storage = cv.CreateMemStorage()
haar=cv.Load("/home/spy/facedetect-and-replace/haarcascade_frontalface_default.xml")
detected = cv.HaarDetectObjects(im, haar, storage, 1.1, 2,cv.CV_HAAR_DO_CANNY_PRUNING,(10,10))

i = 0
doneIm = Image.open(data)
if detected:
    for face in detected:
	irand = randrange(0,5)
	imageFile = imgarray[irand]
	trollface = Image.open(imageFile)
        i= i + 1
	xx = face[0][0]
        yy = face[0][1]
        width = face[0][2]
        height = face[0][3]

        trollresize = trollface.resize((width, height), Image.ANTIALIAS)
        doneIm.paste(trollresize, (xx,yy), mask=trollresize)

doneIm.save(data, "JPEG")
print(data+" is done, "+str(i)+"faces detected.")
