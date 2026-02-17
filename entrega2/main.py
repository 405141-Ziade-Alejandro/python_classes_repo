from paquete.client_class import Vip_Cliente, Client


anita = Client("ana", 30, "10/05/1994", 50)
print(anita)
anita.informacion_cliente()

print("\n-----------------\n")

marquito = Vip_Cliente("marco",23,"17 de enero 2020", 90, 360)

marquito.informacion_cliente()

print("\n-----------------\n")

Client.cantidad_total_clientes()


# anita.save_txt() # comentado para no crear un archivo cada vez