import os
from General_Utilities.option_list import option_list


class laravel_orders():
    '''
    Clase de compendio de ordenes para proyectos laravel
    '''

    def __init__(self):
        '''
        Inicializa la instancia.
        '''
        import tkinter as tk
        from tkinter import filedialog
        # Seleccionando el directorio
        root = tk.Tk()
        root.withdraw()
        dir_path = filedialog.askdirectory()

        self.dir_path = dir_path


    def new_project(self):
        '''
        main_description: Nuevo proyecto.
        '''
        import subprocess
        self.project_name = input('Nombre del Proyecto: ')
        self.project_path = os.path.join(self.dir_path, self.project_name)
        # subprocess.run(["laravel", "new", project_name])
        print(os.getcwd())
    
    def conn_project(self):
        '''
        main_description: Conectar Proyecto.
        '''
        proyectos_laravel = []
        for raiz, directorios, archivos in os.walk(self.dir_path):
            for directorio in directorios:
                ruta_completa = os.path.join(raiz, directorio)
                if os.path.isdir(ruta_completa):
                    archivos_proyecto = os.listdir(ruta_completa)
                    if 'artisan' in archivos_proyecto:
                        proyectos_laravel.append(ruta_completa)

        if len(proyectos_laravel)>0:
            print("Se encontraron los siguientes proyectos Laravel:")
            # for proyecto in proyectos_laravel:
            #     print(proyecto)

            proyecto = option_list(proyectos_laravel)
            print(proyecto)

        else:
            print("No se encontraron proyectos Laravel en el directorio general.")


    def attributes(self):
        '''
        main_description: Atributos.
        '''

        print(
            self.dir_path,
            self.project_name,
            self.project_path,
        )

