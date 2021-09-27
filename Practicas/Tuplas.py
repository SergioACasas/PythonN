#Las tuplas son listas Inmutables pero si soportan busqueda index
tupla = ("Sebastian","Horacio","Caterine","Lorena",3342,99,7)
print(tupla[3])
print(tupla)
#Transforma una tupla a lista
lista = list(tupla)
print(type(tupla),type(lista))
print(lista)
#Lista [ ], Tupla ( ) en terminal
#Ahora transformamos una lista en tupla
lista = tuple(lista)
print(lista)
lista = list(lista)
#Buscamos un elemento en la tupla
print("Juean" in tupla)
#Cuenta la cantidad de veces de un elementa en la tupla
print(tupla.count(7))
#Nos da el tamaño de la tupla
print(len(tupla))
#Tupla unitaria lleeva si o si una coma
tupla1 = ("Razor",)
print(len(tupla1),tupla1)
#Desempaquetado de tupla
tupla2 = ("Luis",21,9,1992)
nom, dia, mes, agno = tupla2
print(nom)
print(dia)
print(mes)
print(agno)