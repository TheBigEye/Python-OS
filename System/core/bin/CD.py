from ...core.filesystem import change_directory, get_current_directory
from ...shell.Components.UITextbox import UITextbox

def CD(command: str, output: UITextbox) -> int:
    """ Change the current directory """

    # Split the command: CD <directory> -> get directory and put it in a list
    directory = command.split()[1]

    # Try change the current directory and get the output
    fsout = change_directory(directory)

    if fsout == 0: # Success
        output.insert_color_word("Changed directory to " + get_current_directory(), [(get_current_directory(), "#B8BA37")])
        output.append_newline()
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
