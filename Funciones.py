#Principal utlilidad es la reutilizacion de codigo
#Vamos a crear una Funcion

def mensaje():
    print("")
    print("Estamos aprendiendo python")
    print("Aprendiendo intrucciones Basicas")
    print("Poco a poco vamos avanzando")
    print("")
mensaje()
print("Ejecutando codigo fuera de la funcion")
mensaje()
#Definiremos una funcion de suma con parametros o argumentos
def sumaF(n1,n2):
    print("La suma de",n1,"mas",n2,"es =",n1+n2)
sumaF(10,7)
x=int(input("ingrese un numero :"))
y=int(input("INgrese otro numero :"))
def multiplicar(x,y):
    z = x*y
    return z
#se debe almazenar la funcion si tiene un return
z=multiplicar(x,y)
print("La suma de",x,"mas",y,"es=",z)