import cv2
import numpy as np

src = cv2.imread('images/lenna.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.add(src, 100)
dst2 = cv2.add(src, (100,100,100,0))
dst3 = cv2.add(src + 100.,0,255).astype(np.uint8)

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.imshow('dst2',dst2)
cv2.imshow('dst3',dst3)


cv2.waitKey()
cv2.destroyAllWindows()