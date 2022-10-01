import time
import mysql.connector ,os ,os.path
from  mysql.connector import Error

def insert_variables_libros(lista):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='libroscatalog',
                                            user='root',
                                            password='@soni21ericsonSQ')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Conectado a MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();") #se coloca el nombre de la base de datos
            record = cursor.fetchone()
            print("Conectado a la Base de Datos: ", record)
            '''realizando un insert a la tabla de libros'''
            for x, y in lista:
                INSERT_Query = f"INSERT INTO libros (nombre_libro,direccion_libro) values ('{x}','{y}');"
                cursor.execute(INSERT_Query)
                connection.commit()
            print(cursor.rowcount,"lista se añadio en la base de datos con exito!!!")
            cursor.close()
        
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL conexion se cerrada")

def extract_path_name_type (searchers,direccion_carpeta):
    count = 0
    LL_D = []
    for dirpath, dirnames, filenames in os.walk(direccion_carpeta):
        for filename in [f for f in filenames if f.endswith(searchers)]:
            #print(filename,"------------------------")  #nombre de archivo.txt
            direccion_libro = os.path.join(dirpath, filename)
            nombre_libro_ext_lista = os.path.join(filename).split(".")
            #print(nombre_libro_ext_lista)               #innecesatio 
            n= nombre_libro_ext_lista.pop()
            #print ("".join(nombre_libro_ext_lista))     #nombre de archivo
            #print(direccion_libro)                      #direccion D:/a/d/nombre de archivo.txt
            #print(n)                                    #typo de archivo
            direccion_libro = direccion_libro.replace("\\","/")
            direccion_libro = direccion_libro.replace("'", r"\'")
            direccion_libro = direccion_libro.replace('"', r'\"')
            nom_libro = "".join(nombre_libro_ext_lista)
            nom_libro = nom_libro.replace("'", r"\'")
            nom_libro = nom_libro.replace('"', r'\"')
            LL_D.append((nom_libro,direccion_libro))
            count += 1
            
    print("---------N° de archivos detectados:",count,"-----------")
    return(LL_D)

start_wtime = time.time()
start_ptime = time.process_time()

search_for =["pdf","epub","cbr","cbz","mobi"]
to_search = tuple(search_for)

directorio = "D:\Documents\Libros de Dibujos\Mejores"
lista = extract_path_name_type(to_search,directorio)

insert_variables_libros(lista)

end_wtime = time.time()
end_ptime = time.process_time()
print("Time for execution (Wall-Clock Time) :",(end_wtime-start_wtime)*1000,"ms")
print("Time for execution (CPU time)",(end_ptime-start_ptime)*1000,"ms")
print("------------------------programa finalizo---------------------------------")