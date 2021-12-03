import json

from System.Utils.Utils import print_log

Kernel_lvl = 6  # Variable principal de nucleo o kernel

# Cada pantalla tiene un ID
Is_FAIL =           False  # 0
Is_in_BIOS =        False  # 1
Is_in_INSTALLER =   False  # 2
Is_in_Boot =        False  # 3
Is_in_Login =       False  # 4
Is_in_Desktop =     False  # 5
Is_Boot =           False  # 6


# Inicia el orden de arranque
if Kernel_lvl == 0:
    Is_FAIL = True

elif Kernel_lvl == 1:
    Is_in_BIOS = True

elif Kernel_lvl == 2:
    Is_in_INSTALLER = True

elif Kernel_lvl == 3:
    Is_in_Boot = True

elif Kernel_lvl == 4:
    Is_in_Login = True

elif Kernel_lvl == 5:
    Is_in_Desktop = True

elif Kernel_lvl == 6:
    Is_Boot = True


# Rutinas
def routines():

    print_log("--- Comenzando la ejecucion del sistema ---")


def delete_logs():
    # Borra los archivos dentro de la carpeta Logs usando el modulo os
    import os
    from System.Utils.Utils import print_info

    # Obtiene la ruta relativa de la carpeta Logs
    Logs_path = os.path.join(os.getcwd(), "Logs")

    # Obtiene la lista de archivos dentro de la carpeta Logs
    Logs_files = os.listdir(Logs_path)

    # Imprime un mensaje de informacion
    print_info("Borrando archivos de la carpeta Logs")

    # Borra los archivos dentro de la carpeta Logs
    for file in Logs_files:
        os.remove(os.path.join(Logs_path, file))
        print(os.path.join(Logs_path, file))



# Sistema de archivos ---------------------------------------------------------------------------------------------------------------------

FileSystem_directory = "Disk/FileSystem.json"

FileSystem = []
Index_file_extension = "pfs"
Python_script_extension = "pys"

# El sistema de archivos tiene esta estructura (No es muy avanzada, pero funciona)
#[
#    {
#        "DriveName": "C:",
#        "DriveContent": [
#            {
#                "FolderContent": [
#                    {
#                        "FileName": "",
#                        "FileExtension": "",
#                        "FileContent": ""
#                    }
#                ]
#            },
#            {
#                "FolderName": "",
#                "FolderContent": [
#                    {
#                        "SubFolderName": "",
#                        "SubFolderContent": [
#                            {
#                                "SubFileName": "",
#                                "SubFileExtension": "",
#                                "SubFileContent": ""
#                            }
#                        ]
#                    },
#                    {
#                        "FileName": "",
#                        "FileExtension": "",
#                        "FileContent": ""
#                    }
#                ]
#            }
#        ]
#    }
#]

def save_file():
     with open(FileSystem_directory, "w") as file:
        json.dump(FileSystem, file)


def save_folder():
    with open(FileSystem_directory, "w") as folder:
        json.dump(FileSystem, folder)


def Create_folder(FolderName):

    # Obtiene la fecha de la ultima modificacion y la retorna como LastWriteTime
    import time
    LastWriteTime = time.strftime("%m-%d-%Y     %H:%M")


    # Crea una carpeta en el contenido del disco
    for drive in FileSystem:
        drive["DriveContent"].append({
            "FolderName": FolderName,
            "FolderContent": [
                {
                    # Crea un archivo index.pfs, servira para identificar un archivo de una carpeta
                    "FileName": "Index",
                    "FileExtension": Index_file_extension,
                    "FileLastWriteTime": LastWriteTime,
                    "FileContent": "---"
                }
            ]
        })

    # Guarda la carpeta en el sistema de archivos en FileSystem
    save_folder()


def Create_file(FileName, FileExtension, FileContent):

    # Obtiene la fecha y la hora de la ultima modificacion
    import time
    LastWriteTime = time.strftime("%m/%d/%Y     %H:%M")

    # por defecto, crea el archivo dentro de la carpeta "Main".
    for drive in FileSystem:
        for folder in drive["DriveContent"]:
            if folder["FolderName"] == "Main":
                folder["FolderContent"].append({
                    "FileName": FileName,
                    "FileExtension": FileExtension,
                    "FileLastWriteTime": LastWriteTime,
                    "FileContent": FileContent
                })

    # Guarda el archivo dentro del sistema de archivos en FileSystem
    save_file()


def Read_file(FolderName, FileName, FileExtension):
    # Obtiene el contenido del archivo.
    for drive in FileSystem:
        for folder in drive["FolderContent"]:
            if folder["FolderName"] == FolderName:
                for file in folder["FolderContent"]:
                    if file["FileName"] == FileName and file["FileExtension"] == FileExtension:
                        return file["FileContent"]


def Delete_file(FolderName, FileName, FileExtension):
    for drive in FileSystem:
        for folder in drive["DriveContent"]:
            if folder["FolderName"] == FolderName:
                for file in folder["FolderContent"]:
                    if file["FileName"] == FileName and file["FileExtension"] == FileExtension:
                        folder["FolderContent"].remove(file)

    # Guarda el archivo dentro del sistema de archivos en FileSystem
    save_file()


def Delete_folder(FolderName):
    for drive in FileSystem:
        for folder in drive["DriveContent"]:
            if folder["FolderName"] == FolderName:
                drive["DriveContent"].remove(folder)

    # save the folder in FileSystem
    save_folder()


def Rename_file(FolderName, FileName, FileExtension, NewFileName, NewFileExtension):
    for drive in FileSystem:
        for folder in drive["DriveContent"]:
            if folder["FolderName"] == FolderName:
                for file in folder["FolderContent"]:
                    if file["FileName"] == FileName and file["FileExtension"] == FileExtension:
                        file["FileName"] = NewFileName
                        file["FileExtension"] = NewFileExtension

    # save the file in FileSystem
    save_file()


def Rename_folder(FolderName, NewFolderName):
    for drive in FileSystem:
        for folder in drive["DriveContent"]:
            if folder["FolderName"] == FolderName:
                folder["FolderName"] = NewFolderName

    # save the folder in FileSystem
    save_folder()


def Clear_file(FolderName, FileName, FileExtension):
    for drive in FileSystem:
        for folder in drive["DriveContent"]:
            if folder["FolderName"] == FolderName:
                for file in folder["FolderContent"]:
                    if file["FileName"] == FileName and file["FileExtension"] == FileExtension:
                        file["FileContent"] = ""

    # save the file in FileSystem
    save_file()


def Move_file(FileName, FileExtension, FromFolderName, ToFolderName):

    import time
    LastWriteTime = time.strftime("%m/%d/%Y     %H:%M")

    for drive in FileSystem:
        for folder in drive["DriveContent"]:
            if folder["FolderName"] == FromFolderName:
                for file in folder["FolderContent"]:
                    if file["FileName"] == FileName and file["FileExtension"] == FileExtension:
                        file_content = file["FileContent"]
                        file_name = file["FileName"]
                        file_extension = file["FileExtension"]
                        break

    # make the file in the destination folder.
    for drive in FileSystem:
        for folder in drive["DriveContent"]:
            if folder["FolderName"] == ToFolderName:
                folder["FolderContent"].append({
                    "FileName": file_name,
                    "FileExtension": file_extension,
                    "FileLastWriteTime": LastWriteTime,
                    "FileContent": file_content
                })

    # delete the old file
    for drive in FileSystem:
        for folder in drive["DriveContent"]:
            if folder["FolderName"] == FromFolderName:
                for file in folder["FolderContent"]:
                    if file["FileName"] == FileName and file["FileExtension"] == FileExtension:
                        folder["FolderContent"].remove(file)

    # Guarda los cambios
    save_file()


def Copy_file(FileName, FileExtension, Folder):
    FileSystem[Folder]["FolderContent"].append(FileName)

    # Guarda los cambios
    save_file()


def Copy_folder(FolderName, NewFolderName):
    FileSystem[NewFolderName]["FolderContent"].append(FolderName)

    # Guarda los cambios
    save_folder()


def Open_file( FileName, FileExtension):
    # Obtiene el contenido del archivo
    for drive in FileSystem:
        for folder in drive["DriveContent"]:
            if folder["FolderName"] == "Main":
                for file in folder["FolderContent"]:
                    if file["FileName"] == FileName and file["FileExtension"] == FileExtension:
                        return file["FileContent"]


def Open_folder(FolderName):
    # Obtiene el contenido de la carpeta
    for drive in FileSystem:
        for folder in drive["DriveContent"]:
            if folder["FolderName"] == FolderName:
                return folder["FolderContent"]


# Guarda todos los cambios del sistema de archivos a FileSsystem.json usando la lista FileSystem[]
def Save_FileSystem():
    with open("Disk/FileSystem.json", "w") as file:
        json.dump(FileSystem, file, sort_keys=False, indent=4)


# Carga el sistema de archivos desde FileSystem.json
def Load_FileSystem():

    # global para que pueda ser leido
    global FileSystem

    with open("Disk/FileSystem.json", "r") as file:
        FileSystem = json.load(file)


def Get_FileSystem():

    # Carga el sistema de archivos para no tener que reiniciar.
    Load_FileSystem()

    # Variable donde se almacena la informacion
    FileSystem_string = ""

    # Calcula el tamaño del archivo en bytes según el número de caracteres dentro del contenido del archivo.
    def file_size(FileContent):
        FileSize_string = str(len(FileContent)) + " bytes"
        return FileSize_string

    # Retorna el contenido del sistema de archivos dentro de un string por cada carpeta y archivo dentro.
    for drive in FileSystem:
        for folder in drive["DriveContent"]:
            FileSystem_string += "    " + folder["FolderName"] + "/" + "\n"
            for file in folder["FolderContent"]:
                FileSystem_string += "        " + file["FileLastWriteTime"] + "     " + file_size(file["FileContent"]) + "    " + file["FileName"] + "." + file["FileExtension"] + "\n"

    return FileSystem_string


# Obtiene el recuento de archivos y carpetas.
def Get_Files_Count():
    Load_FileSystem()

    Files_Count = 0

    for drive in FileSystem:
        for folder in drive["DriveContent"]:
            for files in folder["FolderContent"]:
                Files_Count += 1

                if Files_Count == -1:
                    print(files)

    return Files_Count


# Calcula el tamaño total del archivo en bytes de todo el sistema de archivos en función del número de caracteres dentro del contenido del archivo.
def Get_Fils_size():
    Load_FileSystem()

    FileSize = 0

    for drive in FileSystem:
        for folder in drive["DriveContent"]:
            for file in folder["FolderContent"]:
                FileSize += len(file["FileContent"])

    return FileSize


def Get_Tree():

    Load_FileSystem()

    Tree_string = ""

    for drive in FileSystem:
        Tree_string += drive["DriveName"] + ":\n"
        for folder in drive["DriveContent"]:

            # si es la última carpeta en la unidad, agrega un salto de línea.
            if folder == drive["DriveContent"][-1]:
                Tree_string += "└─── " + folder["FolderName"] + "\n"

                for file in folder["FolderContent"]:
                    # si es el último archivo de la carpeta, agrega un salto de línea.
                    if file == folder["FolderContent"][-1]:
                        Tree_string += "     └─── " + file["FileName"] + "." + file["FileExtension"] + "\n"
                    else:
                        Tree_string += "     ├─── " + file["FileName"] + "." + file["FileExtension"] + "\n"
            else:
                Tree_string += "├─── " + folder["FolderName"] + "\n"

                for file in folder["FolderContent"]:
                    # si es el último archivo de la carpeta, agrega un salto de línea.
                    if file == folder["FolderContent"][-1]:
                        Tree_string += "│    └─── " + file["FileName"] + "." + file["FileExtension"] + "\n"
                    else:
                        Tree_string += "│    ├─── " + file["FileName"] + "." + file["FileExtension"] + "\n"

    return Tree_string


def Tree_FileSystem_Advanced():

    FileSystem_string = ""

    for drive in FileSystem:
        FileSystem_string += drive["DriveName"] + ">──┐" + "\n"

        for folder in drive["DriveContent"]:

            # si es la última carpeta del directorio, se pone un └─, si no un ├─
            if folder == drive["DriveContent"][-1]:
                FileSystem_string += " └─ " + folder["FolderName"] + "/" + "\n"
            else:
                FileSystem_string += " ├─ " + folder["FolderName"] + "/" + "\n"

            for file in folder["FolderContent"]:
                if file["FileName"] == "Index" and file["FileExtension"] == Index_file_extension:
                    FileSystem_string += "    ├─ Index" + "." + Index_file_extension + "\n"
                else:

                    # si es el ultimo archivo de la carpeta, se pone un └─, si no un ├─
                    if file == folder["FolderContent"][-1]:
                        FileSystem_string += "    └─ " + file["FileName"] + "." + file["FileExtension"] + "\n"
                    else:
                        FileSystem_string += "    ├─ " + file["FileName"] + "." + file["FileExtension"] + "\n"

    return FileSystem_string


def Format_FileSystem():
    global FileSystem

    # Borra todo el contenido del sistema de archivos.
    FileSystem = []

    # save the file in FileSystem
    save_file()


# Import_file, importa un archivo real y su contenido al sistema de archivos, ejemplo: import_file(C:/Users/User/Desktop/file.txt, "txt", "Main")
def Import_file(FilePath, ToFolderName):
    global FileSystem

    # obtiene el nombre del archivo sin la extensión.
    FileName = FilePath.split("/")[-1].split(".")[0]

    # obtiene la extension del archivo.
    FileExtension = FilePath.split("/")[-1].split(".")[1]

    # obtiene el contenido del archivo.
    with open(FilePath, "r") as file:
        FileContent = file.read()

    # crea un nuevo archivo en el sistema de archivos, con el nombre, extension y contenido del archivo. importado
    for drive in FileSystem:
        for folder in drive["DriveContent"]:
            if folder["FolderName"] == ToFolderName:
                folder["FolderContent"].append({"FileName": FileName, "FileExtension": FileExtension, "FileContent": FileContent, "FileLastWriteTime": "Invalido"})

    # guarda los cambios
    save_file()


# Execute_file, si el archivo tiene la extensión pys, ejecutará el código que tiene como contenido en python.
def Execute_file(FolderName, FileName, FileExtension):
    # obtiene el contenido
    for drive in FileSystem:
        for folder in drive["DriveContent"]:
            if folder["FolderName"] == FolderName:
                for file in folder["FolderContent"]:
                    if file["FileName"] == FileName and file["FileExtension"] == FileExtension:
                        if file["FileExtension"] == Python_script_extension:
                            exec(file["FileContent"])
                        else:
                            print("This file can not be executed.")

    # obtiene el resultado o la salida (exec) del código ejecutado en un String.
    def get_result():
        result = ""

        for drive in FileSystem:
            for folder in drive["DriveContent"]:
                if folder["FolderName"] == FolderName:
                    for file in folder["FolderContent"]:
                        if file["FileName"] == FileName and file["FileExtension"] == FileExtension:
                            result = file["FileContent"]
        return result

    return get_result()



# Export_file, export a file from the file system to a real file.
def Export_file(FolderName, FileName, FileExtension, ToPath):
    # get the file content.
    for drive in FileSystem:
        for folder in drive["DriveContent"]:
            if folder["FolderName"] == FolderName:
                for file in folder["FolderContent"]:
                    if file["FileName"] == FileName and file["FileExtension"] == FileExtension:
                        with open(ToPath, "w") as file:
                            file.write(file["FileContent"])

    # save the file in FileSystem
    save_file()









