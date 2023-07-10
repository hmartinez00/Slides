import os
import time

curso='python311'
clase='tipos_de_datos'
source_file=os.path.join(curso, clase + '.html')     # ruta_del_archivo_a_monitorear
destination_file=os.path.join('../reveal.js', 'index.html') # ruta_del_archivo_destino

def compare_and_update(source_file, destination_file):
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
        print(f'[{time_ud}] Actualizado.')

while True:
    compare_and_update(source_file, destination_file)
    time.sleep(1)