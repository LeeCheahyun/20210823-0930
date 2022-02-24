import cv2
import numpy as np
import random
oldx = oldy = -1
img = np.ones((480, 640, 3), dtype=np.uint8) * 255
def on_mouse(event, x, y, flags, param):
    global oldx, oldy
    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), random.randint(10,100), (random.randint(10,255),random.randint(10,255),random.randint(10,255)), -1)
        cv2.imshow('image', img)
cv2.imshow('image', img)
cv2.setMouseCallback('image', on_mouse, img)
cv2.waitKey()

