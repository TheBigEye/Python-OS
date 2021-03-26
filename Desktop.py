from tkinter import *
import tkinter as tk
import time

ventana = tk.Tk()
ventana.title("Windows PY")
ventana.geometry('1024x720')  # Ancho x Alto
ventana.resizable(False, False)
ventana.configure(background="cornflower blue")

# Variables
Wallpaper_DIR = "Assets/Wallpapers"


def times():
    current_time = time.strftime("%H: %M")
    clock.config(bg="#080D11", text=current_time,
                 fg="white", font="arial 10 bold")
    clock.after(200, times)


# imagen de fondo
background_image = tk.PhotoImage(file=Wallpaper_DIR + "/Bliss_night.png")

background_label = tk.Label(ventana, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# ============================================== Barra de tareas =====================================================

# Crea y posiciona la barra de tareas en la ventana
# Taskbar textura
TaskbarTexture = tk.PhotoImage(file='Assets/Taskbar.png')


# Taskbar posicion
toolbar = Label(ventana, width=148, height=29, borderwidth="0", image=TaskbarTexture,
                text="", background="black", foreground="gray", relief="raised")
toolbar.pack(fill=X, expand=True, anchor="s")

# =============================================== Menu de inicio =====================================================

# Gui del menu
StartMenu = tk.PhotoImage(file='Assets/Menu.png')
Menu = Label(ventana, width=315, height=441, image=StartMenu, borderwidth="0")


# Esta funcion abre y cierra la GUI del menu.. para hacerlo facil, cada vez que se clcikea el bootn, se cambian los mismos

# Abre el menu
def Click_1():
    Menu.place(x=1, y=245)
    time.sleep(0.1)
    start_1.place(x=0, y=50)
    start_2.place(x=0, y=0)


# Cerra el menu
def Click_2():
    Menu.place(x=1, y=1000)
    time.sleep(0.1)
    start_1.place(x=0, y=0)
    start_2.place(x=0, y=32)


# Crea y posiciona el boton de Inicio en la Barra de tareas
# Textura del boton de "INICIO"
StartTexture = tk.PhotoImage(file='Assets/Start_Button.png')
StartLightTexture = tk.PhotoImage(file='Assets/Start_Light_Button.png')


# Boton original
start_1 = Button(toolbar, width=48, height=28, borderwidth="0",
                 bg="black", relief="raised", image=StartTexture, command=Click_1)
start_1.place(x=0, y=0)

# Segundo boton
start_2 = Button(toolbar, width=48, height=28, borderwidth="0",
                 bg="black", relief="raised", image=StartTexture, command=Click_2)
start_2.place(x=0, y=32)

# ============================================== Barra del reloj =====================================================

ClockTexture = tk.PhotoImage(file='Assets/Clockbar.png')

clockbar = Label(toolbar, width=70, height=28, borderwidth="0",
                 relief="raised", bg="#080D11")
clockbar.place(x=950, y=1)

current_time = time.strftime("%H: %M")
clock = Label(toolbar, borderwidth="0", relief="raised")
clock.config(bg="#080D11", text=current_time, fg="white", font="arial 10 bold")
clock.after(200, times)
clock.place(x=963, y=5)

# ====================================================================================================================

ventana.mainloop()
