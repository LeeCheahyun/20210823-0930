import cv2
import numpy as np

img1 = cv2.imread('images\cat.jpg')
img2 = img1[20:400, 250:700] # numpy.ndarray의 슬라이싱
img3 = img1[20:400, 250:700].copy()
img2.fill(0)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2) # 검은색
cv2.imshow('img3', img3) # 부분 이미지
cv2.waitKey()
cv2.destroyAllWindows()
