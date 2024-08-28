import mysql.connector
from mysql.connector import Error

def create_connection():
    #"""Establece una conexión con la base de datos MySQL."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',        # Cambia esto si tu MySQL está en otro host
            user='root',    # Tu nombre de usuario de MySQL
            password='',# Tu contraseña de MySQL
            database='example' # El nombre de tu base de datos
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos MySQL")
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    return connection

def list_data():
    """Lista los datos de una tabla en la base de datos MySQL."""
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM users"  
            cursor.execute(query)
            results = cursor.fetchall()
            
            for row in results:
                print(row)
                
        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")
        finally:
            cursor.close()
            connection.close()

list_data()