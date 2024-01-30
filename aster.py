import tkinter as tk
from tkinter import messagebox

def buscar_error(errores, codigo_error):
    error_info = errores.get(codigo_error, {"respuesta": "Código de error no reconocido", "accion": "Verificar el código e intentar nuevamente.", "tipificacion": "---------"})
    return error_info["respuesta"], error_info["accion"], error_info["tipificacion"]

def mostrar_respuesta(event=None):
    codigo_error = entry.get()
    respuesta, accion, tipificacion = buscar_error(errores, codigo_error)
    descripcion_label.config(text="Descripción: \n" + respuesta)
    accion_label.config(text="Respuesta técnica: \n\n" + accion)

    # Asegúrate de que esta condición se cumple para cambiar los colores del texto y fondo
    if respuesta != "Código de error no reconocido":
        # Texto en color rojo/magenta y fondo blanco
        tipificacion_label.config(text="¿Cómo debo tipificarlo?: " + tipificacion, fg='#E0004D', bg='#FFFFFF')
    else:
        # Texto en blanco y fondo del color original si no hay error
        tipificacion_label.config(text="", fg='#FFFFFF', bg='#221551')

# Diccionario con los códigos de error y la tipificación "No elevar gestión técnica. Funciona correctamente"
errores = {
    "1": {"respuesta": "Contactar al Emisor", "accion": "Cliente debe consultar con el banco."},
    "3": {"respuesta": "Comercio Invalido", "accion": "Realizar otro intento, de persistir el cliente debe consultar con el banco."},
    "4": {"respuesta": "Capturar Tarjeta", "accion": "Cliente debe consultar con el banco."},
    "5": {"respuesta": "DENEGADA", "accion": "Cliente debe consultar con el banco."},
    "12": {"respuesta": "Operacion rechazada por entidad bancaria", "accion": "Cliente debe consultar con el banco"},
    "13": {"respuesta": "MONTO INVALIDO", "accion": "Agente coloca monto invalido (Ejemplo: $1)."},
    "51": {"respuesta": "Fondos Insuficientes", "accion": "Cliente debe intentar con otra tarjeta."},
    "54": {"respuesta": "Tarjeta Vencida", "accion": "Cliente intentar con otra tarjeta."},
    "55": {"respuesta": "PIN Invalido", "accion": "Cliente ingresar correctamente el PIN del cajero automático."},
    "57": {"respuesta": "TRX No permitida por la Tarjeta", "accion": "Cliente debe intentar con otra tarjeta"},
    "61": {"respuesta": "Supera limite diario de extracción", "accion": "Cliente supero el limite diario de extraccion permitido por su banco"},
    "62": {"respuesta": "Tarjeta Restringida", "accion": "Realizar otro intento, de persistir el cliente debe consultar con el banco."},
    "75": {"respuesta": "Excedió la cantidad de intentos de ingresar PIN", "accion": "Cliente esta ingresando reiteradas veces mal el PIN del CAJERO AUTOMATICO."},
    "82": {"respuesta": "Banda o Chip dañados", "accion": "Intentar nuevamente o con otro método"},
    "-2": {"respuesta": "Cancelado por el operador", "accion": "1)Validar operatoria\n2) De persistir elevar caso técnico", "tipificacion": "Débito Fiserv - Otros Inconvenientes"},
    "-5": {"respuesta": "Sin comunicación con SiTef", "accion": "Elevar caso técnico", "tipificacion": "Débito Fiserv - Otros Inconvenientes"},
    "-6": {"respuesta": "Cancelado por el usuario", "accion": "1) Reiniciar pinpad y probar nuevamente\n2) Reiniciar puesto si continúa el inconveniente\n3) Elevar caso técnico si persiste", "tipificacion": "Débito Fiserv - Otros Inconvenientes"},
    "-43": {"respuesta": "Error en operatoria del pinpad", "accion": "1) Validar operatoria\n2) De persistir reiniciar pinpad y probar nuevamente\n3) Reiniciar puesto si continúa el inconveniente\n4) Elevar caso técnico si persiste", "tipificacion": "Débito Fiserv - Otros Inconvenientes"},
    "-100": {"respuesta": "Utiliza CONTACTLESS para EXTRACCIONES", "accion": "Explicar la operatoria y recomendar utilizar chip para las tarjetas que tienen contactless", "tipificacion": "No elevar gestión técnica. Funciona correctamente"}
    # Agregar la tipificación "No elevar gestión técnica. Funciona correctamente" a los errores existentes
}
# Asegurarse de que todos los errores existentes tengan la tipificación adecuada
for key in errores:
    if "tipificacion" not in errores[key]:
        errores[key]["tipificacion"] = "No elevar gestión técnica. Funciona correctamente"

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

# Configuración inicial del label de "¿Cómo debo tipificarlo?:"
# El fondo inicial es el mismo que el de la ventana y el texto en blanco
tipificacion_label = tk.Label(root, text="", fg='#FFFFFF', bg='#221551', font=fuente_tipificacion, wraplength=580)
tipificacion_label.pack()

# Líneas horizontales y labels para resultados
tk.Frame(root, height=2, bd=1, relief="sunken", bg='#221551').pack(fill="x", padx=5, pady=5)
descripcion_label = tk.Label(root, text="", fg='#FFFFFF', bg='#221551', font=fuente_texto, wraplength=580)
descripcion_label.pack()

tk.Frame(root, height=2, bd=1, relief="sunken", bg='#221551').pack(fill="x", padx=5, pady=5)
accion_label = tk.Label(root, text="", fg='#FFFFFF', bg='#221551', font=("Helvetica", 14, "bold"), wraplength=580)
accion_label.pack()

tk.Frame(root, height=2, bd=1, relief="sunken", bg='#221551').pack(fill="x", padx=5, pady=5)
tipificacion_label = tk.Label(root, text="", fg='#FFFFFF', bg='#221551', font=fuente_tipificacion, wraplength=580)
tipificacion_label.pack()

root.mainloop()