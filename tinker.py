import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
from tkinter import CENTER
# Función para conectar a la base de datos
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='localhost', 
            database='testlive',
            user='root', 
        )
        return connection
    except Error as e:
        messagebox.showerror("Error", f"No se pudo conectar a la base de datos: {e}")
        return None

# Función para crear la tabla si no existe
def create_table_if_not_exists():
    connection = connect_to_db()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                Documento VARCHAR(10) PRIMARY KEY,
                Nombres VARCHAR(30),
                Apellidos VARCHAR(30),
                Teléfono VARCHAR(15),
                Dirección VARCHAR(50)
            )
        """)
        connection.commit()
    except Error as e:
        messagebox.showerror("Error", f"No se pudo crear la tabla: {e}")
    finally:
        connection.close()

# Función para insertar un registro
def insert_record():
    connection = connect_to_db()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        query = "INSERT INTO usuarios (Documento, Nombres, Apellidos, Teléfono, Dirección) VALUES (%s, %s, %s, %s, %s)"
        values = (doc_entry.get(), name_entry.get(), surname_entry.get(), phone_entry.get(), address_entry.get())
        cursor.execute(query, values)
        connection.commit()
        messagebox.showinfo("Éxito", "Usuario registrado correctamente")
        update_treeview()
    except Error as e:
        messagebox.showerror("Error", f"No se pudo insertar el registro: {e}")
    finally:
        connection.close()

def fetch_all_records():
    connection = connect_to_db()
    if connection is None:
        return []
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM usuarios"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except Error as e:
        messagebox.showerror("Error", f"No se pudo recuperar los registros: {e}")
        return []
    finally:
        connection.close()

def update_treeview():
    records = fetch_all_records()
    
    # Limpiar el Treeview existente
    for row in tabla.get_children():
        tabla.delete(row)
    
    # Insertar datos en el Treeview
    for row in records:
        tabla.insert("", tk.END, values=row)
# Función para buscar un registro
def search_record():
    connection = connect_to_db()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM usuarios WHERE Documento = %s"
        cursor.execute(query, (doc_entry.get(),))
        row = cursor.fetchone()
        if row:
            name_entry.delete(0, tk.END)
            name_entry.insert(0, row[1])
            surname_entry.delete(0, tk.END)
            surname_entry.insert(0, row[2])
            phone_entry.delete(0, tk.END)
            phone_entry.insert(0, row[3])
            address_entry.delete(0, tk.END)
            address_entry.insert(0, row[4])
        else:
            messagebox.showwarning("No encontrado", "Usuario no encontrado")
    except Error as e:
        messagebox.showerror("Error", f"No se pudo buscar el registro: {e}")
    finally:
        connection.close()

# Función para modificar un registro
def update_record():
    connection = connect_to_db()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        query = "UPDATE usuarios SET Nombres = %s, Apellidos = %s, Teléfono = %s, Dirección = %s WHERE Documento = %s"
        values = (name_entry.get(), surname_entry.get(), phone_entry.get(), address_entry.get(), doc_entry.get())
        cursor.execute(query, values)
        connection.commit()
        messagebox.showinfo("Éxito", "Usuario actualizado correctamente")
        update_treeview()
    except Error as e:
        messagebox.showerror("Error", f"No se pudo actualizar el registro: {e}")
    finally:
        connection.close()

# Función para eliminar un registro
def delete_record():
    connection = connect_to_db()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        query = "DELETE FROM usuarios WHERE Documento = %s"
        cursor.execute(query, (doc_entry.get(),))
        connection.commit()

        # Verificar si alguna fila fue afectada
        if cursor.rowcount > 0:
            clear_form()
            messagebox.showinfo("Éxito", "Usuario eliminado correctamente")
            update_treeview()
        else:
            messagebox.showinfo("Información", "No se encontró un usuario con ese documento")

    except Error as e:
        messagebox.showerror("Error", f"No se pudo eliminar el registro: {e}")
    finally:
        connection.close()


# Función para limpiar los campos del formulario
def clear_form():
    doc_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    surname_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    update_treeview()

# Crear la tabla al iniciar
create_table_if_not_exists()

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Usuarios")

# Colores
label_color = "#007BFF"  # Color azul para las etiquetas
button_bg_color = "white"  # Color blanco para los botones
button_fg_color = "#000000"  # Color negro oscuro para el texto de los botones

# Crear etiquetas y campos de entrada con color en las etiquetas
tk.Label(root, text="Documento", fg=label_color).grid(row=0, column=0, padx=10, pady=10)
doc_entry = tk.Entry(root)
doc_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Nombres", fg=label_color).grid(row=1, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Apellidos", fg=label_color).grid(row=2, column=0, padx=10, pady=10)
surname_entry = tk.Entry(root)
surname_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Teléfono", fg=label_color).grid(row=3, column=0, padx=10, pady=10)
phone_entry = tk.Entry(root)
phone_entry.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Dirección", fg=label_color).grid(row=4, column=0, padx=10, pady=10)
address_entry = tk.Entry(root)
address_entry.grid(row=4, column=1, padx=10, pady=10)

# Crear botones con fondo blanco y letra negra
tk.Button(root, text="Insertar", command=insert_record, bg=button_bg_color, fg=button_fg_color).grid(row=5, column=0, padx=10, pady=10)
tk.Button(root, text="Buscar", command=search_record, bg=button_bg_color, fg=button_fg_color).grid(row=5, column=1, padx=10, pady=10)
tk.Button(root, text="Modificar", command=update_record, bg=button_bg_color, fg=button_fg_color).grid(row=6, column=0, padx=10, pady=10)
tk.Button(root, text="Eliminar", command=delete_record, bg=button_bg_color, fg=button_fg_color).grid(row=6, column=1, padx=10, pady=10)
tk.Button(root, text="Limpiar", command=clear_form, bg=button_bg_color, fg=button_fg_color).grid(row=7, column=0, padx=10, pady=10, columnspan=2)

# Configuración de la tabla (Treeview)
tabla = ttk.Treeview(root, height=10, columns=("doc", "name", "surname", "phone", "address"), show="headings")
tabla.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

# Definir encabezados de la tabla
tabla.heading("doc", text="Documento", anchor=CENTER)
tabla.heading("name", text="Nombres", anchor=CENTER)
tabla.heading("surname", text="Apellidos", anchor=CENTER)
tabla.heading("phone", text="Teléfono", anchor=CENTER)
tabla.heading("address", text="Dirección", anchor=CENTER)

root.mainloop()



