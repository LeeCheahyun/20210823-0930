import cv2
import numpy as np

def on_level_change(pos):
    value = pos * 1
    if value >= 255:
        value = 255

    img[:] = value
    cv2.imshow('image', img)

img = np.full((480, 640, 3), (0, 0, 0), dtype=np.uint8) 
cv2.namedWindow('image')
cv2.createTrackbar('level', 'image', 0, 255, on_level_change)

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()

