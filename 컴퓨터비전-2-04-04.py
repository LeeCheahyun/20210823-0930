import cv2
import sys
import numpy as np

src = cv2.imread('images/coins.jpg')

src = cv2.resize(src, dsize=(0, 0), fx=0.5, fy=0.5,
interpolation=cv2.INTER_AREA)


gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
blr = cv2.GaussianBlur(gray, (0,0), 1.0)

circles = cv2.HoughCircles(blr, cv2.HOUGH_GRADIENT, 1, 50, param1=120, param2=50, minRadius=30, maxRadius=80)

sum_of_money = 0
dst = src.copy()

if circles is not None:
    for i in range(circles.shape[1]):
        cx, cy, radius = circles[0][i]
        cv2.circle(dst, (int(cx), int(cy)), int(radius), (0,0,255), 2, cv2.LINE_AA)

        x1 = int(cx - radius); y1 = int(cy-radius)
        x2 = int(cx+radius); y2 = int(cy+radius)
        radius = int(radius)

        crop = dst[y1:y2, x1:x2, :]
        ch, cw = crop.shape[:2]

        mask = np.zeros((ch, cw), np.uint8)
        cv2.circle(mask, (cw//2, ch//2), radius, 255, -1)

        hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
        hue, _, _ = cv2.split(hsv)
        hue_shift = (hue + 40) % 180
        mean_of_hue = cv2.mean(hue_shift, mask)[0]

        won = 500
        if mean_of_hue > 140.9:
            won = 500
        elif mean_of_hue > 139.1:
            won = 100
        elif mean_of_hue > 100:
            won = 50
        else:
            won = 10
        sum_of_money += won

        cv2.putText(crop, str(won), (20, 50), cv2.FONT_HERSHEY_SIMPLEX,
        0.75, (255, 0, 0), 2, cv2.LINE_AA)

cv2.putText(dst, str(sum_of_money) + 'won', (40, 80),
            cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, 0), 2, cv2.LINE_AA)
            
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
