import socket

#   Crear socket TCP

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    #   Intentamos conectarnos al servidor
    cliente.connect(("example.com", 80))
    print("Conexión exitosa")
except socket.error:
    print("Error")
finally:
    cliente.close()