import cv2
import numpy as np

width = 800
height = 600

RED = (0, 0, 256)
GREEN = (0, 256, 0)
BLUE = (256, 0, 0)
WHITE = (256, 256, 256)

k = width / 230  # коэффициент, чтобы не привысить значение для данного типа данных
horizontal_fill = np.array(
                [[i / k, i / k, i / k] for i in range(width)] * height,
                dtype='uint8')

logo = horizontal_fill.reshape(height, width, 3)

cv2.circle(logo, center=(width // 2, height // 2), radius=250, color=WHITE, thickness=5)

width_line = 60
bias = 120
height_line = 120
thickness = 8
top_pos = height // 2 - 100

# точки слева направо, сверху вниз
pt1 = (width // 2 - bias, top_pos)
pt2 = (width // 2 - width_line, top_pos)
pt3 = (width // 2 + width_line, top_pos)
pt4 = (width // 2 + bias, top_pos)

cv2.line(logo, pt1, pt2, color=RED, thickness=thickness)
cv2.line(logo, pt3, pt4, color=RED, thickness=thickness)

pt5 = (pt1[0], pt1[1] + height_line)
pt6 = (pt2[0], pt2[1] + height_line)
pt7 = (pt3[0], pt3[1] + height_line)
pt8 = (pt4[0], pt4[1] + height_line)

cv2.line(logo, pt1, pt5, color=BLUE, thickness=thickness)
cv2.line(logo, pt2, pt6, color=BLUE, thickness=thickness)
cv2.line(logo, pt3, pt7, color=BLUE, thickness=thickness)
cv2.line(logo, pt4, pt8, color=BLUE, thickness=thickness)

ellipse_center = (pt8[0] - (pt8[0] - pt5[0]) // 2, pt8[1])

cv2.ellipse(logo, ellipse_center, (bias, bias), 0, 0, 180, color=GREEN, thickness=thickness)
cv2.ellipse(logo, ellipse_center, (width_line, width_line), 0, 0, 180, color=GREEN, thickness=thickness)

cv2.imshow('LOGO URBAN-UNIVERSITY', logo)

cv2.waitKey(0)
