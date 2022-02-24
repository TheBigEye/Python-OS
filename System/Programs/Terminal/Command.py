import random
import time
from tkinter.constants import END, INSERT

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

    # Comandos----------------------------------------------------------------------------------------------------------------------------------------------------------------------

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



    # add, suma 2 o mas numeros y puede juntar 2 palabras, ejemplo: add(2, 2), > 4
    def add_command(command):
        """Add command"""

        # Comprueba si los argumentos estan entre parentesis
        if "(" in command and ")" in command:

            # une palabras, como: add("hello", "world") , > hello world., o, como: add("hi", "this", "is", "a", "big", "text") , > hi this is a big text.
            if "\"" in command: # comprueba de que cada palabra este dentro de comillas.

                command = command.replace("add(", "").replace(")", "")
                command = command.replace("\"", "")
                command = command.split(",")

                for word in command:
                    output.insert(INSERT, str(word) + "")

                output.insert(INSERT, "\n")

            # en caso de que se detecte numeros, los suma
            else:
                # suma numeros. como: add(1,2), > 3, o add(1,2,3,4,5) , > 15.
                command = command.replace("add(", "").replace(")", "")
                command = command.split(",")

                add = 0
                for number in command:
                    add += int(number)

                output.insert(INSERT, add)
                output.insert(INSERT, "\n")
                output.see(END)

        else:
            # si el comando no tiene parentesis, aparece un error
            output.insert(INSERT, "Error: no tiene parentesis" + "\n")

    # Si el comando ingresado en la terminal comienza por add(, entonces ejecuta el comando add(numero_o_palabra)
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
        command = command.split(",")

        min_number = command[0]
        max_number = command[1]

        random_number = random.randint(int(min_number), int(max_number))
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
    # exxample: repeat(print(hello), 3) , > hello, hello, hello.
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

    def mkfolder_command(command):

        """
            Summary:
                Make a folder in the disk

            Example:
                mkfolder C:/folder_name

        """

        from System.Core.FileSystem import Create_folder, Save_FileSystem

        command = command.replace("mkfolder ", "")
        command = command.split("/")

        drive_name = command[0]
        folder_name = command[1]

        Create_folder(drive_name, folder_name)

        print_log("Folder " + folder_name + " created in " + drive_name)
        output.insert(INSERT, "Folder " + folder_name + " created in " + drive_name + "\n")
        output.see(END)

    if command.startswith("mkfolder "):
        mkfolder_command(command)


    def mkfile_command(command):

        """
            Summary:
                Make a file in the disk

            Example:
                mkfile C:/folder_name/file_name.txt, "conttent :)" (the extension is important)

        """

        from System.Core.FileSystem import Create_file

        command = command.replace("mkfile ", "")
        command = command.split(", ")

        drive_name = command[0].split("/")[0]
        folder_name = command[0].split("/")[1]

        # evita poner doble extension
        file_name = command[0].split("/")[2].split(".")[0]
        extension = command[0].split("/")[2].split(".")[1]

        content = command[1]

        Create_file(drive_name, folder_name, file_name, extension, content)

        print_log("Archivo " + file_name + "." + extension + " fue creado en " + drive_name + "/" + folder_name)
        output.insert(INSERT, "Archivo " + file_name + "." + extension + " fue creado en " + drive_name + "/" + folder_name + "\n")
        output.see(END)

    if command.startswith("mkfile "):
        mkfile_command(command)


    def read_file_command(command):

        from System.Core.FileSystem import Read_file

        command = command.replace("read_file(", "")
        command = command.replace(")", "")
        command = command.split("/")

        drive_name = command[0]
        folder_name = command[1]
        file_name = command[2].split(".")[0]
        extension = command[2].split(".")[1]

        output.insert(INSERT, Read_file(drive_name, folder_name, file_name, extension))
        output.insert(INSERT, "\n")
        output.see(END)

    if command.startswith("read_file("):
        read_file_command(command)


    def copy_folder_command(command):

        from System.Core.FileSystem import Copy_folder

        # -> copy_folder(C:/System, D:)
        command = command.replace("copy_folder(", "")
        command = command.replace(")", "")
        command = command.split(", ")

        drive_name = command[0].split("/")[0]
        folder_name = command[0].split("/")[1]

        to_drive_name = command[1]

        Copy_folder(drive_name, folder_name, to_drive_name)

        output.insert(INSERT, "Carpeta " + drive_name + "/" + folder_name + " fue copiada en " + to_drive_name + "\n")
        print_log("Carpeta " + drive_name + "/" + folder_name + " fue copiada en " + to_drive_name)
        output.see(END)

    if command.startswith("copy_folder("):
        copy_folder_command(command)


    def copy_file_command(command):

        from System.Core.FileSystem import Copy_file

        # -> copy_file(C:/System/file.txt, C:/Programs)
        command = command.replace("copy_file(", "")
        command = command.replace(")", "")
        command = command.split(", ")

        drive_name = command[0].split("/")[0]
        folder_name = command[0].split("/")[1]
        file_name = command[0].split("/")[2].split(".")[0]
        extension = command[0].split("/")[2].split(".")[1]

        to_drive_name = command[1].split("/")[0]
        to_folder_name = command[1].split("/")[1]

        Copy_file(drive_name, folder_name, file_name, extension, to_drive_name, to_folder_name)

        output.insert(INSERT, "Archivo " + drive_name + "/" + folder_name + "/" + file_name + "." + extension + " fue copiado en " + to_drive_name + "/" + to_folder_name + "\n")
        print_log("Archivo " + drive_name + "/" + folder_name + "/" + file_name + "." + extension + " fue copiado en " + to_drive_name + "/" + to_folder_name)
        output.see(END)

    if command.startswith("copy_file("):
        copy_file_command(command)


    def move_folder_command(command):

        from System.Core.FileSystem import Move_folder

        # -> move_folder(C:/System, D:)
        command = command.replace("move_folder(", "")
        command = command.replace(")", "")
        command = command.split(", ")

        drive_name = command[0].split("/")[0]
        folder_name = command[0].split("/")[1]

        to_drive_name = command[1]

        Move_folder(drive_name, folder_name, to_drive_name)

        output.insert(INSERT, "Carpeta " + folder_name + " movida desde " + drive_name + " hacia " + to_drive_name + "\n")
        print_log("Carpeta " + folder_name + " movida desde " + drive_name + " hacia " + to_drive_name)
        output.see(END)

    if command.startswith("move_folder("):
        move_folder_command(command)


    # move_file command will move a file, like: move_file(file_name, extension, folder_name) , > .
    def move_file_command(command):

        from System.Core.FileSystem import Move_file

        # -> move_file(C:/System/file.txt, C:/System)
        command = command.replace("move_file(", "")
        command = command.replace(")", "")
        command = command.split(", ")

        drive_name = command[0].split("/")[0]
        folder_name = command[0].split("/")[1]
        file_name = command[0].split("/")[2].split(".")[0]
        extension = command[0].split("/")[2].split(".")[1]

        to_drive_name = command[1].split("/")[0]
        to_folder_name = command[1].split("/")[1]

        Move_file(drive_name, folder_name, file_name, extension, to_drive_name, to_folder_name)

        output.insert(INSERT, "Archivo " + file_name + "." + extension + " fue movido a " + to_drive_name + "/" + to_folder_name + "\n")
        print_log("Archivo " + file_name + "." + extension + " fue movido a " + to_drive_name + "/" + to_folder_name)
        output.see(END)

    if command.startswith("move_file("):
        move_file_command(command)



    def delete_folder_command(command):

        from System.Core.FileSystem import Delete_folder

        command = command.replace("dfolder ", "")
        command = command.split("/")

        drive_name = command[0]
        folder_name = command[1]

        Delete_folder(drive_name, folder_name)

        output.insert(INSERT, "Carpeta " + folder_name + " borrada desde " + drive_name + "\n")
        print_log("Carpeta " + folder_name + " borrada desde " + drive_name)
        output.see(END)

    if command.startswith("dfolder "):
        delete_folder_command(command)


    # delete_file command will delete a file, like: delete_file(file_name, extension) , > .
    def delete_file_command(command):

        from System.Core.FileSystem import Delete_file, Save_FileSystem

        # example: delete_file(drive_name/folder_name/filename.extension) -> delete_file(C:/System/test.pys)
        command = command.replace("dfile ", "")
        command = command.split("/")

        drive_name = command[0]
        folder_name = command[1]
        file_name = command[2].split(".")[0]
        extension = command[2].split(".")[1]

        # si la extension es .pfs, entonces no se puede eliminar
        if extension == "pfs":
            output.insert(INSERT, "No es posible eliminar el archivo " + file_name + "." + extension + "\n")
            print_error("No es posible eliminar el archivo " + file_name + "." + extension)

        else:
            Delete_file(drive_name, folder_name, file_name, extension)
            output.insert(INSERT, "Archivo " + file_name + "." + extension + " borrado desde " + folder_name + "\n")
            print_log("Archivo " + file_name + "." + extension + " borrado desde " + folder_name)

        Save_FileSystem()
        output.see(END)

    if command.startswith("dfile "):
        delete_file_command(command)


    def rename_folder_command(command):

        from System.Core.FileSystem import Rename_folder

        # -> rename_folder(drive_name/folder_name, new_folder_name)
        command = command.replace("rename_folder(", "")
        command = command.replace(")", "")
        command = command.split(", ")

        drive_name = command[0].split("/")[0]
        folder_name = command[0].split("/")[1]
        new_folder_name = command[1]

        Rename_folder(drive_name, folder_name, new_folder_name)

        output.insert(INSERT, "Carpeta " + folder_name + " renombrada a " + new_folder_name + " en " + drive_name + "\n")
        print_log("Carpeta " + folder_name + " renombrada a " + new_folder_name + " en " + drive_name)

    if command.startswith("rename_folder("):
        rename_folder_command(command)


    def rename_file_command(command):

        from System.Core.FileSystem import Rename_file, Save_FileSystem

        # -> rename_file(C:/System/test.pys, test2.txt)
        command = command.replace("rename_file(", "")
        command = command.replace(")", "")
        command = command.split(", ")

        drive_name = command[0].split("/")[0]
        folder_name = command[0].split("/")[1]
        file_name = command[0].split("/")[2].split(".")[0]
        extension = command[0].split("/")[2].split(".")[1]

        new_name = command[1].split(".")[0]
        new_extension = command[1].split(".")[1]

        Rename_file(drive_name, folder_name, file_name, extension, new_name, new_extension)
        Save_FileSystem()

        output.insert(INSERT, "Archivo " + file_name + "." + extension + " de " +  drive_name + "/" + folder_name + " renombrado como " + new_name + "." + new_extension + "\n")
        print_log("Archivo " + file_name + "." + extension + " de " +  drive_name + "/" + folder_name + " renombrado como " + new_name + "." + new_extension)
        output.see(END)

    if command.startswith("rename_file("):
        rename_file_command(command)



    def import_file_command(command):

        from System.Core.FileSystem import Import_file, Save_FileSystem

        # import_file(path, C:/System)
        command = command.replace("import_file(", "")
        command = command.replace(")", "")
        command = command.split(", ")

        path = command[0]
        drive_name = command[1].split("/")[0]
        folder_name = command[1].split("/")[1]

        Import_file(path, drive_name, folder_name)
        Save_FileSystem()

        output.insert(INSERT, "Archivo " + path + " importado a " + drive_name + "/" + folder_name + "\n")
        print_log("Archivo " + path + " importado a " + drive_name + "/" + folder_name)
        output.see(END)

    if command.startswith("import_file("):
        import_file_command(command)


    def export_file_command(command):

        from System.Core.FileSystem import Export_file, Save_FileSystem

        command = command.replace("export_file(", "")
        command = command.replace(")", "")
        command = command.split(", ")

        folder_name = command[0]
        file_name = command[1]
        extension = command[2]
        file_path = command[3]

        Export_file(folder_name, file_name, extension, file_path)
        Save_FileSystem()

        output.insert(INSERT, "Archivo " + file_name + "." + extension + " de " + folder_name + " exportado hacia " + file_path + "\n")
        print_log("Archivo " + file_name + "." + extension + " de " + folder_name + " exportado hacia " + file_path)
        output.see(END)

    if command.startswith("export_file("):
        export_file_command(command)


    def execute_file(command):

        from System.Core.FileSystem import Execute_file, Save_FileSystem

        command = command.replace("execute_file(", "")
        command = command.replace(")", "")
        command = command.split(", ")

        folder_name = command[0]
        file_name = command[1]
        extension = command[2]

        Save_FileSystem()

        # insert the code result.
        print_log("Archivo " + file_name + "." + extension + " ejecutado")
        output.insert(INSERT, Execute_file(folder_name, file_name, extension))
        output.insert(INSERT, "\n")

        output.see(END)

    if command.startswith("execute_file("):
        execute_file(command)


    # dir command will print the directory of the current file (using the filesystem in core.py), like: dir() , > dir.
    def dir_command():

        from System.Core.FileSystem import Get_Files_Count, Get_FileSystem

        output.insert(INSERT, "Directories: " + "\n")
        output.insert(INSERT, Get_FileSystem())
        output.insert(INSERT,  "\n\n")

        output.see(END)

    if command.startswith("?") or command.startswith("dir"):
        dir_command()


    # Tree imprime el contenido del directorio actual en forma de arbol, como: tree() , > tree.
    def tree_command():
        from System.Core.FileSystem import (Get_Files_Count, Get_Fils_size,
                                            Get_Tree)

        output.insert(INSERT, "Directory tree: " + "\n")
        output.insert(INSERT, Get_Tree() + "\n")

        # imprime el numero de archivos en el directorio.
        output.insert(INSERT, Get_Files_Count() )
        output.insert(INSERT, " indexed files, with a size of ")
        output.insert(INSERT, Get_Fils_size() )
        output.insert(INSERT, " bytes." +  "\n\n")

        output.see(END)

    if command.startswith("tree"):
        tree_command()


    # delete_logs
    def delete_logs_command():
        from System.Core.Core import delete_logs

        delete_logs()

        output.insert(INSERT, "Deleted logs" + "\n")
        output.see(END)

    if command.startswith("dlogs"):
        delete_logs_command()


    def get_processes_command():
        from System.Core.TaskSystem import get_all_tasks

        output.insert(INSERT, "Procesos: " + "\n")
        output.insert(INSERT, get_all_tasks() + "\n")
        output.see(END)

    if command.startswith("ps"):
        get_processes_command()


    def registry_tree_command():
        from System.Core.KeysSystem import reg_tree_view

        output.insert(INSERT, "Registry: " + "\n")
        output.insert(INSERT, reg_tree_view())
        output.insert(INSERT, "\n")
        output.see(END)

    if command.startswith("reg"):
        registry_tree_command()


    def foreground_command(command):

        """
        Changes the terminal foreground color

        Command:
            foreground "color"

        Colors:
            black (never), red, green, yellow, blue, magenta, cyan, white, etc.

        """

        from System.Programs.Terminal.Terminal import set_foreground

        command = command.replace("foreground ", "")

        # The color is beetween quotation marks
        color = command.split("\"")[1]

        set_foreground(color)

        output.insert(INSERT, "Foreground changed to " + command + ", please restart to see the change", "\n\n")
        output.see(END)

    if command.startswith("foreground"):
        foreground_command(command)


# -------------------------------------------------------------------------------------------------------------------------------------------------

    # info, imprime la informacion del sistema base
    def info_command():
        """Info command"""

        import platform

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


    def help_command():
        """Help command"""

        output.insert(INSERT, 'Help: ─────────────────────────────────────────────────────────────────────' + '\n')
        output.insert(INSERT, 'print "text"             - print a string' +                                   '\n')
        output.insert(INSERT, 'echo "text"              - print a string' +                                   '\n')
        output.insert(INSERT, 'clear | cls              - clear the terminal' +                               '\n')
        output.insert(INSERT,                                                                                 '\n')
        output.insert(INSERT, 'dir | ?                  - show the file system directory' +                   '\n')
        output.insert(INSERT, 'tree                     - show the file system directory as tree' +           '\n')
        output.insert(INSERT,                                                                                 '\n')
        output.insert(INSERT, 'mkfolder C:/folder_name                - create a folder in the file system' + '\n')
        output.insert(INSERT, 'mkfile C:/.../file_name.ext, "content" - create a file in the file system' +   '\n')
        output.insert(INSERT, 'dfolder C:/folder_name                 - delete a folder in the file system' + '\n')
        output.insert(INSERT, 'dfile C:/folder/file_name.ext          - delete a file in the file system' +   '\n')
        output.insert(INSERT,                                                                                 '\n')
        output.insert(INSERT, 'dlogs                    - delete system logs' +                               '\n')
        output.insert(INSERT, 'info                     - show the system info' +                             '\n')
        output.insert(INSERT, 'ps                       - show all processes' +                               '\n')
        output.insert(INSERT, 'reg                      - show the registry' +                                '\n')
        output.insert(INSERT, 'foreground "color"       - change the terminal foreground color' +             '\n')
        output.insert(INSERT, '>>> python code          - run a python interpreter where you can code' +      '\n')
        output.insert(INSERT, '───────────────────────────────────────────────────────────────────────────' + '\n\n')
        output.see(END)

    if command.startswith("help"):
        help_command()
