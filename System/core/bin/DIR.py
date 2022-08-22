from ...core.filesystem import get_current_directory, list_directory
from ...shell.Components.UITextbox import UITextbox

def DIR(output: UITextbox) -> str:
    """ Change the current directory """

    # Get the list of files in the current directory
    dirout = list_directory()

    # TODO: add more extensions and special folders
    keywords = [
        ("Home/", "#B8BA37"),
        ("System/", "#B8BA37"),
        ("---", "#B8BA37"),

        ("mbr", "#8BB482"),
        ("img", "#8BB482"),
        ("iso", "#8BB482"),

        ("txt", "#8BB482"),
        ("text", "#8BB482"),

        ("exe", "#8BB482"),
        ("com", "#8BB482"),
        ("bat", "#8BB482"),
        ("py", "#8BB482"),
        ("pyw", "#8BB482"),
        ("pyc", "#8BB482"),
        ("pyo", "#8BB482"),
        ("pys", "#8BB482"),

        ("jpg", "#AAB666"),
        ("jpeg", "#AAB666"),
        ("png", "#AAB666"),
        ("bmp", "#AAB666"),
        ("gif", "#AAB666"),
        ("tiff", "#AAB666"),
        ("tif", "#AAB666"),

        ("torrent", "#8BB482"),
        ("log", "#8BB482"),
        ("reg", "#7FAEA2")
    ]

    output.insert_color_word("Contents of " + get_current_directory(), [(get_current_directory(), "#B8BA37")])
    output.append_newline()
    output.insert_color_word(dirout, keywords)
    output.append_newline()
    output.update()

    return output.get_text()
