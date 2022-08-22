from ...core.filesystem import move_file
from ...shell.Components.UITextbox import UITextbox

def MV(command: str, output: UITextbox) -> int:
    """ Move a file to a folder """

    # Split the command: MV <file> <folder> -> get file and folder and put it in a list
    file = command.split()[1]
    folder = command.split()[2]

    # Try move the file and get the output
    fsout = move_file(file, folder)

    if fsout == 0: # Success
        output.append_colored("Moved file " + file + " to " + folder + "\n", "#B8BA37")
        output.update()
    elif fsout == 1: # Error: File not found
        output.append_colored("Error: File " + file + " not found \n", "#D63A35")
        output.update()
    elif fsout == 2: # Error: The destination is not exist
        output.append_colored("Error: The destination " + folder + " is not exist \n", "#D63A35")
        output.update()
    elif fsout == 3: # Error: The destination is not a directory
        output.append_colored("Error: The destination " + folder + " is not a directory \n", "#D63A35")
        output.update()
    elif fsout == 4: # Error: File already exists in the destination
        output.append_colored(str("Error: File " + file + " already exists in the destination " + folder + "\n"), "#D63A35")
        output.update()
    else:
        output.append_colored("Error: Unknown error (" + fsout + ") \n", "#D63A35")
        output.update()

    return fsout
