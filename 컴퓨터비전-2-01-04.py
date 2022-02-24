import cv2
import numpy as np

#샤프닝
# src = cv2.imread('images/lenna.bmp', cv2.IMREAD_GRAYSCALE)
# mask = np.array([[0, -1, 0],
# [-1, 5, -1],
# [0, -1, 0]])
# dst = cv2.filter2D(src, -1, mask)
# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

#언샤프
# src_f = src.astype(np.float32)
# blr = cv2.GaussianBlur(src_f, (0, 0), 2)
# dst = np.clip(2.0*src_f - blr, 0, 255).astype(np.uint8)
# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

#미디언 필터
# src = cv2.imread('images/lenna_noise.bmp', cv2.IMREAD_GRAYSCALE)
# dst = cv2.medianBlur(src, 3)
# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

#양방향 필터
# src = cv2.imread('images/lenna.bmp')
# dst = cv2.bilateralFilter(src, -1, 20, 5)
# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()