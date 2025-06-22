import socket

#   Crear socket
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#   Conectar al servidor
cliente.connect(("localhost", 9999))

#   Enviar mensaje
cliente.send("Hola servidor".encode())

#   Recibir respuesta
respuesta = cliente.recv(1024).decode()
print(f"Respuesta del servidor: {respuesta}")

#   Cerrar conexion
cliente.close()