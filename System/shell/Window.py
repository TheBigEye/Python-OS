
from doctest import master
from tkinter import *


class Window(Frame):
    def __init__(self, master=None, app=Widget, title: str = "Window", win_w: int = None, win_h: int = None, win_x: int = 0, win_y: int = 0):
        Frame.__init__(self, master)
        self.master = master
        self.app = app
        self.title = title
        self.win_x = win_x
        self.win_y = win_y
        self.win_w = win_w
        self.win_h = win_h
        self.place(x=self.win_x, y=self.win_y, width=self.win_w, height=self.win_h)
        self.init_window()
        self.update()

    def init_window(self):
        self.titlebar()

    def titlebar(self):
        self.Titlebar = Frame(self, bg="blue", width=self.win_w, height=24)
        self.Titlebar.pack(side="top", fill="x")

        self.title_label = Label(self.Titlebar, text=self.title, anchor="w", bg=self.Titlebar.cget("bg"), fg="white")
        self.title_label.place(x=0, y=2)

        self.quit_button = Button(self.Titlebar, text="X", fg = "white", command=self.client_exit, anchor="e", bg="red", relief="flat")
        self.quit_button.place(x=self.win_w - 24, y=2)

    # when click, update the widget
    def update(self):
        self.app.place(x=self.win_x, y=24)
        self.app.lift
        self.app.update()

    def client_exit(self):
        self.destroy()

# test
root = Tk()
root.geometry("1024x600")
root.configure(background='#000000')
app = Button(text="Hello World")
Window(root, app, "lol", win_w=200, win_h=400, win_x=10, win_y=10)

root.mainloop()
