print("----------------------------------------")
print("---------Creador de Contraseñas---------")
print("----------------------------------------")
import random
#Creando el diccionario
abcd = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
Uabcd= []
for a in abcd:
    Uabcd.append(a.upper())
abcd.extend(Uabcd)   #abcd = abcd + Uabcd    ------Nos daria el mismo resultado que arriba
abcd.extend(["@","!","&","$","%",1,2,3,4,5,6,7,8,9,0]) #simbolos recuerda los [ ] ya que solo acepta un argumento
#Ahora ya tenemos el abecedario mas numeros y simbolos-----> comenzamos el password
psw = ""
tam = int(input("Introduzca la cantidad de caracteres deseado : "))
for i in range(tam):
    psw = psw + str(random.choice(abcd))
print(psw)

#Otro metodo? operando con string
'''import string
New = string.ascii_letters + string.digits
print(New)

psw2 = random.choice(string.ascii_letters+string.digits)
print(psw2)
'''
#Funcion random Funciona pero necesita importar String es un Modulo
"""def newranstring(y):
    import string
    import random
    sw = ""
    for i in range(y):
        sw = sw + random.choice(string.ascii_letters+string.digits)
    return sw
y = int(input("Ingrese un numero de caracteres : "))
PSW = newranstring(y)
print(PSW)"""