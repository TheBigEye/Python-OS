from tkinter import Label, PhotoImage
from System.Utils.Colormap import Black
from System.Utils.Utils import print_log

__author__ = 'TheBigEye'
__version__ = '1.5'

def Boot_loader(master): 

    print_log("Bootloader: Iniciado...")

    global Logon

    master.configure(background=Black)  #   Establece el fondo a negro

    Logon = PhotoImage(file="Assets/logon.png")
    Boot_Logo = Label(master, image=Logon, borderwidth=0.1)
    Boot_Logo.place(x= 400, y= 160)

    # Animacion 
    frameCnt = 60 # Frames por segundo

    # Crea una lista de cada frame del gif
    frames = [
        PhotoImage(file="Assets/Loading.gif", format="gif -index %i" % (i))
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

        print_log("Bootloader: Terminando...")

    master.after(1, update, 0)

    master.after(10000, End_bootloader)
