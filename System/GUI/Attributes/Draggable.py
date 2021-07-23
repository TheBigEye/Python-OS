from tkinter import *

# Drag and drop function

def on_drag_start(event):

    global widget

    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

    widget['cursor'] = "hand2"


def on_drag_finish(event):

    global widget

    widget = event.widget
    widget._drag_start_x = 0
    widget._drag_start_y = 0

    widget['cursor'] = ""


def on_drag_motion(event): 

    global widget, x, y

    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x 
    y = widget.winfo_y() - widget._drag_start_y + event.y 
    widget.place(x = x, y = y)


def make_draggable(widget):

    global on_drag_start, on_drag_motion

    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<ButtonRelease-1>", on_drag_finish)
    widget.bind("<B1-Motion>", on_drag_motion)