import cv2
import numpy as np 

image = cv2.imread("f.jpeg")

#Mean Filter işlemi ile resimi yumuşatırız 
meanFilter = cv2.blur(image, (3,3)) 
meanFilter2 = cv2.blur(image, (5,5)) 
meanFilter3 = cv2.blur(image, (7,7)) 

medianFilter = cv2.medianBlur(image, 3) # daha çok orjinalliği korur
medianFilter2 = cv2.medianBlur(image, 5) 
medianFilter3 = cv2.medianBlur(image, 7) 

gauss = cv2.GaussianBlur(image, (3,3), 0)
gauss2 = cv2.GaussianBlur(image, (5,5), 0)
gauss3 = cv2.GaussianBlur(image, (7,7), 0)

cv2.imshow("Orijinal Resim", image)

cv2.imshow("Mean Filter 3*3", meanFilter)
cv2.imshow("Mean Filter 5*5", meanFilter2)
cv2.imshow("Mean Filter 7*7", meanFilter3)

cv2.imshow("Median Filter 3*3", medianFilter)
cv2.imshow("Median Filter 5*5", medianFilter2)
cv2.imshow("Median Filter 7*7", medianFilter3) 

cv2.imshow("Gauss Filter 3*3", gauss)
cv2.imshow("Gauss Filter 5*5", gauss2)
cv2.imshow("Gauss Filter 7*7", gauss3)

cv2.waitKey(0)
cv2.destroyAllWindows()