import cv2
import numpy as np

img = cv2.imread('input_color_text.jpg')

b, g, r = cv2.split(img)

_, black_b = cv2.threshold(b, 240, 255, cv2.THRESH_BINARY)
_, black_g = cv2.threshold(g, 240, 255, cv2.THRESH_BINARY)
_, black_r = cv2.threshold(r, 240, 255, cv2.THRESH_BINARY)

img = cv2.merge((black_b, black_g, black_r))

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 0)
img = cv2.Canny(img, 30, 50)

contour, _ = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

new_img = np.zeros(img.shape, dtype='uint8')

cv2.drawContours(new_img, contour, -1, (255, 224, 200), 1)

img_color_str = np.zeros((img.shape[0], img.shape[1], 3), dtype='uint8')

first_line = 160
second_line = 310

img_color_str[0:first_line, :, 1] = new_img[0:first_line, :, ]

img_color_str[first_line:second_line, :, 2] = new_img[first_line:second_line, :, ]

img_color_str[second_line:, :, 0] = new_img[second_line:, :, ]
img_color_str[second_line:, :, 2] = new_img[second_line:, :, ] // 2

cv2.imshow('result', img_color_str)
cv2.waitKey(0)
