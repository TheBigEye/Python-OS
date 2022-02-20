from tkinter import *

class Window(Frame):
    # args: master, title, width, height, x, y, icon, widgets
    def __init__(self, master, title, width, height, x, y, icon, widgets):
        Frame.__init__(self, master)
        self.master = master
        self.title = title
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.icon = icon
        self.widgets = widgets

        # make the window base
        self.base = Frame(self.master, width=self.width, height=self.height, bg="#000000")
        self.base.place(x=self.x, y=self.y)

        # maake the titlebar as frame
        self.titlebar = Frame(self.base, width=500, height=24, bg="#808080")
        self.titlebar.place(x=0, y=0)

        self.titlebar_text = Label(self.titlebar, text=self.title, bg="#808080", fg="white")
        self.titlebar_text.place(x=0, y=0)

        # make the close button
        self.close_button = Button(self.titlebar, text="X", width=1, height=1, bg="#ff0000", borderwidth=0, command= self.destroy)
        self.close_button.place(x=480, y=0)

        # get the widgets in the list, change the widget master to the base frame
        for widget in self.widgets:
            widget.master = self.base
            widget.lift()
            widget.place(x=self.base_x + 1, y=self.base_y + 24)

            # if the base is destroyed, destroy the widgets
            self.base.bind("<Destroy>", lambda event: widget.destroy())

    def resize(self, width, height):
        self.width = width
        self.height = height
        self.base.config(width=self.width, height=self.height)

    def destroy(self):
        self.base.destroy()


# test
if __name__ == "__main__":
    root = Tk()
    root.title("test")
    root.geometry("1024x600")
    root.resizable(False, False)

    w = Window(root, "Window", 500, 300, 100, 100, "", [Button(text="Hello World", bg="#2E2E2E", fg="#FFFFFF")])
    w.place(x=0, y=0)
    root.mainloop()


