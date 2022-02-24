import cv2

cap = cv2.VideoCapture(0) # 카메라 열기

while True: # 카메라 프레임 처리
    ret, frame = cap.read()
    inversed = ~frame # 반전
    
    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)

    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()