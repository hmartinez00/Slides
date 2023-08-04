import tkinter as tk
import subprocess
def ejecutar_programa():
    # Ruta al programa que deseas ejecutar
    ruta_programa = "ruta_al_programa.exe"  # Reemplaza con la ruta correcta
     # Ejecuta el programa utilizando subprocess
    subprocess.call(ruta_programa)
 # Crear una ventana
ventana = tk.Tk()
 # Definir elementos de la interfaz
boton = tk.Button(ventana, text="Ejecutar programa", command=ejecutar_programa)
 # Colocar los elementos en la ventana
boton.pack()
 # Iniciar el bucle de eventos
ventana.mainloop()