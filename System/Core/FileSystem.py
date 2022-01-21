import datetime
import json
import random
import sys
from os import urandom

from System.Utils.Utils import print_info

FileSystem = [] # Aqui se guarda y carga temporalmente el systema de archivos


def fs_routines():

    # Carga el sistema de archivos desde el archivo .JSON
    Load_FileSystem()

    # Verifica si existe la crpeta System en el sistema de archivos usando Exist_folder, si no es asi, la crea
    if Exist_folder("C:", "System") == False:
        Create_folder("C:", "System")
        print_info("Se ha creado la carpeta System de nuevo debido a que no existia")

    # Se vuelve a cargar para estar seguros
    Load_FileSystem()
    print_info("Se termino de cargar el sistema de archivos")


# Extensiones ----------------------------------------------------------------------------------------------------------------------------

Index_file_ext = "pfs"
Python_script_extension = "pys"

# Sistema de archivos ---------------------------------------------------------------------------------------------------------------------

FileSystem_directory = "Disk/FileSystem.json"


def save_file():
     with open(FileSystem_directory, "w") as file:
        json.dump(FileSystem, file)


def save_folder():
    with open(FileSystem_directory, "w") as folder:
        json.dump(FileSystem, folder)


def Exist_folder(Drive, FolderName):
    for drive in FileSystem:
        if drive["DriveName"] == Drive:
            for folder in drive["DriveContent"]:
                if folder["FolderName"] == FolderName:
                    return True

    return False


def Exist_file(Drive, FolderName, FileName, FileExtension):
    for drive in FileSystem:
        if drive["DriveName"] == Drive:
            for folder in drive["DriveContent"]:
                if folder["FolderName"] == FolderName:
                    for file in folder["FolderContent"]:
                        if file["FileName"] == FileName and file["FileExtension"] == FileExtension:
                            return True
    return False


def Create_folder(Drive, FolderName):

    # Obtiene la fecha de la ultima modificacion y la retorna como LastWriteTime
    import time
    LastWriteTime = time.strftime("%m/%d/%Y     %H:%M")


    # Si la carpeta ya existe no se crea, en cambio si existe se crea
    if Exist_folder(Drive, FolderName) == True:
        return
    else:
        for drive in FileSystem:
            if drive["DriveName"] == Drive:
                drive["DriveContent"].append({
                    "FolderName": FolderName,
                    "LastWriteTime": LastWriteTime,
                    "FolderContent": [
                        {
                            # Crea un archivo index.pfs, servira para identificar un archivo de una carpeta
                            "FileName": "Index",
                            "FileExtension": Index_file_ext,
                            "FileLastWriteTime": LastWriteTime,
                            "FileContent": "---"
                        }
                    ],
                })

    # Guarda la carpeta en el sistema de archivos en FileSystem
    save_folder()


def Create_file(Drive, FolderName, FileName, FileExtension, FileContent):

    # Obtiene la fecha y la hora de la ultima modificacion
    import time

    LastWriteTime = time.strftime("%m/%d/%Y     %H:%M")

    for drive in FileSystem:
        if drive["DriveName"] == Drive:
            for folder in drive["DriveContent"]:
                if folder["FolderName"] == FolderName:
                    folder["FolderContent"].append({
                        "FileName": FileName,
                        "FileExtension": FileExtension,
                        "FileLastWriteTime": LastWriteTime,
                        "FileContent": FileContent
                    })

    # Guarda los cambios
    save_file()


def Read_file(Drive, FolderName, FileName, FileExtension):

    # retorna el contenid odela rchivo como un string

    content = ""

    for drive in FileSystem:
        if drive["DriveName"] == Drive:
            for folder in drive["DriveContent"]:
                if folder["FolderName"] == FolderName:
                    for file in folder["FolderContent"]:
                        if file["FileName"] == FileName and file["FileExtension"] == FileExtension:
                            content += str(file["FileContent"])

    return content



def Delete_file(Drive, FolderName, FileName, FileExtension):

    for drive in FileSystem:
        if drive["DriveName"] == Drive:
            for folder in drive["DriveContent"]:
                if folder["FolderName"] == FolderName:
                    for file in folder["FolderContent"]:
                        if file["FileName"] == FileName and file["FileExtension"] == FileExtension:
                            folder["FolderContent"].remove(file)

    # Guarda los cambios
    save_file()


def Delete_folder(Drive, FolderName):

    for drive in FileSystem:
        if drive["DriveName"] == Drive:
            for folder in drive["DriveContent"]:
                if folder["FolderName"] == FolderName:
                    drive["DriveContent"].remove(folder)

    # Guarda los cambios
    save_file()


def Rename_file(Drive, FolderName, FileName, FileExtension, NewFileName, NewFileExtension):
    for drive in FileSystem:
        if drive["DriveName"] == Drive:
            for folder in drive["DriveContent"]:
                if folder["FolderName"] == FolderName:
                    for file in folder["FolderContent"]:
                        if file["FileName"] == FileName and file["FileExtension"] == FileExtension:
                            file["FileName"] = NewFileName
                            file["FileExtension"] = NewFileExtension

    # Guarda los cambios
    save_file()


def Rename_folder(Drive, FolderName, NewFolderName):

    # se verifica si no hay ninguna carpeta con el mismo nombre en el drive, en caso de que sea asi, se le agregara un numero aleatorio al final del nombre
    if Exist_folder(Drive, NewFolderName) == True:
        NewFolderName += str(random.randint(1, 255))

    for drive in FileSystem:
        if drive["DriveName"] == Drive:
            for folder in drive["DriveContent"]:
                if folder["FolderName"] == FolderName:
                    folder["FolderName"] = NewFolderName

    # Guarda los cambios
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


def Move_file(Drive, FolderName, FileName, FileExtension, ToDrive, ToFolderName):

    # obtiene los datos del archivo, nombre, extension, contenido, lastwritetime:
    file_data = {}
    for drive in FileSystem:
        if drive["DriveName"] == Drive:
            for folder in drive["DriveContent"]:
                if folder["FolderName"] == FolderName:
                    for file in folder["FolderContent"]:
                        if file["FileName"] == FileName and file["FileExtension"] == FileExtension:
                            file_data = file

    # se elimina el archivo de la carpeta actual
    for drive in FileSystem:
        if drive["DriveName"] == Drive:
            for folder in drive["DriveContent"]:
                if folder["FolderName"] == FolderName:
                    for file in folder["FolderContent"]:
                        if file["FileName"] == FileName and file["FileExtension"] == FileExtension:
                            folder["FolderContent"].remove(file)

    # se agrega el archivo a la carpeta destino
    for drive in FileSystem:
        if drive["DriveName"] == ToDrive:
            for folder in drive["DriveContent"]:
                if folder["FolderName"] == ToFolderName:
                    folder["FolderContent"].append(file_data)

    # Guarda los cambios
    save_file()


def Move_folder(Drive, FolderName, ToDrive):

    # Se obtiene los datos d ela carpeta, como su nombre y archivos
    folder_data = {}
    for drive in FileSystem:
        if drive["DriveName"] == Drive:
            for folder in drive["DriveContent"]:
                if folder["FolderName"] == FolderName:
                    folder_data = folder

    # Se elimina la carpeta de la unidad actual
    for drive in FileSystem:
        if drive["DriveName"] == Drive:
            for folder in drive["DriveContent"]:
                if folder["FolderName"] == FolderName:
                    drive["DriveContent"].remove(folder)

    # Se agrega la carpeta a la unidad destino
    for drive in FileSystem:
        if drive["DriveName"] == ToDrive:
            drive["DriveContent"].append(folder_data)

    # Guarda los cambios
    save_folder()



def Copy_file(Drive, FolderName, FileName, FileExtension, ToDrive, ToFolder):

    # Se obtiene los datos del archivo, nombre, extension, contenido, lastwritetime:
    file_data = {}
    for drive in FileSystem:
        if drive["DriveName"] == Drive:
            for folder in drive["DriveContent"]:
                if folder["FolderName"] == FolderName:
                    for file in folder["FolderContent"]:
                        if file["FileName"] == FileName and file["FileExtension"] == FileExtension:
                            file_data = file

    # Se agrega el archivo a la carpeta destino, si en dicho destino hay un archivo igual con mismo nombre y extension, se renombra la copia del archivo agregndole un numero leatorio al final del nombre, por ejemplo file2.txt, mientras que el archivo original es file.txt, osea no se renombra
    for drive in FileSystem:
        if drive["DriveName"] == ToDrive:
            for folder in drive["DriveContent"]:
                if folder["FolderName"] == ToFolder:
                    for file in folder["FolderContent"]:
                        if file["FileName"] == FileName and file["FileExtension"] == FileExtension:
                            file["FileName"] += str(random.randint(1, 255))

    # Se agrega el archivo a la carpeta destino
    for drive in FileSystem:
        if drive["DriveName"] == ToDrive:
            for folder in drive["DriveContent"]:
                if folder["FolderName"] == ToFolder:
                    folder["FolderContent"].append(file_data)


    # Guarda los cambios
    save_file()


def Copy_folder(Drive, FolderName, ToDrive):

    # Se obtiene los datos de la carpeta, como su nombre y archivos
    folder_data = {}
    for drive in FileSystem:
        if drive["DriveName"] == Drive:
            for folder in drive["DriveContent"]:
                if folder["FolderName"] == FolderName:
                    folder_data = folder

    # si en el destino  hay una carpeta con el mismo nombre, se le agrega un numero aleatorio al final del nombre
    for drive in FileSystem:
        if drive["DriveName"] == ToDrive:
            for folder in drive["DriveContent"]:
                if folder["FolderName"] == FolderName:
                    folder["FolderName"] += str(random.randint(1, 255))

    # Se agrega la carpeta a la unidad destino
    for drive in FileSystem:
        if drive["DriveName"] == ToDrive:
            drive["DriveContent"].append(folder_data)

    # Guarda los cambios
    save_folder()


def Open_file( FileName, FileExtension):
    # Obtiene el contenido del archivo
    for drive in FileSystem:
        for folder in drive["DriveContent"]:
            if folder["FolderName"] == "System":
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
        FileSystem_string += "" + drive["DriveName"] + "/" + "\n"
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
        Tree_string += drive["DriveName"] + "\n"
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
                if file["FileName"] == "Index" and file["FileExtension"] == Index_file_ext:
                    FileSystem_string += "    ├─ Index" + "." + Index_file_ext + "\n"
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

    global Result
    Result = ""

    # obtiene el contenido, lo ejecuta y obtiene la salida
    for drive in FileSystem:
        for folder in drive["DriveContent"]:
            if folder["FolderName"] == FolderName:
                for file in folder["FolderContent"]:
                    if file["FileName"] == FileName and file["FileExtension"] == FileExtension:
                        try:
                            code = compile(file["FileContent"], "<string>", "exec")
                            exec(code, globals())
                        except Exception as e:
                            Result += e
                            Result += "\n"

    return Result



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
