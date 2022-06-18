import random
from tkinter import Frame, Label, PhotoImage

from Libs.pyLogger.Logger import Logger
from System.Utils.Utils import Asset_colored
from System.Utils.Vars import Assets_directory

__author__ = 'TheBigEye'
__version__ = '1.5'


class Bootloader(Frame):

    def __init__(self, master, loading_time: int):

        super().__init__(master)

        self.master = master
        self.loading_time = loading_time

        # Set the background color to black.
        self.master.configure(background="#000000")

        # VMware logo
        self.VMW_logo_image = Asset_colored("Bootloader", "vwboot1.png", 1)
        self.VMW_logo = Label(self.master, image=self.VMW_logo_image, borderwidth=0)
        self.VMW_logo.place(relx=.2, y=16)

        # Show and update the frames
        def update_vmw_loader(ind):

            ind += 1

            if ind >= 50:
                ind = 50

            self.loader_bar.configure(width=ind)
            self.master.after(10, update_vmw_loader, ind)

        self.loader_bar = Label(self.master, width=1, height=1, bg="#FFFFFF", borderwidth=0)

        self.Boot_logo_image = Asset_colored("Bootloader", "logon.png", 1)
        self.Boot_logo = Label(self.master, image=self.Boot_logo_image, borderwidth=0.1)

        # Animation...
        self.frames_count = 95  # Frames per second

        # Make a list of frames
        self.frames = [
            PhotoImage(file="Assets/UI/Boot/Bootloader/Loading.gif", format="gif -index %i" % (i)) for i in range(self.frames_count)
        ]

        # Show and update the frames
        def update_os_loader(ind):

            frame = self.frames[ind]
            ind += 1

            if ind == self.frames_count:
                ind = 0

            rnd = random.randint(8, 24)

            self.loading.configure(image=frame)
            self.master.after(rnd, update_os_loader, ind)

        self.loading = Label(self.master, borderwidth=0.1)

        def add_progressbar():

            self.loader_bar.place(x=290, y=456)

        def add_loading():

            self.loading.place(relx=.5, y=416, anchor="center")
            self.master.after(1200, self.Boot_logo.place(relx=.5, y=276, anchor="center"))

        def quit_os_bootloader():

            self.Boot_logo.place_forget()
            self.loading.place_forget()

            Logger.log("Finishing...")

        def quit_vmw_bootloader():

            self.VMW_logo.place_forget()
            self.loader_bar.place_forget()

        self.master.after(1, update_vmw_loader(0))
        self.master.after(1, add_progressbar)
        self.master.after(2000, quit_vmw_bootloader)
        self.master.after(1, update_os_loader(0))
        self.master.after(2000, add_loading)
        self.master.after(int(self.loading_time - 1000), quit_os_bootloader)
