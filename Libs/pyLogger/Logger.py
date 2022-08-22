# -*- coding: utf-8 -*-

"""
    Module Name:
        Logger.py

    Module Description:
        This module implement the Logger and related functions.
"""

import datetime
import inspect
import logging
import logging.handlers
import os
import re
import sys

can_log = False

class Color:
    """ Logger styles and colors """

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

    GRAY_BLOCK = '\x1b[6;30;40m'
    RED_BLOCK = '\x1b[6;30;41m'
    GREEN_BLOCK = '\x1b[6;30;42m'
    YELLOW_BLOCK = '\x1b[6;30;43m'
    BLUE_BLOCK = '\x1b[6;30;44m'
    PURPLE_BLOCK = '\x1b[6;30;45m'

    BOLD_RED = "\x1b[31;1m"
    LIGHT_BLUE = "\x1b[1;36m"

    RESET = "\x1b[0m"
    END = '\033[0m'

class ColorizedArgsFormatter(logging.Formatter):
    """ Rewrite the record to add the color to the message """

    arg_colors = [Color.PURPLE, Color.LIGHT_BLUE]
    level_fields = ["levelname", "levelno"]
    level_to_color = {
        logging.DEBUG: Color.PURPLE,
        logging.INFO: Color.GREEN,
        logging.WARNING: Color.YELLOW,
        logging.ERROR: Color.RED,
        logging.CRITICAL: Color.BOLD_RED,
    }

    def __init__(self, fmt: str) -> None:
        """ Initialize the formatter """

        super().__init__()
        self.level_to_formatter = {}

        def add_color_format(level: int):
            """ Add a color format for the given level """

            color = ColorizedArgsFormatter.level_to_color[level]
            _format = fmt
            for fld in ColorizedArgsFormatter.level_fields:
                search = "(%\(" + fld + "\).*?s)"
                _format = re.sub(search, f"{color}\\1{Color.RESET}", _format)
            formatter = logging.Formatter(_format)
            self.level_to_formatter[level] = formatter

        add_color_format(logging.DEBUG)
        add_color_format(logging.INFO)
        add_color_format(logging.WARNING)
        add_color_format(logging.ERROR)
        add_color_format(logging.CRITICAL)

    @staticmethod
    def rewrite_record(record: logging.LogRecord) -> None:
        """ Rewrite the record to add the color to the message """

        if not BraceFormatStyleFormatter.is_brace_format_style(record):
            return

        msg = record.msg
        msg = msg.replace("{", "_{{")
        msg = msg.replace("}", "_}}")
        placeholder_count = 0
        # add ANSI escape code for next alternating color before each formatting parameter
        # and reset color after it.
        while True:
            if "_{{" not in msg:
                break
            color_index = placeholder_count % len(ColorizedArgsFormatter.arg_colors)
            color = ColorizedArgsFormatter.arg_colors[color_index]
            msg = msg.replace("_{{", color + "{", 1)
            msg = msg.replace("_}}", "}" + Color.RESET, 1)
            placeholder_count += 1

        record.msg = msg.format(*record.args)
        record.args = []

    def format(self, record: logging.LogRecord) -> str:
        """ Format the record """

        orig_msg = record.msg
        orig_args = record.args
        formatter = self.level_to_formatter.get(record.levelno)
        self.rewrite_record(record)
        formatted = formatter.format(record)
        record.msg = orig_msg
        record.args = orig_args
        return formatted


class BraceFormatStyleFormatter(logging.Formatter):
    """ Rewrite the record to add the color to the message """

    def __init__(self, fmt: str) -> None:
        """ Initialize the formatter """

        super().__init__()
        self.formatter = logging.Formatter(fmt)

    @staticmethod
    def is_brace_format_style(record: logging.LogRecord) -> bool:
        """ Check if the record is in brace format style """

        if len(record.args) == 0:
            return False

        msg = record.msg
        if '%' in msg:
            return False

        count_of_start_param = msg.count("{")
        count_of_end_param = msg.count("}")

        if count_of_start_param != count_of_end_param:
            return False

        if count_of_start_param != len(record.args):
            return False

        return True

    @staticmethod
    def rewrite_record(record: logging.LogRecord) -> None:
        """ Rewrite the record to add the color to the message """

        if not BraceFormatStyleFormatter.is_brace_format_style(record):
            return

        record.msg = record.msg.format(*record.args)
        record.args = []

    def format(self, record: logging.LogRecord) -> str:
        """ Format the record """

        orig_msg = record.msg
        orig_args = record.args
        self.rewrite_record(record)
        formatted = self.formatter.format(record)

        # restore log record to original state for other handlers
        record.msg = orig_msg
        record.args = orig_args
        return formatted


class Logger:
    """ This class implements the Logger and related functions. """

    # Check if the Logs folder exists. If not, create it.
    if not os.path.exists("Logs"):
        os.makedirs("Logs")

    # Check  if are more than 6 files in the Logs folder. If so, delete the oldest one.
    if len(os.listdir("Logs")) > 6:
        oldest_file = min(os.listdir("Logs"), key=os.path.getctime)
        os.remove(os.path.join("Logs", oldest_file))

    if can_log is not False:
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)

        console_level = "DEBUG"
        console_handler = logging.StreamHandler(stream=sys.stdout)
        console_handler.setLevel(console_level)
        console_format = "%(asctime)s - %(levelname)-8s - %(name)-25s - %(message)s"
        colored_formatter = ColorizedArgsFormatter(console_format)
        console_handler.setFormatter(colored_formatter)
        root_logger.addHandler(console_handler)

        file_handler = logging.FileHandler("Logs/Log_" + str(datetime.datetime.now().strftime("%Y-%m-%d")) + ".log")
        file_level = "DEBUG"
        file_handler.setLevel(file_level)
        file_format = "%(asctime)s - %(name)s (%(lineno)s) - %(levelname)-8s - %(threadName)-12s - %(message)s"
        file_handler.setFormatter(BraceFormatStyleFormatter(file_format))
        root_logger.addHandler(file_handler)

        with open("Logs/Log_" + str(datetime.datetime.now().strftime("%Y-%m-%d")) + ".log", "a") as f:
            f.write("\n" + "-" * 132 + "\n")

    def debug(msg: str, *args, **kwargs) -> None:
        """
        This function is used to log debug messages.

        Arguments:
            `msg [str]`: The message to be logged.
            `args [list]`: Optional logging arguments.
            `kwargs [dict]`: Optional logging keyword arguments.
        """

        if can_log is not False:
            frame = inspect.stack()[1]
            calling_function = frame[3]
            calling_function = calling_function.split(".")[-1]
            logger = logging.getLogger(calling_function)
            logger.debug(msg, *args, **kwargs)

    def info(msg: str, *args, **kwargs) -> None:
        """
        Logs an info message.

        Arguments:
            `msg [str]`: The message to be logged.
            `args [list]`: Optional logging arguments.
            `kwargs [dict]`: Optional logging keyword arguments.
        """

        if can_log is not False:
            frame = inspect.stack()[1]
            calling_function = frame[3]
            calling_function = calling_function.split(".")[-1]
            logger = logging.getLogger(calling_function)
            logger.info(msg, *args, **kwargs)

    def warning( msg: str, *args, **kwargs):
        """
        Logs a warning message.

        Arguments:
            `msg [str]`: The message to be logged.
            `args [list]`: Optional logging arguments.
            `kwargs [dict]`: Optional logging keyword arguments.
        """

        if can_log is not False:
            frame = inspect.stack()[1]
            calling_function = frame[3]
            calling_function = calling_function.split(".")[-1]
            logger = logging.getLogger(calling_function)
            logger.warning(msg, *args, **kwargs)

    def error(msg: str, *args, **kwargs):
        """
        Logs an error message.

        Arguments:
            `msg [str]`: The message to be logged.
            `args [list]`: Optional logging arguments.
            `kwargs [dict]`: Optional logging keyword arguments.
        """

        if can_log is not False:
            frame = inspect.stack()[1]
            calling_function = frame[3]
            calling_function = calling_function.split(".")[-1]
            logger = logging.getLogger(calling_function)
            logger.error(msg, *args, **kwargs)

    def critical(msg: str, *args, **kwargs):
        """
        Logs a critical error.

        Arguments:
            `msg [str]`: The message to be logged.
            `args [list]`: Optional logging arguments.
            `kwargs [dict]`: Optional logging keyword arguments.
        """

        if can_log is not False:
            frame = inspect.stack()[1]
            calling_function = frame[3]
            calling_function = calling_function.split(".")[-1]
            logger = logging.getLogger(calling_function)
            logger.critical(msg, *args, **kwargs)

    def delete_logs():
        """ Delete all the logs file in the Logs folder. """

        import os

        # Shutdown the logger to avoid logging messages while deleting the logs.
        logging.shutdown()

        for file in os.listdir("Logs"):
            if file.startswith("Log_"):
                os.remove("Logs/" + file)

        asctime_var = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ",255")

        levelname_var = str(Color.GREEN + "INFO" + Color.RESET) + " " * (8 - len("INFO"))
        name_var = "loggerCleaner" + " " * (25 - len("loggerCleaner"))
        message_var = "All the logs files have been deleted."
        print(asctime_var + " - " + levelname_var + " - " + name_var + " - " + message_var)
