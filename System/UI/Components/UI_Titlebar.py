from tkinter import Frame, Label, Button

from System.Utils.Utils import Asset, Image_getcolor
from System.UI.Attributes.Draggable import drag_n_drop


class UI_Titlebar(Frame):
    def __init__(self, parent, x, y, width):
        Frame.__init__(self, parent)

        self.parent = parent
        self.x = x
        self.y = y
        self.width = width

        # Get the parent bg color
        self.parent_bg_color = parent.cget("bg")

        self.Titlebar_img = Asset("Titlebar.png")
        self.Close_img_red = Asset("Close_red.png")
        self.Close_img_normal = Asset("Close_normal.png")

        self.Minimize_img_light = Asset("Minimize_light.png")
        self.Minimize_img_normal = Asset("Minimize_normal.png")

        self.Maximize_img_light = Asset("Maximize_light.png")
        self.Maximize_img_normal = Asset("Maximize_normal.png")

        def close_click(event):
            self.parent.destroy()

        self.Titlebar = Label(self.parent, image=self.Titlebar_img, width=self.width, borderwidth="0")
        self.Titlebar.place(x=x, y=y)

        self.Close = Button(self.Titlebar, width=13, height=13, image=self.Close_img_normal, borderwidth="0")
        self.Close.place(x=self.width - 22, y=4)
        self.Close.bind("<Button-1>", close_click)
        self.Close.bind("<Enter>", lambda event: self.Close.configure(image=self.Close_img_red))
        self.Close.bind("<Leave>", lambda event: self.Close.configure(image=self.Close_img_normal))

        self.Minimize = Button(self.Titlebar, width=13, height=13, image=self.Minimize_img_normal, borderwidth="0")
        self.Minimize.place(x=self.width - 44, y=4)
        self.Minimize.bind("<Button-1>", close_click)
        self.Minimize.bind("<Enter>", lambda event: self.Minimize.configure(image=self.Minimize_img_light))
        self.Minimize.bind("<Leave>", lambda event: self.Minimize.configure(image=self.Minimize_img_normal))

        self.Maximize = Button(self.Titlebar, width=13, height=13, image=self.Maximize_img_normal, borderwidth="0")
        self.Maximize.place(x=self.width - 66, y=4)
        self.Maximize.bind("<Button-1>", close_click)
        self.Maximize.bind("<Enter>", lambda event: self.Maximize.configure(image=self.Maximize_img_light))
        self.Maximize.bind("<Leave>", lambda event: self.Maximize.configure(image=self.Maximize_img_normal))

        self.titlecolor = Image_getcolor("Titlebar.png", 0, 0)

        self.Title = Label(self.Titlebar, text="Title", bg=self.titlecolor, fg="white", font=("Tahoma bold", 8))
        self.Title.place(x=10, y=2)

        self.Titlebar.bind("<Button-1>", drag_n_drop(self.parent))



