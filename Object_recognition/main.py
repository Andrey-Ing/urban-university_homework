import cv2

cap = cv2.VideoCapture(0)



#cap.set(cv2.CAP_PROP_FPS, 2) # Частота кадров
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1900) # Ширина кадров в видеопотоке.
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1880) # Высота кадров в видеопотоке.

while True:
    ret, img = cap.read()
    cv2.imshow("camera", img)
    if cv2.waitKey(1) == 27: # Клавиша Esc
        break

cap.release()
cv2.destroyAllWindows()






