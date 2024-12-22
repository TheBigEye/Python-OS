import tkinter as tk
from sources.window.manager import WindowManager, WindowFlags
from sources.program.notepad import Notepad
from sources.program.terminal import Terminal

def main():
    root = tk.Tk()
    app = WindowManager(root)

    #app.create_window(title="No Dragable", flags=WindowFlags.WN_DRAGABLE)
    #app.create_window(title="No Controls", flags=WindowFlags.WN_CONTROLS)
    #app.create_window(title="No Resizable", flags=WindowFlags.WN_RESIZABLE)

    #app.create_window()

    app.create_window(title="Notepad", content=Notepad, size=(800, 50, 200, 300))
    app.create_window(title="Terminal", content=Terminal, size=(275, 50, 500, 300))

    parent_window = app.create_window(title="Parent Window", size=(50, 50, 200, 300))
    app.create_child(parent_window, title="Child Window")
    root.mainloop()

if __name__ == "__main__":
    main()