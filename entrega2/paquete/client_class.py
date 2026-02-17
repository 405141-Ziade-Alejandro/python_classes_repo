from .auxiliary_methods import typewritter_printing
from datetime import datetime

class Client:
    """
    clase cliente existe para representar un cliente
    """
    fecha_ingreos: str = ""
    cantidad_clientes: int = 0

    def __init__(self, nombre :str, edad :int, fecha_nacimiento: str, puntaje:int):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.puntaje = puntaje
        self.fecha_ingreos =datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        Client.cantidad_clientes += 1

    def __str__(self):
        string = f"se creo el cliente {self.nombre} con un puntaje {self.puntaje}"
        return string

    def modificar_puntaje(self, numero_puntaje: int):
        """
        modifica el puntaje del cliente, de manera acumulativa
        :param numero_puntaje: el puntaje que suma o resta
        """
        self.puntaje += numero_puntaje

    def mostrar_puntaje(self) -> None:
        """
        mostra el puntaje del cliente
        :return:
        """
        typewritter_printing(f"el cliente {self.nombre} tiene un puntaje de {self.puntaje}")

    def informacion_cliente(self):
        """
        trae una descripcion del cliente, y todos sus atributos
        :return:
        """
        typewritter_printing(f"el cliente {self.nombre} tiene {self.edad} y nacio el {self.fecha_nacimiento}, tiene un puntaje de {self.puntaje}, ingreso al sistema el {self.fecha_ingreos}")

    @classmethod
    def cantidad_total_clientes(cls):
        print(f"Cantidad total de clientes creados: {Client.cantidad_clientes}")

    def save_txt(self):
        """
        esto guarda un archivo txt con el nombre edad y fecha nacimiento del cliente
        :return:
        """
        name= self.nombre + ".txt"
        with open(name, "w", encoding="utf-8") as file:
            file.write(f"1. {self.nombre}\n2. {self.edad}\n3. {self.fecha_nacimiento}\n")


class Vip_Cliente(Client):
    """
    cliente vip son representados por esta clase
    los clientes vip tienen un atributo de subscripcion que representa cuantos dias le quedan como vip
    """
    def __init__(self, nombre:str, edad:int, fecha_nacimiento: str, puntaje:int, vip_subscripcion_remaining_days: int):
        super().__init__(nombre,edad,fecha_nacimiento,puntaje)
        self.vip_subscripcion_remaining_days = vip_subscripcion_remaining_days

    def __str__(self):
        return f"se creo el cliente {self.nombre} con un puntaje {self.puntaje} y es un VIP con {self.vip_subscripcion_remaining_days} dias en subscripcion"

    def informacion_cliente(self):
        """
        trae una descripcion del cliente, y todos sus atributos
        :return:
        """
        typewritter_printing(f"el cliente {self.nombre} tiene {self.edad} y nacio el {self.fecha_nacimiento}, tiene un puntaje de {self.puntaje}, ingreso al sistema el {self.fecha_ingreos} y tiene {self.vip_subscripcion_remaining_days} dias de subscripcion")

    def un_dia_menos(self):
        """
        funcion que reduce en uno los dias de subscripcion vip que le quedan al cliente
        diseña para usarse en un schedule
        :return:
        """
        self.vip_subscripcion_remaining_days -= 1