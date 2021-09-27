#Intento Original arreglado si Funciona !!!!!!
asignaturas = ["Informatica","Pruebas de software","Matematicas Discretas","A"]
print("Asignaturas optativas de Ciencias Informaticas")
print(asignaturas)
asig= str(input("Introduce la materia a tomar : ")).lower() #Si funciona para pasarlo directamente
#No es necesario inicializar i = 0 siempre comienza desde el inicio
for i in range(len(asignaturas)):
    asignaturas[i] = asignaturas[i].lower()
    print(asignaturas)
if asig in asignaturas :
    print("Elegiste la materia de :",asig)
else :
    print("No se introducio una materia valida")
#Intento con nueva lista modificada si funciona!!!!!!!
'''asignaturas = ["Informatica","Pruebas de software","Matematicas Discretas","A"]
print("Asignaturas optativas de Ciencias Informaticas")
print(asignaturas)
asig= str(input("Introduce la materia a tomar : ")).lower()
i = 0
asos = []
print(type(asos))
for i in asignaturas:
    x= i
    x =x.lower()
    asos.append(x)
    print(asos)
if asig in asos :
    print("Elegiste la materia de :",asig)
else :
    print("No se introducio una materia valida")'''
'''edad = -7
if 0<edad<100  :
    print("la edad es correcta")
else :
    print("la edad es incorrecta")
print("Programa de becas")
distancia = int(input("Introduce distancia a la escuela en km : "))
numherm = int(input("Introduce el numero de hermanos : "))
salario = int(input("Introduce el salario anual en bruto : "))
if distancia>40 and numherm>2 or salario<20000 :
    print("Usted es elegible a una beca")
else :
    print("No es elegible para una beca")'''