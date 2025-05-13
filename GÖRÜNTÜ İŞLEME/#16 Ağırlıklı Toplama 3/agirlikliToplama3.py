import cv2
import numpy as np

resim1 = cv2.imread("bitki.webp")
resim2 = cv2.imread("beyaz.jpg")

print(resim1[120,100])
print(resim2[50,50])

cv2.imshow("Bitki Resmi", resim1)
cv2.imshow("Beyaz Resmi", resim2)

print(resim1[120,100]+ resim2[50,50])

cv2.waitKey(0)
cv2.destroyAllWindows()