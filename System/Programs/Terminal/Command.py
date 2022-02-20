import os
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

    # print, imprime un mensaje (string) en la terminal, print("algo"), > algo
    def print_command():

        # si los argumentos de comando esta entre parentesis, entonces:
        if "(" in command and ")" in command:
            # si los argumentos estan entre comillas (Obligatorio para que se lea como un string), entonces:
            if "\"" in command:
                # Reemplaza el comando por comillas, estas se eliminan, y solo se imprime el string o mensaje declarado
                output.insert(INSERT, eval(command.replace("print(", "").replace(")", "")) + "\n")
            else:
                # En caso de que no se halla declarado con comillas, aparece un error
                output.insert(INSERT, "Error: se necesitan comillas." + "\n")
        else:
            # En caso de que el comando no tenga parentesis para declarar los argumentos, se mostrara un error
            output.insert(INSERT, "Error: se necesitan parentesis" + "\n")

    # Si la terminal detecta el comando print, ejecuta el comando solicitado
    if command.startswith("print("):
        print_command()



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

        from System.Core.FileSystem import Create_folder, Save_FileSystem

        # example: mkfolder(drive_name/folder_name) -> delete_file(C:/System)
        command = command.replace("mkfolder(", "")
        command = command.replace(")", "")
        command = command.split("/")

        drive_name = command[0]
        folder_name = command[1]

        Create_folder(drive_name, folder_name)

        output.insert(INSERT, "Folder " + folder_name + " created in " + drive_name + "\n")
        print_log("Folder " + folder_name + " created in " + drive_name)
        output.see(END)

    if command.startswith("mkfolder("):
        mkfolder_command(command)


    def mkfile_command(command):

        from System.Core.FileSystem import Create_file

        command = command.replace("mkfile(", "")
        command = command.replace(")", "")
        command = command.split(", ")

        drive_name = command[0].split("/")[0]
        folder_name = command[0].split("/")[1]

        # evita poner doble extension
        file_name = command[0].split("/")[2].split(".")[0]
        extension = command[0].split("/")[2].split(".")[1]

        content = command[1]

        Create_file(drive_name, folder_name, file_name, extension, content)

        output.insert(INSERT, "Archivo " + file_name + "." + extension + " fue creado en " + drive_name + "/" + folder_name + "\n")
        print_log("Archivo " + file_name + "." + extension + " fue creado en " + drive_name + "/" + folder_name)
        output.see(END)

    if command.startswith("mkfile("):
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

        command = command.replace("delete_folder(", "")
        command = command.replace(")", "")
        command = command.split("/")

        drive_name = command[0]
        folder_name = command[1]

        Delete_folder(drive_name, folder_name)

        output.insert(INSERT, "Carpeta " + folder_name + " borrada desde " + drive_name + "\n")
        print_log("Carpeta " + folder_name + " borrada desde " + drive_name)
        output.see(END)

    if command.startswith("delete_folder("):
        delete_folder_command(command)


    # delete_file command will delete a file, like: delete_file(file_name, extension) , > .
    def delete_file_command(command):

        from System.Core.FileSystem import Delete_file, Save_FileSystem

        # example: delete_file(drive_name/folder_name/filename.extension) -> delete_file(C:/System/test.pys)
        command = command.replace("delete_file(", "")
        command = command.replace(")", "")
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


    if command.startswith("delete_file("):
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
        output.insert(INSERT,  "\n")

        output.see(END)

    if command.startswith("execute_file("):
        execute_file(command)


    # dir command will print the directory of the current file (using the filesystem in core.py), like: dir() , > dir.
    def dir_command():

        from System.Core.FileSystem import Get_Files_Count, Get_FileSystem

        output.insert(INSERT, "Directorios: " + "\n")
        output.insert(INSERT, Get_FileSystem())
        output.insert(INSERT,  "\n")

        # print the number of files directory.
        output.insert(INSERT, "Archivos: ")
        output.insert(INSERT,  Get_Files_Count())
        output.insert(INSERT,  "\n\n")

        output.see(END)

    if command.startswith("?") or command.startswith("dir"):
        dir_command()


    # Tree imprime el contenido del directorio actual en forma de arbol, como: tree() , > tree.
    def tree_command():
        from System.Core.FileSystem import (Get_Files_Count, Get_Fils_size, Get_Tree)

        output.insert(INSERT, "Arbol de directorios: " + "\n")
        output.insert(INSERT, Get_Tree() + "\n")

        # imprime el numero de archivos en el directorio.
        output.insert(INSERT, Get_Files_Count() )
        output.insert(INSERT, " archivos indexados, con un tamaño de ")
        output.insert(INSERT, Get_Fils_size() )
        output.insert(INSERT, " bytes." +  "\n\n")

        output.see(END)

    if command.startswith("tree"):
        tree_command()


    # delete_logs
    def delete_logs_command():
        from System.Core.Core import delete_logs

        delete_logs()

        output.insert(INSERT, "Logs eliminados" + "\n")
        output.see(END)

    if command.startswith("delete_logs"):
        delete_logs_command()


    def get_processes_command():
        from System.Core.TaskSystem import get_all_tasks

        output.insert(INSERT, "Procesos: " + "\n")
        output.insert(INSERT, get_all_tasks() + "\n")
        output.see(END)

    if command.startswith("ps"):
        get_processes_command()

    
    def registry_tree_command():
        from System.Core.KeysSystem import reg_tree

        output.insert(INSERT, "Registry: " + "\n")
        output.insert(INSERT, reg_tree() + "\n")
        output.see(END)

    if command.startswith("rtree"):
        registry_tree_command()


# -------------------------------------------------------------------------------------------------------------------------------------------------

    # info, imprime la informacion del sistema base
    def info_command():
        """Info command"""

        import platform

        output.insert(INSERT, "Info: ─────────────────────────────────────────────────────────────────────" + "\n")
        output.insert(INSERT, "Sistema base: " + platform.system() + "\n")
        output.insert(INSERT, "Release: " + platform.release() + "\n")
        output.insert(INSERT, "Version: " + platform.version() + "\n")
        output.insert(INSERT, "Maquina: " + platform.machine() + "\n")
        output.insert(INSERT, "Procesador: " + platform.processor() + "\n")
        output.insert(INSERT, "───────────────────────────────────────────────────────────────────────────" + "\n\n")
        output.see(END)

    if command.startswith("info"):
        info_command()

    # help, va a imprimir la ayuda acerca de todos los comandos, como: help , >.
    def help_command():
        """Help command"""

        output.insert(INSERT, "Ayuda: ────────────────────────────────────────────────────────────────────" + "\n")
        output.insert(INSERT, "print() - imprime un string" + "\n")
        output.insert(INSERT, "add() - suma numeros o une strings" + "\n")
        output.insert(INSERT, "sub() - reta numeros" + "\n")
        output.insert(INSERT, "mul() - multiplica numeros" + "\n")
        output.insert(INSERT, "div() - divide numeros" + "\n")
        output.insert(INSERT, "random(min_number, max_number) - genera un numero aleatorio" + "\n")
        output.insert(INSERT, "\n")
        output.insert(INSERT, "var(variable_name, value) - crea una variable" + "\n")
        output.insert(INSERT, "print_value(variable_name) - imprime el valor de una variable" + "\n")
        output.insert(INSERT, "clear_var(variable_name) - establece el valor de una variable a 0" + "\n")
        output.insert(INSERT, "\n")
        output.insert(INSERT, "repeat(command(args), number) - repite un comando o funcion un numero de veces" + "\n")
        output.insert(INSERT, "\n")
        output.insert(INSERT, "? | dir - imprime el directorio actual" + "\n")
        output.insert(INSERT, "cd(directory) - cambia el directorio actual" + "\n")
        output.insert(INSERT, "mkfolder(Drive/folder_name) - crea una nueva carpeta" + "\n")
        output.insert(INSERT, "mkfile(Drive/folder_name/file_name.extension, content) - crea un nuevo archivo" + "\n")
        output.insert(INSERT, "move_file(C:/folder_name/file_name.extension, to_folder) - mueve un archivo a otra carpeta" + "\n")
        output.insert(INSERT, "Rename_file(folder_name, file_name, extension, new_name, new_extension) - renombra un archivo, ademas de su extension" + "\n")
        output.insert(INSERT, "Import_file(file_path, folder_name) - importa un archivo real del sistema base hasta el sistema de archivos" + "\n")
        output.insert(INSERT, "Execute_file(folder_name, file_name, extension) - ejecuta un archivo .pys (python script)" + "\n")
        output.insert(INSERT, "delete_file(file_name, extension) - borra un archivo" + "\n")
        output.insert(INSERT, "\n")
        output.insert(INSERT, "time - imprime la hora actual" + "\n")
        output.insert(INSERT, "tree - imprime un directorio de arbol de todos los archivos y carpetas" + "\n")
        output.insert(INSERT, "help - imprime esta ayuda" + "\n")
        output.insert(INSERT, "info - imprime la informacion basica del sistema" + "\n")
        output.insert(INSERT, "clear | cls - limpia la pantalla de la terminal" + "\n")
        output.insert(INSERT, "exit - ale de la terminal" + "\n")
        output.insert(INSERT, "\n")
        output.insert(INSERT, ">>> python_command - ejecuta funciones de python" + "\n")
        output.insert(INSERT, "───────────────────────────────────────────────────────────────────────────" + "\n\n")
        output.see(END)

    if command.startswith("help"):
        help_command()
