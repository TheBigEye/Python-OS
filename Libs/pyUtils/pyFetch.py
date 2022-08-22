"""
    Module Name:
        pyFetch

    Module Description:
        Little Neofetch implementation in Python
"""

import os
import platform
import sys
import time
import psutil

class Color:
    """ Neofetch colors and styles. """

    HEADER = '\033[95m'
    CYAN = '\033[96m'

    WHITE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'

    GREY = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'

    DARK_BLACK_BLOCK = '\x1b[6;30;40m'
    DARK_RED_BLOCK = '\x1b[6;30;41m'
    DARK_GREEN_BLOCK = '\x1b[6;30;42m'
    DARK_YELLOW_BLOCK = '\x1b[6;30;43m'
    DARK_BLUE_BLOCK = '\x1b[6;30;44m'
    DARK_PURPLE_BLOCK = '\x1b[6;30;45m'
    DARK_CYAN_BLOCK = '\x1b[6;30;46m'
    DARK_WHITE_BLOCK = '\x1b[6;30;47m'

    LIGHT_GREY_BLOCK = '\33[100m'
    LIGHT_RED_BLOCK = '\33[101m'
    LIGHT_GREEN_BLOCK = '\33[102m'
    LIGHT_YELLOW_BLOCK = '\33[103m'
    LIGHT_BLUE_BLOCK = '\33[104m'
    LIGHT_PURPLE_BLOCK = '\33[105m'
    LIGHT_CYAN_BLOCK = '\33[106m'
    LIGHT_WHITE_BLOCK = '\33[107m'

    BOLD_RED = "\x1b[31;1m"
    LIGHT_BLUE = "\x1b[1;36m"

    RESET = "\x1b[0m"
    END = '\033[0m'

# ---------------------------------------------------------------------------------------------------------------------------------

def Set_chars_colors(ascii_art: str, chars: str, color: Color) -> str:
    """
    Sets the colors of the characters

    Arguments:
        `ascii_art [str]`: The ascii art to be colored
        `chars [str]`: The characters from the ascii art to be colored
        `color [Color]`: The color to be used

    Returns:
        `str`: The colored ascii art
    """

    for data in ascii_art: # Loop through the ascii art
        if chars != None: # If the chars are not none
            for char in chars: # Loop through the chars list
                if data == char: ascii_art = ascii_art.replace(data, color + data + Color.RESET) # Replace the char with the color + char

    return ascii_art

def Get_username(color: Color) -> str:
    """ Returns the username of the user """

    Username = "" # Initialize the username
    if color != None: # If the color is not none
        Username += str(Color.BOLD + color + str(os.getlogin() + "@" + platform.node()).upper() + Color.RESET) + "\n"
        Username += str("-" * len(str(os.getlogin() + "@" + platform.node()).upper())) + "\n"
    else:
        Username += str(str(os.getlogin() + "@" + platform.node()).upper()) + "\n"
        Username += str("-" * len(str(os.getlogin() + "@" + platform.node()).upper())) + "\n"
    return Username

def Get_OS_info(color: Color, OS_name: str = str(platform.platform()), OS_kernel: str = str(platform.release())) -> str:
    """ Returns the OS information """

    OS_info = ""
    if color != None:
        OS_info += str(Color.BOLD + color + "OS: " + Color.RESET + OS_name + Color.RESET) + "\n"
        OS_info += str(Color.BOLD + color + "Kernel: " + Color.RESET + OS_kernel + Color.RESET) + "\n"
    else:
        OS_info += str("OS: " + OS_name) + "\n"
        OS_info += str("Kernel: " + OS_kernel) + "\n"
    return OS_info

def Get_uptime(color: Color) -> str:
    """ Returns the uptime of the system """

    Uptime_string = ""
    Uptime = ""

    Current_time = time.time()
    Boot_time = psutil.boot_time()

    if Current_time - Boot_time < 60:
        Uptime_string = str(int(Current_time - Boot_time)) + " seconds"
    elif Current_time - Boot_time < 3600:
        Uptime_string = str(int((Current_time - Boot_time) / 60)) + " minutes"
    else:
        Uptime_string = str(int((Current_time - Boot_time) / 3600)) + " hours"

    if color != None:
        Uptime = str(Color.BOLD + color + "Uptime: " + Color.RESET + Uptime_string + Color.RESET) + "\n"
    else:
        Uptime = str("Uptime: " + Uptime_string) + "\n"
    return Uptime

def Get_Software_info(color: Color) -> str:
    """ Returns the software information """

    Software_info = ""
    if color != None:
        Software_info += str(Color.BOLD + color + "Packages: " + Color.RESET + "14 (py-pkg)" + Color.RESET) + "\n"
        Software_info += str(Color.BOLD + color + "Python: " + Color.RESET + str(sys.version.split(" ")[0]) + Color.RESET) + "\n"
        Software_info += str(Color.BOLD + color + "Shell: " + Color.RESET + str(sys.platform) + Color.RESET) + "\n"
    else:
        Software_info += str("Packages: " + "14 (py-pkg)") + "\n"
        Software_info += str("Python: " + str(sys.version.split(" ")[0])) + "\n"
        Software_info += str("Shell: " + str(sys.platform)) + "\n"
    return Software_info

def Get_Hardware_info(color: Color) -> str:
    """ Returns the hardware information """

    Hardware_info = ""
    # get cpu name and freq, eg: Intel(R) i7-4770 CPU @ 3.40GHz
    cpu_name = str(platform.processor().split(" ")[0] + " " + platform.processor().split(" ")[1])
    if color != None:
        Hardware_info += str(Color.BOLD + color + "CPU: " + Color.RESET + cpu_name + Color.RESET) + "\n"
        Hardware_info += str(Color.BOLD + color + "GPU: " + Color.RESET + str("N/A")) + "\n"
        Hardware_info += str(Color.BOLD + color + "Memory: " + Color.RESET + str(int(psutil.virtual_memory().used / 1024 / 1024)) + "MiB / " + str(int(psutil.virtual_memory().total / 1024 / 1024)) + "MiB" + Color.RESET) + "\n"
    else:
        Hardware_info += str("CPU: " + cpu_name) + "\n"
        Hardware_info += str("GPU: " + str("N/A")) + "\n"
        Hardware_info += str("Memory: " + str(int(psutil.virtual_memory().used / 1024 / 1024)) + "MiB / " + str(int(psutil.virtual_memory().total / 1024 / 1024)) + "MiB") + "\n"
    return Hardware_info

# ---------------------------------------------------------------------------------------------------------------------------------

def get_neofetch(logo_file_path: str, info_color: Color = Color.YELLOW, chars: list = [None, None, None, None, None, None, None]) -> str:
    """
    This function prints the neofetch in terminal

    Arguments:
        `logo_file_path : [str]` The path to the logo file
        `chars : [list]` The color scheme for the characters [`blue`, `green`, `red`, `yellow`, `purple`, `cyan`, `white`]

    Returns:
        The neofetch ascii string (Logo + system info)

    Example:
        >>> Neofetch("/path/to/logo.txt", ["/*+", None, "123", None, "abcd", None, None])
    """

    # Check  if the path to the logo file is valid
    if not os.path.exists(logo_file_path):
        raise Exception("The path to the logo file is invalid")

    # Make the neoftech string list
    Info_string = ""
    Info_string += Get_username(info_color)
    Info_string += Get_OS_info(info_color, OS_name = str(platform.platform()), OS_kernel= str(platform.release()))
    Info_string += Get_uptime(info_color)
    Info_string += Get_Software_info(info_color)
    Info_string += Get_Hardware_info(info_color)
    Info_string += "\n"
    if info_color != None:
        Info_string += Color.DARK_BLACK_BLOCK + "   " + Color.RESET + Color.DARK_RED_BLOCK + "   " + Color.RESET + Color.DARK_GREEN_BLOCK + "   " + Color.RESET + Color.DARK_YELLOW_BLOCK + "   " + Color.RESET + Color.DARK_BLUE_BLOCK + "   " + Color.RESET + Color.DARK_PURPLE_BLOCK + "   " + Color.RESET + Color.DARK_CYAN_BLOCK + "   " + Color.RESET + Color.DARK_WHITE_BLOCK + "   " + Color.RESET + "\n"
        Info_string += Color.LIGHT_GREY_BLOCK + "   " + Color.RESET + Color.LIGHT_RED_BLOCK + "   " + Color.RESET + Color.LIGHT_GREEN_BLOCK + "   " + Color.RESET + Color.LIGHT_YELLOW_BLOCK + "   " + Color.RESET + Color.LIGHT_BLUE_BLOCK + "   " + Color.RESET + Color.LIGHT_PURPLE_BLOCK + "   " + Color.RESET + Color.LIGHT_CYAN_BLOCK + "   " + Color.RESET + Color.LIGHT_WHITE_BLOCK + "   " + Color.RESET + "\n"

    Logo_file = open(logo_file_path, "r")
    Logo_string = Logo_file.read()

    # Apply the colors to the logo
    Logo_string = Set_chars_colors(Logo_string, chars[0], Color.BLUE)
    Logo_string = Set_chars_colors(Logo_string, chars[1], Color.GREEN)
    Logo_string = Set_chars_colors(Logo_string, chars[2], Color.RED)
    Logo_string = Set_chars_colors(Logo_string, chars[3], Color.YELLOW)
    Logo_string = Set_chars_colors(Logo_string, chars[4], Color.PURPLE)
    Logo_string = Set_chars_colors(Logo_string, chars[5], Color.CYAN)
    Logo_string = Set_chars_colors(Logo_string, chars[6], Color.WHITE)

    # Make the neoftech string
    Neofetch_string = ""
    # make a list of the line of Info_string
    Neofetch_lines = Info_string.split("\n")

    # Get the lines of the logo, and if the items from neoftch_sys_list are less that the lines of the logo, add a new line
    for line in Logo_string.split("\n"):
        if len(Neofetch_lines) > 0:
            Neofetch_string += line + "   " + Neofetch_lines.pop(0) + "\n"
        else:
            Neofetch_string += line + "\n"

    return Neofetch_string
