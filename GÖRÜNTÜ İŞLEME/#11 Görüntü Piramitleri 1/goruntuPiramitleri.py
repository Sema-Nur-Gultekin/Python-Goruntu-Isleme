import cv2
import numpy as np 

resim = cv2.imread("NataliePortman.jpg")

ikiKatBuyuk = cv2.pyrUp(resim) # Resimimizi 2 kat büyütür 
ikiKatKucuk = cv2.pyrDown(resim ) # Resimimizi 2 kat küçültür 
garipResim = (cv2.pyrUp(resim))**2

print("Orijinal Resim", resim.shape)
print("iki kat buyutulmus resim", ikiKatBuyuk.shape)
print("iki kat kucultulmus resim", ikiKatKucuk.shape)

cv2.imshow("Orijinal Resim",resim)
cv2.imshow("iki kat buyutulmus resim",ikiKatBuyuk)
cv2.imshow("iki kat kucultulmus resim",ikiKatKucuk)
cv2.imshow("Garip Resim",garipResim)

cv2.waitKey(0)
cv2.destroyAllWindows()