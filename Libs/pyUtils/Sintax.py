"""
    Module Name:
        Sintax.py

    Module Description:
        Contains the sintax functions and snippets.
"""

# datatypes
def typeof(obj):
    """Returns the type of an object."""
    return type(obj).__name__

def indexOf(list, obj):
    """Returns the index of the object in the list."""
    # example: cars = ["Ford", "Volvo", "BMW"]
    # indexOf(cars, "BMW") -> 2

    # find the index
    for i in range(len(list)):
        if list[i] == obj:
            return i
    return -1

def toString(obj) -> str:
    """Converts an object to string."""
    return str(obj)

def toInt(obj) -> int:
    """Converts an object to int."""
    return int(obj)

def toFloat(obj) -> float:
    """Converts an object to float."""
    return float(obj)

def toChar(int) -> str:
    """Returns the character from the integer (ascii code)."""
    return chr(int)

# String utils
def toUpperCase(string) -> str:
    """Returns the string in upper case."""
    return string.upper()

def toLowerCase(string) -> str:
    """Returns the string in lower case."""
    return string.lower()

def getLength(string) -> int:
    """Returns the length of the string."""
    return len(string)

def getCharsCount(string, char) -> int:
    """Returns the number of times the character appears in the string."""
    return string.count(char)

def getCharIndex(string, char) -> int:
    """Returns the index of the character."""
    return string.index(char)

def getCharAt(string, index) -> str:
    """Returns the character at the index."""
    return string[index]
