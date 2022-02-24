import sys
import cv2


cap = cv2.VideoCapture(0)
w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # *'DIVX' == 'D','I','V','X'
out = cv2.VideoWriter('output.avi', fourcc, 24, (w, h))
while True: # 카메라 프레임 처리
    ret, frame = cap.read()
    
   
    dst = cv2.Canny(frame, 120, 180)
    out1 = 255- dst
    

    #inversed = ~frame # 반전
    out.write(frame)
    
    cv2.imshow('frame', frame)
    cv2.imshow('dst', dst)
    cv2.imshow('out', out1)
    #cv2.imshow('inversed', inversed)
    
    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.waitKey()
cv2.destroyAllWindows()