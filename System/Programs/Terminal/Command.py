import os
import platform
import time
from tkinter.constants import END, INSERT

import psutil
from System.Utils.Utils import print_error, print_log

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

    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    command = entry.get()
    entry.delete(0, END)

    # Commands ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def print_command(command):

        """
        Summary:
            This is used to print a message/string in the terminal.

        Example:
            print "Hello"

        """

        command = command.replace("print ", "")

        # The string must be in quotes
        text = command.split("\"")[1]

        output.insert(INSERT, text + "\n")
        output.see(END)

    if command.startswith("print "):
        print_command(command)


    def echo_command(command):

        """
        Summary:
            This is used to print a message/string in the terminal.

        Example:
            echo "Hello"

        """

        command = command.replace("echo ", "")

        # The string must be in quotes
        text = command.split("\"")[1]

        output.insert(INSERT, text + "\n")
        output.see(END)

    if command.startswith("echo "):
        echo_command(command)


    # var command will create a variable, like: var(name, value) , > .
    def var_command(command):
        """Var command"""

        command = command.replace("var(", "")
        command = command.replace(")", "")
        command = command.split(",")
        var_name = command[0]
        var_value = command[1]
        globals()[var_name] = var_value
        output.insert(INSERT, f'{var_name} = {var_value}' + "\n")
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
        output.insert(INSERT, f'{command} = ' + "\n")
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


    def repeat_command(command):
        """Repeat command"""

        command = command.replace("repeat(", "")
        command = command.replace(")", "")
        command = command.split(",")
        repeat_command = command[0]
        repeat_number = command[1]
        for _ in range(int(repeat_number)):
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
        output.insert(INSERT, f"Delay {command} seconds" + "\n")
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

        master.after(1000, master.destroy)


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
            output.insert(INSERT, f">>> {command}" + "\n")
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

    def cd_command(command):
        """Cd command"""

        from System.Core.FileSystem import cd

        command = command.replace("cd ", "")

        output.insert(INSERT, cd(command) + "\n")
        output.see(END)

    if command.startswith("cd "):
        cd_command(command)

    def mkfolder_command(command):

        """
            Summary:
                Make a folder in the disk

            Example:
                mkfolder folder_name

        """

        from System.Core.FileSystem import mkdir

        command = command.replace("mkfolder ", "")

        output.insert(INSERT, mkdir(command) + "\n")
        output.see(END)

    if command.startswith("mkfolder "):
        mkfolder_command(command)


    def dfolder_command(command):

        """
            Summary:
                Delete a folder in the disk

            Example:
                dfolder folder_name

        """

        from System.Core.FileSystem import rmdir

        command = command.replace("dfolder ", "")

        output.insert(INSERT, rmdir(command) + "\n")
        output.see(END)

    if command.startswith("dfolder "):
        dfolder_command(command)


    def mkfile_command(command):

        """
            Summary:
                Make a folder in the disk

            Example:
                mkfolder folder_name

        """

        from System.Core.FileSystem import mkfile

        command = command.replace("mkfile ", "")

        mkfile(command)

        output.insert(INSERT, f"File {command} created " + "\n")
        output.see(END)

    if command.startswith("mkfile "):
        mkfile_command(command)


    def dfile_command(command):

        """
            Summary:
                Delete a file in the disk

            Example:
                dfolder file_name

        """

        from System.Core.FileSystem import rmfile

        command = command.replace("dfile ", "")

        rmfile(command)

        output.insert(INSERT, f"File {command} deleted " + "\n\n")
        output.see(END)

    if command.startswith("dfile "):
        dfile_command(command)


    def edit_file_command(command):

        from System.Core.FileSystem import edit_file, get_file_content

        command = command.replace("efile ", "")

        #efile file_name "content"
        command = command.split(" \"")
        file_name = command[0]
        file_content = command[1]

        output.insert(INSERT, edit_file(file_name, "\"" + file_content) + "\n")
        output.see(END)

    if command.startswith("efile "):
        edit_file_command(command)

    
    def metafile_command(command):

        from System.Core.FileSystem import get_file_content, get_file_metadata

        command = command.replace("metafile ", "")

        name = command

        output.insert(INSERT, get_file_metadata(name) + "\n")
        output.insert(INSERT, f"Content: {get_file_content(name)}" + "\n")
        output.see(END)

    if command.startswith("metafile "):
        metafile_command(command)


    # dir command will print the directory of the current file (using the filesystem in core.py), like: dir() , > dir.
    def dir_command():

        from System.Core.FileSystem import ls

        output.insert(INSERT, ls())
        output.insert(INSERT,  "\n")

        output.see(END)

    # if start with dir or DIR lower or upper
    if command.startswith("dir") or command.startswith("DIR") or command.startswith("ls") or command.startswith("?"):
        dir_command()


    # delete_logs
    def delete_logs_command():
        from System.Core.Core import delete_logs

        delete_logs()

        output.insert(INSERT, "Deleted logs" + "\n")
        output.see(END)

    if command.startswith("dlogs"):
        delete_logs_command()


    def get_processes_command():

        output.insert(INSERT, "Processes: " + "\n")
        output.insert(INSERT, "Sorry, something is wrong" + "\n")
        output.see(END)

    if command.startswith("ps"):
        master.after(512, get_processes_command())

    def tree_command(command):
        from System.Core.FileSystem import tree

        if command.startswith("tree "): # Specific directory, tree <directory>
            command = command.replace("tree ", "")

            output.insert(INSERT, tree(command))
            output.insert(INSERT, "\n")
            output.see(END)

        elif command.startswith("tree"): # Current directory, tree
            command = command.replace("tree", "")

            command = "$null"

            output.insert(INSERT, tree(command))
            output.insert(INSERT, "\n")
            output.see(END)

    if command.startswith("tr"):
        master.after(1000, tree_command(command))

    def foreground_command(command):

        """
        Changes the terminal foreground color

        Command:
            foreground "color"

        Colors:
            black, red, green, yellow, blue, magenta, cyan, white, etc.

        """

        from System.Programs.Terminal.Terminal import set_foreground

        command = command.replace("foreground ", "")

        # The color is beetween quotation marks
        color = command.split("\"")[1]

        set_foreground(color)

        output.insert(
            INSERT,
            f"Foreground changed to {command}"
            + ", please restart to see the change",
            "\n\n",
        )

        output.see(END)

    if command.startswith("foreground"):
        master.after(1000, foreground_command(command))


    def background_command(command):

        """
        Changes the terminal background color

        Command:
            background "color"

        Colors:
            black, red, green, yellow, blue, magenta, cyan, white, etc.

        """

        from System.Programs.Terminal.Terminal import set_background

        command = command.replace("background ", "")

        # The color is beetween quotation marks
        color = command.split("\"")[1]

        set_background(color)

        output.insert(
            INSERT,
            f"Background changed to {command}"
            + ", please restart to see the change",
            "\n\n",
        )

        output.see(END)

    if command.startswith("background"):
        master.after(1000, background_command(command))


    def neofetch_command():

        from System.Programs.Terminal.Terminal import (get_background, get_foreground)

        neo = ""

        neo += os.getlogin() + "\n"
        neo += "--------\n"
        neo += f"OS: {platform.system()} {platform.release()}" + "\n"
        neo += f"Kernel: {platform.version()}" + "\n"
        neo += f"Uptime: {str(psutil.boot_time() - psutil.boot_time())}" + "\n"
        neo += "Shell: " + "Py-OS" + "\n"
        neo += "Terminal: " + "Iris CLI" + "\n"
        neo += f"CPU: {str(psutil.cpu_percent())}" + "%\n"
        neo += f"Memory: {str(psutil.virtual_memory().percent)}" + "%\n\n"

        neo += "--------\n"
        neo += f"Foreground: {get_foreground()}" + "\n"
        neo += f"Background: {get_background()}" + "\n"

        output.insert(INSERT, neo + "\n")
        output.see(END)

    if command.startswith("neofetch"):
        master.after(1000, neofetch_command())


# -------------------------------------------------------------------------------------------------------------------------------------------------

    # info, print the base system information
    def info_command():
        """Info command"""

        import platform

        output.insert(INSERT, "Info: ─────────────────────────────────────────────────────────────────────" + "\n")
        output.insert(INSERT, f"System:     {platform.system()}" + "\n")
        output.insert(INSERT, f"Release:    {platform.release()}" + "\n")
        output.insert(INSERT, f"Version:    {platform.version()}" + "\n")
        output.insert(INSERT, f"Machine:    {platform.machine()}" + "\n")
        output.insert(INSERT, f"Processor:  {platform.processor()}" + "\n")
        output.insert(INSERT, "───────────────────────────────────────────────────────────────────────────" + "\n\n")
        output.see(END)

    if command.startswith("info"):
        info_command()


    def help_command():
        """Help command"""

        output.insert(INSERT, 'Help: ─────────────────────────────────────────────────────────────────────' + '\n')
        output.insert(INSERT, 'print "text"             - print a string' +                                   '\n')
        output.insert(INSERT, 'echo "text"              - print a string' +                                   '\n')
        output.insert(INSERT, 'clear | cls              - clear the terminal' +                               '\n')
        output.insert(INSERT,                                                                                 '\n')
        output.insert(INSERT, 'dir | ? | ls             - show the file system directory' +                   '\n')
        output.insert(INSERT, 'tree                     - show the file system directory as tree' +           '\n')
        output.insert(INSERT,                                                                                 '\n')
        output.insert(INSERT, 'mkfolder folder_name           - create a folder in the file system' +         '\n')
        output.insert(INSERT, 'mkfile file_name.ext           - create a file in the file system' +           '\n')
        output.insert(INSERT, 'dfolder folder_name            - delete a folder in the file system' +         '\n')
        output.insert(INSERT, 'dfile file_name.ext            - delete a file in the file system' +           '\n')
        output.insert(INSERT, 'efile file_name.ext "content"  - edit a file in the file system' +             '\n')
        output.insert(INSERT, 'metafile file_name.ext         - show the metadata, like content or date' +    '\n')
        output.insert(INSERT,                                                                                 '\n')
        output.insert(INSERT, 'dlogs                    - delete system logs' +                               '\n')
        output.insert(INSERT, 'info                     - show the system info' +                             '\n')
        output.insert(INSERT, 'ps                       - show all processes' +                               '\n')
        output.insert(INSERT, 'reg                      - show the registry' +                                '\n')
        output.insert(INSERT, 'foreground "color"       - change the terminal foreground color' +             '\n')
        output.insert(INSERT, 'background "color"       - change the terminal background color' +             '\n')
        output.insert(INSERT, 'neofetch                 - show the terminal and system info' +                '\n')
        output.insert(INSERT, '>>> python code          - run a python interpreter where you can code' +      '\n')
        output.insert(INSERT, '───────────────────────────────────────────────────────────────────────────' + '\n\n')
        output.see(END)

    if command.startswith("help"):
        help_command()
