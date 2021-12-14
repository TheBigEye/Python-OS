from tkinter import Button, Label, PhotoImage
import tkinter as tk


class Window(Label):
    def __init__(self, master, title = "Ventana", draggable = True, programm: object = None):
        Label.__init__(self, master)

        self.master = master
        self.title = title
        self.draggable = draggable

        # --------------------------------------------------------------------- [ Variables ] -----------------------------------------------------------------------

        # Base de la ventana

        self.Window_GUI_image = PhotoImage(file="Assets/GUI/Window/Window.png")
        global Window_base
        global Window_GUI_image

        self.Window_base = Label(
            self.master,
            bg = "black",
            image = self.Window_GUI_image,
            borderwidth = 0
        )

        self.Window_base_x = (self.master.winfo_width() / 2) - (self.Window_base.winfo_width() / 2)
        self.Window_base_y = (self.master.winfo_height() / 2) - (self.Window_base.winfo_height() / 2)

        def Update_base_position():

            self.Window_base.lift()
            self.Window_base.place(x = self.Window_base_x, y = self.Window_base_y)

        self.master.after(100, Update_base_position)


        # ---------------------------------------------------------------------- [ Componentes ] -------------------------------------------------------------------------------


        global Window_control_pane
        global Window_control_pane_image
        self.Window_control_pane_image = PhotoImage(file="Assets/GUI/Window/Control_pane.png")

        # Panel de botones
        self.Window_control_pane = Label(
            self.Window_base,
            bg = "black",
            image = self.Window_control_pane_image,
            borderwidth = 0,
        )

        self.Window_control_pane_x = 723
        self.Window_control_pane_y = self.Window_base.winfo_height() - self.Window_control_pane.winfo_height()

        def Update_control_position():

            self.Window_control_pane.lift()
            self.Window_control_pane.place(x = self.Window_control_pane_x, y = self.Window_control_pane_y)

        self.Window_base.after(100, Update_control_position)


        # Titulo
        global Window_title
        self.Window_title = Label(
            self.Window_base,
            text = self.title,
            bg="#070F12",
            fg = "white",
            font = ("Segoe UI semilight", 9)
        )

        self.Window_title_x = (self.Window_base.winfo_width() / 2) - (self.Window_title.winfo_width() / 2 - 32)
        self.Window_title_y = (self.Window_base.winfo_height() / 2) - (self.Window_title.winfo_height() / 2 - 2)

        def Update_title_position():

            self.Window_title.lift()
            self.Window_title.place(x = self.Window_title_x, y = self.Window_title_y)

        self.Window_base.after(100, Update_title_position)


        # Icono de la ventana
        global Window_icon
        global Window_icon_image
        Window_icon_image = PhotoImage(file="Assets/GUI/Window/Icon.png")

        Window_icon = Button(
            self.Window_base,
            bg = "black",
            image = Window_icon_image,
            borderwidth = 0
        )

        Window_icon_x = self.Window_base.winfo_width() - Window_icon.winfo_width() + 8
        Window_icon_y = self.Window_base.winfo_height() - Window_icon.winfo_height() + 6

        def Update_icon_position():

            Window_icon.place(x = Window_icon_x, y = Window_icon_y)

        self.Window_base.after(100, Update_icon_position)


        # Boton de minimizar

        global Window_minimize_button
        global Window_minimize_button_image
        Window_minimize_button_image = PhotoImage(file="Assets/GUI/Window/Minimize_button.png")

        Window_minimize_button = Button(
            self.Window_base,
            bg = "black",
            image = Window_minimize_button_image,
            borderwidth = 0,
            command = lambda: master.iconify()
        )

        Window_minimize_button_x = 726
        Window_minimize_button_y = self.Window_base.winfo_height() - Window_minimize_button.winfo_height() + 2

        def Update_minimize_button_position():
            Window_minimize_button.lift()

            Window_minimize_button.place(x = Window_minimize_button_x, y = Window_minimize_button_y)

        self.Window_base.after(100, Update_minimize_button_position)

        # --------------------------------------------------------------------- [ Arastrar y soltar ] -----------------------------------------------------------------------
        def make_draggable(widget):
            '''
            the function is used to make the widget draggable.
            '''
            # bind the mousepress event
            widget.bind("<ButtonPress-1>", drag_start)


        def drag_start(event):
            '''
            the function is used to start the draggable.
            '''
            # get the widget
            widget = event.widget
            # get the widget's position
            widget_x = widget.winfo_x()
            widget_y = widget.winfo_y()

            # set the widget's position
            widget.place(x=widget_x + event.x, y=widget_y + event.y)

            # bind the mousemove event
            widget.bind("<B1-Motion>", drag_move)
            # bind the mouserelease event
            widget.bind("<ButtonRelease-1>", drag_stop)

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
            widget.place(x=widget_x + event.x, y=widget_y + event.y)

        def drag_stop(event):
            '''
            the function is used to stop the widget.
            '''
            # get the widget
            widget = event.widget
            # unbind the mousemove event
            widget.unbind("<B1-Motion>")
            # unbind the mouserelease event
            widget.unbind("<ButtonRelease-1>")

        if draggable == True:
            make_draggable(self.Window_base)


        # --------------------------------------------------------------------- [ Funciones ] -----------------------------------------------------------------------

        global set_programm
        def set_programm(programm):
            '''
            the function is used to set the programm.
            '''
            self.programm = programm

            # put the programm in the center of the window
            self.programm.place(x = 64, y = 64)
        set_programm(programm)



# test
root = tk.Tk()
root.geometry("1024x600")

def etiqueta():
    label = Label(Window, text="Hola")
    label.pack()

Window(root, title = "Ventana", draggable = True, programm=etiqueta)

def clone_button():

    def clone_window():
        Window(root, etiqueta, title = "Ventana", draggable = True)

    button = Button(root, text="Hola", command=clone_window)
    button.place(x = 100, y = 100)

clone_button()

root.mainloop()