import tkinter as tk
import sys
import code
from threading import Thread
import queue


class Console(tk.Frame):
    def __init__(self, parent, _locals, exit_callback):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.exit_callback = exit_callback
        self.destroyed = False

        self.real_std_in_out = (sys.stdin, sys.stdout, sys.stderr)

        sys.stdout = self
        sys.stderr = self
        sys.stdin = self

        self.stdin_buffer = queue.Queue()

        self.createWidgets()

        self.consoleThread = Thread(target=lambda: self.run_interactive_console(_locals))
        self.consoleThread.start()

    def run_interactive_console(self, _locals):
        try:
            code.interact(local=_locals)
        except SystemExit:
            if not self.destroyed:
                self.after(0, self.exit_callback)

    def destroy(self):
        self.stdin_buffer.put("\n\nexit()\n")
        self.destroyed = True
        sys.stdin, sys.stdout, sys.stderr = self.real_std_in_out
        super().destroy()

    def enter(self, event):
        input_line = self.ttyText.get("input_start", "end")
        self.ttyText.mark_set("input_start", "end-1c")
        self.ttyText.mark_gravity("input_start", "left")
        self.stdin_buffer.put(input_line)

    def write(self, string):
        self.ttyText.insert('end', string)
        self.ttyText.mark_set("input_start", "end-1c")
        self.ttyText.see('end')

    def createWidgets(self):
        self.ttyText = tk.Text(self.parent, wrap='word')
        self.ttyText.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.ttyText.bind("<Return>", self.enter)
        self.ttyText.mark_set("input_start", "end-1c")
        self.ttyText.mark_gravity("input_start", "left")

    def flush(self):
        pass

    def readline(self):
        line = self.stdin_buffer.get()
        return line


if __name__ == '__main__':
    root = tk.Tk()
    root.config(background="red")
    main_window = Console(root, locals(), root.destroy)
    main_window.mainloop()