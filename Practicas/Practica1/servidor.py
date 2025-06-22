import socket

#   Crear el socket
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#   Liberar el socket 
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#   Escuchando la IP y puerto seleccionado
servidor.bind(("localhost", 9999))

#   Escuchas
servidor.listen(1)

nSocket, ipaddr = servidor.accept()

datos = nSocket.recv(1024).decode()

datosCaps = datos.upper()

print(datosCaps)

nSocket.send("Datos recibidos".encode())

nSocket.close()
servidor.close()