import cv2
import numpy as np

logo = np.zeros((400, 500, 3), dtype='uint8')

cv2.imshow('LOGO URBAN-UNIVERSITY', logo)

cv2.waitKey(0)