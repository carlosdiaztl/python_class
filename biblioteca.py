import mysql.connector
from mysql.connector import Error
from faker import Faker
fake = Faker()

def create_connection():
    """Establece una conexion con la base de datos MySQL."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',        # Cambia esto si tu MySQL está en otro host
            user='root',    # Tu nombre de usuario de MySQL
            password='',    # Tu contraseña de MySQL
            database='example' # El nombre de tu base de datos
        )
        if connection.is_connected():
            print("Conexion exitosa a la base de datos MySQL")
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    return connection

def create_table(connection):
    """Crea la tabla 'libros' en la base de datos si no existe."""
    try:
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS libros (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(255) NOT NULL,
            autor VARCHAR(255) NOT NULL,
            isbn VARCHAR(13) UNIQUE NOT NULL,
            disponibilidad BOOLEAN NOT NULL
        )
        """
        cursor.execute(create_table_query)
        print("Tabla 'libros' creada exitosamente.")
    except Error as e:
        print(f"Error al crear la tabla: {e}")
    finally:
        cursor.close()

class Libro:
    def __init__(self, titulo, autor, isbn, disponibilidad):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponibilidad = disponibilidad
    
    def prestar(self):
        if self.disponibilidad:
            self.disponibilidad = False
            print(f"El libro '{self.titulo}' ha sido prestado")
        else:
            print(f"El libro '{self.titulo}' ya no está disponible")

class Biblioteca:
    def __init__(self):
        self.connection = create_connection()
        if self.connection:
            create_table(self.connection)
    
    def agregar_libro(self, libro):
        """Agrega un libro a la base de datos."""
        try:
            cursor = self.connection.cursor()
            insert_query = """
            INSERT INTO libros (titulo, autor, isbn, disponibilidad) 
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insert_query, (libro.titulo, libro.autor, libro.isbn, libro.disponibilidad))
            self.connection.commit()
            print(f"Libro '{libro.titulo}' agregado a la base de datos.")
        except Error as e:
            print(f"Error al agregar el libro: {e}")
        finally:
            cursor.close()
    def prestar_libro(self, libro):
        """Prestamo de libro."""
        try:
            cursor = self.connection.cursor()
            update_query = """
            UPDATE `example`.`libros` SET `disponibilidad`='0' WHERE  `titulo`=(%s); 
            """
            cursor.execute(update_query, (libro.titulo,))
            self.connection.commit()
            print(f"Libro '{libro.titulo}' Prestado.")
        except Error as e:
            print(f"Error al Prestar el libro: {e}")
        finally:
            cursor.close()
    
    def mostrar_libros(self):
        """Muestra todos los libros disponibles en la base de datos."""
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM libros"
            cursor.execute(query)
            results = cursor.fetchall()
            
            if not results:
                print("No hay libros en la biblioteca.")
            else:
                for row in results:
                    print(f"ID: {row[0]}, Titulo: {row[1]}, Autor: {row[2]}, ISBN: {row[3]}, Disponibilidad: {'Disponible' if row[4] else 'No disponible'}")
                    print("-" * 40)
                
        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")
        finally:
            cursor.close()
            self.connection.close()


biblioteca = Biblioteca()

libro1 = Libro(fake.catch_phrase(), fake.name(), fake.isbn13(), True)
libro2 = Libro(fake.catch_phrase(), fake.name(), fake.isbn13(), True)
libro3 = Libro("1984", "George Orwell", "1234567890", True)

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.prestar_libro(libro3)

biblioteca.mostrar_libros()
