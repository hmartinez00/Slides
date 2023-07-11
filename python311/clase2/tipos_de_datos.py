'''
 1. Operaciones básicas:
   - Concatenación de cadenas:  `+` 
   - Repetición de cadenas:  `*` 
   - Indexación:  `[]` 
   - Slicing:  `[:]` 
   - Verificación de pertenencia:  `in` ,  `not in` 

 2. Secuencias de escape:
 Existen varias secuencias de escape en Python que se utilizan para representar caracteres especiales. Algunas de las más comunes son:   
    - \n: nueva línea 
    - \r: retorno de carro 
    - \t: tabulación horizontal 
    - \b: retroceso 
    - \f: avance de página 
    - \': comilla simple 
    - \": comilla doble 
    - \\: barra invertida 
    - \a: timbre o alerta 
    - \v: tabulación vertical 
    - \ooo: valor octal (reemplaza ooo por un número octal) 
    - \xhh: valor hexadecimal (reemplaza hh por un número hexadecimal de dos dígitos) 
    - \uhhhh: valor Unicode de 16 bits (reemplaza hhhh por un número hexadecimal de cuatro dígitos) 
    - \Uhhhhhhhh: valor Unicode de 32 bits (reemplaza hhhhhhhh por un número hexadecimal de ocho dígitos) 
Estas secuencias de escape se utilizan para representar caracteres que de otra manera serían difíciles de incluir en una cadena de texto.

 3. Métodos de formato y manipulación:
   -  `capitalize()` : Convierte el primer carácter en mayúscula y el resto en minúsculas.
   -  `casefold()` : Devuelve una versión en minúsculas de la cadena.
   -  `center(width[, fillchar])` : Devuelve una cadena centrada en un ancho dado.
   -  `count(sub[, start[, end]])` : Devuelve el número de ocurrencias de una subcadena.
   -  `encode([encoding[, errors]])` : Devuelve una versión codificada de la cadena.
   -  `endswith(suffix[, start[, end]])` : Verifica si la cadena termina con una subcadena dada.
   -  `expandtabs([tabsize])` : Reemplaza los caracteres de tabulación con espacios.
   -  `find(sub[, start[, end]])` : Devuelve el índice de la primera ocurrencia de una subcadena.
   -  `format(*args, **kwargs)` : Formatea la cadena con valores variables.
   -  `index(sub[, start[, end]])` : Devuelve el índice de la primera ocurrencia de una subcadena (lanza una excepción si no se encuentra).
   -  `isalnum()` : Verifica si la cadena contiene solo caracteres alfanuméricos.
   -  `isalpha()` : Verifica si la cadena contiene solo letras.
   -  `isdecimal()` : Verifica si la cadena contiene solo dígitos decimales.
   -  `isdigit()` : Verifica si la cadena contiene solo dígitos.
   -  `isidentifier()` : Verifica si la cadena es un identificador válido.
   -  `islower()` : Verifica si la cadena contiene solo caracteres en minúsculas.
   -  `isnumeric()` : Verifica si la cadena contiene solo caracteres numéricos.
   -  `isprintable()` : Verifica si todos los caracteres de la cadena son imprimibles.
   -  `isspace()` : Verifica si la cadena contiene solo espacios en blanco.
   -  `istitle()` : Verifica si la cadena sigue el formato de título.
   -  `isupper()` : Verifica si la cadena contiene solo caracteres en mayúsculas.
   -  `join(iterable)` : Une los elementos de un iterable con la cadena como separador.
   -  `ljust(width[, fillchar])` : Devuelve una cadena justificada a la izquierda en un ancho dado.
   -  `lower()` : Devuelve una versión en minúsculas de la cadena.
   -  `lstrip([chars])` : Elimina los caracteres iniciales de la cadena.
   -  `maketrans(x[, y[, z]])` : Devuelve una tabla de traducción para usar con el método  `translate()` .
   -  `partition(sep)` : Divide la cadena en una tupla basada en la primera aparición de una subcadena.
   -  `replace(old, new[, count])` : Reemplaza todas las apariciones de una subcadena con otra.
   -  `rfind(sub[, start[, end]])` : Devuelve el índice de la última ocurrencia de una subcadena.
   -  `rindex(sub[, start[, end]])` : Devuelve el índice de la última ocurrencia de una subcadena (lanza una excepción si no se encuentra).
   -  `rjust(width[, fillchar])` : Devuelve una cadena justificada a la derecha en un ancho dado.
   -  `rpartition(sep)` : Divide la cadena en una tupla basada en la última aparición de una subcadena.
   -  `rsplit([sep[, maxsplit]])` : Divide la cadena en una lista de subcadenas a partir de la derecha.
   -  `rstrip([chars])` : Elimina los caracteres finales de la cadena.
   -  `split([sep[, maxsplit]])` : Divide la cadena en una lista de subcadenas.
   -  `splitlines([keepends])` : Divide la cadena en una lista de líneas.
   -  `startswith(prefix[, start[, end]])` : Verifica si la cadena comienza con una subcadena dada.
   -  `strip([chars])` : Elimina los caracteres iniciales y finales de la cadena.
   -  `swapcase()` : Intercambia mayúsculas y minúsculas en la cadena.
   -  `title()` : Devuelve una versión en formato de título de la cadena.
   -  `translate(table)` : Devuelve una copia de la cadena traducida según una tabla de traducción.
   -  `upper()` : Devuelve una versión en mayúsculas de la cadena.
   -  `zfill(width)` : Rellena la cadena con ceros a la izquierda hasta alcanzar un ancho dado.

 Este es un listado extenso de los métodos y operaciones disponibles para cadenas en Python según la documentación oficial. Puedes consultar la documentación para obtener más detalles sobre cada uno de ellos.
'''


# 1. Operaciones con strings
# -----------------------------------------------------------------------
#    - Concatenación de cadenas:  `+` 
cadena1 = "Hola"    #Con comillas dobles
cadena2 = 'Mundo'   #Con comillas simples
cadena = cadena1 + " " + cadena2
print(cadena)
#    - Indexación:  `[]`
primer_caracter = cadena[0]
print(primer_caracter)
#    - Repetición de cadenas:  `*` 
repetida = cadena * 3
print(repetida)
#    - Slicing:  `[:]`
subcadena = cadena[0:4]
print(subcadena)
#    - Verificación de pertenencia:  `in` ,  `not in` 
if "Mundo" in cadena:
    print("La cadena contiene 'Mundo'")


#  2. Secuencias de escape:
# -----------------------------------------------------------------------
# \n: nueva línea - Inserta una nueva línea en la cadena
print("Hola\nMundo")  # Salida: 
# Hola
# Mundo
 # \r: retorno de carro - Mueve el cursor al inicio de la línea actual
print("Hola\rMundo")  # Salida: Mundo
 # \t: tabulación horizontal - Inserta un espacio de tabulación en la cadena
print("Hola\tMundo")  # Salida: Hola     Mundo
 # \b: retroceso - Retrocede el cursor un espacio
print("Hola\bMundo")  # Salida: HolMundo
 # \f: avance de página - Inserta un avance de página en la cadena
print("Hola\fMundo")  # Salida: 
# Hola
#     Mundo
 # \': comilla simple - Inserta una comilla simple en la cadena
print('Hola\'Mundo')  # Salida: Hola'Mundo
 # \": comilla doble - Inserta una comilla doble en la cadena
print("Hola\"Mundo")  # Salida: Hola"Mundo
 # \\: barra invertida - Inserta una barra invertida en la cadena
print("Hola\\Mundo")  # Salida: Hola\Mundo
 # \a: timbre o alerta - Produce un sonido de alerta
print("\aHola Mundo")  # Salida: (Sonido de alerta) Hola Mundo
 # \v: tabulación vertical - Inserta un espacio de tabulación vertical en la cadena
print("Hola\vMundo")  # Salida: 
# Hola
#    Mundo
 # \ooo: valor octal - Representa un carácter octal (reemplaza ooo por un número octal)
print("\123")  # Salida: S
 # \xhh: valor hexadecimal - Representa un carácter hexadecimal (reemplaza hh por un número hexadecimal de dos dígitos)
print("\x48\x6f\x6c\x61")  # Salida: Hola
 # \uhhhh: valor Unicode de 16 bits - Representa un carácter Unicode de 16 bits (reemplaza hhhh por un número hexadecimal de cuatro dígitos)
print("\u00A9")  # Salida: ©
 # \Uhhhhhhhh: valor Unicode de 32 bits - Representa un carácter Unicode de 32 bits (reemplaza hhhhhhhh por un número hexadecimal de ocho dígitos)
print("\U0001F600")  # Salida: 😀


# 3. Métodos de formato y manipulación:
# -----------------------------------------------------------------------
# capitalize(): Convierte el primer carácter en mayúscula y el resto en minúsculas.
print("hola mundo".capitalize())  # Salida: Hola mundo
 # casefold(): Devuelve una versión en minúsculas de la cadena.
print("HOLA MUNDO".casefold())  # Salida: hola mundo
 # center(width[, fillchar]): Devuelve una cadena centrada en un ancho dado.
print("hola".center(10, '-'))  # Salida: --hola---
 # count(sub[, start[, end]]): Devuelve el número de ocurrencias de una subcadena.
print("hola mundo".count('o'))  # Salida: 2
 # encode([encoding[, errors]]): Devuelve una versión codificada de la cadena.
print("hola".encode('utf-8'))  # Salida: b'hola'
 # endswith(suffix[, start[, end]]): Verifica si la cadena termina con una subcadena dada.
print("hola".endswith('a'))  # Salida: True
 # expandtabs([tabsize]): Reemplaza los caracteres de tabulación con espacios.
print("hola\tmundo".expandtabs(10))  # Salida: hola      mundo
 # find(sub[, start[, end]]): Devuelve el índice de la primera ocurrencia de una subcadena.
print("hola mundo".find('mundo'))  # Salida: 5
 # format(*args, **kwargs): Formatea la cadena con valores variables.
print("Hola {}, ¿cómo estás?".format("Mundo"))  # Salida: Hola Mundo, ¿cómo estás?
 # index(sub[, start[, end]]): Devuelve el índice de la primera ocurrencia de una subcadena (lanza una excepción si no se encuentra).
print("hola mundo".index('mundo'))  # Salida: 5
 # isalnum(): Verifica si la cadena contiene solo caracteres alfanuméricos.
print("hola123".isalnum())  # Salida: True
 # isalpha(): Verifica si la cadena contiene solo letras.
print("hola".isalpha())  # Salida: True
 # isdecimal(): Verifica si la cadena contiene solo dígitos decimales.
print("123".isdecimal())  # Salida: True
 # isdigit(): Verifica si la cadena contiene solo dígitos.
print("123".isdigit())  # Salida: True
 # isidentifier(): Verifica si la cadena es un identificador válido.
print("hola".isidentifier())  # Salida: True
 # islower(): Verifica si la cadena contiene solo caracteres en minúsculas.
print("hola".islower())  # Salida: True
 # isnumeric(): Verifica si la cadena contiene solo caracteres numéricos.
print("123".isnumeric())  # Salida: True
 # isprintable(): Verifica si todos los caracteres de la cadena son imprimibles.
print("hola mundo".isprintable())  # Salida: True
 # isspace(): Verifica si la cadena contiene solo espacios en blanco.
print("   ".isspace())  # Salida: True
 # istitle(): Verifica si la cadena sigue el formato de título.
print("Hola Mundo".istitle())  # Salida: True
 # isupper(): Verifica si la cadena contiene solo caracteres en mayúsculas.
print("HOLA".isupper())  # Salida: True
 # join(iterable): Une los elementos de un iterable con la cadena como separador.
print("-".join(["hola", "mundo"]))  # Salida: hola-mundo
 # ljust(width[, fillchar]): Devuelve una cadena justificada a la izquierda en un ancho dado.
print("hola".ljust(10, '-'))  # Salida: hola------
 # lower(): Devuelve una versión en minúsculas de la cadena.
print("HOLA".lower())  # Salida: hola
 # lstrip([chars]): Elimina los caracteres iniciales de la cadena.
print("   hola mundo".lstrip())  # Salida: hola mundo
 # maketrans(x[, y[, z]]): Devuelve una tabla de traducción para usar con el método translate().
# translate(table): Devuelve una copia de la cadena traducida según una tabla de traducción.
trans = str.maketrans('aeiou', '12345')
print("hola mundo".translate(trans))  # Salida: h4l1 m5nd4
 # partition(sep): Divide la cadena en una tupla basada en la primera aparición de una subcadena.
print("hola mundo".partition(' '))  # Salida: ('hola', ' ', 'mundo')
 # replace(old, new[, count]): Reemplaza todas las apariciones de una subcadena con otra.
print("hola mundo".replace('hola', 'adios'))  # Salida: adios mundo
 # rfind(sub[, start[, end]]): Devuelve el índice de la última ocurrencia de una subcadena.
print("hola mundo mundo".rfind('mundo'))  # Salida: 10
 # rindex(sub[, start[, end]]): Devuelve el índice de la última ocurrencia de una subcadena (lanza una excepción si no se encuentra).
print("hola mundo mundo".rindex('mundo'))  # Salida: 10
 # rjust(width[, fillchar]): Devuelve una cadena justificada a la derecha en un ancho dado.
print("hola".rjust(10, '-'))  # Salida: ------hola
 # rpartition(sep): Divide la cadena en una tupla basada en la última aparición de una subcadena.
print("hola mundo mundo".rpartition('mundo'))  # Salida: ('hola mundo ', 'mundo', '')
 # rsplit([sep[, maxsplit]]): Divide la cadena en una lista de subcadenas a partir de la derecha.
print("hola mundo mundo".rsplit(' '))  # Salida: ['hola', 'mundo', 'mundo']
 # rstrip([chars]): Elimina los caracteres finales de la cadena.
print("hola mundo   ".rstrip())  # Salida: hola mundo
 # split([sep[, maxsplit]]): Divide la cadena en una lista de subcadenas.
print("hola mundo mundo".split(' '))  # Salida: ['hola', 'mundo', 'mundo']
 # splitlines([keepends]): Divide la cadena en una lista de líneas.
print("hola\nmundo".splitlines())  # Salida: ['hola', 'mundo']
 # startswith(prefix[, start[, end]]): Verifica si la cadena comienza con una subcadena dada.
print("hola".startswith('h'))  # Salida: True
 # strip([chars]): Elimina los caracteres iniciales y finales de la cadena.
print("   hola mundo   ".strip())  # Salida: hola mundo
 # swapcase(): Intercambia mayúsculas y minúsculas en la cadena.
print("hOlA MuNdO".swapcase())  # Salida: HoLa mUnDo
 # title(): Devuelve una versión en formato de título de la cadena.
print("hola mundo".title())  # Salida: Hola Mundo
 # upper(): Devuelve una versión en mayúsculas de la cadena.
print("hola".upper())  # Salida: HOLA
 # zfill(width): Rellena la cadena con ceros a la izquierda hasta alcanzar un ancho dado.
print("hola".zfill(10))  # Salida: 000000hola


# 4. Formateo de cadenas
# -----------------------------------------------------------------------
nombre = "Juan"
edad = 25
# El método  .format()  es una forma común de formatear cadenas en Python. Permite combinar valores variables con una cadena utilizando marcadores de posición. Aquí tienes un ejemplo de cómo se utiliza:
mensaje = "Hola, mi nombre es {} y tengo {} años.".format(nombre, edad)
print(mensaje)
# Además del método  .format() , también hay otras formas de formatear cadenas en Python, como el f-string (disponible a partir de Python 3.6) y el método  % .
# Método f-string
mensaje = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print(mensaje)
# Método  % :
mensaje = "Hola, mi nombre es %s y tengo %d años." % (nombre, edad)
print(mensaje)

'''
Aquí tienes una lista de los marcadores de formato más comunes en Python:
 - %s: utilizado para cadenas de caracteres (strings).
- %d: utilizado para números enteros (integers).
- %f: utilizado para números de punto flotante (floats).
- %x: utilizado para números enteros en formato hexadecimal.
- %o: utilizado para números enteros en formato octal.
- %e: utilizado para números de punto flotante en notación científica.
- %c: utilizado para caracteres individuales.
- %r: utilizado para representaciones de cadenas de caracteres (strings) con comillas.
- %i: utilizado para números enteros (integers) (similar a %d).
- %u: utilizado para números enteros (integers) sin signo.
- %g: utilizado para números de punto flotante (floats), elige automáticamente entre %f y %e según la longitud del número.
- %%: utilizado para imprimir un signo de porcentaje (%).
 Estos marcadores de formato se utilizan en combinación con el operador de formato "%" o con el método de formato de cadenas ".format()".
'''
