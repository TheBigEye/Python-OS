from tkinter import Label, PhotoImage, Frame

from System.Utils.Colormap import Black
from System.Utils.Utils import Asset, Logger, Asset_colored
from System.Utils.Vars import Assets_directory

__author__ = 'TheBigEye'
__version__ = '1.5'


class Boot_loader(Frame):

    def __init__(self, master, time):

        super().__init__(master)

        self.master = master
        self.time = time

        self.master.configure(background=Black)  # Set the background color to black.

        self.Logon = Asset_colored("Bootloader", "logon.png", 1)
        self.Boot_Logo = Label(self.master, image=self.Logon, borderwidth=0.1)

        self.Boot_Logo.place(x= 408, y= 160)

        # Animation...
        self.frames_count = 95 # Frames per second

        # Make a list of frames
        self.frames = [
            PhotoImage(file= Assets_directory + "/UI/Boot/Bootloader/Loading.gif", format="gif -index %i" % (i))
            for i in range(self.frames_count)
        ]

        # Show and update the frames
        def update(ind):

            frame = self.frames[ind]
            ind += 1

            if ind == self.frames_count:
                ind = 0

            self.loading.configure(image=frame)
            self.master.after(8, update, ind)

        self.loading = Label(self.master, borderwidth=0.1)
        self.loading.place(x= 480, y= 400)

        def End_bootloader():

            self.Boot_Logo.place_forget()
            self.loading.place_forget()

            Logger.log("Finishing...")

        self.master.after(1, update, 0)

        self.master.after(time, End_bootloader)
