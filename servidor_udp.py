import socket
import sqlite3

IP = "0.0.0.0"
PUERTO = 5000

socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_udp.bind((IP, PUERTO))

while True:
    datos, direccion = socket_udp.recvfrom(1024)
    mensaje = datos.decode("utf-8").strip()
    
    partes = mensaje.split(";")

    if len(partes) == 4 and partes[0] == "UBICACION":
        _, fecha_hora, latitud, longitud = partes
        fecha, hora = fecha_hora.split(" ")

        conexion = sqlite3.connect("ubicaciones.db")
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO ubicaciones
            (latitud, longitud, fecha, hora)
            VALUES (?, ?, ?, ?)
        """, (float(latitud), float(longitud), fecha, hora))

        conexion.commit()
        conexion.close()
