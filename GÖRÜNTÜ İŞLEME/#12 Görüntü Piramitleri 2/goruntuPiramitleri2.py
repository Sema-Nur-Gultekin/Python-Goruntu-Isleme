import cv2 as cv
import numpy as np 

resim = np.zeros((300,300,3),dtype = "uint8") # Şekil oluştururuz np.zeros(shape,dtype)
#shape = (yükseklik,genişlik,kanal sayısı) -> arkada bir liste olarak döndürür karşımıza ise matris çıkarır 

print(resim)

cv.imshow("Resim",resim)

cv.waitKey(0)
cv.destroyAllWindows()