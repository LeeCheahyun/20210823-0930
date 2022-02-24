import cv2
import numpy as np

image = np.zeros((300,400), np.uint8)
image.fill(200)

cv2.imshow('window title', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#------------------------------------------------------------
import sys
import cv2

print('Hello OpenCV', cv2.__version__)

image = cv2.imread('images\cat.bmp', cv2.IMREAD_COLOR)
#image = cv2.imread('images\cat.bmp', cv2.IMREAD_GRAYSCALE)
#image = cv2.imread('images\cat.bmp', cv2.IMREAD_UNCHANGED)
print(image.shape)
print(image)

if image is None:
    print('Image load failed!')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image', image)
cv2.waitKey()

cv2.destroyAllWindows()
#--------------------------------------------------------------
img1 = cv2.imread('images/cat.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imwrite('images/cat_gray.jpg', img1, [cv2.IMWRITE_JPEG_QUALITY, 90])

if img2 is None:
    print('Image save gailed!')
    sys.exit()