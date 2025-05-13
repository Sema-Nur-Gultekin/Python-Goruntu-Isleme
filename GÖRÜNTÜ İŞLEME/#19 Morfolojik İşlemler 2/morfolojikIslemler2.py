import cv2
import numpy as np

image = cv2.imread("a.png")

kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(image, kernel, iterations=1)
dilation = cv2.dilate(erosion, kernel, iterations=1)

#Daha çok gürültülü resimlerde kullanılır
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel) # Yukarıdaki işlemleri yapmadan opening ile aynı sonucu elde edebiliriz çünkü zaten bu işlemleri yapar 

#Daha çok birleştirmeli kopuk resimlerde kullanılır 
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel) # openingin tam tersi dilationdan sonra erosion işlemi gerçekleşir 

gradyan = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel) # dilation ile erosian arasındaki fark 

#Ön planı değil arka planı istediğimiz işlemlerde kullanılır 
tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel) # orijinal resim ile opening arasındaki fark 

blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel) # closing ile orijinal resimimiz arasındaki fark 

cv2.imshow("Orijinal", image)
cv2.imshow("dilation", dilation)
cv2.imshow("erosion", erosion)

cv2.imshow("opening", opening)
cv2.imshow("closing", closing)
cv2.imshow("gradyan", gradyan)
cv2.imshow("tophat", tophat)
cv2.imshow("blackhat", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()