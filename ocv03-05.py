import cv2
import numpy as np

src = cv2.imread('images/airplane.bmp', cv2.IMREAD_COLOR)

mask = np.zeros_like(src)
#cv2.circle(mask, (380,210), 100, (255,255,255), -1)
cv2.rectangle(mask, (100,100), (550, 300), (255,255,255), -1)
masked = cv2.bitwise_and(src, mask)
dst = cv2.imread('images/field.bmp', cv2.IMREAD_COLOR)
cv2.copyTo(src, mask, dst)

#mask = cv2.imread('images/mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
#dst = cv2.imread('images/field.bmp', cv2.IMREAD_COLOR)
#cv2.copyTo(src, mask, dst)

cv2.imshow('src', src)
cv2.imshow('mask', mask)
cv2.imshow('masked', masked)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()