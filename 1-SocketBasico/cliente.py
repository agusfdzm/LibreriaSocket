import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #   Creación del socket. IPv4 y TCP

cliente.connect(("example.com", 80))
cliente.close()