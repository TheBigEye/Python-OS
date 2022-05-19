# -*- coding: utf-8 -*-

"""
    Module Name:
        Logger.py

    Abstract:
        This  module implement the Logger and related functions.

    Author:
        TheBigEye 10-apr-2022
"""

import datetime
import inspect
import os

from System.Utils.Vars import Logs_directory

class Style:

    """
    This class implements the styles and colors of the logger.
    """

    HEADER = '\033[95m'
    CYAN = '\033[96m'

    WHITE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'

    GRAY = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'

    GRAY_BLOCK = '\x1b[6;30;40m'
    RED_BLOCK = '\x1b[6;30;41m'
    GREEN_BLOCK = '\x1b[6;30;42m'
    YELLOW_BLOCK = '\x1b[6;30;43m'
    BLUE_BLOCK = '\x1b[6;30;44m'
    PURPLE_BLOCK = '\x1b[6;30;45m'

    END = '\033[0m'

class Logger:

    """ This is a logger that is used to save the messages in a file.

    Returns:
        `Output : [String]` the logs text.

    Examples:
        # Simple usage
        >>> Logger.log("This is a log message")
        >>> Logger.info("This is an info message")
        >>> Logger.warning("This is a warning message")
        >>> Logger.fail("This is a fail message")

        # Advanced usage
        >>> Logger.log("This is a log message with {}", args)
        >>> Logger.info("This is an info message with {}", args)
        >>> Logger.warning("This is a warning message with {}", args)
        >>> Logger.fail("This is a fail message with {}", args)
    """

    showConsole = False

    # Verify if the log folder exists, if not, create it
    if not os.path.exists(Logs_directory):
        os.makedirs(Logs_directory)

    # Verify if in the Logs folder exist more than 6 files if yes, delete the oldest one
    log_files = os.listdir(Logs_directory)
    if len(log_files) > 6:
        log_files.sort()
        os.remove(Logs_directory + "/" + log_files[0])

    # Make the logs file
    log_filename = "Log_" + datetime.datetime.now().strftime("%Y-%m-%d") + ".log"

    console_header = []
    file_header = [] # Store the log file header

    # Logger header
    console_header.append("---------------------------------------------------------------------------------------")
    console_header.append("| Type |        Name         |                         Action                         |")
    console_header.append("---------------------------------------------------------------------------------------")

    def header():
        for line in Logger.console_header:
            print(line)

    # File header
    file_header.append("-------------------------------------------------------------------------------------------------------------------------")
    file_header.append("|        Date          |  Type  |         Name         |                            Action                              |")
    file_header.append("-------------------------------------------------------------------------------------------------------------------------")

    # Write the header in the log file
    with open(Logs_directory + "/" + log_filename, "a", encoding="utf8") as log_file:
        for line in file_header:
            log_file.write(line + "\n")

    def log(message: str, *args):

        """
        This function is used to log a message.

        arguments:
            `message : [String]` the message to log.
            `args : [List, String]` the arguments to log.

        Returns:
            `Output : [String]` the logs text.

        Examples:
            # Simple usage
            >>> Logger.log("This is a log message")

            # Advanced usage
            >>> Logger.log("This is a log message with {}", "args")
        """

        # Get the current date and time
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Get the function name
        function_name = inspect.stack()[1][3]

        log_label = Style.GREEN + "[LOG] " + Style.WHITE + " |" + Style.WHITE
        function_label = Style.WHITE + "[" + function_name + "]" + Style.WHITE

        # Get the args from {}
        if len(args) > 0:
            message = message.format(*args)

        spaceSeparator = 28 - len(function_label)

        # Print the message in the console
        if (Logger.showConsole == True):
            print(log_label + " " + function_label + " " * spaceSeparator + "|-> " + message)

        # Save the message in the log file
        with open(Logs_directory + "/" + Logger.log_filename, "a", encoding="utf8") as log_file:
            log_file.write("[" + date + "] " + " | " + "[LOG] " + " | " + "[" + function_name + "] " + " " * spaceSeparator + "|-> " + message + "\n")

    def info(message: str, *args):

        """
        Log an info message (not save to the log file).

        arguments:
            `message : [String]` the message to log.
            `*args : [List, String]` the args to put in the message.

        Returns:
            `Output : [String]` the message to log.

        Examples:
            # Simple usage
            >>> Logger.info("This started sucessfully")

            # Advanced usage
            >>> Logger.info("This started sucessfully at {}", datetime.datetime.now())
        """


        # Get the current date and time
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Get the function name
        function_name = inspect.stack()[1][3]

        info_label = Style.BLUE + "[INFO]" + Style.WHITE + " |" + Style.WHITE
        function_label = Style.WHITE + "[" + function_name + "]" + Style.WHITE

        # Get the args from {}
        if len(args) > 0:
            message = message.format(*args)

        spaceSeparator = 28 - len(function_label)

        # Print the message in the console
        if (Logger.showConsole == True):
            print(info_label + " " + function_label + " " * spaceSeparator + "|-> " + message)


    def warning(message: str, *args):
        """
        Log a warning message.

        arguments:
            `message : [String]` the message to log.
            `*args : [List, String]` the args to put in the message.

        Returns:
            `Output : [String]` the message to log.

        Examples:
            # Simple usage
            >>> Logger.warning("This whould fail")

            # Advanced usage
            >>> Logger.warning("This whould fail because {}", get_error())

        """


        # Get the current date and time
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Get the function name
        function_name = inspect.stack()[1][3]

        warning_label = Style.YELLOW + "[WARN]" + Style.WHITE + " |" + Style.WHITE
        function_label = Style.WHITE + "[" + function_name + "]" + Style.WHITE

        # Get the args from {}
        if len(args) > 0:
            message = message.format(*args)

        spaceSeparator = 28 - len(function_label)

        # Print the message in the console
        if (Logger.showConsole == True):
            print(warning_label + " " + function_label + " " * spaceSeparator + "|-> " + message)

        # Save the message in the log file
        with open(Logs_directory + "/" + Logger.log_filename, "a", encoding="utf8") as log_file:
            log_file.write("[" + date + "] " + " | " + "[WARN] | " + "[" + function_name + "] " + " " * spaceSeparator + "|-> " + message + "\n")


    def fail(message: str, *args):

        """
        This function is used to log a fail message.

        arguments:
            `message : [String]` the message to log.
            `*args : [List, String]` the args to put in the message.

        Returns:
            `Output : [String]` the logs text.

        Examples:
            # Simple usage
            >>> Logger.fail("Oh no, something went wrong!") # Log a fail message

            # Advanced usage
            >>> Logger.fail("Oh no, something went wrong with {}", class())
        """

        # Get the current date and time
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Get the function name
        function_name = inspect.stack()[1][3]

        fail_label = Style.RED + "[FAIL] |" + Style.WHITE
        function_label = Style.WHITE + "[" + function_name + "]" + Style.WHITE

        # Get the args from {}
        if len(args) > 0:
            message = message.format(*args)

        spaceSeparator = 28 - len(function_label)

        # Print the message in the console
        if (Logger.showConsole == True):
            print(fail_label + " " + function_label + " " * spaceSeparator + "|-> " + message)

        # Save the message in the log file
        with open(Logs_directory + "/" + Logger.log_filename, "a", encoding="utf8") as log_file:
            log_file.write("[" + date + "] " + " | " + "[FAIL] | " + "[" + function_name + "] " + " " * spaceSeparator + "|-> " + message + "\n")
