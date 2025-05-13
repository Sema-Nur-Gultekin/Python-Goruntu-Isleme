import cv2
import numpy as np

resim = np.zeros((300,300,3), dtype = "uint8")

cv2.line(resim, (0,0), (100,100), (0,0,255), 3) # Çizgi oluşturma
# cv2.line(img, başlangıcı, bitişi, renk, kalınlık )

cv2.circle(resim, (150,150), 25, (0,255,0), 2) # Daire oluşturma
# cv2.circle(img, merkezi, yarıçapı, renk, kalınlık )

cv2.putText(resim, "Selam", (100,200), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 1) # Metin kutusu oluşturma
# cv2.putText(img, metinimiz, başlangıç koordinatı, yazı tipi özelliği, yazının boyutu, renk, kalınlık)

cv2.imshow("deneme", resim)


cv2.waitKey(0)
cv2.destroyAllWindows()