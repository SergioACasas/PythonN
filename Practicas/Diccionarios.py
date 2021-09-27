#Los diccionarios son listas desordenadas con clave : valor
mi_dicc ={"Alemanio":"Berlin","Francia":"Paris","Reino Unido":"London","España":"Madrid",23:"Dragon"}
print(mi_dicc["Reino Unido"])#Recuerda va con [ ]
print(mi_dicc)
#Aumentar el diccionario y no se puede asignar mas de una pareja a cada valor
mi_dicc["Italia"] = "Lisboa"
print(mi_dicc)
mi_dicc["Italia"] = "Roma"
print(mi_dicc)
#Borramos del diccionario
del mi_dicc["Reino Unido"]
print(mi_dicc)
#Usando TUPLAS
tupla = ("Alemania","Francia","España")
new_dicc = {tupla[0]:"Berlin",tupla[1]:"Paris",tupla[2]:"Madrid"}
print(new_dicc)
#Diccionario contiene otros diccionarios, listas o tuplas
n_dicc = {23:"jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":{"Temporadad":[1991,1992,1993,1996,1997,1998]}}
print(n_dicc["Anillos"])
print(n_dicc)
#Mostramos las Keys=Claves y Values=Valores
print(n_dicc.keys())
print(n_dicc.values())
print(len(n_dicc))