import cv2
import os
import sys
file_list = os.listdir('images')
img_files = [file for file in file_list if file.endswith('.jpg')]
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
while True:
    for img  in file_list:
        image = cv2.imread('images/'+ img)
        cv2.imshow('image',image)
        key = cv2.waitKey(1000)
        if key == 27 :
            break
        elif key == ord('s') or key == ord('S'):
            img = ~img # ~ : NOT
            cv2.imshow('image', img)
cv2.destroyAllWindows()
