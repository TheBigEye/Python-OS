import json
import random

from System.Utils.Utils import print_error, print_info, print_warning


# Sistema de tareas -----------------------------------------------------------------------------------------------------------------------

TaskSystem = []

def ts_routines():
    """
    Rutinas del sistema de tareas
    """

    # carga el sistema de tareas desde el archivo .JSON
    Load_TaskSystem()

    # verifica si existen tareas dentro del archivo, en caso de ser asi, todas las tareas seran borradas
    close_all_tasks()

    # se crea el proceso del sistema "System", los valores de CPU, RAM, Disk y Network son aleatorios
    add_task("System", random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), "normal", "running")

    print_info("Se termino de cargar los procesos")


TaskSystem_directory = "Disk/TaskSystem.json"

def save_task():
    global TaskSystem
    with open(TaskSystem_directory, "w") as task:
        json.dump(TaskSystem, task)


def load_task():
    global TaskSystem
    with open(TaskSystem_directory, "r") as task:
        TaskSystem = json.load(task)


def Exist_task(ProgramName):
    global TaskSystem
    for task in TaskSystem:
        if task["Program_name"] == ProgramName:
            return True
    return False


def add_task(ProgramName, CPU, RAM, Disk, Network, Priority, Status):
    """
    Agrega un proceso al sistema de tareas
    """
    global TaskSystem
    TaskSystem.append({
        "Program_name": ProgramName,
        "Program_info": [
            {
                "CPU": CPU,
                "RAM": RAM,
                "Disk": Disk,
                "Network": Network,
                "Priority": Priority,
                "Status": Status
            }
        ]
    })

    save_task()


def stop_task(ProgramName):
    """
    Detiene un proceso
    """

    global TaskSystem
    for task in TaskSystem:
        if task["Program_name"] == ProgramName:
            task["Program_info"][0]["Status"] = "Terminated"
            save_task()


def update_task(ProgramName, CPU, RAM, Disk, Network, Priority, Status):
    """
    Actualiza los valores de CPU, RAM, Disk, Network, Priority y Status de un proceso
    """

    global TaskSystem
    for task in TaskSystem:
        if task["Program_name"] == ProgramName:
            task["Program_info"][0]["CPU"] = CPU
            task["Program_info"][0]["RAM"] = RAM
            task["Program_info"][0]["Disk"] = Disk
            task["Program_info"][0]["Network"] = Network
            task["Program_info"][0]["Priority"] = Priority
            task["Program_info"][0]["Status"] = Status

    save_task()


def close_all_tasks():
    """
    Verifica si existen tareas dentro del archivo, en caso de ser asi, todas las tareas seran borradas
    """

    global TaskSystem

    # se borra el contenido del archivo dejandolo en blanco
    TaskSystem = []

    # se guarda el archivo
    save_task()


def get_task(ProgramName):
    global TaskSystem
    for task in TaskSystem:
        if task["Program_name"] == ProgramName:
            return str(task)


def get_all_tasks():
    global TaskSystem
    tasks = ""

    tasks += "╔══════════════════════════════════════════════════════════════════╗\n"
    tasks += "║[program]     [cpu]  [ram]  [disk] [network] [priority] [status]  ║\n"
    tasks += "║──────────────────────────────────────────────────────────────────║\n"

    for task in TaskSystem:
        # se imprime cada uno de los procesos, los valores deben estar alineados
        tasks += "║" + task["Program_name"].ljust(13) + "|" + str(task["Program_info"][0]["CPU"]).ljust(5) + "%|" + str(task["Program_info"][0]["RAM"]).ljust(5) + "%|" + str(task["Program_info"][0]["Disk"]).ljust(5) + "%|" + str(task["Program_info"][0]["Network"]).ljust(5) + "%|".ljust(7) + str(task["Program_info"][0]["Priority"]).ljust(5) + "|".ljust(3) + str(task["Program_info"][0]["Status"]).ljust(6) + "|".ljust(3) + "║" + "\n"

    tasks += "╚══════════════════════════════════════════════════════════════════╝\n"

    return tasks


def Load_TaskSystem():
    """
    Carga el sistema de tareas desde el archivo .JSON
    """

    global TaskSystem
    with open(TaskSystem_directory, "r") as task:
        TaskSystem = json.load(task)


def Save_TaskSystem():
    """
    Guarda el sistema de tareas en el archivo .JSON
    """

    global TaskSystem
    with open(TaskSystem_directory, "w") as task:
        json.dump(TaskSystem, task)