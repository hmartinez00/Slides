import os
import rarfile

def extract_rar(file_path, destination_path):
    with rarfile.RarFile(file_path) as rf:
        rf.extractall(destination_path)

 # Ruta del archivo RAR que deseas descomprimir
rar_file_path = 'python311/Ejercicios/ejercicio1.rar'
 # Ruta de destino para la extracción
destination_path = os.getcwd()
 # Llama a la función para descomprimir el archivo RAR
extract_rar(rar_file_path, destination_path)