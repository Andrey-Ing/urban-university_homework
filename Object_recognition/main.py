import cv2
import numpy as np

cap_img = cv2.VideoCapture(0)

while True:
    ret, frame = cap_img.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    eyes = cv2.CascadeClassifier('haarcascade_eye.xml')
    result_eyes = eyes.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

    pt1_area = [frame.shape[1], 0]
    pt2_area = [0, 0]

    print(pt1_area, pt2_area)

    for (x, y, w, h) in result_eyes:
        if x < pt1_area[0]:
            pt1_area = [x, y]

        if y + h > pt2_area[1]:
            pt2_area = [x + w, y + h]

    horizontal_offset = 30

    if pt1_area[0] < pt2_area[0]:
        pt1_area[0] = pt1_area[0] - horizontal_offset
        pt2_area[0] = pt2_area[0] + horizontal_offset
    else:
        pt1_area[0] = pt1_area[0] + horizontal_offset
        pt2_area[0] = pt2_area[0] - horizontal_offset

    for(x, y, w, h) in result_eyes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), thickness=1)

    # cv2.rectangle(frame, pt1_area, pt2_area, (0, 255, 0), 2)

    # cv2.rectangle(frame, (200, 200), (300, 300), (200, 255, 70), 2)

    cv2.rectangle(frame, pt1_area, pt2_area, (0, 255, 0), 2)

   # cv2.rectangle(frame, (200, 200), (300, 300), (200, 255, 70)

    horizontal_offset = 30

    x_min = frame.shape[1]
    x_max = 0
    y_min = frame.shape[0]
    y_max = 0


    for (x, y, w, h) in result_eyes:
        x_list = list()
        y_list = list()

        x_list += [x, x+w]
        y_list += [y, y+h]

        x_list.sort()
        y_list.sort()

        x_min = x_list[0] - horizontal_offset
        if x_min < 0:
            x_min = 0

        x_max = x_list[-1] + horizontal_offset
        if x_max > frame.shape[1]:
            x_max = frame.shape[1]

        y_min = y_list[0]

        y_max = y_list[-1]

        if y_max > frame.shape[0]:
            y_max = frame.shape[0]



    color_gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    color_gray = cv2.GaussianBlur(color_gray, (5, 5), cv2.BORDER_DEFAULT)

    mask = np.zeros((100, 100), dtype='uint8')

    color_gray[0:0, 100:300] = frame[0:0, 100:300]














    cv2.rectangle(frame, (x_min, y_min), (x_max,  y_max), (0, 0, 200), 2)


    cv2.imshow('Blured eyes', color_gray)
    key_press = cv2.waitKey(50)
    if key_press == 0x1B:  # Esc
        break

cap_img.release()
cv2.destroyAllWindows()







