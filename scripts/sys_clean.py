import tkinter as tk
from General_Utilities.sys_clean import sys_clean

def ejecutar_programa():
    sys_clean()

def crear_interfaz():
    ventana = tk.Tk()
    boton = tk.Button(ventana, text="Ejecutar programa", command=ejecutar_programa)
    boton.pack()
    ventana.mainloop()

crear_interfaz()
