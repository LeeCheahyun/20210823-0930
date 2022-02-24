import cv2, os, sys, datetime ,random, math
import numpy as np
import matplotlib.pyplot as plt
src1 = cv2.imread('images/fig1.png',cv2.IMREAD_COLOR)
src1 = src1[:500,:600,:]
src2 = cv2.imread('images/fig2.png',cv2.IMREAD_COLOR)
src2 = src2[:500,:600,:]
dst =  cv2.absdiff(src1,src2)
titles =['src1','src2','dst'  ]
for t in titles : cv2.imshow(t, eval(t))
cv2.waitKey()
cv2.destroyAllWindows()