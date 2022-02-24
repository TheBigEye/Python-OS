# Drag and drop function
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
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x = x, y = y)


def make_draggable(widget):

    global on_drag_start, on_drag_motion, on_drag_finish

    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<ButtonRelease-1>", on_drag_finish)
    widget.bind("<B1-Motion>", on_drag_motion)


# Drag n drop function
def drag_n_drop(widget):

    # can drag an label with text and image without blinking bug
    widget.config(cursor = "hand2")
    widget.bind("<ButtonPress-1>", lambda event: on_drag_start(event))
    widget.bind("<ButtonRelease-1>", lambda event: on_drag_finish(event))
    widget.bind("<B1-Motion>", lambda event: on_drag_motion(event))

def make_draggable_button(Button):

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