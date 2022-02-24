import sys
import cv2

# 영상파일 불러오기
img = cv2.imread('images/cat.jpg', cv2.IMREAD_COLOR)
#img = cv2.imread('images/cat.jpg', cv2.IMREAD_COLOR)
#img = cv2.imread('images/cat.jpg', cv2.IMREAD_COLOR)
print(img.shape)
print(img)
