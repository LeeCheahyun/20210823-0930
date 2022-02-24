import sys
import cv2

img1 = cv2.imread('images\cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imwrite('images/cat_gray.jpg', img1, [cv2.IMWRITE_JPEG_QUALITY, 90])

if img2 is None:
    print('Image save gailed!')
    sys.exit()

image = cv2.imread('images/cat_gray.jpg')
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()