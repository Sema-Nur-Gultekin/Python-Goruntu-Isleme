import cv2
import numpy as np

image = cv2.imread("labirent.jpg", 0)

#simple thresholding
ret, thresh1 = cv2.threshold(image, 160, 255, cv2.THRESH_BINARY)

#adaptive thresholding # mean belirlediğimiz bölgenin ortalaması alınır #gaussian ağırlıklı toplam alır 
thresh2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,\
                                           cv2.THRESH_BINARY, 11,2)

thresh3 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                                              cv2.THRESH_BINARY, 11,2)

cv2.imshow("Orijinal Resim", image)
cv2.imshow("simple thresholding", thresh1)
cv2.imshow("mean adaptive thresholding", thresh2)
cv2.imshow("gaussian adaptive thresholding", thresh3)

cv2.waitKey(0)
cv2.destroyAllWindows()