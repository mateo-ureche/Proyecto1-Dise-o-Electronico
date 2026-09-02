# Proyecto 1 - Diseño Electrónico: GPS Tracker 📍

Repositorio para el sistema de adquisición y visualización de tramas GPS mediante UDP y Servidor Web.

## Pasos para ejecutar el proyecto:
1. Instalar Python 3.
2. Ejecutar `python crear_bd.py` para inicializar la base de datos SQLite.
3. En una terminal, ejecutar `python servidor_udp.py` para iniciar la escucha de tramas GPS en el puerto 5000.
4. En otra terminal, ejecutar `python servidor_web.py` para arrancar el backend en el puerto 8000.
5. Abrir un navegador e ingresar a `http://localhost:8000` para visualizar los datos en tiempo real.
