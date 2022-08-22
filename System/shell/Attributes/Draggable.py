import time
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

        self.widget.lift() # move to the top

        # save the x and y coordinates
        self.widget._drag_start_x = event.x
        self.widget._drag_start_y = event.y

        # move the widget to the cursor position
        self.widget.place(x = self.widget.winfo_x() - self.widget._drag_start_x + event.x, y = self.widget.winfo_y())

        self.widget['cursor'] = "hand2"

    def on_drag_finish(self, event):

        self.widget.master.update()

        self.widget.lift()

        # reset the coordinates
        self.widget._drag_start_x = 16
        self.widget._drag_start_y = 4

        self.widget['cursor'] = ""

    def on_drag_motion(self, event):

        # calculate the new coordinates
        self.x = self.widget.winfo_x() - self.widget._drag_start_x + event.x
        self.y = self.widget.winfo_y() - self.widget._drag_start_y + event.y

        # move the widget (the cursor are positioned in the middle of the widget)
        self.widget.place(x = self.x, y = self.y)
        self.widget.update_idletasks()

        for component in self.widget.winfo_children():
            component.update_idletasks()

        # evoiding the blinking bug (oh well, close enough)
        self.widget.master.update_idletasks()
