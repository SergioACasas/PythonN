from PIL import Image
f = "D:\\Proyectos\\Python Pr\\Practicas\\Datos\\0001-2.jpg"
foto1 = Image.open(f)
new_foto = foto1.reduce(4)#Divide el tamaño mantiene el ratio (Tambien se le puede dar una funcion crop , (x,y,w,h))
#foto1.show()
new_foto.save("D:\\Proyectos\\Python Pr\\Practicas\\Datos\\monito.jpg",format="JPEG")

