from Desktop import Ventana
from tkinter import *


# Bootscreen

def Bootscreen():
    Logon_image = PhotoImage(file = "Assets/logon.png")
    BootLogo = Label(Ventana, image = Logon_image, borderwidth= 0.1)
    BootLogo.place(x = 400, y = 160)
    return Bootscreen

    
     
