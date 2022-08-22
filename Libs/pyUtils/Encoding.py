"""
    Module Name:
        Encoding.py

    Module Description:
        This module contains functions that convert objects to different text encodings.
"""

from typing import Literal

# FORMATS CONVERSORS
__author__ = "TheBigEye"

# Hexadecimal ----------------------------------------------------------------
def toHex(obj: str | int , separator: str = " "):
    """
    Converts an object (string or int) to hexadecimal.

    Arguments:
        `obj : [str | int]` The value to convert.
        `separator : [str]` The separator to use between each byte.

    Returns:
        `str` The hexadecimal string.

    Raises:
        `TypeError` If the object is not a string or int.

    Examples:
        >>> toHex("Hello World!")
        "48 65 6c 6c 6f 20 57 6f 72 6c 64 21"
    """

    # Converts each character to hexadecimal
    if type(obj) == str:
        hex_string = ""
        for char in obj:
            hex_string += hex(ord(char))[2:] + separator
        return hex_string[:-1]

    # Converts each byte to hexadecimal
    elif type(obj) == int:
        hex_string = ""
        for i in range(0, obj.bit_length(), 8):
            hex_string += hex(obj >> i & 0xff)[2:] + separator
        return hex_string[:-1]

    # If the object is not a string or int, returns a error
    else:
        raise TypeError("The object must be a string or int.")

def fromHex(hex_string: str):
    """Converts a hexadecimal string to string.

    Arguments:
        `hex_string : [str]` The hexadecimal string.

    Returns:
        `str` The decoded string.

    Raises:
        `TypeError` If the object is not a string.

    Examples:
        >>> fromHex("48 65 6c 6c 6f 20 57 6f 72 6c 64 21")
        "Hello World!"
    """

    if type(hex_string) == str:
        return bytes.fromhex(hex_string).decode("utf8")
    else:
        raise TypeError("The object must be a string.")


# Binary ---------------------------------------------------------------------
def toBinary(obj: str, bits: Literal[8, 16, 32, 64] = 8):
    """Converts an object to binary

    Arguments:
        `obj : [str]` The object to convert to binary.
        `bits : [Literal[8, 16, 32, 64]]` The number of bits to use.

    Returns:
        `str` The binary string.

    Raises:
        `TypeError` If the object is not a string.

    Examples:
        >>> toBinary("Hi")
        "01001000 01101001"
    """

    if type(obj) == str:
        binary_string = ""

        # Converts each character to binary
        for char in obj:
            binary_string += bin(ord(char))[2:].zfill(bits) + " "

        # Returns the binary string
        return binary_string[:-1]
    else:
        raise TypeError("The object must be a string.")

def fromBinary(binary_string: str):
    """Converts a binary value to string.

    Arguments:
        `binary_string : [str]` The binary string.

    Returns:
        `str` The decoded string.

    Raises:
        `TypeError` If the object is not a string.

    Examples:
        >>> fromBinary("01001000 01101001")
        "Hi"
    """

    if type(binary_string) == str:
        binary_values = binary_string.split() # Split string on whitespaces
        binary_string = ""

        for binary_value in binary_values:
            binary_int = int(binary_value, 2) # Converts the binary value to int
            binary_char = chr(binary_int) # Converts the int to char
            binary_string += binary_char # Adds the char to the string

        return binary_string
    else:
        raise TypeError("The object must be a string.")


# Base64 ---------------------------------------------------------------------
def toBase64(obj: str | int):
    """Converts an object to base64.

    Arguments:
        `obj : [str | int]` The object to convert to base64.

    Returns:
        `str` The base64 string.

    Raises:
        `TypeError` If the object is not a string or int.

    Examples:
        >>> toBase64("Hello World!")
        "SGVsbG8gV29ybGQh"
    """
    import base64

    if type(obj) == str:
        return base64.b64encode(obj.encode("utf8")).decode("utf8")

    elif type(obj) == int:
        return base64.b64encode(obj.to_bytes(obj.bit_length() // 8, "big")).decode("utf8")

    else:
        raise TypeError("The object must be a string or int.")

def fromBase64(base64_string: str):
    """Converts a base64 string to string.

    Arguments:
        `base64_string : [str]` The base64 string.

    Returns:
        `str` The decoded string.

    Raises:
        `TypeError` If the object is not a string.

    Examples:
        >>> fromBase64("SGVsbG8gV29ybGQh")
        "Hello World!"
    """
    import base64

    if type(base64_string) == str:
        return base64.b64decode(base64_string).decode("utf8")

    else:
        raise TypeError("The object must be a string.")
