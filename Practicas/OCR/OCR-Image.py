import pytesseract
import cv2

conf = r' --oem 3 --psm 6 outputbase digits'

pytesseract.pytesseract.tesseract_cmd ="C:\Program Files\Tesseract-OCR\Tesseract.exe"
img = cv2.imread("D:\Proyectos\Python Pr\Practicas\OCR\Real.png")
#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img,lang="spa"))
#tomamos los datos del ancho y altura de la imagen
Himg,Wimg,Col=(img.shape)
#tomamos los datos de las letras y su ubicacion en la imagen
'''boxes= pytesseract.image_to_boxes(img,config=conf)#config=conf
for b in boxes.splitlines():
    b=b.split(' ')
    x,y,w,h=b[1],b[2],b[3],b[4]
    x=int(x)
    y=int(y)
    w=int(w)
    h=int(h)
    print(x,y,w,h)
    cv2.rectangle(img,(x,Himg-y),(w,Himg-h),(0,0,255),1)
    cv2.putText(img,b[0],(x,Himg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)'''
#Tomamos Palabras y las ubicamos
datos= pytesseract.image_to_data(img)
for dx,dy in enumerate(datos.splitlines()):
    if  dx != 0:
        d=dy.split()
        print(d)
        if len(d) == 12:
            rx,ry,rw,rh=d[6],d[7],d[8],d[9]
            rx=int(rx)
            ry=int(ry)
            rw=int(rw)
            rh=int(rh)
            print(rx,ry,rw,rh)
            cv2.rectangle(img,(rx,ry),(rx+rw,ry+rh),(0,0,255),1)
            cv2.putText(img,d[11],(rx,ry-20),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)

#Muesta la imagen procesada 
cv2.imshow("Result",img)
cv2.waitKey(0)
