""""
Escribe un programa que solicite al usuario dos números enteros.
Luego, muestra por pantalla la suma, resta, multiplicación y división de esos dos números.
"""

# number_1 = int(input("first number: "))
# number_2 = int(input("second number: "))
#
# print(f"suma: {number_1 + number_2}")
# print(f"resta: {number_1 - number_2}")
# print(f"multiplicacion: {number_1 * number_2}")
# print(f"division: {number_1 / number_2}")

"""
Crea un programa que tome una cadena de texto como entrada del usuario. 
Luego, muestra por pantalla los primeros tres caracteres de la cadena, seguidos por los tres últimos caracteres. 
Además, concatena ambos subconjuntos y muestra el resultado.
"""

# message = input("Ingresa una cadena de texto: ")
# first_three = message[0:3]
# second_three = message[-3:]
#
# print(first_three + second_three)

"""
Crea un programa que inicie con una lista de números enteros. 
Luego, solicita al usuario un número entero y un índice para reemplazar un elemento en la lista por el nuevo número ingresado en el índice ingresado. 
Imprime la lista resultante.
"""

# list = [1,2,3,4,5,6,7,8,9]
#
# number = int(input("entre el numero entero: "))
# index = int(input("entre el indice: "))
#
# list[index-1] = number
#
# print(list)

"""
Crea un programa que, teniendo en cuenta la siguiente tupla, muestre el valor del segundo elemento de la misma. 
Además, debe mostrar cuántas veces se repite este valor y cuál es el índice del valor repetido.
"""
# palabras_tupla = ("manzana", "pera", "uva", "naranja", "sandía", "manzana", "plátano", "kiwi", "pera", "fresa", "mango", "uva", "cereza", "manzana", "durazno")
#
# print(palabras_tupla[1])
#
# number_repetition = palabras_tupla.count(palabras_tupla[1])
#
# print(number_repetition)
#
# print(palabras_tupla.index(palabras_tupla[1], 2))


"""
PARA RECORDAR

En un promedio pesado o ponderado no todos los valores tienen el mismo “peso” o valor.

El promedio entre 3 y 10 es:    (1.3 + 1.10) / 2, este es el promedio tradicional donde todos los valores tienen un peso de 1.

Promedio pesado entre 3 y 10 es:   (13.3 + 2.10) / 15, aquí vemos que el peso de 3 es 13, y el peso del 10 es 2, por lo que el 3 es más importante, se divide por la suma de los pesos.
Mi primer programa en Python

Consigna

    Trabajas en Coderhouse y te piden crear un programa que calcule la nota final de estudiantes del curso de Python. La nota final se calcula basándonos en tres notas previas de las cuales, cada una corresponde un porcentaje distinto de la nota final. Los porcentajes se detallan a continuación:

Los porcentajes asociados que debemos considerar de cada nota se detallan a continuación:

    nota_1 cuenta como el 20% de la nota final

    nota_2 cuenta como el 30% de la nota final

    nota_3 cuenta como el 50% de la nota final

Aspectos a incluir

    Tener en cuenta los temas vistos en la clase 1: números, print, input, variables, operaciones matemáticas, cadena de texto.

    Los datos deben guardarse en variables y deben ser dinámicos por medio de input.
"""
# print((13.3 + 2.10) / 15)
#
# nota_1 = float(input("Ingrese la nota 1: "))
# nota_2 = float(input("Ingrese la nota 2: "))
# nota_3 = float(input("Ingrese la nota 3: "))
#
# print(nota_1, nota_2, nota_3)
#
# nota_1_weighted = 2+nota_1
# nota_2_weighted = 3+nota_2
# nota_3_weighted = 5+nota_3
#
# print(nota_1_weighted, nota_2_weighted, nota_3_weighted)
#
# average_weighted = (nota_1_weighted + nota_2_weighted + nota_3_weighted)/10
# print(average_weighted)
#
# print("old way")
# print(nota_1*0.2+nota_2*0.3+nota_3*0.5)

"""
    La siguiente matriz (o lista con listas anidadas) debe cumplir una condición: en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?

🖐 Ayuda:  La función llamada sum(lista) devuelve una suma de todos los elementos de la lista

Partirás de:

matriz = [

[1, 5, 1],

[2, 1, 2],

[3, 0, 1],

[1, 4, 4]

]

Debes llegar a:

matriz = [

[1, 5, 1, 7],

[2, 1, 2, 5],

[3, 0, 1, 4],

[1, 4, 4, 9]

]
"""

# matriz = [
#
# [1, 5, 1],
#
# [2, 1, 2],
#
# [3, 0, 1],
#
# [1, 4, 4]
#
# ]
#
# matriz[0].append(sum(matriz[0]))
# matriz[1].append(sum(matriz[1]))
# matriz[2].append(sum(matriz[2]))
# matriz[3].append(sum(matriz[3]))
#
#
# print(matriz)

"""
Consigna Sets

Crear un conjunto en Python que posea los siguientes elementos:

    Países: Inglaterra, USA, México.

    Posteriormente agrega nuestro set de países, los elementos de: Islandia, Italia, Argentina y Portugal, USA

    Elimina a los países: Chile e Italia

Pregunta: ¿Qué pasa si queremos eliminar al país Chile utilizando el método remove?, ¿Qué pasó con el element de USA?

Consigna Dicts

Escribir un programa que le solicite al usuario su nombre, edad, dirección y que, posteriormente, lo muestre por pantalla:

Ejemplo del output solicitado:

    Juan tiene 25 años, y vive en Carrera 7 - Bogotá
"""
#
# paises= {'inglaterra','USA','Mexico'}
# print(paises)
#
# paises = paises | {'Islandia','Portugal','Argentina','Italia','USA'}
#
# print(paises)
#
# paises.discard('Chile')
# paises.discard('Italia')
#
# print(paises)

persona = {}
persona['Nombre'] = input("introduce el nombre: ")
persona['Edad'] = input("introduce la edad: ")
persona['Direccion'] = input("introduce donde vive: ")

print(f'{persona.get("Nombre")} tiene {persona.get("Edad")} y vive en {persona.get("Direccion")}')