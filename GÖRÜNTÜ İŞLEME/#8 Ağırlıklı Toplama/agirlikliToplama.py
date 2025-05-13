import cv2
import numpy as np 

resim1 = cv2.imread("EmelSayin.jpg")
resim2 = cv2.imread("TurkanSoray.jpg")

#Seçili koordinatların BGR değerlerini bulmak
print(resim1[100,200]) 
print(resim2[100,230])

cv2.imshow("Emel Sayin", resim1)
cv2.imshow("Turkan Soray", resim2)

print(resim1[100,200]+ resim2[100,230]) 

cv2.waitKey(0) 
cv2.destroyAllWindows()