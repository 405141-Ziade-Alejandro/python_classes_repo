# variables

"""
variables tiene que ser nombrada de forma que sea obvio lo que guardan
"""

fecha_de_nacimiento = "15 de noviembre" #variable de cadena
fecha_de_nacimiento_2 = '15 de noviembre' # snake_case

print(fecha_de_nacimiento)

numero = 546 #int
numero_flotante = 12.5 #float

print(numero,numero_flotante) #con , se concatenan


modulo = 10%2
print(modulo)

# un_number = input("Introduce un numero: ")
# print(un_number)
# parse

parsed_number = int("26")
print(type(parsed_number),parsed_number)


# f-string

conmbined_chain = f"hello wolrd + {parsed_number}"

# slices
cadena = "hello world"
print(cadena[0:4])

# copia

print(cadena[:])

