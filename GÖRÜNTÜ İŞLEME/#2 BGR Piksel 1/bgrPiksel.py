import cv2
import numpy as np 

kurtResmi = cv2.imread("kurt.jpg")

cv2.imshow("Kurt Resmi", kurtResmi)

print(kurtResmi[(230,80)]) # Sol üstten ilk değer aşağı doğru ikinci değer sağa doğru giderek o pikselin RGB değerini gösterir 

print("Resmin Boyutu: " + str(kurtResmi.size))
print("Resmin Özellikleri: " + str(kurtResmi.shape))
print("Resmin veri tipini: " + str(kurtResmi.dtype))

cv2.waitKey(0)
cv2.destroyAllWindows()