from ...shell.Components.UITextbox import UITextbox

def ECHO(command: str, output: UITextbox) -> str:
    """ Prints a message or string on the screen """

    # Split the command: ECHO <message> <optional arguments> -> get message and put it in a list
    # optional arguments are separated by spaces:
    # ECHO "Hello World" -color=red -> print "Hello World" in red color
    # ECHO "Hello World" -color=red -bgcolor=blue -> print "Hello World" in red color and in blue background
    # ECHO "Hello World" -color=red -bgcolor=blue -font=arial -> print "Hello World" in red color, in blue background and in arial font
    message = command.split()[1:]

    # If the message is empty, will print a error message and return
    if message == []:
        output.append_colored("Error: No input specified \n", "#D63A35")
        return output.get_text()

    # If the message is not empty but is not beetween quotes, will print a error message and return
    if message[0][0] != '"' or message[0][-1] != '"':
        output.append_colored("Error: Input must be between quotes \n", "#D63A35")
        return output.get_text()
    else:
        # Remove the quotes from the message
        message[0] = message[0][1:-1]

    # get arguments and put it in a list
    arguments = message[1:]
    # get the message and put it in a variable
    message = message[0]

    color = None
    bgcolor = None
    font = None

    # Loop through the arguments and set the variables
    for argument in arguments:
        if argument.startswith('-color='):
            # the value must be between quotes
            argument = argument.split('=')[1]
            if argument[0] != '"' or argument[-1] != '"':
                output.append_colored("Error: Color must be between quotes \n", "#D63A35")
                return output.get_text()
            else:
                # Remove the quotes from the color
                argument = argument[1:-1]
                color = argument
        elif argument.startswith('-bgcolor='):
            # the value must be between quotes
            argument = argument.split('=')[1]
            if argument[0] != '"' or argument[-1] != '"':
                output.append_colored("Error: Background color must be between quotes \n", "#D63A35")
                return output.get_text()
            else:
                # Remove the quotes from the color
                argument = argument[1:-1]
                bgcolor = argument

        elif argument.startswith('-font='):
            # like -font="arial_bold_8" -> "{} {} {}".format(font, size, style)
            argument = argument.split('=')[1]
            if argument[0] != '"' or argument[-1] != '"':
                output.append_colored("Error: Font must be between quotes \n", "#D63A35")
                return output.get_text()
            else:
                font = ""
                # Remove the quotes from the font
                argument = argument[1:-1]
                # Split the font in 3 parts: font, style and size
                font_parts = argument.split('_')
                # exmaple: font_parts = ["arial", 8, "bold"]
                # if only is font, will set the only the font, if is font and style, will set the font and style, if is font, style and size, will set the font, style and size
                if len(font_parts) == 1:
                    font = font_parts[0]
                    font_style = ""
                    font_size = ""
                elif len(font_parts) == 2:
                    font = font_parts[0]
                    font_style = font_parts[1]
                    font_size = ""
                elif len(font_parts) == 3:
                    font = font_parts[0]
                    font_style = font_parts[1]
                    font_size = font_parts[2]
                else:
                    output.append_colored("Error: Font must be in the format: font_style_size \n", "#D63A35")
                    return output.get_text()

                font = "{} {} {}".format(font, font_size, font_style)

        else:
            keywords = [
                ("Error:", "#D63A35"),
                ("Invalid", "#D63A35"),
                ("argument", "#D63A35"),
                (argument, "#DD6633"),
                ("\n", "#D63A35")
            ]
            output.insert_color_word("Error: Invalid argument " + argument + " \n", keywords)
            return output.get_text()

    # print the message in the specified color, in the specified background color and in the specified font
    output.insert_text(message, color, bgcolor, font)
    output.append_newline()
    output.update()

    return output.get_text()
