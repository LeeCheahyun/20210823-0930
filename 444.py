import cv2
img = cv2.imread('images\cat.bmp')
(x , y, z) = img.shape
cv2.imshow('image',img)
cv2.resizeWindow('image',y+100,x+100)
cv2.moveWindow('image',300,300)
cv2.waitKey()
cv2.destroyAllWindows()