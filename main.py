import tkinter as tk
from sources.window.manager import WindowManager, WindowFlags
from sources.program.notepad import Notepad
from sources.program.terminal import Terminal


def main():
    root = tk.Tk()

    # We need to create an instance of the WindowManager class
    app = WindowManager(root) # And pass the root window to it

    #app.create_window(title="No Dragable", flags=WindowFlags.WN_DRAGABLE) # A window that can't be dragged
    #app.create_window(title="No Controls", flags=WindowFlags.WN_CONTROLS) # A window without controls
    #app.create_window(title="No Resizable", flags=WindowFlags.WN_RESIZABLE) # A window that can't be resized

    # A normal window
    #app.create_window()

    # Windows with content
    app.create_window(title="Notepad", content=Notepad, size=(800, 50, 200, 300))
    app.create_window(title="Terminal", content=Terminal, size=(275, 50, 500, 300))

    # Parent window with child window
    parent_window = app.create_window(title="Parent Window", size=(50, 50, 200, 300))
    app.create_child(parent_window, title="Child Window")

    # Finally, start the main loop
    root.mainloop()


if __name__ == "__main__":
    main()
