from tkinter import Frame, Label
from System.Utils.Utils import Asset, Asset_color


class UI_Checkbutton(Frame):
    def __init__(self, parent, x, y, value):
        Frame.__init__(self, parent)

        self.parent = parent
        self.x = x
        self.y = y
        self.value = value

        self.Checkbutton_img_Uncheckd = Asset("Uncheck.png")
        self.Checkbutton_img_checked = Asset("Checked.png")

        if self.value == True:
            self.Checkbutton_img = self.Checkbutton_img_checked
        else:
            self.Checkbutton_img = self.Checkbutton_img_Uncheckd

        self.Checkbutton = Label(parent, image=self.Checkbutton_img, borderwidth="0")

        self.Checkbutton.place(x=x, y=y)

        def checkbutton_click(event):
            if self.value:
                self.Checkbutton.configure(image=self.Checkbutton_img_Uncheckd)
                self.value = False
            else:
                self.Checkbutton.configure(image=self.Checkbutton_img_checked)
                self.value = True


        self.Checkbutton.bind("<Button-1>", checkbutton_click)
