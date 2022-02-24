import sys
import cv2, numpy as np

image1 = cv2.imread('images/sp.jpg')
img1 = cv2.imread('images/sp.jpg')


def color_quantization(img, k): # 색상 양자화 (색상 수 줄이기)

  data = np.float32(img).reshape((-1, 3))
  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)
  ret, label, center = cv2.kmeans(data, k, None, criteria, 20, cv2.KMEANS_RANDOM_CENTERS)
  center = np.uint8(center)
  result = center[label.flatten()]
  result = result.reshape(img.shape)
  return result



def edge_mask(img, line_size, blur_value): #마스크 만들기 (선따기)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  gray_blur = cv2.medianBlur(gray, blur_value)
  edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value)
  return edges


line_size = 5  # 선의 두께
blur_value = 5
edges = edge_mask(image1, line_size, blur_value)


def color_quantization(img, k): # 색상 양자화 (색상 수 줄이기)

  data = np.float32(img).reshape((-1, 3))

  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

  ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
  center = np.uint8(center)
  result = center[label.flatten()]
  result = result.reshape(img.shape)
  return result

total_color = 21 #색상의 수 
img = color_quantization(image1, total_color)
blurred = cv2.bilateralFilter(img, d=9, sigmaColor=30,sigmaSpace=30) #양뱡향 필터
cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)

#cv2.imshow('ww', image1)
cv2.imshow('cartoon', cartoon)
#cv2.imshow('emeeee', edges)
# cv2.imshow('emge',img)
# cv2.imshow('eee', blurred)
cv2.waitKey()
cv2.destroyAllWindows()