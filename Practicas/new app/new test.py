"listar todas los archivos en la carpeta dir_path (no toma carpetas)"
"""import os

dir_path = r"D:\Documents\Books\Gesta _ Emotion expression\How to draw Moe characters (11)"
lista = []

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path,path)):
        lista.append(path)
print(lista)
for files in lista :
    nombre = files
    if nombre.endswith('pdf') or nombre.endswith('epub') or nombre.endswith('cbr') or nombre.endswith('cbz'):
        nstring = nombre.split('.')
        print(nstring[0])"""

import os
"""import os.path
count = 0
for dirpath, dirnames, filenames in os.walk("D:\Documents\Libros de Dibujos\Mejores"):
    for filename in [f for f in filenames if (f.endswith(".pdf") or f.endswith("epub") or f.endswith("cbz") or f.endswith("cbr"))]:
        direccion_libro = os.path.join(dirpath, filename)
        nombre_libro_ext_lista = os.path.join(filename).split(".")
        print(nombre_libro_ext_lista)               #innecesatio 
        n= nombre_libro_ext_lista.pop()
        print ("".join(nombre_libro_ext_lista))     #nombre de archivo
        print(direccion_libro)                      #direccion D:/a/d/nombre de archivo.txt
        print(n)                                    #typo de archivo
        count += 1
        
print("---------N° de archivos detectados:",count,"-----------")"""

import os.path
def extract_path_name_type (searchers):
    count = 0
    for dirpath, dirnames, filenames in os.walk("D:\Documents\Libros de Dibujos\Mejores"):
        for filename in [f for f in filenames if f.endswith(searchers)]:
            print(filename,"------------------------")  #nombre de archivo.txt
            direccion_libro = os.path.join(dirpath, filename)
            nombre_libro_ext_lista = os.path.join(filename).split(".")
            print(nombre_libro_ext_lista)               #innecesatio 
            n= nombre_libro_ext_lista.pop()
            print ("".join(nombre_libro_ext_lista))     #nombre de archivo
            print(direccion_libro)                      #direccion D:/a/d/nombre de archivo.txt
            print(n)                                    #typo de archivo
            count += 1
            
    print("---------N° de archivos detectados:",count,"-----------")

search_for =["pdf","epub","cbr","cbz","mobi"]
to_search = tuple(search_for)

extract_path_name_type(to_search)
print("-------------------end-------------------------")