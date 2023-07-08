import os
import time
import shutil


curso='python311'
clase='Intro'
source_file=os.path.join(curso, clase + '.html')     # ruta_del_archivo_a_monitorear
destination_file=os.path.join('../reveal.js', 'index.html') # ruta_del_archivo_destino

def compare_and_update(source_file, destination_file):
    with open(source_file, 'r', encoding='utf-8') as source:
        source_content = source.read()
        source.close()
    with open(destination_file, 'r', encoding='utf-8') as destination:
        destination_content = destination.read()
        destination.close()
    if source_content != destination_content:
        # shutil.copy2(source_file, destination_file)
        f = open(destination_file, 'w', encoding='utf-8')
        f.write(source_content)
        f.close()
        print('Actualizado!')

while True:
    compare_and_update(source_file, destination_file)
    time.sleep(1)