import cv2
import numpy as np

def on_levelb(pos):
    img[:,:,0] = pos
    cv2.imshow('image',img)

def on_levelg(pos):
    img[:,:,1] = pos
    cv2.imshow('image',img)

def on_levelr(pos):
    img[:,:,2] = pos
    cv2.imshow('image',img)

img = np.zeros((480,640,3),np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('blue','image',0,255,on_levelb)
cv2.createTrackbar('green','image',0,255,on_levelg)
cv2.createTrackbar('red','image',0,255,on_levelr)

cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()