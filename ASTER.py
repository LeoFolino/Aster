import tkinter as tk
from tkinter import ttk
import sys
import os

def cargar_errores(archivo):
    errores = {}
    with open(archivo, 'r', encoding='utf-8') as file:
        for linea in file:
            partes = linea.strip().split('|')
            if len(partes) == 4:
                codigo, respuesta, accion, tipificacion = partes
                accion = accion.replace("\\n", "\n")  # Reemplazar marcador por salto de línea real
                errores[codigo] = {"respuesta": respuesta, "accion": accion, "tipificacion": tipificacion}
    return errores

# Determinar la ruta base de la aplicación (la misma del script o ejecutable)
if getattr(sys, 'frozen', False):
    # Si está congelado, usar el directorio del sistema
    application_path = os.path.dirname(sys.executable)
else:
    # Si no está congelado, usar el directorio del script
    application_path = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta al archivo de errores
archivo_errores = os.path.join(application_path, 'data\errores.txt')

# Cargar los errores
errores = cargar_errores(archivo_errores)


def buscar_error(errores, codigo_error):
    error_info = errores.get(codigo_error, {"respuesta": "Código de error no reconocido", "accion": "Verificar el código e intentar nuevamente.", "tipificacion": "---------"})
    return error_info["respuesta"], error_info["accion"], error_info["tipificacion"]

def mostrar_respuesta(event=None):
    codigo_error = entry.get()
    respuesta, accion, tipificacion = buscar_error(errores, codigo_error)
    descripcion_label.config(text="Descripción: \n" + respuesta)
    accion_label.config(text="Respuesta técnica: \n\n" + accion)

    if respuesta != "Código de error no reconocido":
        tipificacion_label.config(text="¿Cómo debo tipificarlo?: " + tipificacion, fg='#E0004D', bg='#FFFFFF')
    else:
        tipificacion_label.config(text="", fg='#FFFFFF', bg='#221551')

# Asegúrate de que la ruta al archivo 'errores.txt' sea la correcta.
errores = cargar_errores('data\errores.txt')


# Configuraciones de la ventana principal y estilo de texto
root = tk.Tk()
root.title("Buscador de Errores")
root.geometry("600x400")
root.configure(bg='#221551')
root.resizable(False, False)

fuente_texto = ("Arial", 12)
fuente_label_titulo = ("Helvetica", 14, "bold") 
fuente_tipificacion = ("Comic Sans MS", 14, "bold") 

# Widgets de la interfaz
label_titulo = tk.Label(root, text="Ingrese el código de error:", font=fuente_label_titulo, bg='#221551', fg='#FFFFFF')
label_titulo.pack()

entry = tk.Entry(root, font=fuente_texto)
entry.pack()
entry.bind("<Return>", mostrar_respuesta)

button = tk.Button(root, text="Buscar", command=mostrar_respuesta, font=fuente_texto, bg='#E0004D', fg='#FFFFFF')
button.pack()

# Para el campo de entrada
entry.pack(pady=(10, 0))

# Para el botón, agregamos espacio solo en la parte superior
button.pack(pady=(10, 20))

# Configuración inicial del label de "¿Cómo debo tipificarlo?:"
# El fondo inicial es el mismo que el de la ventana y el texto en blanco
tipificacion_label = tk.Label(root, text="", fg='#FFFFFF', bg='#221551', font=fuente_tipificacion, wraplength=580)
tipificacion_label.pack()

# Líneas horizontales y labels para resultados
tk.Frame(root, height=2, bd=1, relief="sunken", bg='#221551').pack(fill="x", padx=5, pady=5)
descripcion_label = tk.Label(root, text="", fg='#FFFFFF', bg='#221551', font=fuente_texto, wraplength=580)
descripcion_label.pack()

tk.Frame(root, height=2, bd=1, relief="sunken", bg='#221551').pack(fill="x", padx=5, pady=5)
accion_label = tk.Label(root, text="", fg='#FFFFFF', bg='#221551', font=("Helvetica", 14, "bold"), wraplength=580, anchor='w', justify='left')
accion_label.pack(fill='x', padx=(10,0))  # padx con una tupla crea margen solo a la izquierda

tk.Frame(root, height=2, bd=1, relief="sunken", bg='#221551').pack(fill="x", padx=5, pady=5)
tipificacion_label = tk.Label(root, text="", fg='#FFFFFF', bg='#221551', font=fuente_tipificacion, wraplength=580)
tipificacion_label.pack()

root.mainloop()