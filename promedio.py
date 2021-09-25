nombre = input("¿Cual es tu nombre? : ")
mat = int(input("¿cual es tu calificacion en matematicas? : "))
eng = int(input("¿cual es tu calificacion en ingles? : "))
soc = int(input("¿cual es tu calificacion en sociales? : "))
prom = (mat + eng + soc)/3
if prom >= 6 :
    print("Felicidades",nombre,"Aprobaste con un promedio de",round(prom,2))
else :
    #round(el numero a limitar. numero de decimales)
    print("Lo lamento",nombre,"tu promedio es",round(prom,2))
print("Fin")