import cv2
import numpy as np

resim = cv2.imread("AdileNasit.webp")

aynalananResim = cv2.copyMakeBorder(resim,75,75,125,125,cv2.BORDER_REFLECT) 
# Uzatma, Aynalama, Tekrar Etme, Sarmalamada bu kodu kullanacağız (Parametreleri (hangi resmi aynalayacağımız, üst, alt, sol, sağ, işlem ))

uzatilanResim = cv2.copyMakeBorder(resim,120,120,120,120,cv2.BORDER_REPLICATE) 

tekrarResim = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_WRAP)

sarilanResim = cv2.copyMakeBorder(resim,50,50,50,50,cv2.BORDER_CONSTANT,
                                  value = (150,40,25))

cv2.imshow("Aynalanan Adile Nasit", aynalananResim)
cv2.imshow("Uzatilan Adile Nasit", uzatilanResim)
cv2.imshow("Tekrarlanan Adile Nasit", tekrarResim)
cv2.imshow("Sarilan Adile Nasit", sarilanResim)

cv2.waitKey(0)
cv2.destroyAllWindows()