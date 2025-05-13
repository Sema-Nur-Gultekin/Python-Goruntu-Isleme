import cv2 
import numpy as np 

resim = cv2.imread("cocukBayrami.jpg")

kesit = resim[50:150,300:400] # (y,x) koordinatlarındaki alanı kesiyoruz 

resim[0:100,0:100] = kesit # kesiti resimde belirtilen koordinatlara yapıştırıyoruz (Kesitin boyutunu aşarsak hata alırız )

resim[:,:,0] = 255 # Efekt ekleme 

resim[400:450,300:350] = (0,150,255) # BGR sıralaması ile belirli bir alana efekt ekleme 

cv2.imshow("Kesit Alani", kesit)
cv2.imshow("23 Nisan Ulusal Egemenlik Ve Cocuk Bayrami", resim)

cv2.waitKey(0)
cv2.destroyAllWindows()