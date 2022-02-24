import cv2
import numpy as np

img1 = np.empty((240, 320), dtype=np.uint8) # grayscale image
img2 = np.zeros((240, 320, 3), dtype=np.uint8) # color image
img3 = np.ones((240, 320), dtype=np.uint8) * 255 # dark gray
img4 = np.full((240, 320, 3), (0, 255, 255), dtype=np.uint8) # yellow
print(type(img1))
print(img1.ndim)
print(img1.shape)
print(img1.size)
print(img1.dtype)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.waitKey()
cv2.destroyAllWindows()