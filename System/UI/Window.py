
class content(Label):
    """
    Clase Content
    """

    def __init__(self, master, text, width, height, x, y):
        """
        Constructor de la clase Content
        """

        Label.__init__(self, master)
        self.master = master
        self.text = text
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.config(
            text=self.text,
            width=self.width,
            height=self.height,
            bg="#CCCCfC",
            fg="#000000",   
            font=("Consolas", 10),
            borderwidth="0",
            relief="flat",
        )

        self.place(x=self.x, y=self.y)



    
    

class Window(Frame):
    # args: master, title, width, height, x, y, content
    #  the content of the window is a widget (can be a frame, a label, a button, etc), always is centered in the window
    # the windows is  a frame, so you can add widgets to it
    # the content arg is a widget or class, so you can add widgets to it
    def __init__(self, master, title, width, height, x, y, content):
        Frame.__init__(self, master)
        self.master = master
        self.title = title
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.content = content

        # Window base
        self.Window_base = Frame(   
            self.master,
            bg="#CCCCCC",
            borderwidth="0",
            width=self.width,   
            height=self.height,

        )

        self.Window_base.place(x=self.x, y=self.y)

        # Window title bar
        self.Window_title_bar = Frame(
            self.Window_base,
            bg="#CFAFCF",
            borderwidth="0",
            width=self.width,
            height=20,
        )

        self.Window_title_bar.place(x=0, y=0)


        # Window title
        self.Window_title = Label(
            self.Window_title_bar,
            text=self.title,
            bg="#CFAFCF",
            fg="#000000",
            font=("Consolas", 12),
            borderwidth="0",
        ) 

        self.Window_title.place(x=5, y=0)

        # Window close button
        self.Window_close_button = Button(
            self.Window_title_bar,
            bg="#FF0F0F",
            fg="#000000",
            font=("Consolas", 12),
            borderwidth="0",
            text="X"
        )

        self.Window_close_button.place(x=self.width-20, y=0)

        # Window content, load the class or widget
        self.Window_content = content(
            self.Window_base,
            "lol",
            30,
            30,
            10,
            10
        )


# test
if __name__ == "__main__":
    root = Tk()
    Window(root, "Window", 300, 300, 100, 100, content)
    root.mainloop()






