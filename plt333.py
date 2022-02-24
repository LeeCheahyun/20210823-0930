import matplotlib.pyplot as plt
import cv2

imgBGR1 = cv2.imread('images\cat.bmp')
imgRGB1 = cv2.cvtColor(imgBGR1, cv2.COLOR_BGR2RGB)
imgGray1 = cv2.imread('images\cat.bmp', cv2.IMREAD_GRAYSCALE)

imgBRG2 = cv2.imread('images\penguin.jpg')
imgRGB2 = cv2.cvtColor(imgBRG2, cv2.COLOR_BGR2RGB)
imgGray2 = cv2.imread('images\penguin.jpg', cv2.IMREAD_GRAYSCALE)

plt.subplot(221), plt.axis('off'), plt.imshow(imgRGB1)
plt.subplot(222), plt.axis('off'), plt.imshow(imgGray1, cmap='gray')

plt.subplot(223), plt.axis('off'), plt.imshow(imgRGB2)
plt.subplot(224), plt.axis('off'), plt.imshow(imgGray2, cmap = 'gray')

plt.show()
