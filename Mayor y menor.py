print("----------------------------")
print("---Buscamos mayor y menor---")
print("----------------------------")

print("ingrese tres numeros:")
a = int(input())
b = int(input())
c = int(input())
if a>b and a>c :
    may = a 
elif b>a and b>c :
    may = b
else :
    may = c
if a<b and a<c :
    men = a 
elif b<a and b<c :
    men = b
else :
    men = c 
print(may,"Es el mayor y",men,"es el menor")