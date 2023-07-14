import os
import shutil

dir     = os.path.join(os.getcwd(), 'laravel')
project = os.path.join(dir, 'ejemplo')
file    = '.gitignore'

ignorefile_path = os.path.join(project, file)

with open(ignorefile_path, encoding='utf-8') as ignorefile:
    content = [str(i).split('\n')[0] for i in ignorefile.readlines()]
    ignorefile.close()

print(content)

def copiar_elemento(elemento, directorio_origen, directorio_destino):
    import os
    ruta_elemento   = os.path.join(directorio_origen, elemento)
    ruta_destino    = os.path.join(directorio_destino, elemento)
    if os.path.isdir(ruta_elemento):
        shutil.copytree(ruta_elemento, ruta_destino)
        print(f"Directorio '{elemento}' copiado a '{directorio_destino}' de forma recursiva.")
    elif os.path.isfile(ruta_elemento):
        shutil.copy2(ruta_elemento, ruta_destino)
        print(f"Archivo '{elemento}' copiado a '{directorio_destino}'.")
    else:
        print(f"El elemento '{elemento}' no existe en el directorio de origen.")

directorio_origen   = project
directorio_destino  = os.path.join('C:', 'Users', 'Hector', 'Mi unidad (hmbackups00@gmail.com)', 'laravel_projects', 'ejemplo')  # Reemplaza con la ruta del directorio de destino

for elemento in content:
    copiar_elemento(elemento, directorio_origen, directorio_destino)