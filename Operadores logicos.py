print("Conjunciones")
a = int(input("escribe un numero mayor a 3 y menor a 7 : "))
if a>3 and a < 7 :
    print("el numero cumple la conjuncion")
else :
    print("el numero no cumple la conjuncion")
pal = str(input("escriba ´si´ o ´yes´ : "))
if pal == "si" or pal == "yes" :
    print("la condicion se a cumplido")
else :
    print("no cumple la conjuncion")
b = int(input("No ingrese 5 : "))
if not b == 5 :
    print("se cumplio la condicion")
else :
    print("el numero no cumple la condicion")
print("Fin")