import tkinter as tk
import time
from tkinter import *


"""
==========================================================
 OS.py 

 The main class where the first functions are executed

==========================================================
"""


# Universal variables 
__author__ = 'TheBigEye'


Os = tk.Tk()
Os.title("PythonOS")
Os.iconbitmap('Assets\Images\icon.ico')


Os.geometry("1024x600")
Os.resizable(0, 0)
Os.configure(background="#000000")

# Local variables 
Kernel = 3  

Load = 0

Booted = False  
Logined = False 
In_Login = False
In_Desktop = False

# The boot order is chain (which means that the system [According to the kernel variable, which represents the different levels] starts the processes one after the other) is still in the testing phase since this needs a lot of logic

# System variables (for now they will be basic variables until something similar to control over the hardware is implemented)

Is_FAIL = False

Is_in_BIOS = False
Is_in_INSTALLER = False
Is_in_Boot = False
Is_in_Login = False
Is_in_Desktop = False


# In case the variable "Kernel" in Os.py has a value between 0 and 5:
if (Kernel == 0):

    Is_FAIL = True

elif (Kernel == 1):

    Is_in_BIOS = True

elif (Kernel == 2):

    Is_in_INSTALLER = True

elif (Kernel == 3):

    Is_in_Boot = True    

elif (Kernel == 4):

    Is_in_Login = True  

elif (Kernel == 5):

    Is_in_Desktop = True    

# ------------------------------------------------------------------[ Boot ]------------------------------------------------------------------------- #


"""
  ----------------------[ Boot ]-----------------------  
  This function simulates the Boot screen of an OS       
  (As with a real one, the functions and variables       
  are loaded while the screen operates)                  
                                                         
  For now it is that simple, in the future I will        
  add a BIOS screen in case they find important          
  variables                                              
                                                         
  -----------------------------------------------------   
"""

if Is_in_Boot == True :

    # Boot logo
    Logon_image = tk.PhotoImage(file="Assets/logon.png")
    BootLogo = tk.Label(Os, image=Logon_image, borderwidth=0.1)
    BootLogo.place(x=400, y=160)


    # Loading animation
    frameCnt = 60
    frames = [
        PhotoImage(file="Assets\Loading.gif", format="gif -index %i" % (i))
        for i in range(frameCnt)
    ]


    def update(ind):

        global Booted, Load

        Load += 1
        #print(Load)
        #print(Booted)

        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        loading.configure(image=frame)
        Os.after(50, update, ind)


    loading = Label(Os, borderwidth=0.1)
    loading.place(x=480, y=400)

    Os.after(1, update, 0)


if Is_in_Boot == True :
    print("Booting!...")

# -----------------------------------------------------------------[ Login ]------------------------------------------------------------------------- #


"""
  ----------------------[ Login ]----------------------  
  Create the login interface once the Boot is
  finished, it is not necessary to put a password
  since for now it will be simple and unsafe XD
  just press the button ._.                                          
                                                         
  -----------------------------------------------------  
"""  


   
# Login
Login_GUI_Image = tk.PhotoImage(file="Assets/GUI/Login.png")
Login = Label(Os, image=Login_GUI_Image, borderwidth=0.1)
Login.place(x=0, y=1000)

# Login entry (Password)
Login_Password_Entry = Entry(
    Login, 
    show= "-",
    borderwidth= 0.1,
    width= 20,
    fg= "White",
    bg="#5A7EFC",
    font= ("Segou UI", 10)
    )

Login_Password_Entry.config(insertbackground="White")
Login_Password_Entry.insert(0,"Password")
Login_Password_Entry.place(x= 0, y= 1000)


Login_Button_icon = tk.PhotoImage(file="Assets/Buttons/Login_Button.png")
Login_Button = Button(
    Login,
    width=30,
    height=19,
    borderwidth="0",
    relief="raised",
    bg="#080D11",
    image=Login_Button_icon,
    #command=Open_FileManager,
    ) 
Login_Button.place(x=0, y=1000)  

def Login_screen():
    global Booted, Is_in_Login

    print("Finished!")
    
    Os.configure(background="#000000")

    BootLogo.place(x=400, y=1000)
    loading.place(x=480, y=1000)

    Os.configure(background="#050505")
    Os.configure(background="#477afb")

    #Booted = True
    Is_in_Login = True

    if Is_in_Login == True:
        print("Entering to login screen!...")

    Login.place(x=0, y=0)
    Login_Password_Entry.place(x= 435, y= 344)
    Login_Button.place(x=495, y=384)  


Os.after(15000, Login_screen)  



Os.mainloop()
