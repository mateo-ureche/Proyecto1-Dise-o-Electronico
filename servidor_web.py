from http.server import HTTPServer, SimpleHTTPRequestHandler
import sqlite3
import json
import os

class MiServidor(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/ubicacion":
            conexion = sqlite3.connect("../ubicaciones.db")
            cursor = conexion.cursor()

            cursor.execute("""
                SELECT latitud, longitud, fecha, hora
                FROM ubicaciones
                ORDER BY id DESC
                LIMIT 1
            """)
            resultado = cursor.fetchone()
            conexion.close()

            if resultado:
                respuesta = {"latitud": resultado[0], "longitud": resultado[1], "fecha": resultado[2], "hora": resultado[3]}
            else:
                respuesta = {"latitud": None, "longitud": None, "fecha": None, "hora": None}

            datos = json.dumps(respuesta).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(datos)
        else:
            super().do_GET()

os.chdir("web")
servidor = HTTPServer(("0.0.0.0", 8000), MiServidor)
servidor.serve_forever()
