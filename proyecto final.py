#proyecto final
#submodulo
#autor:yareimi delgado verdier y marco antonio martinez diaz

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Necesita instalar pillow: pip install pillow
import os


# -------------------------
# FUNCIONES (pantallas vacías por ahora)
# -------------------------
def abrir_registro_productos():
    messagebox.showinfo("Registro de Productos", "Aquí irá el módulo de registro de productos.")

def abrir_registro_ventas():
    messagebox.showinfo("Registro de Ventas", "Aquí irá el módulo de registro de ventas.")

def abrir_reportes():
    messagebox.showinfo("Reportes", "Aquí irá el módulo de reportes.")

def abrir_acerca_de():
    messagebox.showinfo("Acerca de", "Punto de Venta de Ropa\nProyecto Escolar\nVersión 1.0")


# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("MeloComo")
ventana.geometry("500x600")
ventana.resizable(False, False)
ventana.configure(bg="#ffffff")


# -------------------------
# LOGO
# -------------------------
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    imagen = Image.open(os.path.join(BASE_DIR, "ventas2025.png"))  # Cambia por el archivo del alumno
    imagen = imagen.resize((250, 250))  # Tamaño recomendado
    img_logo = ImageTk.PhotoImage(imagen)

    lbl_logo = tk.Label(ventana, image=img_logo)
    lbl_logo.pack(pady=20)
except:
    lbl_sin_logo = tk.Label(ventana, text=os.path.join(BASE_DIR, "ventas2025.png"), font=("Arial", 14))
    lbl_sin_logo.pack(pady=40)


# -------------------------
# BOTONES PRINCIPALES
# -------------------------
# Estilo de los botones (color rojo vino, texto blanco, fuente de 12 puntos)
btn_color = "#8B0000"  # Rojo vino
btn_texto_color = "white"
fuente_boton = ("Arial", 12)

# Definimos el tamaño común para todos los botones
btn_width = 20  # Ancho en caracteres
btn_height = 2  # Alto en líneas

# Creación de botones con la configuración de color y fuente
btn_reg_prod = tk.Button(ventana, text="Registro de Productos", command=abrir_registro_productos,
                         bg=btn_color, fg=btn_texto_color, font=fuente_boton, relief="flat", 
                         padx=10, pady=10, width=btn_width, height=btn_height)
btn_reg_prod.pack(pady=10)

btn_reg_ventas = tk.Button(ventana, text="Registro de Ventas", command=abrir_registro_ventas,
                           bg=btn_color, fg=btn_texto_color, font=fuente_boton, relief="flat", 
                           padx=10, pady=10, width=btn_width, height=btn_height)
btn_reg_ventas.pack(pady=10)

btn_reportes = tk.Button(ventana, text="Reportes", command=abrir_reportes,
                         bg=btn_color, fg=btn_texto_color, font=fuente_boton, relief="flat", 
                         padx=10, pady=10, width=btn_width, height=btn_height)
btn_reportes.pack(pady=10)

btn_acerca = tk.Button(ventana, text="Acerca de", command=abrir_acerca_de,
                       bg=btn_color, fg=btn_texto_color, font=fuente_boton, relief="flat", 
                       padx=10, pady=10, width=btn_width, height=btn_height)
btn_acerca.pack(pady=10)


ventana.mainloop()
