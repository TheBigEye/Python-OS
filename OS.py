import tkinter as tk

from System.Core.Core import (
    Is_Boot,
    Is_FAIL,
    Is_in_BIOS,
    Is_in_Boot,
    Is_in_Desktop,
    Is_in_INSTALLER,
    Is_in_Login,
    Load_FileSystem,
    routines
)

from System.GUI.Boot.BIOS import BIOS
from System.GUI.Boot.Bootloader import Boot_loader
from System.GUI.Boot.Desktop import Desktop
from System.GUI.Boot.Installer import Os_Installer
from System.GUI.Boot.Login import Login
from System.GUI.Boot.RSOD import RSOD
from System.Utils.Colormap import Black
from System.Utils.Utils import (print_error, print_info, print_log, print_warning)
from System.Utils.Vars import Assets_dir

# -----------------------------------------------------------------[ Main ]----------------------------------------------------------------------- #


Os = tk.Tk()  # Crea la ventana que sera la base del programa
Os.title("PythonOS")  # El titulo de la ventana
Os.iconbitmap(Assets_dir + "/Images/icon.ico")  # Icono de la ventana

Os.geometry("1024x600")  # Resolucion de la pantalla
Os.resizable(False, False)  # No se puede agarandar o achicar
Os.configure(background = Black)  # El negro es el color base


#  Advertencias.
def warnings():

    # En caso de que la resolucion de la pantalla sea menor a la esperada en la ventana, se mostrara una advertencia
    if Os.winfo_screenwidth() < 1024 and Os.winfo_screenheight() < 600:

        print_warning("La resolucion de la pantalla es menor al de la ventana.")


warnings() # Muestra las advertencias antes de la ejecucion
routines() # Ejecuta las rutinas del programa (En este caso nada, ya que no se ejecuta sobre un sistema en blanco)
Load_FileSystem() # Carga el sistema de archivos desde el archivo .JSON
print_info("Sistema de archivos cargado")

# -----------------------------------------------------------------[ Boot ]-------------------------------------------------------------------------- #

# Esta parte inicia las funciones importantes del programa
def start_boot():

    # Inicia la animacion del bootloader (Cargador del arranque)
    Boot_loader(Os)

    # Despues de 12 segundos (o cuando todo este cargado), inicia el escritorio.
    Os.after(12000, Desktop, Os)


# Aqui se comprueba las variables del orden de arranque y se ejecuta la funcion correspondiente:
if Is_FAIL == True:
    RSOD(Os) # Pantalla roja de la muerte (Red screen of death)
    print_error("El sistema ha fallado.")

    # Para el programa despues de 8 segundos.
    Os.after(8000, Os.destroy)

elif Is_in_BIOS == True:
    BIOS(Os) # Inicia la BIOS
    print_log("Empezando desde el BIOS/UEFI")

elif Is_in_INSTALLER == True:
    Os_Installer(Os) # Inicia el instalador (Por ahora es el modo no grafico)
    print_log("Empezando desde el modo no grafico")

elif Is_in_Boot == True:
    Boot_loader(Os) # Inicia el cargador de arranque
    print_log("Empezando desde el bootloader")

elif Is_in_Login == True:
    Login(Os) # Inicia el login
    print_log("Empezando desde Login") # Sin utilizar

elif Is_in_Desktop == True:
    Desktop(Os) # Inicia el escritorio
    print_log("Empezando desde el escritorio")

elif Is_Boot == True:
    start_boot() # Inicia el arranque en general
    print_log("Empezando desde el arranque normal")

# En caso de que el orden que arranque falle, detiene el programa y se escribe lo siguiente:
else:
    print_error("Orden de arranque invalido o no encontrado, PARANDO...")

    # detiene el programa destruyendo la ventana
    Os.destroy()


Os.mainloop() # Bucle principal de tkinter

# ------------------------------------------------------------------[ End ]-------------------------------------------------------------------------- #
