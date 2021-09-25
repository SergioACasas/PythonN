print("------------------------")
print("---Numero par o impar---")
print("------------------------")

rta = "y"
while rta == "y" :
    n = int(input("Ingrese un numero : "))
    if n % 2 == 0 :
        print(n,"Es Par")
    else :
        print(n,"Es Impar")
    rta = str(input("¿Desea ingresar otro numero? y/n : "))
print("Fin")
