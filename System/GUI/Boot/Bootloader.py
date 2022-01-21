from tkinter import Label, PhotoImage
from System.Utils.Colormap import Black

from System.Utils.Utils import get_asset, print_log
from System.Utils.Vars import Assets_dir

__author__ = 'Nahuel senek'
__version__ = '1.5'

def Boot_loader(master):

    print_log("Iniciado...")

    global Logon

    master.configure(background=Black)  #   Establece el fondo a negro

    Logon = get_asset("Assets/logon.png")
    Boot_Logo = Label(master, image=Logon, borderwidth=0.1)

    # colocar Boot_Logo en el centro de la pantalla
    Boot_Logo.place(x= 408, y= 160)

    # Animacion
    frameCnt = 27 # Frames por segundo #60

    # Crea una lista de cada frame del gif
    frames = [
        PhotoImage(file= Assets_dir + "/Loading2.gif", format="gif -index %i" % (i))
        for i in range(frameCnt)
    ]

    # Muestra y va cambiando (Actualizando) el frame
    def update(ind):

        frame = frames[ind]
        ind += 1

        if ind == frameCnt:
            ind = 0

        loading.configure(image=frame)
        master.after(50, update, ind)

    loading = Label(master, borderwidth=0.1)
    loading.place(x= 480, y= 400)

    def End_bootloader():

        Boot_Logo.place_forget()
        loading.place_forget()

        print_log("Terminando...")

    master.after(1, update, 0)

    master.after(10000, End_bootloader)