"Python SQL insert script for Libros"
import mysql.connector
from  mysql.connector import Error

def insert_variables_libros(nombre_libro,direccion_libro):

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
            '''realizando un insert a la tabla de libros'''
            INSERT_Query = "INSERT INTO libros (nombre_libro,direccion_libro) values (%s,%s);"
            cursor= connection.cursor()
            cursor.execute(INSERT_Query)
            connection.commit()
            print(cursor.rowcount,"revisa a ver si se actualizo la base de datos!!!")
            cursor.close()
    
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL conexion se cerrada")


