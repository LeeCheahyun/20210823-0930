import cv2
import mediapipe as mp
import time, datetime, numpy as np

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

x = datetime.datetime.now().strftime('%Y-%m-%d %H %M')

file = f'photo{x}.jpg'

def color_quantization(img, k): # 색상 양자화 (색상 수 줄이기)

  data = np.float32(img).reshape((-1, 3))
  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 1, 0.001)
  ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
  center = np.uint8(center)
  result = center[label.flatten()]
  result = result.reshape(img.shape)
  return result


def edge_mask(img, line_size, blur_value): #마스크 만들기 (선따기)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  gray_blur = cv2.medianBlur(gray, blur_value)
  edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value)
  return edges


while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)



    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                #print(id, cx, cy)
                # if id == 4:
                cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    #cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,(0, 255, 0), 3)

    cv2.imshow("Image", img)
    
    z = cv2.waitKey(10)
    if z == 27 : break
    elif z == 13 :      
        line_size = 5  # 선의 두께
        blur_value = 5
        edges = edge_mask(img, line_size, blur_value)
        total_color = 9 #색상의 수 
        img = color_quantization(img, total_color)
        blurred = cv2.bilateralFilter(img, d=9, sigmaColor=30,sigmaSpace=30) #양뱡향 필터
        cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)
        img_frame =cartoon.copy()
        img_size = img_frame[10:1000,10:1000]
        cv2.imwrite(file, img_size)
        print(file, '저장됨')
        cv2.imshow("immm",cartoon)


cap.release()
cv2.destroyAllWindows()
