import cv2

src1 = cv2.imread('images/paris1.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('images/paris2.bmp', cv2.IMREAD_GRAYSCALE)

dst = cv2.absdiff(src1, src2)

cv2.imshow('dst',dst)

cv2.waitKey()
cv2.destroyAllWindows()