import cv2 
import numpy as np 

resim = cv2.imread("KemalSunal.webp")

#Tüm resime efekt eklemek 
#resim[:,:,0] = 255 #BGR sıralaması ile blue kısmına 0 ile erişim sağlayıp 255 tonunda efekt ekliyoruz 1-Green 2-Red
#resim[:,:,2] = 150

#Belirli bir kısıma efekt eklemek 
resim[150:200,350:500,0] = 255 # [y,x,BGR değeri]

cv2.imshow("Kemal Sunal Fotografi", resim)

cv2.waitKey(0)
cv2.destroyAllWindows()