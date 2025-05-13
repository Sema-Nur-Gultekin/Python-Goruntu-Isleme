import cv2
import numpy as np 

resim = cv2.imread("harleyQuinn.webp")

resim[50,30] = [255,255,255] # İlk değer sol üst köşeden aşağı iner ikinci değer sağa gider ve o pikselin rengini belirtilen rgb değeri ile değiştirir 

for i in range(100): 
    resim[70,i] = [255,255,255] 

cv2.imshow("Harley Quinn", resim)

cv2.waitKey(0)
cv2.destroyAllWindows()