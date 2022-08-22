from ...core.filesystem import get_current_directory, make_directory
from ...shell.Components.UITextbox import UITextbox

def MKDIR(command: str, output: UITextbox) -> str:
    """ Create a new directory """

    # Split the command: MKDIR <directory>
    directory = command.split()[1]

    fsout = make_directory(directory)

    if fsout == 0: # Success: Directory created
        output.insert_color_word("Directory " + directory + " created in " + str("/" + "/".join(get_current_directory())) + "\n", [(directory, "#B8BA37")])
        output.update()
    elif fsout == 1: # Error: Directory already exists
        output.append_colored("Error: Directory " + directory + " already exists \n", "#D63A35")
        output.update()
    elif fsout == 2: # Error: Not a directory
        output.append_colored("Error: " + directory + " is not a valid directory name \n", "#D63A35")
        output.update()
    else:
        output.append_colored("Error: Unknown error (" + fsout + ") \n", "#D63A35")
        output.update()

    return fsout
