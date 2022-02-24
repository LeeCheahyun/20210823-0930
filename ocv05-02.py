import cv2


cap = cv2.VideoCapture('videos/video1.mp4') # 비디오 열기
fps = round(cap.get(cv2.CAP_PROP_FPS))
delay = round(1000 / fps)
while True: # 카메라 프레임 처리
    ret, frame = cap.read()
    inversed = ~frame # 반전
    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)
    if cv2.waitKey(10) == 27:
        break
cap.release()
cv2.destroyAllWindows()