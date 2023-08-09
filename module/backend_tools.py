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


    def location(self):
        '''
        main_description: Directorio Actual.
        '''
        dir = os.getcwd()
        print(dir)


    def new_project(self):
        '''
        main_description: Nuevo proyecto.
        '''
        self.project_name = input('Nombre del Proyecto: ')
        self.project_path = os.path.join(self.dir_path, self.project_name)
        os.chdir(self.dir_path)
        os.system(f'laravel new {self.project_name}')

        # Creando database
        try:
            self.conn_database()
        except:
            print("Error al conectar DB.")

    
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
            self.project_path = option_list(proyectos_laravel)
            print(self.project_path)

            self.project_name = os.path.basename(self.project_path)

        else:
            print("No se encontraron proyectos Laravel en el directorio general.")


    def conn_database(self):
        '''
        main_description: Verificar conexion DB
        '''
        import mysql.connector
        # Instanciamos
        cnx = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = ''
        )
        # Verificamos el estado
        if cnx.is_connected():
            # Creamos el cursor para poder enviar las querys
            curs = cnx.cursor()
            # Diseñamos la query
            print(f'Creando database: {self.project_name}')
            sql = f'CREATE DATABASE {self.project_name}'
            # Ejecutamos la query
            curs.execute(sql)
            # Cerramos el cursor
            curs.close()
            # Cerramos la conexion
            cnx.close()
        # Verificamos el estado
        if not cnx.is_connected():
            print('Conexion cerrada.')


    def attributes(self):
        '''
        main_description: Atributos.
        '''
        print(
            self.dir_path,
            self.project_name,
            self.project_path,
        )


    def new_model(self):
        '''
        main_description: Nuevo modelo.
        '''
        model_name = input('Nombre del modelo: ')
        os.chdir(self.project_path)
        os.system(f'php artisan make:model {model_name} --migration')


    def migrate(self):
        '''
        main_description: Migrar.
        '''
        os.chdir(self.project_path)
        os.system(f'php artisan migrate')
