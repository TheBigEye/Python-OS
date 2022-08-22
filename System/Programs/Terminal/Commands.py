import time
from tkinter import Entry, Label
from tkinter.constants import END, INSERT

from Libs.pyUtils.pyFetch import get_neofetch
from System.core.bin.CAT import CAT
from System.core.bin.CD import CD
from System.core.bin.CLEAR import CLEAR
from System.core.bin.DIR import DIR
from System.core.bin.ECHO import ECHO
from System.core.bin.MKDIR import MKDIR
from System.core.bin.MV import MV
from System.core.bin.RMDIR import RMDIR
from System.core.bin.TOUCH import TOUCH
from System.shell.Components.UITextbox import UITextbox

__author__ = 'TheBigEye'
__version__ = '1.0'

### COMMANDS:

def CMD(master: Label, entry: Entry, output: UITextbox) -> None:

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

    if command.lower().startswith("cat "):
        CAT(command, output)

    if command.lower().startswith("cd "):
        CD(command, output)

    dir_commands = ("dir", "ls", "dirs", "lsdirs", "?")
    if command.lower().startswith(dir_commands):
        DIR(output)

    echo_commands = ("echo", "print")
    if command.lower().startswith(echo_commands):
        ECHO(command, output)

    clear_commands = ("clear", "cls")
    if command.lower().startswith(clear_commands):
        CLEAR(output)

    mkdir_commands = ("mkdir", "md", "mkfolder")
    if command.lower().startswith(mkdir_commands):
        MKDIR(command, output)

    rmdir_commands = ("rmdir", "rd", "rmfolder", "dfolder")
    if command.lower().startswith(rmdir_commands):
        RMDIR(command, output)

    touch_commands = ("touch", "mkfile", "mf")
    if command.lower().startswith(touch_commands):
        TOUCH(command, output)

    if command.lower().startswith("mv"):
        MV(command, output)

    # Commands ----------------------------------------------------------------------------------------------------------------------------------------------------------------------


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

    def python_interpreter(command):

        command = command.replace(">>> ", "")
        command = command.replace("", "")
        command = command.replace("", "")

        # if command is empty, will print a new line.
        if command == "":
            output.insert_colored(">>> " + "\n", "#F84B3C" )

            # if command is not empty, will print the command in Terminal_screen and execute it.
        else:

            output.insert_colored(">>> ", "#F84B3C")

            # list of sintax color
            stx_color = [
                ("print", "#F84B3C"),
                ("if", "#F84B3C"),
                ("while", "#F84B3C"),
                ("elif", "#F84B3C"),
                ("else", "#F84B3C"),
                ("for", "#F84B3C"),
                ("in", "#F84B3C"),
                ("def", "#F84B3C"),
                ("return", "#F84B3C"),

                ("import", "#8FB969"),
                ("from", "#8FB969"),
                ("as", "#8FB969"),

                ("=", "#F84B3C"),
                ("==", "#F84B3C"),
                ("!=", "#F84B3C"),
                ("<", "#F84B3C"),
                (">", "#F84B3C"),
                ("<=", "#F84B3C"),
                (">=", "#F84B3C"),
                ("+", "#F84B3C"),
                ("-", "#F84B3C"),
                ("*", "#F84B3C"),
                ("/", "#F84B3C"),
                ("%", "#F84B3C"),
                ("//", "#F84B3C"),
                ("**", "#F84B3C"),
                ("+=", "#F84B3C"),
                ("-=", "#F84B3C"),
                ("*=", "#F84B3C"),
                ("/=", "#F84B3C"),
                ("%=", "#F84B3C"),
                ("//=", "#F84B3C"),

                ("{", "#F84B3C"),
                ("}", "#F84B3C"),
                ("[", "#F84B3C"),
                ("]", "#F84B3C"),

                ("1", "#D2879B"),
                ("2", "#D2879B"),
                ("3", "#D2879B"),
                ("4", "#D2879B"),
                ("5", "#D2879B"),
                ("6", "#D2879B"),
                ("7", "#D2879B"),
                ("8", "#D2879B"),
                ("9", "#D2879B"),
                ("0", "#D2879B"),
                ("None" , "#D2879B"),
                ("True" , "#D2879B"),
                ("False" , "#D2879B")
            ]

            output.insert_color_word(str(command), stx_color)
            output.insert_colored("\n", "#F84B3C")
            try:
                # Execute the command and use the variables
                exec(command, globals())

            except Exception as error:
                output.insert(INSERT, str(error) + "\n")
                output.see(END)

    if command.startswith(">>> "):
        python_interpreter(command)


# -------------------------------------------------------------------------------------------------------------------------------------------------

    def dfile_command(command):

        """
            Summary:
                Delete a file in the disk

            Example:
                dfolder file_name

        """

        from System.core.filesystem import remove_file

        command = command.replace("dfile ", "")

        remove_file(command)

        output.insert(INSERT, "File " + command + " deleted " + "\n\n")
        output.see(END)

    if command.startswith("dfile "):
        output.insert(INSERT, "~$" + command + "\n")
        dfile_command(command)


    def edit_file_command(command):

        from System.core.filesystem import edit_file

        command = command.replace("efile ", "")

        #efile file_name "content"
        command = command.split(" \"")
        file_name = command[0]
        file_content = command[1]

        output.insert(INSERT, edit_file(file_name, "\"" + file_content) + "\n")
        output.see(END)

    if command.startswith("efile "):
        output.insert(INSERT, "~$" + command + "\n")
        edit_file_command(command)


    def metafile_command(command):

        from System.core.filesystem import get_file_metadata, get_file_content

        command = command.replace("metafile ", "")

        name = command

        output.insert(INSERT, get_file_metadata(name) + "\n")
        output.insert(INSERT, "Content: " + get_file_content(name) + "\n")
        output.see(END)

    if command.startswith("metafile "):
        output.insert(INSERT, "~$" + command + "\n")
        metafile_command(command)


    def get_processes_command():

        output.insert(INSERT, "Processes: " + "\n")
        output.insert(INSERT, "Sorry, something is wrong" + "\n")
        output.see(END)

    if command.startswith("ps"):
        master.after(512, get_processes_command())

    def foreground_command(command):

        """
        Changes the terminal foreground color

        Command:
            foreground "color"

        Colors:
            black, red, green, yellow, blue, magenta, cyan, white, etc.

        """

        from System.programs.Terminal.Terminal import set_foreground

        command = command.replace("foreground ", "")

        # The color is beetween quotation marks
        color = command.split("\"")[1]

        set_foreground(color)

        output.insert(INSERT, "Foreground changed to " + command + ", please restart to see the change" + "\n\n")
        output.see(END)

    if command.startswith("foreground"):
        output.insert(INSERT, "~$ " + command + "\n")
        master.after(1000, foreground_command(command))


    def background_command(command):

        """
        Changes the terminal background color

        Command:
            background "color"

        Colors:
            black, red, green, yellow, blue, magenta, cyan, white, etc.

        """

        from System.programs.Terminal.Terminal import set_background


        output.insert(INSERT, "~$ " + command + "\n")
        command = command.replace("background ", "")

        # The color is beetween quotation marks
        color = command.split("\"")[1]

        set_background(color)

        output.insert(INSERT, "Background changed to " + command + ", please restart to see the change" + "\n\n")
        output.see(END)

    if command.startswith("background"):
        master.after(1000, background_command(command))


    def neofetch_command():

        from System.programs.Terminal.Terminal import (get_background,
                                                       get_foreground)

        output.insert(INSERT, "~$ neofetch" + "\n")

        neo = ""
        neo += "--------\n"
        neo += "Foreground: " + get_foreground() + "\n"
        neo += "Background: " + get_background() + "\n"

        output.insert(INSERT, get_neofetch("Assets/Data/mini_logo.txt", None) + "\n")
        output.insert(INSERT, neo + "\n")
        output.see(END)

    if command.startswith("neofetch"):
        master.after(1000, neofetch_command())


# -------------------------------------------------------------------------------------------------------------------------------------------------

    # info, print the base system information
    def info_command():
        """Info command"""

        import platform

        output.insert(INSERT, "~$ info" + "\n")
        output.insert(INSERT, "Info: ─────────────────────────────────────────────────────────────────────" + "\n")
        output.insert(INSERT, "System:     " + platform.system() +    "\n")
        output.insert(INSERT, "Release:    " + platform.release() +   "\n")
        output.insert(INSERT, "Version:    " + platform.version() +   "\n")
        output.insert(INSERT, "Machine:    " + platform.machine() +   "\n")
        output.insert(INSERT, "Processor:  " + platform.processor() + "\n")
        output.insert(INSERT, "───────────────────────────────────────────────────────────────────────────" + "\n\n")
        output.see(END)

    if command.startswith("info"):
        info_command()

# -------------------------------------------------------------------------------------------------------------------------------------------------

    def help_command():
        """Help command"""

        output.insert(INSERT,  "~$ help" + "\n")
        output.insert(INSERT,  "Help: ─────────────────────────────────────────────────────────────────────" + "\n")
        output.insert(INSERT,  "Commands:                                                                  " + "\n")
        output.insert(INSERT,  "  help                        - Prints this help message                   " + "\n")
        output.insert(INSERT,  "  clear                       - Clears the terminal screen                 " + "\n")
        output.insert(INSERT,  "  exit                        - Closes the terminal                        " + "\n")
        output.insert(INSERT,  "  info                        - Prints system information                  " + "\n")
        output.insert(INSERT,  "  ps                          - Prints the processes                       " + "\n")
        output.insert(INSERT,  "  dir                         - Prints the current directory               " + "\n")
        output.insert(INSERT,  "  tree | <directory>          - Prints the directory tree                  " + "\n")
        output.insert(INSERT,  "  mkfolder | mkdir <name>     - Makes a new folder                         " + "\n")
        output.insert(INSERT,  "  rmfolder | rmdir <name>     - Removes a folder                           " + "\n")
        output.insert(INSERT,  "  mkfile | touch <name>       - Makes a new file on the current dir        " + "\n")
        output.insert(INSERT,  "  efile <file>                - Edit a file content                        " + "\n")
        output.insert(INSERT,  "  metafile <file>             - Show the metadata of a file                " + "\n")
        output.insert(INSERT,  "  neofetch                    - Prints the system information              " + "\n")
        output.insert(INSERT,  "  foreground <color>          - Change the terminal foreground color       " + "\n")
        output.insert(INSERT,  "  background <color>          - Change the terminal background color       " + "\n")
        output.insert(INSERT,  "  >>> <python code>           - Run a python command                       " + "\n")
        output.insert(INSERT,  "───────────────────────────────────────────────────────────────────────────" + "\n\n")
        output.see(END)

    if command.startswith("help"):
        help_command()

# -------------------------------------------------------------------------------------------------------------------------------------------------
