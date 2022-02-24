import numpy as np
import cv2

img = np.full((400, 600, 3), (255, 255, 255), dtype=np.uint8) 

img = cv2.circle(img, (300,200), 100, (0, 0, 255), -1, lineType=None, shift=None)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()