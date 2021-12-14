import datetime
from System.Core.FileSystem import fs_routines
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


# Rutinas, son las primeras tareas que se ejecutan en los primeros segundos del arranque del sistema
def routines():

    print_log("\n" + "--- Comenzando la ejecucion del sistema ---")


    # Carga el sistema de archivos
    fs_routines()


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


# Sistema de procesos ----------------------------------------------------------------------------------------------------

Processes = []

# Los procesos tienen la siguiente extructura:
# {
#     "ProcessName": "",
#     "ProcessStatus": "",
#     "ProcessPriority": "",
#     "ProcessMemory": "",
#     "ProcessCPU": "",
#     "ProcessStartTime": "",
#     "ProcessEndTime": "",
#     "ProcessDuration": "",
#     "ProcessProgram": ""
# },
# {
#     "ProcessName": "",
#     "ProcessStatus": "",
#     "ProcessPriority": "",
#     "ProcessMemory": "",
#     "ProcessCPU": "",
#     "ProcessStartTime": "",
#     "ProcessEndTime": "",
#     "ProcessDuration": "",
#     "ProcessProgram": ""
# }

def Save_Process():
    global Processes

    # Guarda loss procesos en Processes.json
    with open("Disk/Processes.json", "w") as file:
        json.dump(Processes, file)


def Start_process(ProcessName, ProcessProgram, ProcessPriority):
    global Processes

    time = datetime.datetime.now()
    # GET THE TIME AAS INT
    current_time = int(time.strftime("%H%M%S"))

    # crea un nuevo proceso
    Processes.append({
        "ProcessName": ProcessName,
        "ProcessStatus": "Running",
        "ProcessPriority": ProcessPriority,
        "ProcessMemory": 0,
        "ProcessCPU": 0,
        "ProcessStartTime": current_time,
        "ProcessEndTime": 0,
        "ProcessDuration": 0,
        "ProcessProgram": ProcessProgram
    })

    # guarda los cambios
    Save_Process()


def Stop_process(ProcessName):
    global Processes
    import datetime

    time = datetime.datetime.now()
    # GET THE TIME AAS INT
    current_time = int(time.strftime("%H%M%S"))

    # obtiene el proceso
    for process in Processes:
        if process["ProcessName"] == ProcessName:
            # cambia el estado del proceso
            process["ProcessStatus"] = "Terminated"

            # obtiene el tiempo de inicio y finalización del proceso
            process["ProcessEndTime"] = current_time
            process["ProcessDuration"] = process["ProcessEndTime"] - process["ProcessStartTime"]

            # guarda los cambios
            Save_Process()


def Update_Process_Status(ProcessName, ProcessStatus):
    global Processes

    # obtiene el proceso
    for process in Processes:
        if process["ProcessName"] == ProcessName:
            # cambia el estado del proceso
            process["ProcessStatus"] = ProcessStatus

            # guarda los cambios
            Save_Process()


def Update_Process_Memory(ProcessName, ProcessMemory):
    global Processes

    # obtiene el proceso
    for process in Processes:
        if process["ProcessName"] == ProcessName:
            # cambia el estado del proceso
            process["ProcessMemory"] = ProcessMemory

            # guarda los cambios
            Save_Process()


def Update_Process_CPU(ProcessName, ProcessCPU):
    global Processes

    # obtiene el proceso
    for process in Processes:
        if process["ProcessName"] == ProcessName:
            # cambia el estado del proceso
            process["ProcessCPU"] = ProcessCPU

            # guarda los cambios
            Save_Process()


def Get_Processes():
    global Processes

    # Retorna como un String con la siguiente estructura pro ejemplo:
    # Processes:
    #     - ProcessName: "Proceso1"
    #       ProcessStatus: "Running"
    #       ProcessPriority: "Normal"
    #       ProcessMemory: "0"
    #       ProcessCPU: "0"
    #       ProcessStartTime: "Invalido"
    #       ProcessEndTime: "Invalido"
    #       ProcessDuration: "Invalido"
    #       ProcessProgram: "Proceso1.py"
    #
    #     - ProcessName: "Proceso2"
    #       ProcessStatus: "Running"
    #       ProcessPriority: "Normal"
    #       ProcessMemory: "0"
    #       ProcessCPU: "0"
    #       ProcessStartTime: "Invalido"
    #       ProcessEndTime: "Invalido"
    #       ProcessDuration: "Invalido"
    #       ProcessProgram: "Proceso2.py"

    # obtiene los procesos
    processes_list = ""

    for process in Processes:
        processes_list += "- ProcessName: " + process["ProcessName"] + "\n"
        processes_list += "  ProcessStatus: " + process["ProcessStatus"] + "\n"
        processes_list += "  ProcessPriority: " + process["ProcessPriority"] + "\n"
        processes_list += "  ProcessMemory: " + str(process["ProcessMemory"]) + "\n"
        processes_list += "  ProcessCPU: " + str(process["ProcessCPU"]) + "\n"
        processes_list += "  ProcessStartTime: " + str(process["ProcessStartTime"]) + "\n"
        processes_list += "  ProcessEndTime: " + str(process["ProcessEndTime"]) + "\n"
        processes_list += "  ProcessDuration: " + str(process["ProcessDuration"]) + "\n"
        processes_list += "  ProcessProgram: " + process["ProcessProgram"] + "\n"

    return processes_list


def Get_Process(ProcessName):
    global Processes

    # Retorna como un String con la siguiente estructura pro ejemplo:
    # Processes:
    #     - ProcessName: "Proceso1"
    #       ProcessStatus: "Running"
    #       ProcessPriority: "Normal"
    #       ProcessMemory: "0"
    #       ProcessCPU: "0"
    #       ProcessStartTime: "Invalido"
    #       ProcessEndTime: "Invalido"
    #       ProcessDuration: "Invalido"
    #       ProcessProgram: "Proceso1.py"
    #
    #     - ProcessName: "Proceso2"
    #       ProcessStatus: "Running"
    #       ProcessPriority: "Normal"
    #       ProcessMemory: "0"
    #       ProcessCPU: "0"
    #       ProcessStartTime: "Invalido"
    #       ProcessEndTime: "Invalido"
    #       ProcessDuration: "Invalido"
    #       ProcessProgram: "Proceso2.py"

    # obtiene los procesos
    processes_list = ""

    for process in Processes:
        if process["ProcessName"] == ProcessName:
            processes_list += "- ProcessName: " + process["ProcessName"] + "\n"
            processes_list += "  ProcessStatus: " + process["ProcessStatus"] + "\n"
            processes_list += "  ProcessPriority: " + process["ProcessPriority"] + "\n"
            processes_list += "  ProcessMemory: " + process["ProcessMemory"] + "\n"
            processes_list += "  ProcessCPU: " + process["ProcessCPU"] + "\n"
            processes_list += "  ProcessStartTime: " + process["ProcessStartTime"] + "\n"
            processes_list += "  ProcessEndTime: " + process["ProcessEndTime"] + "\n"
            processes_list += "  ProcessDuration: " + process["ProcessDuration"] + "\n"
            processes_list += "  ProcessProgram: " + process["ProcessProgram"] + "\n"

    return processes_list


def Clear_processes():
    global Processes

    # limpia los procesos
    Processes = ""

    # guarda los cambios
    Save_Process()










