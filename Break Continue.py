##Ejemplo Break
i=0
while i <11 :
    i +=1
    if i == 5 :
        break
    else :
        print("el numero es",i)
print("El brake se activo")
#Ejemplo Continue
t=0
while t <11 :
    t +=1
    if t == 5 :
        continue
        #Funciona como un go to while
    else :
        print("el numero es",t)
print("El continue se activo en 5")