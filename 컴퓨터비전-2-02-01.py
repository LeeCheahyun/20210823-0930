import cv2
import numpy as np

#소벨필터미분
# src = cv2.imread('images/lenna.bmp', cv2.IMREAD_GRAYSCALE)
# dx = cv2.Sobel(src, -1, 1, 0, delta=128)
# dy = cv2.Sobel(src, -1, 0, 1, delta=128)
# cv2.imshow('src', src)
# cv2.imshow('dx', dx)
# cv2.imshow('dy', dy)
# cv2.waitKey()
# cv2.destroyAllWindows()

#소벨필터에지검출
# src = cv2.imread('images/lenna.bmp', cv2.IMREAD_GRAYSCALE)
# dx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
# dy = cv2.Sobel(src, cv2.CV_32F, 0, 1)
# mag = cv2.magnitude(dx, dy)
# mag = np.clip(mag, 0, 255).astype(np.uint8)
# dst = np.zeros(src.shape[:2], np.uint8)
# dst[mag > 120] = 255
# cv2.imshow('src', src)
# cv2.imshow('mag', mag)
# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

#케니에지검출
# src = cv2.imread('images/lenna.bmp', cv2.IMREAD_GRAYSCALE)
# dst = cv2.Canny(src, 50, 150)
# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

#케니컬러에지검출
def onTrackbar(th):
    rep_edge = cv2.Canny(rep_gray, th, th*2, 5)
    h, w = src.shape[:2]
    cv2.rectangle(rep_edge, (0, 0, w, h), 255, -1)
    color_edge = cv2.bitwise_and(rep_img, rep_img, mask=rep_edge)
    cv2.imshow("color edge", color_edge)
src = cv2.imread('images/lenna.bmp', cv2.IMREAD_COLOR)
th = 50
rep_img = cv2.repeat(src, 1, 2)
rep_gray = cv2.cvtColor(rep_img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow("color edge", cv2.WINDOW_NORMAL)
cv2.createTrackbar("Canny th", "color edge", th, 100, onTrackbar)
onTrackbar(th)
cv2.waitKey()
cv2.destroyAllWindows()

