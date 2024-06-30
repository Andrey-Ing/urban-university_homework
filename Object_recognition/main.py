import cv2
import numpy as np

cap_img = cv2.VideoCapture(0)

while True:
    ret, frame = cap_img.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    eyes = cv2.CascadeClassifier('haarcascade_eye.xml')
    result_eyes = eyes.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=19)

    horizontal_offset = 30

    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0

    x_list = list()
    y_list = list()

    for (x, y, w, h) in result_eyes:

        x_list += [x, x+w]
        y_list += [y, y+h]

        x_min = min(x_list) - horizontal_offset
        if x_min < 0:
            x_min = 0

        x_max = max(x_list) + horizontal_offset
        if x_max > frame.shape[1]:
            x_max = frame.shape[1]

        y_min = min(y_list)

        y_max = max(y_list)

        if y_max > frame.shape[0]:
            y_max = frame.shape[0]

    #gray = cv2.GaussianBlur(gray, (5, 9), cv2.BORDER_DEFAULT)
    gray = cv2.medianBlur(gray, 7)
    color_gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    color_gray = color_gray[y_min:y_max, x_min:x_max]


    frame[y_min:y_max, x_min:x_max] = color_gray

    cv2.rectangle(frame, (x_min, y_min), (x_max,  y_max), (0, 0, 200), 2)

    for (x, y, w, h) in result_eyes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), thickness=1)


    cv2.imshow('Blured eyes', frame)
    key_press = cv2.waitKey(50)
    if key_press == 0x1B:  # Esc
        break

cap_img.release()
cv2.destroyAllWindows()
