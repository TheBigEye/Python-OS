from tkinter import Label, PhotoImage
from System.Utils.Colormap import Black
from System.Utils.Utils import print_log

__author__ = 'TheBigEye'
__version__ = '1.5'

# Specific Colors
Login_background_color = "#477afb"
Login_entry_color = "#5A7EFC"

def Boot_loader(master): 

    print_log("Bootloader: Initializing...")

    global Logon

    master.configure(background=Black)  # Sets the background to Black

    Logon = PhotoImage(file="Assets/logon.png")
    Boot_Logo = Label(master, image=Logon, borderwidth=0.1)
    Boot_Logo.place(x= 400, y= 160)

    # Loading animation
    frameCnt = 60
    frames = [
        PhotoImage(file="Assets/Loading.gif", format="gif -index %i" % (i))
        for i in range(frameCnt)
    ]

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

        print_log("Bootloader: Finishing...")



    master.after(1, update, 0)

    master.after(10000, End_bootloader)