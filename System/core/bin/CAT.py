from ...core.filesystem import get_file_content
from ...shell.Components.UITextbox import UITextbox

def CAT(command: str, output: UITextbox) -> str:
    """ Prints and return the files content """

    # Split the command: CAT <file> -> get files and put it in a list
    files = command.split()[1:]

    # Loop through the files and print them
    for file in files:
        # if thee filename not have a dot in the name, will prit a error message and continue to the next file
        if not file.find('.') != -1:
            output.append_colored("Error: File " + file + " not found \n", "#D63A35")
            continue
        # get the content of the file and put it in a variable
        content = get_file_content(file)
        # if the content is empty, will print a info message and continue to the next file
        if content == "":
            output.append_colored("Info: File " + file + " is empty \n", "#4A91A7")
            continue
        # print the content of the file
        output.append_colored("-> ", "#B8BA37")
        output.append(content)
        output.append_newline()
        output.update()

        return str(content)
