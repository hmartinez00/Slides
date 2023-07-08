import time

# Estos son los archivos de trabajo
archivo_partida='partida.txt'
archivo_destino='destino.txt'

# Aca definimos la funcion de actualizacion
def file_update(source_file, destination_file):
    from datetime import datetime as dt
    with open(source_file, 'r', encoding='utf-8') as source:
        source_content = source.read()
        source.close()
    with open(destination_file, 'r', encoding='utf-8') as destination:
        destination_content = destination.read()
        destination.close()
    if source_content != destination_content:
        f = open(destination_file, 'w', encoding='utf-8')
        f.write(source_content)
        f.close()
        time_ud=dt.now().strftime('%H:%M:%S')
        print(f'[{time_ud}]\tActualizado!')

while True:
    file_update(archivo_partida, archivo_destino)
    time.sleep(1)