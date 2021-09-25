rta = input("Hola,¿quieres sumar o restar? :")
if rta == "sumar":
    print("Vamos a sumar")
    x = int(input("ingresa el primer numero : "))
    y = int(input("ingresa el segundo numero : "))
    z = x+y
    print(x,"mas",y,"es",z)
if rta == "restar":
    print("Vamos a restar")
    x = int(input("ingresa el primer numero : "))
    y = int(input("ingresa el segundo numero : "))
    z = x-y
    print(x,"menos",y,"es",z)
else :
    print("Fin de la operacion")