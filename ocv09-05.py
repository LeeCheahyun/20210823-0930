import cv2

src1 = cv2.imread('images/lenna_gray.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('images/square.bmp', cv2.IMREAD_GRAYSCALE)

dst1 = cv2.add(src1, src2, dtype=cv2.CV_8U)
dst2 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0.0)
dst3 = cv2.subtract(src1, src2)
dst4 = cv2.absdiff(src1, src2)

titles = ['src1', 'src2', 'dst1', 'dst2', 'dst3', 'dst4']
for t in titles:
    cv2.imshow(t,eval(t))

cv2.waitKey()
cv2.destroyAllWindows()