print("------------------------")
print("------Calculadora-------")
print("------------------------")
print(" ")
rta = "y"
while rta == "y" :
    print("Ingrese el codigo de la operacion a realizar : ")
    print(" 1 . Suma")
    print(" 2 . Resta")
    print(" 3 . Multiplicacion")
    print(" 4 . Division")
    print(" 5 . Exponente")
    print(" 6 . Modulo o Resto")
    code = int(input(" "))
    if code == 1 :
        a = int(input("Suma \n Ingrese el primer numero : "))
        b = int(input(" Ingrese el segundo numero : "))
        c = a+b
        print(" El resultado de",a,"+",b,"es:",c)
    elif code == 2 :
        a = int(input("Resta \n Ingrese el primer numero : "))
        b = int(input(" Ingrese el segundo numero : "))
        c = a-b
        print(" El resultado de",a,"-",b,"es:",c)
    elif code == 3 :
        a = int(input("Multiplicacion \n Ingrese el primer numero : "))
        b = int(input(" Ingrese el segundo numero : "))
        c = a*b
        print(" El resultado de",a,"x",b,"es:",c)
    elif code == 4 :
        a = int(input("Division \n Ingrese el dividendo : "))
        b = int(input(" Ingrese el divisor : "))
        if b == 0 :
            print(" No se puede dividir por 0")
        else :
            c = a/b
            print(" El resultado de",a,"/",b,"es:",round(c,2))
    elif code == 5 :
        a = int(input("Exponente \n Ingrese la base : "))
        b = int(input(" Ingrese el exponente : "))
        c = a**b
        print(" El resultado de",a,"elevado a",b,"es:",c)
    elif code == 6 :
        a = int(input("Modulo o Resto \n Ingrese el dividendo: "))
        b = int(input(" Ingrese el divisor : "))
        c = a%b
        print(" El resto de",a,"/",b,"es:",c)
    else :
        print("El codigo ingresado no es valido")
    rta =str(input("¿Quiere realizar otra operacion? y/n : "))
print("Fin")