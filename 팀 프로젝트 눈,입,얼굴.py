import cv2
import numpy as np
import dlib, sys, datetime

img = cv2.imread('photo2021-09-28 14 22.jpg',cv2.IMREAD_COLOR)


x = datetime.datetime.now().strftime('%Y-%m-%d %H %M')

filele = f'photo{x}.jpg'


if img is None:
    print('image load failed!')
    sys.exit()

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def midpoint(p1 ,p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = detector(gray)
for face in faces:
    landmarks = predictor(gray, face)
    # left_point = (landmarks.part(36).x, landmarks.part(36).y)
    # right_point = (landmarks.part(39).x, landmarks.part(39).y)
    # center_top = midpoint(landmarks.part(37), landmarks.part(38))
    # center_bottom = midpoint(landmarks.part(41), landmarks.part(40))

    # left_point1 = (landmarks.part(42).x, landmarks.part(42).y)
    # right_point1 = (landmarks.part(45).x, landmarks.part(45).y)
    # center_top1 = midpoint(landmarks.part(43), landmarks.part(44))
    # center_bottom1 = midpoint(landmarks.part(47), landmarks.part(45))

    left_eye_region = np.array([(landmarks.part(i).x, landmarks.part(i).y) for i in range(36,42)], np.int32) # 왼쪽 눈 
    
    right_eye_region = np.array([(landmarks.part(i).x, landmarks.part(i).y) for i in range(42,48)], np.int32) # 오른쪽 눈

    mm = np.array([(landmarks.part(i).x, landmarks.part(i).y) for i in range(48,61)], np.int32) # 입

    head = np.array([(landmarks.part(i).x, landmarks.part(i).y) for i in range(26)], np.int32) #얼굴

    min_x3 = np.min(head[:,0])
    max_x3 = np.max(head[:,0])
    min_y3 = np.min(head[:,1])
    max_y3 = np.max(head[:,1])
     
    head_ = img[min_y3 : max_y3, min_x3 : max_x3]
    head_ = cv2.resize(head_, None,fx=3 ,fy=3)


    min_x2 = np.min(mm[:,0])
    max_x2 = np.max(mm[:,0])
    min_y2 = np.min(mm[:,1])
    max_y2 = np.max(mm[:,1])
     
    m = img[min_y2 : max_y2, min_x2 : max_x2]
    m = cv2.resize(m, None,fx=3 ,fy=5)




    min_x1 = np.min(right_eye_region[:,0])
    max_x1 = np.max(right_eye_region[:,0])
    min_y1 = np.min(right_eye_region[:,1])
    max_y1 = np.max(right_eye_region[:,1])
     
    R_eye = img[min_y1 : max_y1, min_x1 : max_x1]
    R_eye = cv2.resize(R_eye, None,fx=5 ,fy=5)


    min_x = np.min(left_eye_region[:,0])
    max_x = np.max(left_eye_region[:,0])
    min_y = np.min(left_eye_region[:,1])
    max_y = np.max(left_eye_region[:,1])
     
    L_eye = img[min_y : max_y, min_x : max_x]
    L_eye = cv2.resize(L_eye, None,fx=5 ,fy=5)


    # mask = m[:, :, -1] #인덱싱 -1 = 3
    # m = m[:, :, :-1]
    # h, w = mask.shape[:]
    # crop = head_[500:500+h, 200:200+w] #위치

    # cv2.copyTo(m, mask, crop)




    # hor_line = cv2.line(img, left_point, right_point, (0, 255, 0), 2)
    # ver_line = cv2.line(img, center_top, center_bottom, (0, 255, 0), 2)

    # hor_line1 = cv2.line(img, left_point1, right_point1, (0, 255, 0), 2)
    # ver_line1 = cv2.line(img, center_top1, center_bottom1, (0, 255, 0), 2)

    cv2.imshow('eye1111111111',L_eye)
    cv2.imshow('eye21111111111',R_eye)
    cv2.imshow('mm',m)
    cv2.imshow('head',head_)

    cv2.imshow("Frame", img)
while True :
    k=cv2.waitKey()
    if k == 27 : break
# # elif k == 13 : 


cv2.destroyAllWindows()