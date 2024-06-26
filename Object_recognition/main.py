import cv2

cap_img = cv2.VideoCapture(0)

while True:
    ret, frame = cap_img.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    eyes = cv2.CascadeClassifier('haarcascade_eye.xml')
    result_eyes = eyes.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

    pt1_area = (frame.shape[1], 0)
    pt2_area = (0, 0)

    print(pt1_area, pt2_area)

    for (x, y, w, h) in result_eyes:
        if x < pt1_area[0]:
            pt1_area = x, y

        if y + h > pt2_area[1]:
            pt2_area = x + w, y + h


    cv2.rectangle(frame, pt1_area, pt2_area, (0, 255, 0), 2)


    #cv2.rectangle(frame, (400, 400), (400, 400), (0, 255, 0), 2)
    # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    print(result_eyes)



    #print(result)

    for (x, y, w, h) in result_eyes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (45, 89, 255), thickness=1)



    cv2.imshow('Blured eyes', frame)
    key_press = cv2.waitKey(50)
    if key_press == 0x1B:  # Esc
        break

cap_img.release()
cv2.destroyAllWindows()







