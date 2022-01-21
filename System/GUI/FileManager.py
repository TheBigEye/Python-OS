from tkinter import Label, Button, PhotoImage
from System.GUI.Attributes.Draggable import make_draggable
from System.Utils.Utils import get_asset
from System.Utils.Vars import Assets_dir

__author__ = 'Nahuel senek'
__version__ = '1.1'

def Display_FileManager(master, tab: str, draggable: bool = False):

    # Documentation ---------------------------------------------------------------------------------------------------------------

    """
    Create and display the File manager.

    Parameters
    ----------
    `master` : string
        The parent where the File manager will be placed.

    `tab` : string
        The tab that the File manager will display when it appears on the screen, `This PC`, `Desktop`, `Documents`, etc...

    `draggable` : boolean
        Specifies whether or not the File manager can be moved with the mouse., by default False

    """

    # FileManager global variables ------------------------------------------------------------------------------------------------
    global FileManager_GUI_Image, Close_FileManager_image, Navigation_Pane_Image, Control_Pane_Image # Images
    global Window_bg # Colors
    global FileManager, Close_FileManager, Close_FileManager_Button, List, Control_pane, Navigation_pane # Functions

    global List_Pane_Image, List_Desktop_Image, List_Documents_Image, List_Downloads_Image
    global This_PC_list, Desktop_list, Documents_list, Downloads_list

    global This_PC_button_image, Desktop_button_image, Documents_button_image, Downloads_button_image
    global This_PC_button, Desktop_button, Documents_button, Downloads_button

    # Explorador de archivos ----------------------------------------------------------------------------------------------------------------

    # Botones
    This_PC_button_image = get_asset("Assets/GUI/File manager/This_PC_unselected.png")
    Desktop_button_image = get_asset("Assets/GUI/File manager/Desktop_unselected.png")
    Documents_button_image = get_asset("Assets/GUI/File manager/Documents_unselected.png")
    Downloads_button_image = get_asset("Assets/GUI/File manager/Downloads_unselected.png")

    # Componentes de la ventana
    FileManager_GUI_Image = get_asset("Assets/GUI/File manager/FileManager.png") # FileManager image base
    List_Pane_Image = get_asset("Assets/GUI/File manager/List_pane.png") # Files and folder list
    List_Desktop_Image = get_asset("Assets/GUI/File manager/List_Desktop_pane.png") # Desktop files list
    List_Documents_Image = get_asset("Assets/GUI/File manager/List_Documents_pane.png") # Documents file list
    List_Downloads_Image = get_asset("Assets/GUI/File manager/List_Downloads_pane.png") # Downloads file list
    Control_Pane_Image = get_asset("Assets/GUI/File manager/Control_pane.png") # Window control pane (- [] X)
    Navigation_Pane_Image = get_asset("Assets/GUI/File manager/Navigation_pane.png") # Navigation pane
    Close_FileManager_image = get_asset("Assets/Buttons/Close_white.png") # Window close button


    Window_bg = "#000000"

    FileManager = Label(
        master,
        bg= "white",
        image=FileManager_GUI_Image,
        borderwidth="0",
    )

    def Close_FileManager():
        """Close the FileManager"""

        FileManager.place_forget()


    if (draggable == True):

        make_draggable(FileManager)

    Control_pane = Label(
        FileManager,
        width=94,
        height=24,
        bg= Window_bg,
        image=Control_Pane_Image,
        borderwidth="0",
    )

    Navigation_pane = Label(
        FileManager,
        width=151,
        height=374,
        bg= "#212121",
        image=Navigation_Pane_Image,
        borderwidth="0",
    )

    Close_FileManager_Button = Button(
        Control_pane,
        width=10,
        height=10,
        bg="red",
        image=Close_FileManager_image,
        borderwidth="0",
        command=Close_FileManager,
    )

    FileManager.place(x= 225, y= 148)
    Control_pane.place(x= 593, y= 0)
    Navigation_pane.place(x= 0, y= 0)

    Close_FileManager_Button.place(x=73, y=7)


    def List(parent, img):

        global List_pane

        List_pane = Label(
            parent,
            width=536,
            height=350,
            bg= Window_bg,
            image=img,
            borderwidth="0",
        )
        List_pane.place(x= 151, y= 24)



# Functions -------------------------------------------------------------------------------------------------------------------

    def This_PC_list():

        List(FileManager, List_Pane_Image)

    def Desktop_list():

        List(FileManager, List_Desktop_Image)

    def Documents_list():

        List(FileManager, List_Documents_Image)

    def Downloads_list():

        List(FileManager, List_Downloads_Image)


# When init -------------------------------------------------------------------------------------------------------------------

    if (tab == "This PC"):
        This_PC_list()

    elif (tab == "Desktop"):
        Desktop_list()

    elif (tab == "Documents"):
        Documents_list()

    elif (tab == "Downloads"):
        Downloads_list()

# Tabs ------------------------------------------------------------------------------------------------------------------------

    This_PC_button = Button(
        Navigation_pane,
        width=144,
        height=20,
        bg = "#212121",
        relief="raised",
        borderwidth="0",
        image=This_PC_button_image,
        command= This_PC_list
    )


    Desktop_button = Button(
        Navigation_pane,
        width=144,
        height=20,
        borderwidth="0",
        image=Desktop_button_image,
        command= Desktop_list
    )


    Documents_button = Button(
        Navigation_pane,
        width=144,
        height=20,
        borderwidth="0",
        image=Documents_button_image,
        command= Documents_list
    )


    Downloads_button = Button(
        Navigation_pane,
        width=144,
        height=20,
        borderwidth="0",
        image=Downloads_button_image,
        command= Downloads_list
    )

    This_PC_button.place(x= 3, y= 144)
    Desktop_button.place(x= 3, y= 168)
    Documents_button.place(x= 3, y= 192)
    Downloads_button.place(x= 3, y= 216)