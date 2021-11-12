
__author__ = 'TheBigEye'
__version__ = '1.0'

def CMD(master, entry, output):

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

    # print command output, like: print("something") , > something.
    def print_command():

        if "(" in command and ")" in command:
            if "\"" in command:
                output.insert(INSERT, eval(command.replace("print(", "").replace(")", "")) + "\n")

            else:
                output.insert(INSERT, "Error: Quotation marks are needed." + "\n")
                
        else:
            output.insert(INSERT, "Error: brackets are needed" + "\n")

    if command.startswith("print("):
        print_command()


    # add command is a special command that will add the numbers in the command together, like: add(1,2,3,4,5) , > 15, also can be used to add strings, like: add("hello", "world") , > helloworld, or add variables, like: add(a, b) , > a+b.
    def add_command(command):
        """Add command"""

        # check if the command has brackets
        if "(" in command and ")" in command:

            # add strings, like: add("hello", "world") , > helloworld., or, like: add("hi", "this", "is", "a", "big", "text") , > hi this is a big text.
            if "\"" in command:
                command = command.replace("add(", "").replace(")", "")
                command = command.replace("\"", "")
                command = command.split(",")
                for word in command:
                    output.insert(INSERT, str(word) + "")
                output.insert(INSERT, "\n")

            else:
                # add numbers. like: add(1,2), > 3, or add(1,2,3,4,5) , > 15.
                command = command.replace("add(", "").replace(")", "")
                command = command.split(",")
                add = 0
                for number in command:
                    add += int(number)
                output.insert(INSERT, add)
                output.insert(INSERT, "\n")
                output.see(END)

        else:
            # if the command doesn't have brackets, the command is invalid
            output.insert(INSERT, "Error: doesn't have brackets" + "\n")
        
    if command.startswith("add("):
        add_command(command)


    # subtract command is a special command that will subtract the numbers in the command together, like: rest(1,2,3,4,5) , > -14.
    def sub_command(command):
        """Rest command"""

        command = command.replace("sub(", "")
        command = command.replace(")", "")
        command = command.split(",")
        sub = 0
        for number in command:
            sub -= int(number)
        output.insert(INSERT, sub)
        output.insert(INSERT, "\n")
        output.see(END)

    if command.startswith("sub("):
        sub_command(command)

        
    # multiply command is a special command that will multiply the numbers in the command together, like: multiply(1,2,3,4,5) , > 120.
    def mul_command(command):
        """Multiply command"""

        command = command.replace("mul(", "")
        command = command.replace(")", "")
        command = command.split(",")
        mul = 1
        for number in command:
            mul *= int(number)
        output.insert(INSERT, mul)
        output.insert(INSERT, "\n")
        output.see(END)

    if command.startswith("mul("):
        mul_command(command)


    # divide command is a special command that will divide the numbers, like: divide(number_to_divide, number_by_which_it_is_divided) , > result, like: divide(10,2) , > 5.
    def div_command(command):
        """Divide command"""

        command = command.replace("div(", "")
        command = command.replace(")", "")
        command = command.split(",")
        div = int(command[0]) / int(command[1])
        output.insert(INSERT, div)
        output.insert(INSERT, "\n")
        output.see(END)

    if command.startswith("div("):
        div_command(command)


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

    # print_value command will print the value of one or more variables, like: print_value(name) , > value, or print_value(name1, name2, name3) , > value1, value2, value3.
    def print_value_command(command):
        """Print value command"""

        command = command.replace("print_value(", "")
        command = command.replace(")", "")
        command = command.split(",")
        for name in command:
            output.insert(INSERT, str(globals()[name]) + "\n")
        output.see(END)

    if command.startswith("print_value("):
        print_value_command(command)

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
        

# -------------------------------------------------------------------------------------------------------------------------------------------------

    # clear command will clear the terminal, like: clear() , > .
    def clear_command():
        """Clear command"""

        output.delete(1.0, END)

    if command.startswith("clear") or command.startswith("cls"):
        clear_command()


    # time command will print the current time, like: time() , > time.
    def time_command():
        """Time command"""

        output.insert(INSERT, time.strftime("%H:%M:%S", time.localtime()) + "\n")
        output.see(END)

    if command.startswith("time"):
        time_command()


    # exit command will exit the terminal, like: exit() , > .
    def exit_command():
        """Exit command"""

        master.destroy()
        

    if command.startswith("exit"):
        exit_command()


# -------------------------------------------------------------------------------------------------------------------------------------------------

    def python_command(command):

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

    if command.startswith(">>> "):
        python_command(command)


# -------------------------------------------------------------------------------------------------------------------------------------------------

 
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


    # mkfolder command will create a new folder, like: mkfolder(folder_name) , > .
    def mkfolder_command(command):

        from System.Core.Core import Create_folder, Save_FileSystem

        command = command.replace("mkfolder(", "")
        command = command.replace(")", "")
        Create_folder(command)
        Save_FileSystem()
        output.insert(INSERT, "Folder " + command + " created" + "\n")
        output.see(END)
    
    if command.startswith("mkfolder("):
        mkfolder_command(command)
    
    
    # mkfile command will create a new file, like: mkfile(file_name, content) , > .
    # the content is optional, if not given, will create an empty file.
    def mkfile_command(command):

        from System.Core.Core import Create_file, Save_FileSystem, Move_file

        command = command.replace("mkfile(", "")
        command = command.replace(")", "")
        command = command.split(",")
        file_name = command[0]
        extension = command[1]    
        content = command[2]
        Create_file(file_name, extension, content)  
        Save_FileSystem()
        output.insert(INSERT, "File " + file_name + "." + extension + " created" + "\n")
        output.see(END)


        
    if command.startswith("mkfile("):
        mkfile_command(command)

    
    # move_file command will move a file, like: move_file(file_name, extension, folder_name) , > .
    def move_file_command(command):

        from System.Core.Core import Move_file, Save_FileSystem

        command = command.replace("move_file(", "")
        command = command.replace(")", "")
        command = command.split(", ")
        file_name = command[0]
        extension = command[1]
        folder_name = command[2]
        Move_file(file_name, extension, folder_name)
        Save_FileSystem()

        if file_name == "Index" and extension == "pfs":
            output.insert(INSERT, "It is not possible to move file " + file_name + "." + extension + "\n")

        else:
            output.insert(INSERT, "File " + file_name + "." + extension + " moved to " + folder_name + "\n")

        Save_FileSystem()
        output.see(END)

    if command.startswith("move_file("):
        move_file_command(command)

    
    # delete_file command will delete a file, like: delete_file(file_name, extension) , > .
    def delete_file_command(command):

        from System.Core.Core import Delete_file, Save_FileSystem

        command = command.replace("delete_file(", "")
        command = command.replace(")", "")
        command = command.split(", ")
        file_name = command[0]
        extension = command[1]
        Delete_file(file_name, extension)
        Save_FileSystem()
        output.insert(INSERT, "File " + file_name + extension + " deleted" + "\n")
        output.see(END)

    if command.startswith("delete_file("):
        delete_file_command(command)

    
    def rename_file_command(command):

        from System.Core.Core import Rename_file, Save_FileSystem

        command = command.replace("rename_file(", "")
        command = command.replace(")", "")
        command = command.split(",")
        file_name = command[0]
        extension = command[1]
        new_file_name = command[2]
        new_extension = command[3]
        Rename_file(file_name, extension, new_file_name, new_extension)
        Save_FileSystem()
        output.insert(INSERT, "File " + file_name + "." + extension + " renamed to " + new_file_name + "." + new_extension + "\n")
        output.see(END)

    if command.startswith("rename_file("):
        rename_file_command(command)


    # format command will format the filesystem, like: format() , > , this command is dangerous, the user, after entering the command, should confirm if he really wants to execute it or not.
    def format_command(commnad):

        import threading

        global get_response
        global answer
            
        from System.Core.Core import Format_FileSystem

        answer = ""

        output.insert(INSERT, "Are you sure you want to format the filesystem? (y/n)" + "\n")
        output.see(END)

        # Get the response from the user in the terminal, until a response is given in command, the following lines will not be executed.
        answer = input()
        
        # If the user typed "y", the filesystem will be formatted.
        if answer == "y":
            Format_FileSystem()
            output.insert(INSERT, "Filesystem formatted" + "\n")
            output.see(END)

        # If the user typed "n", the filesystem will not be formatted.
        elif answer == "n":
            output.insert(INSERT, "Filesystem not formatted" + "\n")
            output.see(END)

        # If the user typed something else, the filesystem will not be formatted.
        else:
            output.insert(INSERT, "Filesystem not formatted" + "\n")
            output.see(END)
                
    if command.startswith("format"):
        format_command(command)

    
    def import_file_command(command):

        from System.Core.Core import Import_file, Save_FileSystem

        command = command.replace("import_file(", "")
        command = command.replace(")", "")
        command = command.split(", ")
        file_path = command[0]
        folder_name = command[1]
        Import_file(file_path, folder_name)
        Save_FileSystem()
        output.insert(INSERT, "File form path " + file_path + " imported to " + folder_name + "\n")
        output.see(END)

    
    if command.startswith("import_file("):
        import_file_command(command)
    
    
    def execute_file(command):

        from System.Core.Core import Execute_file, Save_FileSystem

        command = command.replace("execute_file(", "")
        command = command.replace(")", "")
        command = command.split(", ")
        file_name = command[0]
        extension = command[1]
        Execute_file(file_name, extension)
        Save_FileSystem()
        output.insert(INSERT, "File " + file_name + "." + extension + " executed" + "\n")
        output.see(END)

    if command.startswith("execute_file("):
        execute_file(command)
    

    # dir command will print the directory of the current file (using the filesystem in core.py), like: dir() , > dir.
    def dir_command():

        from System.Core.Core import Get_FileSystem

        output.insert(INSERT, "Directories: " + "\n")
        output.insert(INSERT, Get_FileSystem() + "\n")

        # print the number of files directory.
        output.insert(INSERT, "Files: " + str(len(Get_FileSystem().split("\n"))) + "\n\n")

        output.see(END)

    if command.startswith("?") or command.startswith("dir"):
        dir_command()


    # Tree command will print the directory tree of the current file, like: tree() , > tree.
    def tree_command():
        from System.Core.Core import Tree_FileSystem_Advanced

        output.insert(INSERT, "Directory tree: " + "\n")
        output.insert(INSERT, Tree_FileSystem_Advanced() + "\n")

        # print the number of files directory.
        output.insert(INSERT, "[" + str(len(Tree_FileSystem_Advanced().split("\n"))) + "] " + "files indexed." +  "\n\n")

        output.see(END)

    if command.startswith("tree"):
        tree_command()


# -------------------------------------------------------------------------------------------------------------------------------------------------

    # info command will print the info of system, like: info , > info.
    def info_command():
        """Info command"""

        import platform

        output.insert(INSERT, "Info: ---------------------------------------------------------------------" + "\n")
        output.insert(INSERT, "Base-System: " + platform.system() + "\n")
        output.insert(INSERT, "Release: " + platform.release() + "\n")
        output.insert(INSERT, "Version: " + platform.version() + "\n")
        output.insert(INSERT, "Machine: " + platform.machine() + "\n")
        output.insert(INSERT, "Processor: " + platform.processor() + "\n")
        output.insert(INSERT, "---------------------------------------------------------------------------" + "\n\n")
        output.see(END)
    
    if command.startswith("info"):
        info_command()

    # help command will print the help, like: help , >.
    def help_command():
        """Help command"""

        output.insert(INSERT, "Help: ---------------------------------------------------------------------" + "\n")
        output.insert(INSERT, "print() - print a string" + "\n")
        output.insert(INSERT, "add() - adds numbers or strings" + "\n")
        output.insert(INSERT, "sub() - subtract numbers" + "\n")
        output.insert(INSERT, "mul() - multiply numbers" + "\n")
        output.insert(INSERT, "div() - divide numbers" + "\n")
        output.insert(INSERT, "random(max_number) - generate a random number" + "\n")
        output.insert(INSERT, "\n")
        output.insert(INSERT, "var(variable_name, value) - make a variable" + "\n")
        output.insert(INSERT, "print_value(variable_name) - print the variable value" + "\n")
        output.insert(INSERT, "clear_var(variable_name) - clean the variable value" + "\n")
        output.insert(INSERT, "\n")
        output.insert(INSERT, "repeat(command(args), number) - repeats a command a number of times" + "\n")
        output.insert(INSERT, "\n")
        output.insert(INSERT, "? | dir - print the current directory" + "\n")
        output.insert(INSERT, "cd(directory) - change the current directory" + "\n")
        output.insert(INSERT, "mkfolder(folder_name) - create a new folder" + "\n")
        output.insert(INSERT, "mkfile(file_name, extension, content) - create a new file" + "\n")
        output.insert(INSERT, "move_file(file_name, extension, folder_name) - move a file to other folder" + "\n")
        output.insert(INSERT, "Rename_file(file_name, extension, new_name, new_extension) - rename a file" + "\n")
        output.insert(INSERT, "Import_file(file_path, folder_name) - import a real file from the Base-System to the File System" + "\n")
        output.insert(INSERT, "Execute_file(file_name, extension) - execute a .pys file" + "\n")
        output.insert(INSERT, "delete_file(file_name, extension) - delete a file" + "\n")
        output.insert(INSERT, "\n")
        output.insert(INSERT, "time - print the current time" + "\n")
        output.insert(INSERT, "tree - print the directory tree of the current file" + "\n")
        output.insert(INSERT, "help - print the help" + "\n")
        output.insert(INSERT, "info - print the system information" + "\n")
        output.insert(INSERT, "clear | cls - clear the terminal" + "\n")
        output.insert(INSERT, "exit - exit the terminal" + "\n")
        output.insert(INSERT, "\n")
        output.insert(INSERT, ">>> python_command - execute a python command" + "\n")
        output.insert(INSERT, "---------------------------------------------------------------------------" + "\n\n")
        output.see(END)

    if command.startswith("help"):
        help_command()






