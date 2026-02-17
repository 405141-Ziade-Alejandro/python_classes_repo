"""
Actividad: Implementación en Python
Implementar la Clase de Alumno, directamente en Python.
Aclaraciones Generales:
- El método imprimir, deberá mostrar por pantalla el nombre y la nota del estudiante.
- El método resultado, evalúa la nota correspondiente del estudiante. Si el estudiante saca menos de 5 puntos desaprueba la materia, más de 5 puntos aprueba.
    Tip: Para la realización de este apartado, es necesario trabajar con estructuras condicionales.
- Se deberá instanciar, al menos, dos objetos pertenecientes a la clase Alumno.
"""

# class Alumno:
#     def __init__(self, nombre:str, nota:int):
#         self.nombre = nombre
#         self.nota = nota
#
#     def imprimir(self):
#         print(f"el alumno {self.nombre} tiene una nota: {self.nota}")
#
#
#     def resultado(self):
#         if self.nota > 5:
#             print(f"el alumno {self.nombre} ha sido aprobado")
#         else:
#             print(f"el alumno {self.nombre} ha sido reprobado")
#
# marco = Alumno("marco", 5)
# polo = Alumno("polo", 9)
#
# marco.imprimir()
#
# polo.imprimir()
#
# marco.resultado()
# polo.resultado()

"""
Define una clase Figura con un método de instancia area que devuelve el área de la figura. 
Luego, crea clases hijas como Circulo y Rectangulo que hereden de Figura y proporcionen implementaciones diferentes del método area.
"""

# class Figura:
#     def area(self):
#         pass
#
# class Circulo(Figura):
#     def __init__(self, radio):
#         self.radio = radio
#     def area(self):
#         return 3.1416 * self.radio * self.radio
# class Rectangulo(Figura):
#     def __init__(self,base,altura):
#         self.base = base
#         self.altura = altura
#     def area(self):
#         return self.base * self.altura
#
# circulo = Circulo(5)
# rectangulo = Rectangulo(5,5)
#
# print(circulo.area())
# print(rectangulo.area())

"""
Crea una clase Calculadora con un método de clase llamado suma que acepte dos números como argumentos y devuelva la suma de ellos. 
Luego, utiliza este método para realizar algunas operaciones de suma.
"""


# class Calculadora:
#
#     @classmethod
#     def suma(cls, num1: int, num2: int) -> int:
#         return num1 + num2
#
#
# print(Calculadora.suma(1, 2))


"""
Crea una clase Empleado que tenga los siguientes atributos de instancia: nombre, apellido, edad, salario. 
Luego, crea una clase Gerente que herede de Empleado y tenga un atributo adicional departamento. 
Define métodos de instancia para ambas clases, como mostrar_informacion para mostrar los detalles de un empleado y aumentar_salario para aumentar el salario de un empleado en un porcentaje dado. 
Crea instancias de ambas clases y realiza algunas operaciones.

Recuerda utilizar el super para ejecutar el init de una clase padre.
"""

# class Empleado:
#     def __init__(self, nombre, apellido, edad, salario):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.salario = salario
#     def mostrar_informacion(self):
#         return f"here is the info:\n {self.nombre} \n {self.apellido} \n {self.edad}\n {self.salario}"
#     def aumentar_salario(self, percentage):
#         self.salario *= (percentage / 100)
#         print("salario aumentado")
#
# class Gerente(Empleado):
#     def __init__(self, nombre, apellido, edad, salario, departamento):
#         super().__init__(nombre,apellido,edad,salario)
#         self.departamento = departamento
#
#     def mostrar_informacion(self):
#         return super().mostrar_informacion() + f"\n {self.departamento}"

"""
Crea una clase Libro con atributos de instancia como titulo, autor, año_publicacion, y disponible (un valor booleano que indica si el libro está disponible o no). 
Luego, crea una clase Biblioteca que tenga una lista de libros y métodos de instancia para prestar un libro, devolver un libro y mostrar todos los libros disponibles. 
Utiliza atributos de clase para registrar la cantidad total de libros en la biblioteca. 
Crea instancias de ambas clases y realiza operaciones de préstamo y devolución de libros.

Aclaraciones

Para modificar un atributo de clase podes hacer lo siguiente:

Casa.atributo_de_clase = ‘prueba’

En este ejemplo se toma Casa como la clase y el atributo atributo_de_clase, donde se guarda un string (esto puede hacerse desde los metodos.)
"""

class Libro:

    def __init__(self,titulo, autor, anno_publicacion, disponible):
        self.titulo = titulo
        self.autor = autor
        self.anno_publicacion = anno_publicacion
        self.disponible = disponible
class Bibliotecas:
    cantidad_total = 0
    def __init__(self, lista_libros: list):
        self.lista_libros = lista_libros
        self.cantidad_total = len(self.lista_libros)

    def mostrar_todos_libros(self):
        for index in range(len(self.lista_libros)):
            print(index + 1 ,self.lista_libros[index].titulo)
    def prestar_libro(self,index) -> Libro:
        self.cantidad_total -= 1
        return self.lista_libros.pop(index)
    def devolver_libro(self, libro : Libro):
        self.lista_libros.append(libro)
        self.cantidad_total += 1