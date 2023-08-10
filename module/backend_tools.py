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
        self.orders = [
            'laravel new', 
             # Crea un nuevo proyecto de Laravel en un directorio específico.
            'php artisan serve', 
             # Inicia el servidor de desarrollo de Laravel.
            'php artisan migrate', 
             # Ejecuta las migraciones pendientes para actualizar la base de datos.
            'php artisan migrate:rollback', 
             # Revierte la última migración realizada.
            'php artisan migrate:reset', 
             # Revierte todas las migraciones realizadas.
            'php artisan migrate:refresh', 
             # Revierte y vuelve a ejecutar todas las migraciones.
            'php artisan migrate:status', 
             # Muestra el estado actual de todas las migraciones.
            'php artisan db:seed', 
             # Ejecuta los seeders registrados para poblar la base de datos.
            'php artisan make:model', 
             # Crea un nuevo modelo en la carpeta "app" de tu proyecto.
            'php artisan make:migration', 
             # Crea un nuevo archivo de migración en la carpeta "database/migrations".
            'php artisan make:seeder', 
             # Crea un nuevo archivo de seeder en la carpeta "database/seeds".
            'php artisan make:controller', 
             # Crea un nuevo controlador en la carpeta "app/Http/Controllers".
            'php artisan make:resource', 
             # Crea una nueva clase de recurso en la carpeta "app/Http/Resources".
        ]


    def action(self, index, value):
        '''
        Metodo de aplicacion de acciones
        '''
        os.chdir(self.project_path)
        if value != None:
            value = input('Name: ')
            order = self.orders[int(index) + ' ' + value]
        else:
            order = self.orders[int(index)]
        os.system(order)

   
    def attributes(self):
        '''
        main_description: attributes.
        '''
        print(
            self.dir_path,
            self.project_name,
            self.project_path,
        )


    def location(self):
        '''
        main_description: location.
        '''
        dir = os.getcwd()
        print(dir)


    def laravel_new(self):
        '''
        main_description: laravel new.
        '''
        self.project_name = input('proyect name: ')
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


    def create_database(self):
        '''
        main_description: create database.
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


    def serve(self):
        '''
        main_description: serve.
        '''
        # os.chdir(self.project_path)
        # os.system(f'php artisan serve')        
        self.action(1)

    def makemodel(self):
        '''
        main_description: makemodel.
        '''
        model_name = input('model name: ')
        os.chdir(self.project_path)
        os.system(f'php artisan make:model {model_name} --migration')


    def makemigration(self):
        '''
        main_description: makemigration.
        '''
        migration_name = input('migration name: ')
        os.chdir(self.project_path)
        os.system(f'php artisan make:migration {migration_name}')


    def makeseeder(self):
        '''
        main_description: makeseeder.
        '''
        seeder_name = input('seeder name: ')
        os.chdir(self.project_path)
        os.system(f'php artisan make:seeder {seeder_name}')


    def makecontroller(self):
        '''
        main_description: makecontroller.
        '''
        controller_name = input('controller name: ')
        os.chdir(self.project_path)
        os.system(f'php artisan make:controller {controller_name}')


    def makeresource(self):
        '''
        main_description: makeresource.
        '''
        resource_name = input('resource name: ')
        os.chdir(self.project_path)
        os.system(f'php artisan make:resource {resource_name}')


    def migrate(self):
        '''
        main_description: migrate.
        '''
        os.chdir(self.project_path)
        os.system(f'php artisan migrate')


    def dbseed(self):
        '''
        main_description: dbseed.
        '''
        os.chdir(self.project_path)
        os.system(f'php artisan db:seed')


    def newview(self):
        '''
        main_description: newview.
        '''
        view_name = input('view name: ')
        view_path = os.path.join(self.project_path, 'resources', 'views', view_name + '.blade.php')
        with open(view_path, 'w', encoding='utf-8') as view:
            content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{view_name}</title>
</head>
<body>
    
</body>
</html>
'''
            view.write(content)
            view.close()


