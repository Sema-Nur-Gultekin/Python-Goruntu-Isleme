import cv2
import numpy as np

image = cv2.imread("a.png")

kernel = np.ones((5,5), np.uint8)

dilation = cv2.dilate(image, kernel, iterations=1) # Genişleme işlemi 
dilation2 = cv2.dilate(image, kernel, iterations=2) 

erosion = cv2.erode(image, kernel, iterations=1) # Aşınma işlemi

dilation3 = cv2.dilate(erosion, kernel, iterations=1) 

cv2.imshow("Orijinal", image)
cv2.imshow("dilation", dilation)
cv2.imshow("dilation2", dilation2)
cv2.imshow("dilation3", dilation3)
cv2.imshow("erosion", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()