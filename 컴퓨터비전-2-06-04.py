import numpy as np
import cv2
import sys

digits = cv2.imread('images/digits.png', cv2.IMREAD_GRAYSCALE)
h, w = digits.shape[:2]
hog = cv2.HOGDescriptor((20, 20), (10, 10), (5, 5), (5, 5), 9)
print('Descriptor Size:', hog.getDescriptorSize())
cells = [np.hsplit(row, w//20) for row in np.vsplit(digits, h//20)]
cells = np.array(cells)
cells = cells.reshape(-1, 20, 20) # shape=(5000, 20, 20)
desc = []
for img in cells:
    desc.append(hog.compute(img))
train_desc = np.array(desc)
train_desc = train_desc.squeeze().astype(np.float32)
train_labels = np.repeat(np.arange(10), len(train_desc)/10)
print('train_desc.shape:', train_desc.shape)
print('train_labels.shape:', train_labels.shape)

train_images = cells.reshape(-1, 400).astype(np.float32)
train_labels = np.repeat(np.arange(10), len(train_images)/10)

knn = cv2.ml.KNearest_create()
knn.train(train_images, cv2.ml.ROW_SAMPLE, train_labels)

img = np.zeros((400, 400), np.uint8)

oldx = oldy = -1
def on_mouse(event, x, y, flags, param):
    global oldx, oldy
    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (255, 255, 255), 20, cv2.LINE_AA)
            cv2.imshow('img', img)
            oldx, oldy = x, y
            
cv2.imshow('img', img)
cv2.setMouseCallback('img', on_mouse)

while True:
    key = cv2.waitKey()
    if key == 27:
        break
    elif key == ord(' '): 
        test_image = cv2.resize(img, (20, 20), interpolation=cv2.INTER_AREA)
        test_image = test_image.reshape(-1, 400).astype(np.float32)
        ret, _, _, _ = knn.findNearest(test_image, 5)
        print(f'분류된 결과 숫자는: {int(ret)}')
        img.fill(0)
        cv2.imshow('img', img)

cv2.destroyAllWindows()

