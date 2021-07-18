import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('wismar.jpg')

image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img_small = cv2.pyrDown(image)

num_iter = 5
for _ in range(num_iter):
    img_small= cv2.bilateralFilter(img_small, d=9, sigmaColor=9, sigmaSpace=7)

img_rgb = cv2.pyrUp(img_small)

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
img_blur = cv2.medianBlur(img_gray, 7)

img_edge = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 2)

img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)

array = cv2.bitwise_and(image, img_edge)

plt.figure(figsize= (10,10))
plt.imshow(array)

plt.show()