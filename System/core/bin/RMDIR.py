from ...core.filesystem import get_current_directory, remove_directory
from ...shell.Components.UITextbox import UITextbox

def RMDIR(command: str, output: UITextbox) -> int:
    """ Remove a directory """

    # Split the command: RMDIR <directory> -> get directory and put it in a list
    directory = command.split()[1]

    # Try remove the directory and get the output
    fsout = remove_directory(directory)

    if fsout == 0: # Success
        output.insert_color_word("Removed directory " + directory + " from " + get_current_directory() + "\n", [(directory, "#B8BA37")])
        output.update()
    elif fsout == 1: # Error: Directory not found
        output.append_colored("Error: Directory " + directory + " not found \n", "#D63A35")
        output.update()
    elif fsout == 2: # Error: Not a directory
        output.append_colored("Error: " + directory + " is not a directory \n", "#D63A35")
        output.update()
    else:
        output.append_colored("Error: Unknown error (" + fsout + ") \n", "#D63A35")
        output.update()

    return fsout
