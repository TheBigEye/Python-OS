
__author__ = 'TheBigEye'
__version__ = '1.0'

def CMD(entry, output):

    """
    Summary:
    --------
        This function is used to execute a command, get the output, and return the output.
        - Can execute a command with or without arguments.
        - Can execute python commands  (e.g. ">>>  python3 -V")
        - Have owns functions and commands (e.g. "subtract(10, 20)", repeat(print("Hello"), 10) )

    Parameters:
    ----------- 
        entry: str
            The command to be executed. (For better understanding, it can also be a tkinter widget that has input, like Entry)
        output: str
            The output of the command. (or the widget where it will print the output of the data)

    Returns:
    --------
        output: str
            The output of the command.

    Example:
    --------
        CMD("ls", output) or, CMD(Entry_widget, Output_widget)
                
    """
    
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    import os
    from tkinter.constants import END, INSERT
    import time
    import random

    """Execute a command"""

    # could execute python functions, such as: print("something")
    # or could execute system commands, such as: os.system("ls")

    command = entry.get()
    entry.delete(0, END)

    # Commands ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # print command, typing it into terminal_entry and hitting enter should print the set string, like: print("hello") , > Hello.
    def print_command(command):
        """Print command"""

        # Terminal_screen.insert(INSERT, command + "\n")
        output.see(END)

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
        output.insert(INSERT, add)
        output.insert(INSERT, "\n")
        output.see(END)

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
        output.insert(INSERT, subtract)
        output.insert(INSERT, "\n")
        output.see(END)

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
        output.insert(INSERT, multiply)
        output.insert(INSERT, "\n")
        output.see(END)

    if command.startswith("multiply("):
        multiply_command(command)


    # divide command is a special command that will divide the numbers, like: divide(number_to_divide, number_by_which_it_is_divided) , > result, like: divide(10,2) , > 5.
    def divide_command(command):
        """Divide command"""

        command = command.replace("divide(", "")
        command = command.replace(")", "")
        command = command.split(",")
        divide = int(command[0]) / int(command[1])
        output.insert(INSERT, divide)
        output.insert(INSERT, "\n")
        output.see(END)

    if command.startswith("divide("):
        divide_command(command)



    # clear command will clear the terminal, like: clear() , > .
    def clear_command():
        """Clear command"""

        output.delete(1.0, END)

    if command.startswith("clear()"):
        clear_command()


    # exit command will exit the terminal, like: exit() , > .
    def exit_command():
        """Exit command"""

        output.destroy()

    if command.startswith("exit()"):
        exit_command()


    # print command output, like: print("something") , > something.
    if command.startswith("print("):
        command = command.replace("print(", "")
        command = command.replace(")", "")
        output.insert(INSERT, command)
        output.see(END)
    # var command will create a variable, like: var(name, value) , > .
    def var_command(command):
        """Var command"""

        command = command.replace("var(", "")
        command = command.replace(")", "")
        command = command.split(",")
        var_name = command[0]
        var_value = command[1]
        globals()[var_name] = var_value
        output.insert(INSERT, var_name + " = " + var_value + "\n")
        output.see(END)

    if command.startswith("var("):
        var_command(command)


    # clear var command will clear the value of a variable, like: clear(var_name) , > .
    def clear_var_command(command):
        """Clear var command"""

        command = command.replace("clear_var(", "")
        command = command.replace(")", "")
        globals()[command] = ""
        output.insert(INSERT, command + " = " + "\n")
        output.see(END)

    if command.startswith("clear_var("):
        clear_var_command(command)


    # if command will check if a condition is true, like: if(condition) , > .
    def if_command(command):
        """If command"""

        command = command.replace("if(", "")
        command = command.replace(")", "")
        if eval(command):
            output.insert(INSERT, "True" + "\n")
            output.see(END)
        else:
            output.insert(INSERT, "False" + "\n")
            output.see(END)

    if command.startswith("if("):
        if_command(command)


    # while command will check if a condition is true, like: while(condition) , > .
    def while_command(command):
        """While command"""

        command = command.replace("while(", "")
        command = command.replace(")", "")
        while eval(command):
            output.insert(INSERT, "True" + "\n")
            output.see(END)

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
            output.insert(INSERT, repeat_command + "\n")
            output.see(END)

    if command.startswith("repeat("):
        repeat_command(command)


    # delay command will delay the terminal for a number of seconds, like: delay(number) , > .
    def delay_command(command):
        """Delay command"""

        command = command.replace("delay(", "")
        command = command.replace(")", "")
        time.sleep(int(command))
        output.insert(INSERT, "Delay " + command + " seconds" + "\n")
        output.see(END)

    if command.startswith("delay("):
        delay_command(command)


    # random command will generate a random number, like: random(number) , > random number.
    def random_command(command):
        """Random command"""

        command = command.replace("random(", "")
        command = command.replace(")", "")
        random_number = random.randint(1, int(command))
        output.insert(INSERT, random_number)
        output.insert(INSERT, "\n")
        output.see(END)

    if command.startswith("random("):
        random_command(command)


    # print_var_value command will print the value of a variable, like: print_var_value(var_name) , > var_name = value.
    def print_var_value_command(command):
        """Print var value command"""

        command = command.replace("print_var_value(", "")
        command = command.replace(")", "")
        output.insert(INSERT, command + " = " + str(globals()[command]) + "\n")
        output.see(END)

    if command.startswith("print_var_value("):
        print_var_value_command(command)
        

    # time command will print the current time, like: time() , > time.
    def time_command():
        """Time command"""

        output.insert(INSERT, time.strftime("%H:%M:%S", time.localtime()) + "\n")
        output.see(END)

    if command.startswith("time()"):
        time_command()

    if command.startswith(">>> "):
        command = command.replace(">>> ", "")
        command = command.replace("", "")
        command = command.replace("", "")

    # if command is empty, will print a new line.
    if command == "":
        output.insert(INSERT, ">>> " + "\n")
        output.see(END)

        # if command is not empty, will print the command in Terminal_screen and execute it.
    else:
        output.insert(INSERT, ">>> " + command + "\n")
        output.see(END)
            
        try:
            # Execute the command and use the variables
            exec(command, globals())
            
        except Exception as error:
            output.insert(INSERT, str(error) + "\n")
            output.see(END)


    # dir command will print the directory of the current file, like: dir() , > dir.
    def dir_command():
        """Dir command"""

        output.insert(INSERT, os.getcwd() + "\n")
        output.see(END)

    if command.startswith("dir()"):
        dir_command()

        
    # cd command will change the current directory, like: cd(directory) , > , or cd.. to go back one directory.
    def cd_command(command):
        """Cd command"""

        command = command.replace("cd(", "")
        command = command.replace(")", "")

        if command == "..":
            os.chdir(os.path.dirname(os.getcwd()))
        else:
            os.chdir(command)

        output.insert(INSERT, os.getcwd() + "\n")
        output.see(END)

    if command.startswith("cd("):
        cd_command(command)

    # Tree command will print the directory tree of the current file, like: tree() , > tree.
    def tree_command():
        """Tree command"""

        output.insert(INSERT, "Directory tree: " + "\n")
        output.see(END)
        for root, dirs, files in os.walk("."):
            level = root.replace(".", "")
            output.insert(INSERT, level + "\n")
            output.see(END)

    if command.startswith("tree()"):
        tree_command()

    # help command will print the help menu, like: help() , > help - description.
    def help_command():
        """Help command"""

        output.insert(INSERT, "Terminal help menu" + "\n")
        output.insert(INSERT, "clear(var_name) - clear the value of a variable" + "\n")
        output.insert(INSERT, "if(condition) - check if a condition is true" + "\n")
        output.insert(INSERT, "while(condition) - check if a condition is true and repeat the command" + "\n")
        output.insert(INSERT, "repeat(command(args), number) - repeat a command a number of times" + "\n")
        output.insert(INSERT, "delay(number) - delay the terminal for a number of seconds" + "\n")
        output.insert(INSERT, "random(number) - generate a random number" + "\n")
        output.insert(INSERT, "print_var_value(var_name) - print the value of a variable" + "\n")
        output.insert(INSERT, "time() - print the current time" + "\n")
        output.insert(INSERT, "dir() - print the directory of the current file" + "\n")
        output.insert(INSERT, "cd(directory) - change the current directory" + "\n")
        output.insert(INSERT, ">>> python_command - execute a python command" + "\n")
        output.see(END)

    if command.startswith("help()"):
        help_command()
    
    