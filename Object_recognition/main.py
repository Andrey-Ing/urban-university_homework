import cv2

cap_img = cv2.VideoCapture(0)

while True:
    ret, frame = cap_img.read()

    eyes = cv2.CascadeClassifier('haarcascade_eye.xml')
    result = eyes.detectMultiScale(cap_img, scaleFactor=1, minNeighbors=1)



    print(result)


    cv2.imshow('Blured eyes', frame)
    key_press = cv2.waitKey(30)
    if key_press == ord('q'):
        break

cap_img.release()
cv2.destroyAllWindows()







