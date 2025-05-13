import cv2
import numpy as np

#simple thresholding tüm resime uygulanır 
#adaptive thresholding belirlediğimiz bölgeleri alıp uygular 
#otsu thresholding otomatik değer istemeden uygular 

image = cv2.imread("parmakizi.jpeg", 0)

#simple thresholding 
ret1, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

#otsu thresholding
ret2, thresh2 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) # en uç değerleri atayarak otomatik yapmasını sağlıyoruz çünkü 0 ın altına inemez 255 in yukarısına çıkamaz 


cv2.imshow("Orijinal Resim", image)
cv2.imshow("simple thresholding", thresh1)
cv2.imshow("otsu thresholding", thresh2)

cv2.waitKey(0)
cv2.destroyAllWindows()