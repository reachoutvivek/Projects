import cv2 as cv
import time
start_time=0
curr_time=0
cap = cv.VideoCapture('video1.mp4')
while True:
    success,img=cap.read()
    curr_time = time.time()
    fps=1/(curr_time-start_time)
    start_time=curr_time
    cv.imshow('img',img)
    cv.putText(img,str(int(fps)),(20,40),1,1,(0,255,0),1)

    cv.waitKey(0)
