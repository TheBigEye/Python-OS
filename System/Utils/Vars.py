import os
# Important variables

# Relative paths (used to be able to execute the program from anywhere)
# WARNING: don't touch this unless you know what you're doing.

Assets_directory = os.path.join(os.getcwd(), "Assets")
Assets_directory = Assets_directory.replace("\\", "/")

Disk_directory = os.path.join(os.getcwd(), "Disk")
Disk_directory = Disk_directory.replace("\\", "/")

Logs_directory = os.path.join(os.getcwd(), "Logs")
Logs_directory = Logs_directory.replace("\\", "/")
