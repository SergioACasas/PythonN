#Asignaciones x+= , x-= , x*= , x/= , x//= , X**= , x%= 
nom = "Hola "
nom += str(input("Introduce tu nombre : "))
print(nom,"aumentaremos y disminuiremos un numero X en +5 y *10")
x= int(input("introduce un numero : "))
x += 5
print("X +5 es",x)
x -= 5
x *= 10
print("x por 10 es",x)