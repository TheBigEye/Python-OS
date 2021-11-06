def after(widget, delay, func, *args):
    """
    This method allows to put more functions inside a widget.after() function.
    :param widget:
    :param delay:
    :param func:
    :param args:
    :return:
    """
    def f():
        func(*args)
        widget.after(delay, f)
    widget.after(delay, f)


# 

