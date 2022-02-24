import sys
import cv2
import numpy as np

#침식과 팽창
# src = cv2.imread('images/morph.jpg', cv2.IMREAD_GRAYSCALE)
# se = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# dst1 = cv2.erode(src, se)
# dst2 = cv2.dilate(src, None)
# cv2.imshow('src', src)
# cv2.imshow('dst1', dst1)
# cv2.imshow('dst2', dst2)
# cv2.waitKey()
# cv2.destroyAllWindows()

#열기와 닫기
src = cv2.imread('images/morph.jpg', cv2.IMREAD_GRAYSCALE)
dst1 = np.zeros(src.shape, np.uint8)

bw = src.shape[1] // 4
bh = src.shape[0] //
for y in range(4):
    for x in range(4):
        src_ = src[y*bh:(y+1)*bh, x*bw:(x+1)*bw]
        dst_ = dst1[y*bh:(y+1)*bh, x*bw:(x+1)*bw]
        cv2.threshold(src_, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU, dst_)
cnt1, _ = cv2.connectedComponents(dst1)
print('cnt1:', cnt1)
dst2 = cv2.morphologyEx(dst1, cv2.MORPH_OPEN, None)
cnt2, _ = cv2.connectedComponents(dst2)
print('cnt2:', cnt2)
cv2.waitKey()
cv2.destroyAllWindows()