import shutil

dir = [
    'C:/Windows/Prefetch',
    'C:/Windows/Temp',
    'C:/Users/admin/AppData/Local/Temp',
]

def borrar_contenido_directorio(ruta_directorio):
    import os
    # Verificar si la ruta es un directorio válido
    if os.path.isdir(ruta_directorio):
        num0 = len(os.listdir(ruta_directorio))
        # Eliminar todos los archivos y subdirectorios dentro del directorio
        for nombre_archivo in os.listdir(ruta_directorio):
            ruta_archivo = os.path.join(ruta_directorio, nombre_archivo)
            try:
                if os.path.isfile(ruta_archivo):
                    os.remove(ruta_archivo)
                elif os.path.isdir(ruta_archivo):
                    shutil.rmtree(ruta_archivo)                
            except Exception as e:
                pass
    else:
        print("La ruta especificada no es un directorio válido.")   
    num1 = len(os.listdir(ruta_directorio))
    numr = num0 - num1  
    return numr

 # Ejemplo de uso
for i in dir:
    numr = borrar_contenido_directorio(i)
    print(f'Remociones de {i}: {numr}')
