import cv2

cap = cv2.VideoCapture(0)
file = 'photo.jpg'

while True:
    ret, frame = cap.read()
   
    cv2.rectangle(frame, (180,90),(500,400),(255,255,255),3)
    
    cv2.imshow('frame', frame)
    key =cv2.waitKey(10)
    if key == 27:
        break
    elif key == 13 :
        img_frame = frame.copy()
        img_size = img_frame[90:400, 180:500]
        cv2.imwrite(file, img_size)
        print(file, '저장됨')

cap.release()
cv2.destroyAllWindows()