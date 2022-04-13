
# Drag and drop functions

def drag_start(event):

    """
    This function is invoked when the user presses the left mouse button.
    """

    from System.Utils.Vars import Hand_2

    global widget

    widget = event.widget
    widget.lift()
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y


    widget['cursor'] = Hand_2


def drag_finish(event):

    """
    This function is invoked when the user releases the left mouse button.
    """

    global widget
    widget.lift()
    widget = event.widget
    widget._drag_start_x = 0
    widget._drag_start_y = 0

    widget['cursor'] = ""


def drag_motion(event):

    """
    This function is invoked when the user moves the mouse.
    """

    global widget, x, y
    widget.lift()
    widget = event.widget
    x = (widget.winfo_x() - widget._drag_start_x / 2) + (event.x / 2)
    y = (widget.winfo_y() - widget._drag_start_y / 2) + (event.y / 2)
    widget.master.after(1, lambda: widget.place(x = x, y = y))
    widget.update()

    # evoiding the blinking bug
    widget.master.update()


def make_draggable(widget):

    """
    This function is used to make a widget draggable.
    """

    global drag_start, drag_motion, drag_finish

    widget.bind("<Button-1>", drag_start)
    widget.bind("<ButtonRelease-1>", drag_finish)
    widget.bind("<B1-Motion>", drag_motion)


# Drag n drop function
def drag_n_drop(widget):

    """
    This function is used to make a widget draggable.
    """

    # can drag an label with text and image without blinking bug
    widget.bind("<ButtonPress-1>", lambda event: drag_start(event))
    widget.bind("<ButtonRelease-1>", lambda event: drag_finish(event))
    widget.bind("<B1-Motion>", lambda event: drag_motion(event))

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
