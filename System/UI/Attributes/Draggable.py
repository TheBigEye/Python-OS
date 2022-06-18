from tkinter import dnd
# Drag and drop functions

def make_draggable_button(Button):

    """
    This function is used to make a button draggable.
    """

    def on_drag_start(event):

        global widget

        widget = event.widget
        widget.lift()
        widget._drag_start_x = event.x
        widget._drag_start_y = event.y

        widget['cursor'] = "hand2"


    def on_drag_finish(event):

        global widget
        widget.lift()
        widget = event.widget
        widget._drag_start_x = 0
        widget._drag_start_y = 0

        widget['cursor'] = ""


    def on_drag_motion(event):

        global widget, x, y
        widget.lift()
        widget = event.widget
        x = widget.winfo_x() - widget._drag_start_x + event.x
        y = widget.winfo_y()

        widget.place(x = x, y = y)


    Button.bind("<Button-1>", on_drag_start)
    Button.bind("<ButtonRelease-1>", on_drag_finish)
    Button.bind("<B1-Motion>", on_drag_motion)


class drag_it:

    """
    This class is used to make a widget draggable  using th tkinter.dnd module
    """

    def __init__(self, widget):

        self.widget = widget
        self.widget.bind("<ButtonPress-1>", self.on_drag_start)
        self.widget.bind("<ButtonRelease-1>", self.on_drag_finish)
        self.widget.bind("<B1-Motion>", self.on_drag_motion)

    def on_drag_start(self, event):

        global widget

        widget = event.widget
        widget.lift()
        widget._drag_start_x = event.x
        widget._drag_start_y = event.y

        widget['cursor'] = "hand2"


    def on_drag_finish(self, event):

        global widget
        widget.lift()
        widget = event.widget
        widget._drag_start_x = 16
        widget._drag_start_y = 4

        widget['cursor'] = ""


    def on_drag_motion(self, event):

        global widget, x, y
        widget.lift()
        widget = event.widget
        x = int((widget.winfo_x() - widget._drag_start_x )) + int((event.x) / 2)
        y = int((widget.winfo_y() - widget._drag_start_y )) + int((event.y) / 2)

        widget.place(x = x, y = y)
        widget.update()

        for widget in self.widget.winfo_children():
            widget.update()

        # evoiding the blinking bug
        self.widget.master.update()
