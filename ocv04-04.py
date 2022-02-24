import cv2
import numpy as np

img = cv2.imread('images\catcat.jpg')

red = (0, 0, 255)
black = (0,0,0)

cv2.rectangle(img,(365, 52),(462,150),red,2)
cv2.rectangle(img,(364, 30),(463,50),red,-1)

text = "cat"
cv2.putText(img, text, (365,50), cv2.FONT_HERSHEY_DUPLEX, 0.8, black, 1, cv2.LINE_AA)

cv2.imshow('cat',img)
cv2.waitKey()
cv2.destroyAllWindows()