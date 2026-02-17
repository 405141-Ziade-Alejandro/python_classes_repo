import time
"""
Consigna

Para tu primera entrega, te proponemos que crees un programa que permita emular el registro y almacenamiento de usuarios en una base de datos.
Hazlo utilizando el concepto de funciones, diccionarios, bucles y condicionales.

Objetivos

    Practicar el concepto de funciones.

    Desarrollar la parte lógica para el registro de usuarios.

Requisitos

    Diccionarios (guardado de datos)

    Input (solicitud de datos)

    Variables

    If (chequeo de datos)

    While (iteración para el programa, sea para agregar, loguear o mostrar)

    For (recorrer datos y para búsqueda)

    Print

    Funciones separadas para registro, almacenamiento y muestra

Recomendaciones

    El formato de registro es: Nombre de usuario y Contraseña.

    Utilizar una función para almacenar la información y otra función para mostrar la información.

    Utilizar un diccionario para almacenar dicha información, con el par usuario-contraseña (clave-valor).

    Utilizar otra función para el login de usuarios, comprobando que la contraseña coincida con el usuario.
"""

on = True

database = {}

def type_slowly(text):
    """
    this method i stole it from the internet to make the text appear cooler
    :param text: the string to be printed
    :return:
    """
    for char in text:
        # end='' tells Python NOT to start a new line
        # flush=True tells Python to show the character NOW
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()


def login():
    """
    this method first check with an username if it's in the database.
        if it is then ask for a pasword
            if the password is correct then it logs you in
            if not then it gives you 3 tries
        if not then tells you that you got the username incorrectly and returns you to the menu
    :return:
    """
    username = input("Ingrese su usuario: ")

    if username in database:
        password = input("Ingrese su password: ")
        if password == database[username]:
            type_slowly("Login Correcto")
            type_slowly("Ingresando")
            switch()
        else:
            type_slowly("contraseña incorrecta \n intentelo de nuevo:")
            tries_coutner= 3
            for tries in range(3):
                print(f"usted tiene: {tries_coutner} intentos: \n")
                tries_coutner -= 1
                password = input("Ingrese su password: ")
                if password == database[username]:
                    type_slowly("Login Correcto")
                    type_slowly("Ingresando")
                    switch()
                    return
            type_slowly("se quedo sin intentos, el programa se cerrara")
            switch()
    else:
        print(f"no existe ningun usuario con nombre {username}")
        type_slowly("volviendo al menu principal")


def user_choice(input_text):
    """
    this puts a while loop until the user types a number, this is made to avoid crashing the program with {ValueError} 
    :param input_text: this is the text that is presented to the user to put their input in
    :return: it returns an int that the program can use as a choice option
    """
    while True:
        try:
            user_input = int(input(input_text))
            return user_input
        except ValueError:
            type_slowly("Ingrese una opcion valida")

def create_account():
    """
    this method creates a new account
    it ask an username, password and then confirms if it's correct.
        if it is it creates the account and returns you to the menu
        if it isn't then it start again
    :return:
    """
    type_slowly("Usted usara este nombre para loguearse")
    username = input("Ingrese su nombre de usuario: ")
    for user in database:
        if user == username:
            type_slowly("este nombre ya fue tomado \n volviendo al menu principal")
            return
    password = input("Ingrese su password: ")
    print(f"¿Estos datos son correctos?\n - usuario: {username}\n - password: {password}")
    choice = user_choice(" 1. Si\n 2. No\n")
    if choice == 1:
        type_slowly("Creando un usuario")
        database[username] = password
        type_slowly("Usuario creado, volviendo al menu principal")
    elif choice == 2:
        create_account()
    else:
        type_slowly("Ingrese una opcion valida")


def switch():
    """
    this method switches the global variable on to true or false, the inverse of that it currently holds
    :return:
    """
    global on
    on = not on


def main():
    while on:
        type_slowly("Iniciando...")
        type_slowly("Bienvenido al programa")
        type_slowly("Para continuar necesitas logearte")

        choice = user_choice(
            "seleccione una opcion: \n 1. Ya tengo una cuenta \n 2. No tengo una cuenta, crear una \n 3. Salir del programa \n")
        if choice == 1:
            login()
        elif choice == 2:
            create_account()
        elif choice == 3:
            type_slowly("Saliendo...")
            switch()
        else:
            type_slowly("Ingrese una opcion valida")
main()