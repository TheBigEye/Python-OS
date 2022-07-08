
from tkinter import Button, Label, Tk

class Window_base(Label):
    '''A gradient frame which uses a canvas to draw the background'''
    def __init__(self, parent, borderwidth=0, relief="sunken"):
        Label.__init__(self, parent, borderwidth=borderwidth, relief=relief)

class Window(Label):
    def __init__(self, parent, borderwidth=0, relief="flat"):
        Label.__init__(self, parent)

        WMB = Window_base(self)
        WMB.place(x=10, y=10, width=300 , height=300)
        inner_frame = Label(WMB)
        inner_frame.configure(bg="#0100A6")
        inner_frame.place(x=0, y=0, width=300 , height=300)

        Titlebar = Label(inner_frame, text="Titlebar", font=["Tahoma", 10, "bold"], bg="#0100A6", fg="#FFFFFF")
        Titlebar.pack(side="top", fill="both", anchor="w")

        Buttons_bar = Label(Titlebar, bg="#0100A6", fg="#FFFFFF", relief="flat", width=8)
        Buttons_bar.pack(side="top", anchor="e")

        Close_button = Button(Buttons_bar, text="X", command=WMB.destroy)
        Close_button.place(x=42, y=0, width=16, height=18)

        Maximize_button = Button(Buttons_bar, text="[]", command=WMB.destroy)
        Maximize_button.place(x=21, y=0, width=16, height=18)

        Minimize_button = Button(Buttons_bar, text="_", command=WMB.destroy)
        Minimize_button.place(x=4, y=0, width=16, height=18)

        l1 = Label(inner_frame, width=40, height=10, borderwidth=1, bg="black", text="Hello World", fg="white", font=["Arial", 12, "bold"])
        l1.pack(side="top", fill="both", expand=True)


class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        appWindow = Window(self)
        appWindow.place(x=64, y=64, width=600 , height=600)
        lol = Label(appWindow, width=40, height=10, text="Hello World", font=["Arial", 12, "bold"], bg="gray", fg="white")
        lol.place(x=12, y=38, width=128 , height=128)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
