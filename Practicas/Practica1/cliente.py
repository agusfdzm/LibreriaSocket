import socket

#   Crear socket
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#   Conexión
cliente.connect(("localhost", 9999))

#   Enviar mensaje al server
cliente.send("Hola server".encode())

#   Respuesta
cliente.recv(1024).decode()