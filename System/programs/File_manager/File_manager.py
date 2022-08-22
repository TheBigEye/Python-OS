from tkinter import *
from Libs.pyImage.Image import Image
from System.shell.Attributes.Draggable import drag_it

from System.core.filesystem import *


__author__ = 'TheBigEye'
__version__ = '1.1'

class Folder(Label):
    """ Folder """

    def __init__(self, master, x, y, name: str):
        """ Put the folder in the screen """

        Label.__init__(self, master)

        self.master = master
        self.x = x
        self.y = y
        self.name = name

        self.image = Image.setImage("Assets/Shell/Icons/Folder_icon.png", (24, 24), "#ff00ff", "#00142D")
        self.image_selected = Image.setImage("Assets/Shell/Icons/Folder_icon.png", (24, 24), "#ff00ff", "#001228")

        self.selection_normal = Image.setImage("Assets/Shell/Programs/File manager/Selection.png", None, "#ff00ff", "#00142D")
        self.selection_selected = Image.setImage("Assets/Shell/Programs/File manager/Selection_selected.png", None, "#ff00ff", "#00142D")

        self.selection_label = Label(
            self.master,
            bg="#00142D",
            image=self.selection_normal,
            borderwidth="0",
            relief="flat"
        )

        # if the file is selected, change the image
        self.selection_label.bind("<Enter>", lambda event: select_folder(self))
        self.selection_label.bind("<Leave>", lambda event: unselect_folder(self))

        self.Folder = Label(
            self.master,
            bg="#00142D",
            image=self.image,
            borderwidth="0",
            relief="flat",
            cursor="hand2"
        )

        self.name_label = Label(
            self.master,
            text=self.name,
            bg="#00142D",
            fg="#ffffff",
            font=("Consolas", 8),
            borderwidth="0",
            relief="flat"
        )

        self.name_label.bind("<Enter>", lambda event: select_folder(self))
        self.name_label.bind("<Leave>", lambda event: unselect_folder(self))

        def select_folder(self):
            """ Select the folder """

            self.selection_label.config(image=self.selection_selected)
            self.Folder.config(image=self.image_selected)
            self.name_label.config(bg="#001228")

        def unselect_folder(self):
            """ Unselect the folder """

            self.selection_label.config(image=self.selection_normal)
            self.Folder.config(image=self.image)
            self.name_label.config(bg="#00142D")

        # if click on the folder, change directory to the folder
        self.Folder.bind("<Button-1>", lambda event: change_directory(self.name))
        self.name_label.bind("<Button-1>", lambda event: change_directory(self.name))
        self.selection_label.bind("<Button-1>", lambda event: change_directory(self.name))

        self.Folder.place(x=self.x + 1, y=self.y)
        self.name_label.place(x=self.x + 25, y=(self.y) + 4)
        self.selection_label.place(x=self.x - 4, y=self.y)

class File(Label):
    """ File """

    def __init__(self, master, x, y, name, icon):
        """ Put a file in the scree """

        Label.__init__(self, master)

        self.master = master
        self.x = x
        self.y = y
        self.name = name

        self.icon = icon
        self.file_icon = Image.setImage("Assets/Shell/Icons/" + icon + "_icon.png", (24, 24), "#ff00ff", "#00142D")
        self.file_icon_selected = Image.setImage("Assets/Shell/Icons/" + icon + "_icon.png", (24, 24), "#ff00ff", "#001228")

        self.selection_normal = Image.setImage("Assets/Shell/Programs/File manager/Selection.png", None, "#ff00ff", "#00142D")
        self.selection_selected = Image.setImage("Assets/Shell/Programs/File manager/Selection_selected.png", None, "#ff00ff", "#00142D")

        self.selection_label = Label(
            self.master,
            bg="#00142D",
            image=self.selection_normal,
            borderwidth="0",
            relief="flat"
        )

        # if the file is selected, change the image
        self.selection_label.bind("<Enter>", lambda event: select_file(self))
        self.selection_label.bind("<Leave>", lambda event: unselect_file(self))

        self.File = Label(
            self.master,
            bg="#00142D",
            image=self.file_icon,
            borderwidth="0",
            relief="flat",
            cursor="hand2"
        )

        self.name_label = Label(
            self.master,
            text=self.name,
            bg="#00142D",
            fg="#ffffff",
            font=("Consolas", 8),
            borderwidth="0",
            relief="flat"
        )

        self.name_label.bind("<Enter>", lambda event: select_file(self))
        self.name_label.bind("<Leave>", lambda event: unselect_file(self))

        self.date_label = Label(
            self.master,
            text=get_file_date(self.name),
            bg="#00142D",
            fg="#ffffff",
            font=("Consolas", 8),
            borderwidth="0",
            relief="flat"
        )

        self.date_label.bind("<Enter>", lambda event: select_file(self))
        self.date_label.bind("<Leave>", lambda event: unselect_file(self))

        self.size_label = Label(
            self.master,
            text=get_file_size(self.name),
            bg="#00142D",
            fg="#ffffff",
            font=("Consolas", 8),
            borderwidth="0",
            relief="flat"
        )

        self.size_label.bind("<Enter>", lambda event: select_file(self))
        self.size_label.bind("<Leave>", lambda event: unselect_file(self))

        def select_file(self):
            """ Select the file """

            self.selection_label.config(image=self.selection_selected)
            self.File.config(image=self.file_icon_selected)
            self.name_label.config(bg="#001228")
            self.date_label.config(bg="#001228")
            self.size_label.config(bg="#001228")

        def unselect_file(self):
            """ Unselect the file """

            self.selection_label.config(image=self.selection_normal)
            self.File.config(image=self.file_icon)
            self.name_label.config(bg="#00142D")
            self.date_label.config(bg="#00142D")
            self.size_label.config(bg="#00142D")


        self.File.place(x=self.x + 1, y=self.y)
        self.name_label.place(x=self.x + 25, y=(self.y) + 4)
        self.date_label.place(x=self.x + 192, y=(self.y) + 4)
        self.size_label.place(x=self.x + 332, y=(self.y) + 4)
        self.selection_label.place(x=self.x - 4, y=self.y)

class File_manager(Frame):

    """
    File manager
    """

    def __init__(self, master, draggable: bool = True):
        """
        File manager constructor
        """

        Frame.__init__(self, master)

        self.master = master
        self.draggable = draggable

        self.File_manager_image = Image.setImage("Assets/Shell/Programs/File manager/Window.png")  # File manager image base
        self.Splash_logo_image = Image.setImage("Assets/Shell/Programs/File manager/File_manager_icon.png", (112, 112), "#ff00ff", "#002C4F")  # Splash image
        self.Splash_image = Image.setImage("Assets/Shell/Programs/File manager/Splash.png")  # Splash image

        self.File_manager = Label(
            self.master,
            bg="#CCCCCC",
            image=self.File_manager_image,
            borderwidth="0"
        )

        self.File_manager.place(relx=.2, y=128)

        def render_filesystem(self):
            """ Render the filesystem """

            # remove the folders and files widgets from the File manager
            for widget in self.File_manager.winfo_children():
                widget.update_idletasks()
                widget.destroy()

            # se crea una lista de las carpetas y archivos
            files_n_folders = []
            # se limpia la lista
            files_n_folders.clear()
            # se agregan las carpetas y archivos a la lista
            for folder in get_folders():
                files_n_folders.append(folder)
            for file in get_files():
                files_n_folders.append(file)
            # se ordena la lista de archivos y carpetas segun la extension
            files_n_folders.sort(key=lambda x: x.split(".")[-1])

            disc_extensions = [".mbr", ".img", ".iso"]
            text_extensions = [".txt", ".text"]
            executable_extensions = [".exe", ".bat", ".com", "py", "pyw", "pyc", "pyo", "pys"]
            image_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".tif"]

            # las carpetas y archivos se posicionan siegun el orden de la lista
            for i in range(len(files_n_folders)): # if have a dot in the name is a file
                if files_n_folders[i].find(".") != -1:
                    if files_n_folders[i].endswith(tuple(disc_extensions)):          File(self.File_manager, 160, (i * 25) + 48, files_n_folders[i], "CD")
                    elif files_n_folders[i].endswith(tuple(text_extensions)):        File(self.File_manager, 160, (i * 25) + 48, files_n_folders[i], "Text")
                    elif files_n_folders[i].endswith(tuple(executable_extensions)):  File(self.File_manager, 160, (i * 25) + 48, files_n_folders[i], "Python")
                    elif files_n_folders[i].endswith(tuple(image_extensions)):       File(self.File_manager, 160, (i * 25) + 48, files_n_folders[i], "Image")
                    elif files_n_folders[i].endswith(".torrent"):                    File(self.File_manager, 160, (i * 25) + 48, files_n_folders[i], "Torrent")
                    elif files_n_folders[i].endswith(".log"):                        File(self.File_manager, 160, (i * 25) + 48, files_n_folders[i], "Log")
                    elif files_n_folders[i].endswith(".reg"):                        File(self.File_manager, 160, (i * 25) + 48, files_n_folders[i], "Reg")
                    else:
                        File(self.File_manager, 160, (i * 25) + 48, files_n_folders[i], "Unknown")
                else:
                    Folder(self.File_manager, 160, (i * 25) + 48, files_n_folders[i]) # folder

            def parse_dir_bar(self, value):
                """ Parse the directory bar """

                # remove the / from the value
                value = value[1:]
                change_directory(value)
                render_filesystem(self)

            def update_dir_bar(self):
                """ Clean the directory bar """

                self.dir_bar.delete(0, END)
                self.dir_bar.insert(0, get_current_directory())
                # quit the focus from the dir_bar
                self.File_manager.focus()

            self.dir_bar = Entry(
                self.File_manager,
                bg="#001633",
                fg="#ffffff",
                font=("Consolas", 8),
                borderwidth="0",
                relief="flat",
                insertbackground="#ffffff",
                width=60
            )

            # add the current directory from the file system to the dir_bar
            self.dir_bar.insert(0, get_current_directory())
            self.dir_bar.place(x=160, y=28)

            # on click focus, delete the text
            self.dir_bar.bind("<Button-1>", lambda event: self.dir_bar.delete(0, END))
            # on click outside, put the current directory in the dir_bar
            self.File_manager.bind("<Button-1>", lambda event: update_dir_bar(self))

            self.dir_bar.bind("<Return>", lambda event: parse_dir_bar(self, str(self.dir_bar.get())))

            # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            self.go_button_image = Image.setImage("Assets/Shell/Programs/File manager/Go_arrow.png")

            def go_arrow(self):
                """ Open a folder """

                # render the filesystem
                render_filesystem(self)

            self.go_button = Button(
                self.File_manager,
                width=13,
                height=13,
                image=self.go_button_image,
                activebackground = "#001228",
                borderwidth="0",
                command=lambda: go_arrow(self)
            )

            self.go_button.place(x=548, y=28)

            # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            self.back_button_image = Image.setImage("Assets/Shell/Programs/File manager/Back_arrow.png")


            def back_arrow(self):
                """ Go back to the previous directory """

                # get the current directory
                change_directory("..")
                render_filesystem(self)

            self.back_button = Button(
                self.File_manager,
                width=13,
                height=13,
                image=self.back_button_image,
                activebackground = "#001228",
                borderwidth="0",
                command=lambda: back_arrow(self)
            )

            self.back_button.place(x=532, y=28)


            # ---------------------------------------------------------- Close button ------------------------------------------------------------

            def close_window():
                """
                Close window
                """

                self.File_manager.destroy()

            self.Close_button_image = Image.setImage("Assets/Shell/Window/Close_button.png")
            self.Close_button_red_image = Image.setImage("Assets/Shell/Window/Close_button_red.png")

            self.Close_button = Button(
                self.File_manager,
                bg="#CCCCCC",
                image=self.Close_button_image,
                borderwidth="0",
                relief="flat",
                width="13",
                height="13",
                cursor="hand2",
                command=close_window
            )

            self.Close_button.bind("<Enter>", lambda event: self.Close_button.config(image = self.Close_button_red_image))
            self.Close_button.bind("<Leave>", lambda event: self.Close_button.config(image = self.Close_button_image))

            self.Close_button.place(x=668, y=4)

        render_filesystem(self)

        def Splash_screen(time):
            """Splash screen"""

            self.Splash = Label(
                self.File_manager,
                bg="#002C4F",
                image=self.Splash_image,
                borderwidth="0",
            )

            self.Splash.place(x=0, y=0)

            self.Splash_logo = Label(
                self.Splash,
                image=self.Splash_logo_image,
                borderwidth="0",
            )

            # Put the logo in the middle of the window, .5 is the center of the window
            self.Splash_logo.place(relx=.5, y=170, anchor="center")

            self.Splash.after(time, self.Splash.destroy)

        Splash_screen(5000)

        if self.draggable:
            pass
