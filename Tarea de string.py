#contar la cantidad de letras en una oracion
a = "Esta es la oracion de prueba para la tarea"
print(a)
print("La oracion tiene",len(a),"letras contando espacios")
a = a.split(" ")
print(a) 
a = "".join(a)
print("la cantidad de letras sin espacios es",len(a))
print(a)