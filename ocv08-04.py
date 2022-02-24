import cv2
import numpy as np
import sys

cap1 = cv2.VideoCapture('videos/video1.mp4')
cap2 = cv2.VideoCapture('videos/video2.mp4')

frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS)
effect_frames = int(fps * 2)
w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

for i in range(frame_cnt1 - effect_frames):
    ret1,frame1 = cap1.read()
    
    cv2.imshow('frame1',frame1)
    
    k=cv2.waitKey(30)
    if k == 27:
        break

for i in range(effect_frames):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    
    dx = int(w * i / effect_frames)
    
    frame = np.zeros((h, w, 3), dtype=np.uint8)
    frame[:, 0:dx, :] = frame2[:, 0:dx, :]
    frame[:, dx:w, :] = frame1[:, dx:w, :]
    
    cv2.imshow('frame1',frame)
    
    k=cv2.waitKey(30)
    if k == 27:
        break    

for i in range(effect_frames, frame_cnt2):
    ret2, frame2 = cap2.read()
    
    cv2.imshow('frame1',frame2)
    
    k=cv2.waitKey(30)
    if k == 27:
        break 

cv2.destroyAllWindows()