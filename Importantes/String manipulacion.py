#Formas de manipulacion de strings
#Busqueda de palabras y su lugar (recordemos que cuenta desde 0 por eso el +1)
string = "Aqui hay muchas palabras para Buscar"
print(string)
print("¿esta 'palabra' en la oracion?","palabras" in string )
print("¿en que posicion comienza la palabra 'para'",string.find("para")+1)
print("¿no esta 'palabra' en la oracion?","palabras" not in string)
#Busqueda de cantidad de palabras o letras
print("¿Cuantas veces esta la palabra 'hay' :",string.count("hay"))
print("¿Cuantas veces esta la palabra 'mono' :",string.count("mono"))
print("¿Cuantas veces esta la letra 'a' :",string.count("a"))
#Podemos saber el tamaño de la oracion con len()
print("el tamaño de la primera oracion es de :",len(string))
#Podemos acceder una letra en una posicion o un grupo
print("mostraremos el espacio 7 :",string[6])
print("mostraremos las letras entre 10 y 16 :",string[9:15])
#transformamos las palabras a minusculas o mayusculas
string = string.lower()
print(string)
string = string.upper()
print(string)
#para saber si algo esta en minuscula, Mayuscula, numerica o decimal se usa
print("¿Todo esta en minuscula?",string.islower())
print("¿Es numerico?",string.isnumeric())
print("¿Esta en mayuscula?",string.isupper())
#Nos podemos fijar si comienza o termina como queremos
stringA = "Una nueva oracion para analizar"
print(stringA)
print("¿la nueva oracion comienza con 'una'?",stringA.startswith("Una"))
print("¿la nueva oracion termina con 'dos'?",stringA.endswith("dos"))
#Podemos separar la oracion en un array y usarlo
print(stringA.split(" "))
stringA_separada = stringA.split(" ")
print("se muestra un array guardado",stringA_separada)
print("Ahora uniremos el array con un ' ' de por medio : "," ".join(stringA_separada))
#Podemos eliminar espacios al principio y al final con .strip, .lstrip, .rstrip
stringN = "                    ahora vamos a eliminar el espacio inecesario      "
print(stringN)
print(stringN.strip())
#Podemos remplazar palabras en una nueva variable
stringN = stringN.replace("espacio","universo")
print("cambiaremos la palabra 'espacio' por  'universo' :",stringN)
#Concatenacion dinamica
print("concatenaremos 3 palabras ingresadas :")
print("La oracion a completar es : {} {}. bienvenido!")
a=str(input())
b=str(input())
message= "{},{},Bienvenido".format(a,b)
print(message)
#F string puedes correr codigo en {}
message = f"{a.upper()},{b.lower()}. Buenaventura"
print(message)
#Busqueda de ayuda
print(help(str))