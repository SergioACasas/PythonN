rta = "y"
while rta == "y" :
    print("ingrese dos numros a comparar")
    a = int(input("Numero a : "))
    b = int(input("Numero b : "))
    #tambien estan != diferente <= y >=
    if a==b :
        print(a,"es igual a",b)
    elif a>b :
        print(a,"es mayor que",b)
    else :
        print(a,"es menor que",b)
    print(" ")
    rta = str(input("¿Desea ejecutar el programa de nuevo? y/n : "))
    print(" ")
print("Fin.")