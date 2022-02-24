import cv2
import glob

img_files = glob.glob('images\*.jpg')

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN,
cv2.WINDOW_FULLSCREEN)
for i in range(len(img_files)):
    image = cv2.imread(img_files[i])
    if image is None:
        print('Image load failed!')
        sys.exit()
    
    cv2.imshow("image", image)
    cv2.waitKey()
cv2.destroyAllWindows()

cnt = len(img_files)
idx = 0
while True:
    img = cv2.imread(img_files[idx])

    if img is None:
        print('Image load failed!')
        break

idx += 1
if idx >= cnt:
    idx = 0