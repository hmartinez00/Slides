import os
import sys
import patoolib
import py7zr

source_path = 'python311/Ejercicios/ejercicio1.rar'
outdir = os.getcwd()
password = "www.compucalitv.com"

 # Descomprimir un archivo RAR
# patoolib.extract_archive(source_path, outdir=outdir)

with py7zr.SevenZipFile(source_path, mode='r', password=password) as z:
    z.extractall()