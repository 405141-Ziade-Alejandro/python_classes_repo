"""
Crea un programa que solicite al usuario ingresar nombres separados por comas.
Luego, crea un conjunto con los nombres ingresados y muestra por pantalla la cantidad de nombres únicos en el conjunto.
"""
# list = input("Ingrese nombres separados por comas: ")
#
# list_conjunto = list.split(",")
#
# print(list_conjunto)

"""
Crea un programa que simule un inventario de productos en una tienda. 
Inicia con un diccionario que contenga algunos productos y sus cantidades. 
Luego, permite al usuario agregar un nuevo producto con su cantidad y actualizar la cantidad de un producto existente. 
Muestra el inventario actualizado.

Productos y cantidades:
Manzanas => 50
Bananas => 30
Peras => 40

"""
# products = {
#     "manzanas" : 50,
#     "bananas" : 30,
#     "peras" : 40
# }
#
# new_product = input("Ingrese el nombre del producto: ")
# new_product_quantity = int(input("ingrese la cantidad: "))
#
# products[new_product] = new_product_quantity
#
# print(products)
# # this assumes that the user has perfect knowledge and doesn't make mistakes
# update_product = input("Ingrese el nombre del producto: ")
# update_product_quantity = int(input("ingrese la cantidad: "))
#
# products[update_product] = update_product_quantity
#
# print(products)

"""
Crea un programa que tome una oración ingresada por el usuario y realice las siguientes operaciones: 
convierte la oración a mayúsculas, 
cuenta cuántas veces aparece la palabra "python", 
y muestra la oración sin espacios en blanco al inicio y al final.

"""
#
# oracion_ingresada_por_el_ususario = input("ingrese su frase: ")
#
# print(oracion_ingresada_por_el_ususario.upper())
# print(oracion_ingresada_por_el_ususario.count("python"))
# print(oracion_ingresada_por_el_ususario.strip())

"""
Crea dos conjuntos con números ingresados por el usuario y separados por coma. 
Luego, muestra cuáles elementos tienen en común los conjuntos y crea un nuevo conjunto que contenga la unión de ambos.
"""
# conjunto_a = set(input("los numeros por favor: ").split(","))
# conjunto_b = set(input("los numeros por favor: ").split(","))
#
# print(conjunto_a.intersection(conjunto_b))
#
# conjunto_c = conjunto_a.union(conjunto_b)
#
# print(conjunto_c)

"""
A partir de una lista realizar las siguientes tareas sin modificar la lista original:

    Borrar los elementos duplicados

    Ordenar la lista de mayor a menor

    Eliminar todos los números impares ( for ---- if (%2==1) ---- pop, remove )

    Realizar una suma de todos los números que quedan (sum(lista))

    Añadir como primer elemento de la lista la suma realizada insert(0, suma)

    Devolver la lista modificada

    Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

Nota: Recuerda que para sumar todos los números de una lista puedes usar sum
"""
# lista_original = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
# lista = lista_original
# print(lista)
# lista = list(set(lista))
# print(lista)
# lista.sort(reverse=True)
# print(lista)
# total =  sum(lista)
# print(total)
# lista.insert(0,total)
# print(lista)
# lista.remove(total)
# print("total: ", total,", suma de todos los numeros:", sum(lista))

"""
Consigna: Crear una variable que almacene si se cumplen todas las condiciones.
A partir de dos variables llamadas NOMBRE y EDAD, debes crear una variable
que almacene si se cumplen todas las siguientes condiciones,
encadenando operadores lógicos en una sola línea:
NOMBRE sea diferente de cuatro asteriscos "****"
EDAD sea mayor que 5 y a su vez menor que 20
Que la longitud de NOMBRE sea mayor o igual a 4 pero a la vez menor que 8
EDAD multiplicada por 3 sea mayor que 35
Desde un input conseguir las variables
"""
# nombre = input("ingrese su nombre: ")
# edad = int(input("ingrese la edad: "))
#
# print(nombre, edad)
#
# nombre_differente_asterisco = nombre != "****"
# print(nombre_differente_asterisco)
# edad_mayor_a_5_y_menor_a_20 = edad > 5 and edad < 20
# print(edad_mayor_a_5_y_menor_a_20)
# nombre_longitud = len(nombre)>4 and len(nombre)<8
# print(nombre_longitud)
# edad_mayor_a_35 = edad * 3 > 35
# print(edad_mayor_a_35)
#
# correlacion_de_Variables = nombre_longitud and edad_mayor_a_35 and edad_mayor_a_5_y_menor_a_20 and nombre_differente_asterisco
# print("y el resultado es: ",correlacion_de_Variables)
"""
Utilizando todo lo que sabes sobre cadenas, listas y sus métodos internos, transforma este texto:
gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista
Transforma el texto en:
Gordon lanzó su curva...
- Strawberry ha fallado por un pie! -gritó Joe Castiglione.
- Dos pies le corrigió Troop.
- Strawberry menea la cabeza como disgustado… -agrega el comentarista.

"""

"""
Escribir un programa que guarde en una variable en un diccionario {'Dolar':'$','Euro':'€', 'Libra':'£'}.
Luego se le deberá solicitar al usuario que ingrese la divisa que desea visualizar.
En el caso de ingresar una divisa no existente en nuestro diccionario,
    deberemos indicarle con un mensaje de notificación que la divisa no se encuentra disponible.
"""
currency = {
    'Dolar':'$',
    'Euro':'€',
    'Libra':'£'
}

request = input("ingrese la divisa que desea visualizar: ").capitalize()

print(currency.get(request) or "esa no es una divisa valida")