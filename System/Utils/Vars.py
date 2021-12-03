import os

# Variables mportantes

# Rutas relativas (sirve para poder ejecutar el programa desde cualquier lugar)

Assets_dir = os.path.join(os.getcwd(), "Assets")
Assets_dir = Assets_dir.replace("\\", "/")

Disk_dir = os.path.join(os.getcwd(), "Disk")
Disk_dir = Disk_dir.replace("\\", "/")

Logs_dir = os.path.join(os.getcwd(), "Logs")
Logs_dir = Logs_dir.replace("\\", "/")
