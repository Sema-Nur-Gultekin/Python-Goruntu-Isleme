#Kütüphaneler 
import cv2 
import numpy as np 

resim = cv2.imread("kus_resmi.jpg",0) # Okuma işlemi

cv2.imshow("KusResmi", resim) # Gösterme işlemi

print(resim) # matris hali

print(resim.size) # Boyutu

print(resim.dtype) # Veri tipi

print(resim.shape) # Genişliği,Yüksekliği,Kaç kanal kullandığı 

cv2.imwrite("yeniresim.png", resim) # Resimden bir daha oluşturma 

cv2.waitKey(0) 
cv2.destroyAllWindows() 

