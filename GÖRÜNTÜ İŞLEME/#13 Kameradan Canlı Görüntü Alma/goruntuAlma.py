import cv2
import numpy as np 

kamera = cv2.VideoCapture(0) # 0-Kendi bilgisayarımıza tanımlı kamerayı alır, 1-USB kamera, 2-Harici bir video

while True:

    ret, goruntu = kamera.read() # ret kamera kontrol amaçlı
    
    cv2.imshow("video", goruntu)

    if cv2.waitKey(30) & 0xFF == ord('q'): 
        break

kamera.release() # Kamerayı serbest bırakıyoruz 

cv2.destroyAllWindows()