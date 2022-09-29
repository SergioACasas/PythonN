"Python to SQL database"
import mysql.connector
from  mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='libroscatalog',
                                         user='root',
                                         password='@soni21ericsonSQ')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Conectado a MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Conectado a la Base de Datos: ", record)
        '''comenzando el query para mostrar la tabla libros'''
        sql_select_query  = " SELECT * FROM libros;"
        cursor= connection.cursor()
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        print("Numero total de filas en tabla libros : ",cursor.rowcount)
        print ("\nPrinting each row")
        for row in records:
         print("id = ",row[0])
         print("Nombre = ",row[1])
         print("direccion = ",row[2],"\n")

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL conexion se cerrada")


