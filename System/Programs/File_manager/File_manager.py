from ast import Str
from tkinter import Button, Frame, Label
from System.UI.Attributes.Draggable import drag_it

from System.Utils.Utils import get_image
from System.Core.FileSystem import *

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

        self.image = get_image("Assets/UI/Files/Folder_icon.png", "24x24", "#ff00ff", "#ffffff")
        self.image_selected = get_image("Assets/UI/Files/Folder_icon.png", "24x24", "#ff00ff", "#D6E5FF")

        self.selection_normal = get_image("Assets/UI/Programs/File manager/Selection.png", "null", "#ff00ff", "#ffffff")
        self.selection_selected = get_image("Assets/UI/Programs/File manager/Selection_selected.png", "null", "#ff00ff", "#ffffff")

        self.selection_label = Label(
            self.master,
            bg="#CCCCCC",
            image=self.selection_normal,
            borderwidth="0",
            relief="flat"
        )

        # if the file is selected, change the image
        self.selection_label.bind("<Enter>", lambda event: select_folder(self))
        self.selection_label.bind("<Leave>", lambda event: unselect_folder(self))

        self.Folder = Label(
            self.master,
            bg="#CCCCCC",
            image=self.image,
            borderwidth="0",
            relief="flat",
            cursor="hand2"
        )

        self.name_label = Label(
            self.master,
            text=self.name,
            bg="#ffffff",
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
            self.name_label.config(bg="#D6E5FF")

        def unselect_folder(self):
            """ Unselect the folder """

            self.selection_label.config(image=self.selection_normal)
            self.Folder.config(image=self.image)
            self.name_label.config(bg="#ffffff")


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
        self.file_icon = get_image("Assets/UI/Files/" + icon + "_icon.png", "24x24", "#ff00ff", "#ffffff")
        self.file_icon_selected = get_image("Assets/UI/Files/" + icon + "_icon.png", "24x24", "#ff00ff", "#D6E5FF")

        self.selection_normal = get_image("Assets/UI/Programs/File manager/Selection.png", "null", "#ff00ff", "#ffffff")
        self.selection_selected = get_image("Assets/UI/Programs/File manager/Selection_selected.png", "null", "#ff00ff", "#ffffff")

        self.selection_label = Label(
            self.master,
            bg="#CCCCCC",
            image=self.selection_normal,
            borderwidth="0",
            relief="flat"
        )

        # if the file is selected, change the image
        self.selection_label.bind("<Enter>", lambda event: select_file(self))
        self.selection_label.bind("<Leave>", lambda event: unselect_file(self))

        self.File = Label(
            self.master,
            bg="#CCCCCC",
            image=self.file_icon,
            borderwidth="0",
            relief="flat",
            cursor="hand2"
        )

        self.name_label = Label(
            self.master,
            text=self.name,
            bg="#ffffff",
            font=("Consolas", 8),
            borderwidth="0",
            relief="flat"
        )

        self.name_label.bind("<Enter>", lambda event: select_file(self))
        self.name_label.bind("<Leave>", lambda event: unselect_file(self))

        def select_file(self):
            """ Select the file """

            self.selection_label.config(image=self.selection_selected)
            self.File.config(image=self.file_icon_selected)
            self.name_label.config(bg="#D6E5FF")

        def unselect_file(self):
            """ Unselect the file """

            self.selection_label.config(image=self.selection_normal)
            self.File.config(image=self.file_icon)
            self.name_label.config(bg="#ffffff")


        self.File.place(x=self.x + 1, y=self.y)
        self.name_label.place(x=self.x + 25, y=(self.y) + 4)
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

        self.File_manager_image = get_image("Assets/UI/Programs/File manager/Window.png")  # File manager image base
        self.Splash_logo_image = get_image("Assets/UI/Programs/File manager/File_manager_icon.png", "112x112", "#ff00ff", "#002C4F")  # Splash image
        self.Splash_image = get_image("Assets/UI/Programs/File manager/Splash.png")  # Splash image

        self.File_manager = Label(
            self.master,
            bg="#CCCCCC",
            image=self.File_manager_image,
            borderwidth="0"
        )

        self.File_manager.place(relx=.2, y=128)

        # se crea una lista de las carpetas y archivos
        files_n_folders = []
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
                if files_n_folders[i].endswith(tuple(disc_extensions)):          File(self.File_manager, 160, (i * 25) + 42, files_n_folders[i], "CD")
                elif files_n_folders[i].endswith(tuple(text_extensions)):        File(self.File_manager, 160, (i * 25) + 42, files_n_folders[i], "Text")
                elif files_n_folders[i].endswith(tuple(executable_extensions)):  File(self.File_manager, 160, (i * 25) + 42, files_n_folders[i], "Python")
                elif files_n_folders[i].endswith(tuple(image_extensions)):       File(self.File_manager, 160, (i * 25) + 42, files_n_folders[i], "Image")
                elif files_n_folders[i].endswith(".torrent"):                    File(self.File_manager, 160, (i * 25) + 42, files_n_folders[i], "Torrent")
                elif files_n_folders[i].endswith(".log"):                        File(self.File_manager, 160, (i * 25) + 42, files_n_folders[i], "Log")
                else:
                    File(self.File_manager, 160, (i * 25) + 42, files_n_folders[i], "Unknown")
            else:
                Folder(self.File_manager, 160, (i * 25) + 42, files_n_folders[i]) # folder


        # ---------------------------------------------------------- Close button ------------------------------------------------------------

        def close_window():
            """
            Close window
            """

            self.File_manager.destroy()

        self.Close_button_image = get_image("Assets/UI/Window/Close_button.png")
        self.Close_button_red_image = get_image("Assets/UI/Window/Close_button_red.png")

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
            drag_it(self.File_manager)
