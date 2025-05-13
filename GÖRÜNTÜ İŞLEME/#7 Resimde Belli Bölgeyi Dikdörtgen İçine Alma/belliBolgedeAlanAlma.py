import cv2
import numpy as np 

resim = cv2.imread("HababamSinifi.png")

cv2.rectangle(resim,(400,250),(300,150),[0,0,255],3) #Dikdörtgen çizmemize yarar
#cv2.rectangle(resim,(x,y),(x,y),[0,0,255]->BGR,0-9 arası çerçeve kalınlığı)

cv2.imshow("Hababam Sinifi", resim)

cv2.waitKey(0)
cv2.destroyAllWindows()