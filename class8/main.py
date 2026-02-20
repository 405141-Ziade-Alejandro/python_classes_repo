"""
actividades escritura de archivos
"""
import datetime

"""
Actividad 1
Registrando gastos

Escribe un programa en Python que permita a un usuario registrar sus gastos diarios en un archivo de texto llamado "gastos.txt". El programa debe permitir al usuario ingresar la descripción del gasto y la cantidad gastada. Luego, debe guardar estos datos en el archivo en el siguiente formato:

"Fecha: {fecha} - Descripción: {descripción} - Cantidad: {cantidad}"

Donde fecha es la fecha actual y descripción y cantidad son los datos ingresados por el usuario.

"""

def registrar_gastos():
    fecha = datetime.date.today()
    descripcion = input("describa el gasto a registrar: ")
    cantidad = int(input("ingrese el total del gasto: "))

    linea= f"Fecha: {fecha}, descripcion: {descripcion}, cantidad: {cantidad} \n"

    with open("gastos.txt", "a") as archivo:
        archivo.write(linea)

registrar_gastos()