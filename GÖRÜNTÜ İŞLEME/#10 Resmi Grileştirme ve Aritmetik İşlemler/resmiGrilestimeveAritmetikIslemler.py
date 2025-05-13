import cv2
import numpy as numpy

resim = cv2.imread("NataliePortman.jpg") # Eğer orijinal resim ile hiç işimiz yok ise burada 0 ekleyerek direkt gri yapabiliriz

resimGri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY) #Rengi dönüştürme fonksiyonumuzu kullanarak resimi griye dönüştürüyoruz 

yukseklik,genislik,kanalSayisi = resim.shape 
yukseklik1,genislik1 = resimGri.shape

print("Orijinal Resim", yukseklik,genislik,kanalSayisi)
print("Grilestirilmis Resim", yukseklik1,genislik1)


cv2.imshow("Orijinal Resim", resim)
cv2.imshow("Grilestirilmis Resim", resimGri)

cv2.waitKey(0)
cv2.destroyAllWindows()