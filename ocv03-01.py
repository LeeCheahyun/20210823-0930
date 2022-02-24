import cv2

img1 = cv2.imread('images\cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('images\cat.bmp', cv2.IMREAD_COLOR)

print(type(img1))
print(img1.ndim)
print(img1.shape)
print(img1.size)
print(img1.dtype)


h, w = img2.shape[:2]
print('img2 size: {} * {}'.format(w, h))

if len(img1.shape) == 2:
    print('img1 is a grayscale image')

elif len(img1.shape) == 3:
    print('img1 is a truecolor image')