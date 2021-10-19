# Este programa busca y pinta contornos
import cv2
import numpy as np

imagen = cv2.imread("D:\\Proyectos\\Python Pr\\Practicas\\Datos\\Monito.jpg")
gris1 = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
gris = cv2.bilateralFilter(gris1, 11, 17, 17)

#Magia de refinado 

kernel = np.ones((4,4),np.uint8)
erosion = cv2.erode(gris,kernel,iterations = 1)#remueve puntos pequeños
kernel = np.ones((2,2),np.uint8)
dilation = cv2.dilate(erosion,kernel,iterations = 4)#ensancha las lineas
binari = cv2.Canny(dilation,40,150)
#cv2.imshow("algo",binari)

#a,formas = cv2.threshold(gris,70,255,cv2.THRESH_BINARY)
cnt,b = cv2.findContours(binari,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


rects = [cv2.boundingRect(news) for news in cnt]
imrec=[]
print(len(rects))
for i in rects:
    _,_,w,h=i
    print(i)
    if w>200 and h>100:
        imrec.append(i)
    
print(imrec)

rects = sorted(rects,key=lambda  x:x[1],reverse=True)
for b in imrec:
    x,y,w,h=b
    x=int(x)
    y=int(y)
    w=int(w)
    h=int(h)
    print(x,y,w,h)
    cv2.rectangle(imagen,(x,y),(x+w,y+h),(0,0,255),2)
#cv2.drawContours(imagen,cnt,-1,(0,0,255),2)
cv2.imshow("Imagen de salida",imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()