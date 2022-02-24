import time
import numpy as np
import cv2
cap = cv2.VideoCapture('videos/india.mp4')
tm = cv2.TickMeter()
tm.reset()
tm.start()
t1 = time.time()
while True:
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(10)==27:
        break
cap.release()
tm.stop()
cv2.destroyAllWindows()
print('time:',(time.time()- t1)*1000)
print('Elapsed time: {}ms.'.format(tm.getTimeMilli()))