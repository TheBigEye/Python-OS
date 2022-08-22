from ...shell.Components.UITextbox import UITextbox

def CLEAR(output: UITextbox) -> str:
    """ Clear the screen """

    output.clear()
    output.update()

    return output.get_text()

