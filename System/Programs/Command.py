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
    from System.Utils.Utils import print_log, print_error, print_warning, print_info


    command = entry.get()
    entry.delete(0, END)

    # Commands ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
            # En caso de que el comando n otenga parentesis para declarar los argumentos, se mostrara un error
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

        output.insert(INSERT, "Carpeta " + command + " creada" + "\n")
        print_log("[mkfolder]" + " Carpeta " + command + " creada")
        output.see(END)
    
    if command.startswith("mkfolder("):
        mkfolder_command(command)
    

    def mkfile_command(command):

        from System.Core.Core import Create_file, Save_FileSystem, Move_file

        command = command.replace("mkfile(", "")
        command = command.replace(")", "")
        command = command.split(", ")

        file_name = command[0]
        extension = command[1]    
        content = command[2]

        Create_file(file_name, extension, content)  
        Save_FileSystem()

        output.insert(INSERT, "Archivo " + file_name + "." + extension + " creado" + "\n")
        print_log("[mkfile]" + " Archivo " + file_name + "." + extension + " creado")
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
        from_folder_name = command[2]
        to_folder_name = command[3]
        Move_file(file_name, extension, from_folder_name, to_folder_name)
        Save_FileSystem()

        if file_name == "Index" and extension == "pfs":
            output.insert(INSERT, "No es posible mover el archivo " + file_name + "." + extension + "\n")
            print_error("[move_file]" + " No es posible mover el archivo " + file_name + "." + extension)

        else:
            output.insert(INSERT, "Archivo " + file_name + "." + extension + " movido desde " + from_folder_name + " hacia " + to_folder_name + "\n")
            print_log("[move_file]" + " File " + file_name + "." + extension + " movido desde " + from_folder_name + " hacia " + to_folder_name)

        output.see(END)

    if command.startswith("move_file("):
        move_file_command(command)

    
    # delete_file command will delete a file, like: delete_file(file_name, extension) , > .
    def delete_file_command(command):

        from System.Core.Core import Delete_file, Save_FileSystem

        command = command.replace("delete_file(", "")
        command = command.replace(")", "")
        command = command.split(", ")

        folder_name = command[0]
        file_name = command[1]
        extension = command[2]

        Delete_file(folder_name, file_name, extension)
        Save_FileSystem()

        output.insert(INSERT, "Archivo " + file_name + "." + extension + " borrado desde " + folder_name + "\n")
        print_log("[delete_file]" + " Archivo " + file_name + "." + extension + " borrado desde " + folder_name)
        output.see(END)

    if command.startswith("delete_file("):
        delete_file_command(command)


    def delete_folder_command(command):

        from System.Core.Core import Delete_folder, Save_FileSystem

        command = command.replace("delete_folder(", "")
        command = command.replace(")", "")

        Delete_folder(command)
        Save_FileSystem()

        output.insert(INSERT, "Carpeta " + command + " borrada" + "\n")
        print_log("[mkfolder]" + " Carpeta " + command + " borrada")
        output.see(END)

    if command.startswith("delete_folder("):
        delete_folder_command(command)

    
    def rename_file_command(command):

        from System.Core.Core import Rename_file, Save_FileSystem

        command = command.replace("rename_file(", "")
        command = command.replace(")", "")
        command = command.split(", ")

        folder_name = command[0]
        file_name = command[1]
        extension = command[2]
        new_file_name = command[3]
        new_extension = command[4]

        Rename_file(folder_name, file_name, extension, new_file_name, new_extension)
        Save_FileSystem()

        output.insert(INSERT, "Archivo " + file_name + "." + extension + " de " + folder_name + " renombrado como " + new_file_name + "." + new_extension + "\n")
        print_log("[rename_file]" + " Archivo " + file_name + "." + extension + " de " + folder_name + " renombrado como " + new_file_name + "." + new_extension)
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
        to_folder_name = command[1]

        Import_file(file_path, to_folder_name)
        Save_FileSystem()

        output.insert(INSERT, "File form path " + file_path + " imported to " + to_folder_name + "\n")
        print_log("[import_file]" + " File form path " + file_path + " imported to " + to_folder_name)
        output.see(END)

    if command.startswith("import_file("):
        import_file_command(command)
    

    def export_file_command(command):

        from System.Core.Core import Export_file, Save_FileSystem

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
        print_log("[export_file]" + " Archivo " + file_name + "." + extension + " de " + folder_name + " exportado hacia " + file_path)
        output.see(END)

    if command.startswith("export_file("):
        export_file_command(command)


    def execute_file(command):

        from System.Core.Core import Execute_file, Save_FileSystem

        command = command.replace("execute_file(", "")
        command = command.replace(")", "")
        command = command.split(", ")

        folder_name = command[0]
        file_name = command[1]
        extension = command[2]

        Save_FileSystem()

        # insert the code result.
        print_log("[execute_file]" + " Archivo " + file_name + "." + extension + " ejecutado")
        output.insert(INSERT, Execute_file(folder_name, file_name, extension))
        output.insert(INSERT,  "\n")

        output.see(END)

    if command.startswith("execute_file("):
        execute_file(command)
    

    # dir command will print the directory of the current file (using the filesystem in core.py), like: dir() , > dir.
    def dir_command():

        from System.Core.Core import Get_FileSystem, Get_Files_Count

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
        from System.Core.Core import Get_Files_Count, Get_Fils_size, Get_Tree

        output.insert(INSERT, "Arbol de directorios: " + "\n")
        output.insert(INSERT, Get_Tree() + "\n")

        # imprime el numero de archivos en el directorio.
        output.insert(INSERT, "[")
        output.insert(INSERT, Get_Files_Count() )
        output.insert(INSERT, "]" + " archivos indexados, con un tamaño de ")
        output.insert(INSERT, Get_Fils_size() )
        output.insert(INSERT, " bytes." +  "\n\n")

        output.see(END)

    if command.startswith("tree"):
        tree_command()


# -------------------------------------------------------------------------------------------------------------------------------------------------

    # info, imprime la informacion del sistema base
    def info_command():
        """Info command"""

        import platform

        output.insert(INSERT, "Info: ---------------------------------------------------------------------" + "\n")
        output.insert(INSERT, "Sistema base: " + platform.system() + "\n")
        output.insert(INSERT, "Release: " + platform.release() + "\n")
        output.insert(INSERT, "Version: " + platform.version() + "\n")
        output.insert(INSERT, "Maquina: " + platform.machine() + "\n")
        output.insert(INSERT, "Procesador: " + platform.processor() + "\n")
        output.insert(INSERT, "---------------------------------------------------------------------------" + "\n\n")
        output.see(END)
    
    if command.startswith("info"):
        info_command()

    # help, va a imprimir la ayuda acerca de todos los comandos, como: help , >.
    def help_command():
        """Help command"""

        output.insert(INSERT, "Ayuda: --------------------------------------------------------------------" + "\n")
        output.insert(INSERT, "print() - imprime un string" + "\n")
        output.insert(INSERT, "add() - suma numeros o une strings" + "\n")
        output.insert(INSERT, "sub() - reta numeros" + "\n")
        output.insert(INSERT, "mul() - multiplica numeros" + "\n")
        output.insert(INSERT, "div() - divide numeros" + "\n")
        output.insert(INSERT, "random(max_number) - genera un numero aleatorio" + "\n")
        output.insert(INSERT, "\n")
        output.insert(INSERT, "var(variable_name, value) - crea una variable" + "\n")
        output.insert(INSERT, "print_value(variable_name) - imprime el valor de una variable" + "\n")
        output.insert(INSERT, "clear_var(variable_name) - establece el valor de una variable a 0" + "\n")
        output.insert(INSERT, "\n")
        output.insert(INSERT, "repeat(command(args), number) - repite un comando o funcion un numero de veces" + "\n")
        output.insert(INSERT, "\n")
        output.insert(INSERT, "? | dir - imprime el directorio actual" + "\n")
        output.insert(INSERT, "cd(directory) - cambia el directorio actual" + "\n")
        output.insert(INSERT, "mkfolder(folder_name) - crea una nueva carpeta" + "\n")
        output.insert(INSERT, "mkfile(file_name, extension, content) - crea un nuevo archivo" + "\n")
        output.insert(INSERT, "move_file(file_name, extension, from_folder, to_folder) - mueve un archivo a otra carpeta" + "\n")
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
        output.insert(INSERT, "---------------------------------------------------------------------------" + "\n\n")
        output.see(END)

    if command.startswith("help"):
        help_command()
