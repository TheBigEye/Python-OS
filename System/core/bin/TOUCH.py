from ...core.filesystem import get_current_directory, make_file
from ...shell.Components.UITextbox import UITextbox

def TOUCH(command: str, output: UITextbox) -> str:
    """ Create a new file """

    # Split the command: TOUCH <file>
    file = command.split()[1]

    # Try create the file and get the output
    fsout = make_file(file)

    if fsout == 0: # Success: File created
        output.insert_color_word("File " + file + " created in " + str("/" + "/".join(get_current_directory())) + "\n", [(file, "#B8BA37")])
        output.update()
    elif fsout == 1: # Error: File already exists
        output.append_colored("Error: File " + file + " already exists \n", "#D63A35")
        output.update()
    elif fsout == 2: # Error: Not a file
        output.append_colored("Error: " + file + " is not a valid file name \n", "#D63A35")
        output.update()
    elif fsout == 3: # Error: Name too long (48 chaaracters max)
        output.append_colored("Error: File name too long (48 characters max) \n", "#D63A35")
        output.update()
    elif fsout == 4: # Error: Name too short (1 character min)
        output.append_colored("Error: File name too short (1 character min) \n", "#D63A35")
        output.update()
    else:
        output.append_colored("Error: Unknown error (" + fsout + ") \n", "#D63A35")
        output.update()

    return fsout
