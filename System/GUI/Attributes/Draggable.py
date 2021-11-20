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

    global on_drag_start, on_drag_motion, on_drag_finish

    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<ButtonRelease-1>", on_drag_finish)
    widget.bind("<B1-Motion>", on_drag_motion)


def make_draggable_clean(widget):

    global on_press, on_motion, on_release, on_enter, on_leave

    widget.drag_start = None
    widget.drag_offset = None
    widget.drag_target = None

    def on_press(event):
        widget.drag_start = event.x, event.y
        widget.drag_offset = widget.winfo_x(), widget.winfo_y()
        widget.drag_target = None
        widget.drag_target_index = None

    def on_motion(event):
        if widget.drag_start is None:
            return

        x, y = event.x, event.y
        dx, dy = x - widget.drag_start[0], y - widget.drag_start[1]
        widget.drag_target = widget.drag_target or widget.drag_offset
        widget.drag_target = widget.drag_target[0] + dx, widget.drag_target[1] + dy
        widget.place(x=widget.drag_target[0], y=widget.drag_target[1])
        
    def on_release(event):
        widget.drag_start = None
        widget.drag_offset = None
        widget.drag_target = None
        widget.drag_target_index = None

    def on_enter(event):
        widget.config(cursor='hand2')

    def on_leave(event):
        widget.config(cursor='arrow')

    widget.bind('<Button-1>', on_press)
    widget.bind('<B1-Motion>', on_motion)
    widget.bind('<ButtonRelease-1>', on_release)
    widget.bind('<Enter>', on_enter)
    widget.bind('<Leave>', on_leave)

    return widget


def drag_start(event):

    global drag_x, drag_y

    '''
    the function is used to start drag and drop.
    '''
    # grab the widget
    widget = event.widget
    # store the widget's position
    widget_x = widget.winfo_x()
    widget_y = widget.winfo_y()
    # set the drag_x and drag_y
    drag_x = event.x_root - widget_x
    drag_y = event.y_root - widget_y
    # set the widget's position
    widget.place(x=widget_x, y=widget_y)
    widget.lift()
    # set the drag_flag to True
    drag_flag = True
    # bind the mousemove event
    widget.bind("<Motion>", drag_move)
    widget.bind("<ButtonRelease-1>", drag_end)
    # unbind the mousewheel event
    widget.unbind("<MouseWheel>")


def drag_move(event):
    '''
    the function is used to move the widget.
    '''
    # get the widget
    widget = event.widget
    # get the widget's position
    widget_x = widget.winfo_x()
    widget_y = widget.winfo_y()
    # set the widget's position
    widget.place(x=event.x_root - drag_x, y=event.y_root - drag_y)


def drag_end(event):
    '''
    the function is used to end the drag and drop.
    '''
    # get the widget
    widget = event.widget
    # set the drag_flag to False
    drag_flag = False
    # unbind the mousemove event
    widget.unbind("<Motion>")
    widget.unbind("<ButtonRelease-1>")
    # bind the mousewheel event
    widget.bind("<MouseWheel>", mousewheel)


def mousewheel(event):
    '''
    the function is used to handle the mousewheel event.
    '''
    # get the widget
    widget = event.widget
    # get the widget's position
    widget_x = widget.winfo_x()
    widget_y = widget.winfo_y()
    # set the widget's position
    widget.place(x=widget_x + event.delta, y=widget_y)


def make_draggable_efficient(widget):
    '''
    the function is used to make the widget draggable.
    '''
    # bind the mousepress event
    widget.bind("<ButtonPress-1>", drag_start)
    # bind the mousewheel event
    widget.bind("<MouseWheel>", mousewheel)