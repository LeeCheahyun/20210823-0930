import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('images/lenna.bmp', cv2.IMREAD_COLOR)
img2 = np.zeros((480, 640, 3), np.uint8)
img3 = cv2.imread('images/lenna.bmp', cv2.IMREAD_GRAYSCALE)
img4 = cv2.cvtColor(img3, cv2.COLOR_GRAY2BGR)

plt.subplot(221), plt.axis('off'), plt.imshow(img1), plt.title('img1')
plt.subplot(222), plt.axis('off'), plt.imshow(img2), plt.title('img2')
plt.subplot(223), plt.axis('off'), plt.imshow(img3), plt.title('img3')
plt.subplot(224), plt.axis('off'), plt.imshow(img4), plt.title('img4')
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()