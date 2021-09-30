#Es de convencion usar [] de no usarlos se crea un "TUPLE" es una lista no editable
My_lista = ["Maria" , "Pepe", "Marta", "Antonio","Julio", "Leila",7.77,True]
print(type(My_lista))
#En este caso tenemos   ------> ["Maria","Pepe","Marta","Antonio","Julio", "Leila"]
#donde las direcciones son          0       1       2        3       4        5
print(My_lista)
#acceder a un elemento de la lista recuerda qu siempre se cuenta desde 0
print(My_lista[2])
#Python puede contar desde atras con -
print(My_lista[-0])
print(My_lista[-1])
#Formas de mostrar parte de la lista recuerda que excluye los elementos [,y] y muestra lo del medio
print(My_lista[:2])
print(My_lista[2:])
#MOstramos solo pepe y marta
print(My_lista[1:3])
print("Aumentamos la lista")
#Añadimos un OBJETO:(una lista, documento, letra, numero, etc,)  al final de la lista
nm = str(input("ingrese un nuevo nombre la lista : "))
My_lista.append(nm)
print(My_lista)
nm = str(input("ingrese un nuevo nombre la lista : "))
My_lista.insert(int(input("ingrese la posicion en la cual insertar : ")),nm)
print(My_lista)
#Ahora aumentaremos una lista con otra Asi añadimos MULTIPLES ELEMENTOS no solo un objeto como con append
My_lista.extend(["Jhon","Gabriela","Carolina"])
print(My_lista)
#Busscar la posicion de un nombre
print(My_lista.index("Gabriela"))
#Buscar si se encuentra un elemento nos devuelve True / False
print("Jhon" in My_lista)
#Eliminar un elemento de la lista y pop el ultimo
My_lista.remove("Marta")
My_lista.pop()
print(My_lista)
#Suma de listas no destructiva
My_lista2 = ["Hola","como","estas"]
My_lista3 = [7,False,"dragon"]
My_lista4 = My_lista2 + My_lista3
print(My_lista4)
#LA multiplicacion solo copia y pega la lista al final la cantidad de veces de la multiplicacion
My_lista4 = My_lista4*2
print(My_lista4)