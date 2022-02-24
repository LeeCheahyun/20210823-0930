import cv2
import numpy as np
import sys

#이동
# src = cv2.imread('images/parasol.jpg')

# if src is None:
#     print('Image load failed!')
#     sys.exit()

# aff = np.array([[1,0,200],[0,1,100]], dtype=np.float32)

# dst = cv2.warpAffine(src, aff, (0,0))

# cv2.imshow('src',src)
# cv2.imshow('dst', dst)

# cv2.waitKey()
# cv2.destroyAllWindows()

#전단
# src = cv2.imread('images/parasol.jpg')

# if src is None:
#     print('Image load failed!')
#     sys.exit()

# aff = np.array([[1, 0.5, 0],
# [0, 1, 0]], dtype=np.float32)

# h, w = src.shape[:2]
# dst = cv2.warpAffine(src, aff, (w + int(h * 0.5), h))

# cv2.imshow('src', src)
# cv2.imshow('dst', dst)

# cv2.waitKey()
# cv2.destroyAllWindows()

#확대

# src = cv2.imread('images/rose.bmp')

# dst1 = cv2.resize(src,(0,0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
# dst2 = cv2.resize(src,(1920,1280))
# dst3 = cv2.resize(src,(1920,1280), interpolation=cv2.INTER_CUBIC)
# dst4 = cv2.resize(src, (1920,1280), interpolation=cv2.INTER_LANCZOS4)

# cv2.imshow('src',src)
# cv2.imshow('dst1', dst1[500:900, 400:800])
# cv2.imshow('dst2', dst2[500:900, 400:800])
# cv2.imshow('dst3', dst3[500:900, 400:800])
# cv2.imshow('dst4', dst4[500:900, 400:800])
# cv2.waitKey()
# cv2.destroyAllWindows()

#대칭
# src = cv2.imread('images/airplane.bmp')

# dst1 = cv2.flip(src, 1) # 좌우 대칭
# dst2 = cv2.flip(src, 0) # 상하 대칭
# dst3 = cv2.flip(src,-1) # 좌우&상하 대칭

# cv2.imshow('src', src)
# cv2.imshow('dst1', dst1)
# cv2.imshow('dst2', dst2)
# cv2.imshow('dst3', dst3)

# cv2.waitKey()
# cv2.destroyAllWindows()

#피라미드
# src = cv2.imread('images/butterfly.jpg')
# rc = (280, 150, 200, 200) # rectangle tuple
# # 원본 영상에 그리기
# cpy = src.copy()
# cv2.rectangle(cpy, rc, (0, 0, 255 ), 2)
# cv2.imshow('src', cpy)
# cv2.waitKey()
# # 피라미드 영상에 그리기
# for i in range(1, 4):
#     src = cv2.pyrDown(src)
#     cpy = src.copy()
#     cv2.rectangle(cpy, rc, (0, 0, 255), 2, shift=i)
#     cv2.imshow('src', cpy)
#     cv2.waitKey()
#     cv2.destroyWindow('src')
# cv2.destroyAllWindows()

#영상의 회전
# import math
# src = cv2.imread('images/parasol.jpg')

# if src is None:
#     print('Image load failed!')
#     sys.exit()

# rad = 20 * math.pi / 180
# aff = np.array([[math.cos(rad), math.sin(rad),0], [-math.sin(rad), math.cos(rad),0]], dtype=np.float32)

# dst = cv2.warpAffine(src, aff, (0,0))

# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

#중앙회전
# import math
# src = cv2.imread('images/parasol.jpg')
# if src is None:
#     print('Image load failed!')
#     sys.exit()
# cp = (src.shape[1] / 2, src.shape[0] / 2)
# rot = cv2.getRotationMatrix2D(cp, 20, 1)
# dst = cv2.warpAffine(src, rot, (0, 0))
# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

#투시변환(찌그러진 명함)
# src = cv2.imread('images/namecard.jpg')

# if src is None:
#     print('Image load failed!')
#     sys.exit()

# w,h = 720, 400
# srcQuad = np.array([[164, 112], [608,167], [560,310], [103,250]], np.float32)
# dstQuad = np.array([[0,0], [w-1,0], [w-1,h-1], [0, h-1]], np.float32)

# pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
# dst = cv2.warpPerspective(src, pers, (w,h))

# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

