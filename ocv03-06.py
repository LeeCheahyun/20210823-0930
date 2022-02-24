import cv2
import numpy as np

src = cv2.imread('images/cat.bmp', cv2.IMREAD_COLOR)
logo = cv2.imread('images/mcdonald.png', cv2.IMREAD_UNCHANGED)

mask = logo[:, :, 3] # mask는 알파 채널로 만든 마스크 영상
logo = logo[:, :, :-1] # logo는 b, g, r 3채널로 구성된 컬러 영상
h, w = mask.shape[:2]
crop = src[10:10+h, 10:10+w] # logo, mask와 같은 크기의 부분 영상 추출

cv2.copyTo(logo, mask, crop)

cv2.imshow('src', src)

cv2.waitKey()
cv2.destroyAllWindows()