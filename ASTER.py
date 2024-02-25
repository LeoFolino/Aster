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

def cargar_codigos_en_combobox(errores):
    lista_codigos = list(errores.keys())
    lista_codigos.sort(key=int)  # Ordenamos numéricamente si es posible
    return lista_codigos

def buscar_error(errores, codigo_error):
    error_info = errores.get(codigo_error, {"respuesta": "Código de error no reconocido", "accion": "Verificar el código e intentar nuevamente.", "tipificacion": "---------"})
    return error_info["respuesta"], error_info["accion"], error_info["tipificacion"]

def mostrar_respuesta(event=None):
    codigo_error = combobox.get()
    respuesta, accion, tipificacion = buscar_error(errores, codigo_error)
    descripcion_label.config(text="Descripción: \n" + respuesta)
    accion_label.config(text="Respuesta técnica: \n\n" + accion)
    if respuesta != "Código de error no reconocido":
        tipificacion_label.config(text="¿Cómo debo tipificarlo?: " + tipificacion, fg='#E0004D', bg='#FFFFFF')
    else:
        tipificacion_label.config(text="", fg='#FFFFFF', bg='#221551')

# Determinar la ruta base de la aplicación (la misma del script o ejecutable)
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

archivo_errores = os.path.join(application_path, 'data\errores.txt')
errores = cargar_errores(archivo_errores)

root = tk.Tk()
root.title("Buscador de Errores")
root.geometry("600x400")
root.configure(bg='#221551')
root.resizable(False, False)

fuente_texto = ("Arial", 12)
fuente_label_titulo = ("Helvetica", 14, "bold") 
fuente_tipificacion = ("Comic Sans MS", 14, "bold") 

label_titulo = tk.Label(root, text="Seleccione el código de error:", font=fuente_label_titulo, bg='#221551', fg='#FFFFFF')
label_titulo.pack(pady=(10, 10))

codigos_error = cargar_codigos_en_combobox(errores)
combobox = ttk.Combobox(root, values=codigos_error, font=fuente_texto)
combobox.pack(pady=(0, 20))
combobox.bind('<<ComboboxSelected>>', mostrar_respuesta)  # Vincular evento de selección al método mostrar_respuesta
combobox.bind('<Return>', mostrar_respuesta)  # Evento al presionar Enter

button = tk.Button(root, text="Buscar", command=mostrar_respuesta, font=fuente_texto, bg='#E0004D', fg='#FFFFFF')
button.pack()

descripcion_label = tk.Label(root, text="", fg='#FFFFFF', bg='#221551', font=fuente_texto, wraplength=580)
descripcion_label.pack(pady=(10, 0))

accion_label = tk.Label(root, text="", fg='#FFFFFF', bg='#221551', font=("Helvetica", 14, "bold"), wraplength=580, anchor='w', justify='left')
accion_label.pack(fill='x', padx=(10,0))

tipificacion_label = tk.Label(root, text="", fg='#FFFFFF', bg='#221551', font=fuente_tipificacion, wraplength=580)
tipificacion_label.pack(pady=(10, 0))

root.mainloop()
