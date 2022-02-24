import cv2
import numpy as np
img = np.full((500,500,3),255,dtype=np.uint8)
#color 설정
blue_c = (255,0,0)
red_c = (0,0,255)
cv2.ellipse(img, (250,250),(150,150),0,180,360,red_c,-1)
cv2.ellipse(img, (250,250),(150,150),0,0,180,blue_c,-1)
cv2.ellipse(img, (325,250),(75,75),0,180,360,blue_c,-1)
cv2.ellipse(img, (175,250),(75,75),0,0,180,red_c,-1)
cv2.imshow('태극',img)
cv2.waitKey()
cv2.destroyAllWindows()