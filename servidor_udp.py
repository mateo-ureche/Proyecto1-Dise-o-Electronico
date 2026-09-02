import socket
import sqlite3

IP = "0.0.0.0"
PUERTO = 5000

# Crear socket UDP
socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_udp.bind((IP, PUERTO))

print(f"Servidor UDP escuchando en el puerto {PUERTO}...")

while True:
    datos, direccion = socket_udp.recvfrom(1024)

    mensaje = datos.decode("utf-8").strip()

    print(f"Recibido de {direccion}:")
    print(mensaje)

    # Separar la trama
    partes = mensaje.split(";")

    if len(partes) == 4 and partes[0] == "UBICACION":
        _, fecha_hora, latitud, longitud = partes

        # Separar fecha y hora
        fecha, hora = fecha_hora.split(" ")

        # Guardar en SQLite
        conexion = sqlite3.connect("ubicaciones.db")
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO ubicaciones
            (latitud, longitud, fecha, hora)
            VALUES (?, ?, ?, ?)
        """, (float(latitud), float(longitud), fecha, hora))

        conexion.commit()
        conexion.close()

        print(" Ubicación guardada en la base de datos.")
    else:
        print(" Formato de mensaje incorrecto.")

    print()
