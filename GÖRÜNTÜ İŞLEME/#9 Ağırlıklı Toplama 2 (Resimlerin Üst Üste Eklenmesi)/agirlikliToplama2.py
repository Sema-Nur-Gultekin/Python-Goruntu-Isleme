import cv2
import numpy as np 

resim1 = cv2.imread("cemYilmaz.png")
resim2 = cv2.imread("ozanGuven.png")

cv2.imshow("Cem Yilmaz", resim1)
cv2.imshow("Ozan Guven", resim2)

#Toplanacak resimlerin boyutları aynı olmak zorunda 
toplam = cv2.add(resim1, resim2) #İki resimi üst üste ekler 

#Saydamlıklarını ayarlama (Toplamları 1 olmak zorunda)
agirlikliToplama = cv2.addWeighted(resim1,0.3,resim2,0.7,0) #cv2.addWeighted(ilk resim, ilk resimde istenilen saydamlık, ikinci resim, ikinci resim saydamlığı,0-> her daim sıfır  )

cv2.imshow("Toplanmis Resimler",toplam)
cv2.imshow("Agirlikli Toplanmis Resimler", agirlikliToplama)

cv2.waitKey(0)
cv2.destroyAllWindows()