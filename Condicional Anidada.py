rta = "y"
while rta == "y" :
    print("\n")
    print("Menu de opciones :\n")
    print("Ingresa 1 para convertir numeros a palabras")
    print("Ingresa 2 para convertir palabras a numeros")
    opc = int(input())
    if opc == 1 :
        num = int(input("Ingresa un numero del 1 al 5 : "))
        if num == 1 :
            print("el numero ingresado es UNO ")
        elif num == 2 :
                print("el numero ingresado es DOS ")
        elif num == 3 :
            print("el numero ingresado es TRES ")
        elif num == 4 :
            print("el numero ingresado es CUATRO ")
        elif num == 5 :
            print("el numero ingresado es CINCO ")
        else :
            print("el numero ingresado no esta entre 1 y 5")
    elif opc == 2 :
        num = str(input("Escriba con letras un numero del uno al cinco: "))
        #-lower pasa toda la cadena de palabras a minuscula
        num = num.lower()
        if num == "uno" :
            print("el numero ingresado es 1 ")
        elif num == "dos" :
                print("el numero ingresado es 2 ")
        elif num == "tres" :
            print("el numero ingresado es 3 ")
        elif num == "cuatro" :
            print("el numero ingresado es 4 ")
        elif num == "cinco" :
            print("el numero ingresado es 5 ")
        else :
            print("el numero ingresado no esta entre 1 y 5")
    else :
        print("no se eligio una opcion vaalida")
    rta = str(input("¿quiere correr el programa de nuevo? y/n : "))

print("Fin")