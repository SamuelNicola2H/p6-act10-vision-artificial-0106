import numpy as np 
import cv2 
# visin artificial act 10 NC 0106 
# Lee la imagen en escala de grises 
img = cv2.imread("tierra.jpg", cv2.IMREAD_GRAYSCALE) 
 
cv2.imshow("tierra 0106", img) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
 
# Linea 
print("La Linea 0106") 
img = np.zeros((512,512,3), np.uint8) 
 
img = cv2.line(img,(0,0),(511,511),(255,255,255),3) 
cv2.imshow("Linea 0106", img) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
 
# Circulos 
print("Circulo 0106") 
 
img = cv2.circle(img, (260,260), 10, (255,0,0),-1) 
cv2.imshow("circulo 0106", img) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
 
#Textos 
print("Texto 0106") 
 
img = cv2.putText(img, "Hola soy yo 0106", (200, 30),cv2.FONT_HERSHEY_SIMPLEX, 
                  0.5, (255, 255, 255), 2) 
cv2.imshow("texto 0106", img) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
 
# Thresholding 
print("Thresholding 0106") 
 
img = cv2.imread('tierra.jpg',0) 
 
ret,thr1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY) 
ret,thr2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV) 
ret,thr3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC) 
ret,thr4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO) 
ret,thr5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV) 
 
cv2.imshow('BINARY',thr1) 
cv2.imshow('BINARY_INV',thr2) 
cv2.imshow('TRUNC',thr3) 
cv2.imshow('TOZERO',thr4) 
cv2.imshow('TOZERO_INV',thr5) 
 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
 
#Trackbars 
print("Trackbars 0106") 
 
def on_trackbar(val): 
  print(val) 
 
img = np.zeros((300,512,3), np.uint8) 
cv2.namedWindow('frame') 
 
cv2.createTrackbar('R','frame',0,255,on_trackbar) 
cv2.createTrackbar('G','frame',0,255,on_trackbar) 
cv2.createTrackbar('B','frame',0,255,on_trackbar) 
 
while(True): 
    cv2.imshow('frame',img) 
    k = cv2.waitKey(1) & 0xFF 
    if k == 27: 
        break 
 
    r = cv2.getTrackbarPos('R','frame') 
    g = cv2.getTrackbarPos('G','frame') 
    b = cv2.getTrackbarPos('B','frame') 
 
    img[:] = [b,g,r] 
 
cv2.imshow("trackbars 0106", img) 
cv2.waitKey(0) 
cv2.destroyAllWindows()

print("programa realizaado por Samuel Xavier Nicola NC 0106")