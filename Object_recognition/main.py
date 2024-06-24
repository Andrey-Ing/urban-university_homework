import cv2

cap_img = cv2.VideoCapture(0)

while True:
    ret, frame = cap_img.read()
    frame = cv2.resize(frame, (200, 200))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = cv2.CascadeClassifier('haarcascade_eye.xml')
    result = eyes.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

    # face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    #
    # face_img = face.detectMultiScale(gray, 1.1, 2)
    #
    #
    # for (x, y, w, h) in face_img:
    #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)



    print(result)

    for (x, y, w, h) in result:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (45, 89, 255), thickness=-1)



    cv2.imshow('Blured eyes', frame)
    key_press = cv2.waitKey(30)
    if key_press == 0x1B:  # Esc
        break

cap_img.release()
cv2.destroyAllWindows()







