
from tkinter import Button, Frame, Label, Tk


class Window(Frame):
    def __init__(self, master, width, height, x, y, title, color, widgets, bgcolor):
        Frame.__init__(self, master)
        self.master = master
        self.w = width
        self.h = height
        self.x = x
        self.y = y
        self.title = title
        self.color = color
        self.widgets = widgets
        self.bgcolor = bgcolor

        # make the window base
        # window structure
        # --------------------------------------------------
        # | title                                        x | <------ title bar and close button
        # |------------------------------------------------|
        # |                                                | <------- window frame
        # |                                                |
        # |                                                |
        # |                                                |
        # |                                                |
        # |                    widgets                     |
        # |                                                |
        # |                                                |
        # |                                                |
        # |                                                |
        # |                                                |
        # |                                                |
        # --------------------------------------------------

        # make the window base frame
        window_base = Frame(self.master, width=self.w, height=self.h, bg=self.bgcolor)
        window_base.place(x=self.x, y=self.y)


        # make the title bar
        title_bar = Frame(window_base, width=self.w, height=28, bg=self.color)
        title_bar.place(x=0, y=0)

        global close_window
        def close_window():
            window_base.destroy()

        # make the close button
        close_button = Button(title_bar, text="X", command=close_window, bg=self.color, fg="white")
        close_button.place(x=self.w-30, y=0)

        # make the window frame
        window_frame = Frame(window_base, width=self.w, height=self.h-30, bg=self.bgcolor)
        window_frame.place(x=0, y=30)

        # put the widgets inside the window frame
        for widget in self.widgets:
            widget.master = window_frame
            widget.place(x=self.x + 2, y=self.y + 24)
            widget.lift()

       # drag n drop
        def drag_n_drop(event):
            master.after(1, lambda: window_base.place(x=event.x_root-x, y=event.y_root-y))
            for widget in self.widgets:
                widget.place(x=event.x_root-x + 2, y=event.y_root-y + 24)
                widget.lift()

        window_frame.bind("<B1-Motion>", drag_n_drop)

# test
if __name__ == "__main__":
    root = Tk()
    root.configure(background="black")

    # widgets
    label = Label(text="Hello World!")

    label2 = Label(text="Hello World2324!")


    window = Window(root, width=512, height=400, x=100, y=100, title="test", color="red", widgets=[label, label2], bgcolor="white")
    root.mainloop()