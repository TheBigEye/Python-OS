import tkinter as tk
from tkinter import scrolledtext

class Notepad(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=40, height=10, font=("Fixedsys", 12))
        self.text_area.pack(fill="both", expand=True)
