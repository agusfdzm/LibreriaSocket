import socket

#   Crear socket del servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#   Poder volver a utilizar el puerto
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#   Enlace a IP y Puerto
server.bind(("localhost", 9999))

#   Escuchar conexiones
nEscuchas = server.listen(1)
print(f"Escuchando {nEscuchas} conexion/es")

#   Aceptar una conexión
conexion, addr = server.accept()
print(f"Conexión establecida con {addr}")

#   Recibir datos
datos = conexion.recv(1024).decode()
print(f"Mensaje recibido: {datos}")

#   Enviar respuesta
conexion.send("Hola cliente".encode())

#   Cerrar
conexion.close()
server.close()