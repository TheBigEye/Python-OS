import os
from tkinter import Entry, Label, Button, PhotoImage, Text, Tk
from tkinter.constants import END, INSERT
import time
import random

from System.GUI.Attributes.Draggable import make_draggable

__author__ = 'TheBigEye'
__version__ = '1.0'


def Display_Terminal(master, draggable = False):


    global Terminal_GUI_Image, Close_Terminal_image, Maximize_Terminal_image, Minimize_Terminal_image
    global Terminal, Terminal_screen, Terminal_entry, Close_Terminal_Button, Maximize_Terminal_Button, Minimize_Terminal_Button
    global Close_Terminal, cmd

    Terminal_GUI_Image = PhotoImage(file = "Assets/GUI/Terminal/Terminal.png") # Terminal image base
    Close_Terminal_image = PhotoImage(file = "Assets/GUI/Terminal/Close_Terminal_Button.png") # Terminal close button
    Maximize_Terminal_image = PhotoImage(file = "Assets/GUI/Terminal/Maximize_Terminal_Button.png") # Terminal close button
    Minimize_Terminal_image = PhotoImage(file = "Assets/GUI/Terminal/Minimize_Terminal_Button.png") # Terminal close button

    Terminal = Label(
        master,
        bg= "#CCCCCC",
        image=Terminal_GUI_Image,
        borderwidth="0",
    )

    Terminal_screen = Text(
        Terminal,
        bd=2,
        relief='flat',
        font=('Consolas', 10),
        undo=True,
        wrap='word',
    )

    Terminal_screen.config(width=75, height=20, bg="#000000", fg= "#dfdfdf", state= 'normal', insertbackground='#dfdfdf')
    Terminal_screen.insert(INSERT , "Welcome to the terminal --------------------------------------------------" + "\n\n" + ">/" + "\n")
    Terminal_screen.focus()

    def Close_Terminal():
        """Close the Terminal"""

        Terminal.place_forget()

    Close_Terminal_Button = Button(
        Terminal,
        width=8,
        height=8,
        bg="#CCCCCC",
        image=Close_Terminal_image,
        borderwidth="0",
        command=Close_Terminal,
    )

    Maximize_Terminal_Button = Button(
        Terminal,
        width=8,
        height=8,
        bg="#CCCCCC",
        image=Maximize_Terminal_image,
        borderwidth="0",
        command=Close_Terminal,
    )

    Minimize_Terminal_Button = Button(
        Terminal,
        width=8,
        height=8,
        bg="#CCCCCC",
        image=Minimize_Terminal_image,
        borderwidth="0",
        command=Close_Terminal,
    )


    def cmd(event):
        """Execute a command"""

        # could execute python functions, such as: print("something")
        # or could execute system commands, such as: os.system("ls")

        command = Terminal_entry.get()
        Terminal_entry.delete(0, END)


         # print command, typing it into terminal_entry and hitting enter should print the set string, like: print("hello") , > Hello.
        def print_command(command):
            """Print command"""

            #Terminal_screen.insert(INSERT, command + "\n")
            Terminal_screen.see(END)

        if command.startswith("print"):
            print_command(command)


        # add command is a special command that will add the numbers in the command together, like: add(1,2,3,4,5) , > 15.
        def add_command(command):
            """Sum command"""

            command = command.replace("add(", "")
            command = command.replace(")", "")
            command = command.split(",")
            add = 0
            for number in command:
                add += int(number)
            Terminal_screen.insert(INSERT, add)
            Terminal_screen.see(END)

        if command.startswith("add("):
            add_command(command)


        # subtract command is a special command that will subtract the numbers in the command together, like: rest(1,2,3,4,5) , > -14.
        def subtract_command(command):
            """Rest command"""

            command = command.replace("subtract(", "")
            command = command.replace(")", "")
            command = command.split(",")
            subtract = 0
            for number in command:
                subtract -= int(number)
            Terminal_screen.insert(INSERT, subtract)
            Terminal_screen.see(END)

        if command.startswith("subtract("):
            subtract_command(command)


        # multiply command is a special command that will multiply the numbers in the command together, like: multiply(1,2,3,4,5) , > 120.
        def multiply_command(command):
            """Multiply command"""

            command = command.replace("multiply(", "")
            command = command.replace(")", "")
            command = command.split(",")
            multiply = 1
            for number in command:
                multiply *= int(number)
            Terminal_screen.insert(INSERT, multiply)
            Terminal_screen.see(END)

        if command.startswith("multiply("):
            multiply_command(command)


        # divide command is a special command that will divide the numbers, like: divide(number_to_divide, number_by_which_it_is_divided) , > result, like: divide(10,2) , > 5.
        def divide_command(command):
            """Divide command"""

            command = command.replace("divide(", "")
            command = command.replace(")", "")
            command = command.split(",")
            divide = int(command[0]) / int(command[1])
            Terminal_screen.insert(INSERT, divide)
            Terminal_screen.see(END)

        if command.startswith("divide("):
            divide_command(command)
                

        # clear command will clear the terminal, like: clear() , > .
        def clear_command():
            """Clear command"""

            Terminal_screen.delete(1.0, END)

        if command.startswith("clear()"):
            clear_command()


        # help command will print the help menu, like: help() , > help.
        def help_command():
            """Help command"""

            Terminal_screen.insert(INSERT, "help()\n")
            Terminal_screen.insert(INSERT, "sum(number1, number2, number3, ...)\n")
            Terminal_screen.insert(INSERT, "clear()\n")
            Terminal_screen.insert(INSERT, "exit()\n")
            Terminal_screen.see(END)

        if command.startswith("help()"):
            help_command()


        # exit command will exit the terminal, like: exit() , > .
        def exit_command():
            """Exit command"""

            Terminal.destroy()

        if command.startswith("exit()"):
            exit_command()


        # print command output, like: print("something") , > something.
        if command.startswith("print("):
            command = command.replace("print(", "")
            command = command.replace(")", "")
            Terminal_screen.insert(INSERT, command)
            Terminal_screen.see(END)

        
        # var command will create a variable, like: var(name, value) , > .
        def var_command(command):
            """Var command"""

            command = command.replace("var(", "")
            command = command.replace(")", "")
            command = command.split(",")
            var_name = command[0]
            var_value = command[1]
            globals()[var_name] = var_value
            Terminal_screen.insert(INSERT, var_name + " = " + var_value + "\n")
            Terminal_screen.see(END)

        if command.startswith("var("):
            var_command(command)

        # clear var command will clear the value of a variable, like: clear(var_name) , > .
        def clear_var_command(command):
            """Clear var command"""

            command = command.replace("clear(", "")
            command = command.replace(")", "")
            globals()[command] = ""
            Terminal_screen.insert(INSERT, command + " = " + "\n")
            Terminal_screen.see(END)

        if command.startswith("clear("):
            clear_var_command(command)


        # if command will check if a condition is true, like: if(condition) , > .
        def if_command(command):
            """If command"""

            command = command.replace("if(", "")
            command = command.replace(")", "")
            if eval(command):
                Terminal_screen.insert(INSERT, "True\n")
                Terminal_screen.see(END)
            else:
                Terminal_screen.insert(INSERT, "False\n")
                Terminal_screen.see(END)

        if command.startswith("if("):
            if_command(command)


        # while command will check if a condition is true, like: while(condition) , > .
        def while_command(command):
            """While command"""

            command = command.replace("while(", "")
            command = command.replace(")", "")
            while eval(command):
                Terminal_screen.insert(INSERT, "True\n")
                Terminal_screen.see(END)

        if command.startswith("while("):
            while_command(command)

        
        # repeat command will repeat a command a number of times, like: repeat(command(args), number) , > .
        def repeat_command(command):
            """Repeat command"""

            command = command.replace("repeat(", "")
            command = command.replace(")", "")
            command = command.split(",")
            repeat_command = command[0]
            repeat_number = command[1]
            for i in range(int(repeat_number)):
                Terminal_screen.insert(INSERT, repeat_command + "\n")
                Terminal_screen.see(END)

        if command.startswith("repeat("):
            repeat_command(command)

        
        # delay command will delay the terminal for a number of seconds, like: delay(number) , > .
        def delay_command(command):
            """Delay command"""

            command = command.replace("delay(", "")
            command = command.replace(")", "")
            time.sleep(int(command))
            Terminal_screen.insert(INSERT, "Delay " + command + " seconds\n")
            Terminal_screen.see(END)

        if command.startswith("delay("):
            delay_command(command)

        
        # random command will generate a random number, like: random(number) , > random number.
        def random_command(command):
            """Random command"""

            command = command.replace("random(", "")
            command = command.replace(")", "")
            random_number = random.randint(0, int(command))
            Terminal_screen.insert(INSERT, random_number)
            Terminal_screen.see(END)

        if command.startswith("random("):
            random_command(command)

        
        # print_var_value command will print the value of a variable, like: print_var_value(var_name) , > var_name = value.
        def print_var_value_command(command):
            """Print var value command"""

            command = command.replace("print_var_value(", "")
            command = command.replace(")", "")
            Terminal_screen.insert(INSERT, command + " = " + str(globals()[command]) + "\n")
            Terminal_screen.see(END)

        if command.startswith("print_var_value("):  
            print_var_value_command(command)

        
        # time command will print the current time, like: time() , > time.
        def time_command():
            """Time command"""

            Terminal_screen.insert(INSERT, time.strftime("%H:%M:%S", time.localtime()))
            Terminal_screen.see(END)

        if command.startswith("time()"):
            time_command()


        # python interpreter,(using eval and exec) When executing this command, python commands can be putted through Terminal_entry and executed there as if it were a real terminal and print in Terminal_screen the command result.
        if command.startswith(">>> "):
            command = command.replace(">>> ", "")
            command = command.replace("", "")
            command = command.replace("", "")
            Terminal_screen.insert(INSERT, command + "\n")
            Terminal_screen.see(END)
            try:
                exec(command)
            except Exception as e:
                Terminal_screen.insert(INSERT, str(e) + "\n")
                Terminal_screen.see(END)





        # if the command is not recognized, print an error message.



    Terminal_entry = Entry(
        Terminal,
        width=75,
        #height=4,
        borderwidth = "0",
        fg='white',
        bg = "#000000",
        font=('Consolas', 10),
    )

    Terminal_entry.config(insertbackground='white')
    Terminal_entry.bind('<Return>', cmd)



    if (draggable == True):

        make_draggable(Terminal)

    Terminal.place(x= 225, y= 148)
    Terminal_screen.place(x=3.5, y=25.5)

    Close_Terminal_Button.place(x=520, y=8)
    Maximize_Terminal_Button.place(x=490, y=8)
    Minimize_Terminal_Button.place(x=460, y=8)
    Terminal_entry.place(x=4.5, y=330)

    # pressing enter will execute a command if the user input matches them.


        
        


 
# EXAMPLE TEST  #d ef main():
#   root = Tk()
#   Display_Terminal(root)
##   root.mainloop() 

#main()