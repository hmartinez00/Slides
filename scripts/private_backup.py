import os

dir = os.getcwd()
project = 'laravel/ejemplo'
file = '.gitignore'

path = os.path.join(dir, project, file)

with open(path, encoding='utf-8') as ignorefile:
    content = ignorefile.read()
    print(content)

ignorefile.close()