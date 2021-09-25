print("------------------------------------------------------")
print("-Bienvenido ahora calcularemos sus dias de vacaciones-")
print("------------------------------------------------------")
nom = str (input("Ingrese su nombre por favor : "))
ant = int(input("ingrese su antiguedad en años : "))
cla = int(input("ingrese su clave de departamento : "))
if cla == 1 :
    if ant == 1 : 
        print(nom,"usted tiene derecho a 6 dias de vacaciones")
    elif ant <7 and ant > 1 :
        print(nom,"usted tiene derecho a 14 dias de vacaciones")
    elif ant >= 7 :
        print(nom,"usted tiene derecho a 20 dias de vacaciones")
    else :
        print(nom,"usted aun no tiene antiguedad suficiente para solicitar vacaciones")
elif cla == 2 :
    if ant == 1 : 
        print(nom,"usted tiene derecho a 7 dias de vacaciones")
    elif ant <7 and ant > 1 :
        print(nom,"usted tiene derecho a 15 dias de vacaciones")
    elif ant >= 7 :
        print(nom,"usted tiene derecho a 22 dias de vacaciones")
    else :
        print(nom,"usted aun no tiene antiguedad suficiente para solicitar vacaciones")
elif cla == 3 :
    if ant == 1 : 
        print(nom,"usted tiene derecho a 10 dias de vacaciones")
    elif ant <7 and ant > 1 :
        print(nom,"usted tiene derecho a 20 dias de vacaciones")
    elif ant >= 7 :
        print(nom,"usted tiene derecho a 30 dias de vacaciones")
    else :
        print(nom,"usted aun no tiene antiguedad suficiente para solicitar vacaciones")
else :
    print("No a introducido una clave de departamento valida")
print("Fin")