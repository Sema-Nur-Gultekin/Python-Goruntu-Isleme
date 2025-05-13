import cv2
import numpy as np

image = cv2.imread("labirent.jpg",0)

ret, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY) #127'nin altında kalan pikseller 0'a yuvarlanır 127'nin üstündekiler bizim belirlediğimiz 255 olur

ret, thresh2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

ret, thresh3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC) 

ret, thresh4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO) 

ret, thresh5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV) 

cv2.imshow("Orijinal Resim", image)
cv2.imshow("thresh1", thresh1)
cv2.imshow("thresh2", thresh2)
cv2.imshow("thresh3", thresh3)
cv2.imshow("thresh4", thresh4)
cv2.imshow("thresh5", thresh5)

cv2.waitKey(0)
cv2.destroyAllWindows()