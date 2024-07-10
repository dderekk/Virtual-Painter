import cv2
import numpy as np
import time
import os
import HandTrack as htm

foldPath = "src/header"
myList = os.listdir(foldPath) #['1.jpg', '2.jpg', '3.jpg', '4.jpg']
overlayList = []

for imPath in myList:
    image = cv2.imread(f'{foldPath}/{imPath}')
    overlayList.append(image)

header = overlayList[0]
drawColor = (255, 0, 255)

cap=cv2.VideoCapture(0)

cap.set(3,1280) #size of camera/image shows, 3 is  width
cap.set(4,720)  #4 is height

detector = htm.handDetector(detectionConf=0.75)
xperi, yperi = 0,0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)

brushThickness = 15
eraserThickness = 80

while True:

    # 1. Import image
    success, img = cap.read()
    img = cv2.flip(img,1) # flip image mirror q

    # 2. find hand landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw=False)

    if len(lmList) != 0:
        # tip of index and middle fingers
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        #thumb tip
        x0, y0 = lmList[4][1:]
        #pinky tip
        x4, y4 = lmList[20][1:]



        # 3. check which fingers are up
        fingers = detector.fingersUp()

        # 4. if selection mode - two finger are up

        if fingers[1] and fingers[2]:
            xperi, yperi = 0, 0
            cv2.circle(img, ((x2+x1)//2, (y2+y1)//2), 50, drawColor, 1, cv2.LINE_4)
            # checking click
            if y1<125:
                if 250<x1<450:
                    header = overlayList[0]
                    drawColor = (255, 0, 255)
                elif 550< x1 <750:
                    header = overlayList[1]
                    drawColor = (255, 0, 0)
                elif 800 < x1 < 950:
                    header = overlayList[2]
                    drawColor = (0, 255, 0)
                elif 1050 < x1 < 1200:
                    header = overlayList[3]
                    drawColor = (0, 0, 0)

            print("slection Mode")


        # 5. if drawing mode - index finger is up
        if fingers[1] and fingers[2] == False:
            cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
            print("draw mode")
            if xperi ==0 and yperi ==0:
                xperi, yperi = x1, y1

            if drawColor == (0,0,0):
                cv2.line(img, (xperi, yperi), (x1, y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xperi, yperi), (x1, y1), drawColor, eraserThickness)
            else:
                cv2.line(img, (xperi, yperi), (x1,y1), drawColor, brushThickness)
                cv2.line(imgCanvas, (xperi, yperi), (x1, y1), drawColor, brushThickness)

            xperi, yperi = x1, y1

        if fingers[0] == False and fingers[4] and fingers[1]== False and fingers[2]== False:
            xperi, yperi = 0, 0
            cv2.circle(img, ((x0+x4)//2, (y0+y4)//2), abs(x0-x4), drawColor, cv2.FILLED)
            if drawColor == (0, 0, 0):
                eraserThickness = abs(x0-x4)
            else:
                brushThickness = abs(x0-x4)

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img,imgInv)
    img = cv2.bitwise_or(img,imgCanvas)


    # set header image
    img[0:130,0:1280] = header #slice the image, put the header in this area
    #img = cv2.addWeighted(img,0.5,imgCanvas,0.5,0) #add two image together !!

    cv2.imshow("image",img)
    #cv2.imshow("imageCanvas", imgCanvas)
    cv2.waitKey(1)

    if cv2.waitKey(1) == ord('q'):
        break

