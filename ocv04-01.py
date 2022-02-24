import numpy as np
import cv2

img = np.zeros((512,512,3), dtype=np.uint8)

cv2.line(img,(0,0),(511,511),(255,100,163),1)

cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()