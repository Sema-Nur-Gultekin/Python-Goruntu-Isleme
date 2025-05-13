import cv2
import numpy as np 

kamera = cv2.VideoCapture(0)

while True:
    ret, goruntu = kamera.read()

    cv2.rectangle(goruntu, (100,100), (200,200), (25,36,98), 3) 

    cv2.line(goruntu, (0,0), (100,100), (0,0,255), 2)

    cv2.circle(goruntu, (150,150), 50, (80,150,35), 2)

    cv2.putText(goruntu, "Selam", (220,220), cv2.FONT_HERSHEY_DUPLEX, 1, (200,0,0), 2)

    cv2.imshow("video", goruntu)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

kamera.release()

cv2.destroyAllWindows()