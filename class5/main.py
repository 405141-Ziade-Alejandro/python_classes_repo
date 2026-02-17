"""
Actividad: Función año bisiesto
Consigna

Realizar una función llamada año_bisiesto:

Recibirá un año por parámetro

Imprimirá “El año año es bisiesto” si el año es bisiesto

Imprimirá “El año año no es bisiesto” si el año no es bisiesto

Si se ingresa algo que no sea número, debe indicar que se ingrese un número.

Información a tener en cuenta:

Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.
"""
from operator import truediv
from random import choice
from typing import List


def año_bisiesto(annio: int):
  if (annio % 4 == 0 and annio % 100 != 0) or annio % 400 == 0:
    print("El año año es bisiesto")
  else:
    print("El año año no es bisiesto")
# año_bisiesto(2012)
# año_bisiesto(2010)
# año_bisiesto(2000)
# año_bisiesto(1900)
"""
Actividad: ¡Funciones!
Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo a partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura

🖐 Ayuda: El área de un rectángulo se obtiene al multiplicar la base por la altura.
"""
def area_rectangulo(base, altura):
  return base*altura

"""
Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio

🖐 Ayuda: El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi. Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math.
"""
def area_circulo(radio):
  return (radio**2)/3.14159
"""
Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:
Si el primer número es mayor que el segundo, debe devolver 1.

Si el primer número es menor que el segundo, debe devolver -1.

Si ambos números son iguales, debe devolver un 0.


Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'
"""
def relacion(primer, segundo):
  if primer==segundo:
    return 0
  elif primer<segundo:
    return -1
  else:
    return 1

# print("relacion entre 5 y 10: ",relacion(5,10))
# print("relacion entre 10 y 5: ",relacion(10,5))
# print("relacion entre 5 y 5: ",relacion(5,5))

"""
Realiza una función llamada intermedio() que, a partir de dos números, devuelva su punto intermedio:

🖐 Ayuda: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2

Comprueba el punto intermedio entre -12 y 24
"""
def intermedio(numero_1, numero_2):
  return (numero_1+numero_2)/2
# print("el punto intermedio entre -12 y 24 es: ",int(intermedio(-12,24)))

"""
Realiza una función llamada recortar() que reciba tres parámetros. El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:
Devolver el límite inferior si el número es menor que éste

Devolver el límite superior si el número es mayor que éste.

Devolver el número sin cambios si no se supera ningún límite.

Comprueba el resultado de recortar 15 entre los límites 0 y 10
"""
def recortar(numero_recortar,limite_inferior,limite_superior):
  if limite_superior<numero_recortar:
    return limite_superior
  elif numero_recortar<limite_inferior:
    return limite_inferior
  else:
    return numero_recortar
# print("recortamos entre 0 y 10 a 15: ",recortar(15,0,10))

"""
Crea un programa que permita a un usuario llevar un registro de tareas pendientes. El programa debe:
Permitir al usuario agregar tareas.
Marcar tareas como completadas. agregámdole un tilde o algo que identifique que se completó al principio de la tarea.
Listar las tareas pendientes. 

Notas actividad 1
Aclaraciones

Utiliza una lista y funciones separadas para gestionar las tareas.

"""
# on = True
# to_do_list = []
# done_list = []
# while on:
#   choice = int(input("please select an option: \n 1. see my list \n 2. add a new task \n 3. complete a task \n 4. exit \n: "))
#   if choice == 1:
#     for task in to_do_list:
#       print(task)
#     for task in done_list:
#       print("✓ - "+task)
#   elif choice == 2:
#       new_tas =  input("add new task: ")
#       to_do_list.append(new_tas)
#   elif choice == 3:
#       for index in range(len(to_do_list)):
#         print(index + 1,to_do_list[index])
#         print("0. go back")
#       selected_task = int(input("select the task that is done: "))
#       if selected_task == 0:
#         continue
#       done_list.append(to_do_list[selected_task - 1])
#       to_do_list.remove(to_do_list[selected_task - 1])
#   elif choice == 4:
#     on = False
#     print("exit program")
"""
Desarrolla un programa que permita a un usuario registrar información de contactos (nombre, número de teléfono y correo electrónico). 
El programa debe almacenar estos contactos y permitir al usuario buscar contactos por nombre o número de teléfono. 

Utiliza un diccionario para gestionar los contactos y funciones separadas para realizar estas acciones.

"""
#
# continue_program = True
# contact_list = []
#
# def new_contact():
#     name = input("Ingrese el nombre del contacto: ")
#     telefono = int(input("Ingrese telefono del contacto: "))
#     correo = input("Ingrese correo del contacto: ")
#
#     contacto = {
#         "nombre" : name,
#         "telefono" : telefono,
#         "correo" : correo
#     }
#
#     contact_list.append(contacto)
#     print(contact_list)
#
#
# def search_name(name):
#     for contact in contact_list:
#         if contact["nombre"] == name:
#             print(contact)
#
#
# def search_telephone(tel):
#     for contact in contact_list:
#         if contact["telefono"] == tel:
#             print(contact)
#
#
# while continue_program:
#     choice = int(input("seleccione una opcion: \n 1. ingresar nuevo contacto \n 2. buscar contacto por nombre \n 3. buscar contacto por telefono \n 4. salir \n"))
#     if choice == 1:
#         new_contact()
#     if choice == 2:
#         name = input("Ingrese el nombre del contacto: ")
#         search_name(name)
#     if choice == 3:
#         tel = int(input("Ingrese telefono del contacto: "))
#         search_telephone(tel)
#     if choice == 4:
#         print("Saliendo...")
#         continue_program = False

"""
Crea un programa que permita a un usuario configurar la red de una computadora. 
El programa debe aceptar argumentos clave para configurar la dirección IP, la máscara de subred y la puerta de enlace. 
Luego, muestra la configuración de red completa.


Notas actividad 3
Aclaraciones

Utiliza kwargs como parámetro de la función permitiendote pasar cualquier llave-valor a la función.
"""

# def configurar_red(**configuration):
#     for parametro, valor in configuration.items():
#         nombre = parametro
#         print(f"{nombre}: {valor}")
# on = True
# configuracion = {}
# while on:
#     choice = int(input(
#         "please select an option: \n 1. agregar direccion ip \n 2. agregar mascara de subred \n 3. agregar puerta de enlace \n 4. salir y guardar \n: "))
# 
#     if choice == 1:
#         configuracion["ip"] = input("enter direccion ip: ")
#     elif choice == 2:
#         configuracion["mascara"] = input("enter mascara de subred: ")
#     elif choice == 3:
#         configuracion["puerta"] = input("enter puerta de enlace: ")
#     elif choice == 4:
#         print("configuracion: ", configuracion)
#         on = False
#         configurar_red(**configuracion)
# 
#         configuracion.clear()
#         on = False
#         print("exit program")
#     else:
#         print("please select an option")

"""
Crea un programa que permita calcular el promedio de un número variable de notas ingresadas por el usuario. 
La función calcular_promedio puede recibir un número variable de notas. 
Luego, muestra el promedio de las notas ingresadas.

Notas actividad 4
Aclaraciones

Deberán utilizar *args como parametro para que se permita el número variado de notas.

"""

on = True

promedio = 0

configuracion = {}


def calcular_promedio(lista_string):
    global promedio
    lista_de_strings = lista_string.replace(" ","").split(",")
    lista_int = []
    for nota in lista_de_strings:
        lista_int.append(int(nota))

    promedio = sum(lista_int)/len(lista_int)


def limpiar():
    global promedio
    promedio = 0


while on:
    print("su promedio es: ", promedio)
    choice = int(input(
        "please select an option: \n 1. agregar notas \n 2. limpiar \n 3. salir \n: "))

    if choice == 1:
        lista_string = input("ingrese sus notas separadas con coma")
        calcular_promedio(lista_string)
    elif choice == 2:
        print("limpiando promedio")
        limpiar()
    elif choice == 3:
        on = False
    else:
        print("please select an option")