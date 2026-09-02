import sqlite3

conexion = sqlite3.connect("ubicaciones.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ubicaciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    latitud REAL NOT NULL,
    longitud REAL NOT NULL,
    fecha TEXT NOT NULL,
    hora TEXT NOT NULL
)
""")

conexion.commit()
conexion.close()

