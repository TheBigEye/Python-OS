"""
    Module Name:
        Registry.py

    Abstract:
        This module implements the registry database.

    Author:
        TheBigEye 1-aug-2022
"""

import os
import sqlite3

### DWORD ###
def set_DWORD(value):
    """
    Convert a string to hexadecimal

    Arguments:
        `value`: `[str]` string to convert

    Returns:
        `str` hexadecimal string

    Examples:
        >>> set_DWORD('test')
        >>> '0x74657374'
    """

    byte_array = bytearray(value, 'utf-8')
    hex_string = byte_array.hex()
    return '0x' + hex_string

def get_DWORD(value):
    """
    Convert from hexadecimal to string

    Arguments:
        `value`: `[str]` hexadecimal string to convert

    Returns:
        `str` string

    Examples:
        >>> get_DWORD('0x74657374')
        >>> 'test'
    """

    value = value[2:]
    byte_array = bytearray.fromhex(value)
    string = byte_array.decode('utf-8')
    return string

### BYNARY ###
def set_BINARY(value):
    """
    Convert a string to binary

    Arguments:
        `value`: `[str]` string to convert

    Returns:
        `str` binary string

    Examples:
        >>> set_BINARY('test')
        >>> '01110100...'
    """

    bin = ''.join(format(ord(i),'08b') for i in value)
    return bin

def get_BINARY(value):
    """
    Convert from binary to string

    Arguments:
        `value`: `[str]` binary string to convert

    Returns:
        `str` string

    Examples:
        >>> get_BINARY('01110100...')
        >>> 'test'
    """

    binstr = ''.join(chr(int(value[i:i+8],2)) for i in range(0,len(value),8))
    return binstr

# Registry structure
# - Hive: HKEY_LOCAL_MACHINE
# - Key: SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System
# - Value: EnableLUA (inside of the database it will be converted by the type)
# - Type: REG_DWORD

class REG():
    # Registry simulator using sqlite3
    def install(path):
        # create a blank database with 3 tables (HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE, HKEY_CLASSES_ROOT)
        # and 3 columns (key, value, type)
        # return True if success, False if not
        try:
            conn = sqlite3.connect(path)
            c = conn.cursor()
            c.execute("CREATE TABLE HKEY_CURRENT_USER (key TEXT, value TEXT, type TEXT)")
            c.execute("CREATE TABLE HKEY_LOCAL_MACHINE (key TEXT, value TEXT, type TEXT)")
            c.execute("CREATE TABLE HKEY_CLASSES_ROOT (key TEXT, value TEXT, type TEXT)")
            conn.commit()
            conn.close()
            return True
        except:
            return False

    def uninstall(path):
        # delete the database
        # path is the path to the database
        # return True if success, False if not
        try:
            os.remove(path)
            return True
        except:
            return False

    def add(path, key, value, type):
        # make a new key in the registry
        try:
            # split the hive from the key
            hive = key.split('/')[0] # HKEY_CURRENT_USER
            key = '/'.join(key.split('/')[1:]) # SOFTWARE/Microsoft/Windows/CurrentVersion/etc ...

            # convert the value to the correct type
            if type == 'REG_SZ':
                value = str(value)
            elif type == 'REG_DWORD':
                value = set_DWORD(value)
            elif type == 'REG_BINARY':
                value = set_BINARY(value)
            else:
                raise Exception('Invalid type')

            # connect to the database
            conn = sqlite3.connect(path)
            c = conn.cursor()
            c.execute("INSERT INTO " + hive + " (key, value, type) VALUES (?, ?, ?)", (key, value, type))
            conn.commit()
            conn.close()
            return True
        except:
            return False

    def delete(path, key):
        # delete a key in the registry
        try:
            # split the hive from the key
            hive = key.split('/')[0] # HKEY_CURRENT_USER
            key = '/'.join(key.split('/')[1:]) # SOFTWARE/Microsoft/Windows/CurrentVersion/etc ...

            # connect to the database
            conn = sqlite3.connect(path)
            c = conn.cursor()
            c.execute("DELETE FROM " + hive + " WHERE key = ?", (key,))
            conn.commit()
            conn.close()
            return True
        except:
            return False

    def get(path, key):
        try:
            # split the hive from the key
            hive = key.split('/')[0] # HKEY_CURRENT_USER
            key = '/'.join(key.split('/')[1:]) # SOFTWARE/Microsoft/Windows/CurrentVersion/etc ...

            # Get the key type
            conn = sqlite3.connect(path)
            c = conn.cursor()
            c.execute("SELECT type FROM " + hive + " WHERE key = ?", (key,))
            type = c.fetchone()[0]

            # Get the key value
            c.execute("SELECT value FROM " + hive + " WHERE key = ?", (key,))
            value = c.fetchone()[0]

            # Convert the value to the correct type
            if type == 'REG_SZ':
                value = str(value)
            elif type == 'REG_DWORD':
                value = get_DWORD(value)
            elif type == 'REG_BINARY':
                value = get_BINARY(value)
            else:
                raise Exception('Invalid type')

            conn.close()
            return value
        except:
            return None

    def get_all(path):
        # return a string list of all keys in the registry:
        # - HKEY_CURRENT_USER/ -> SOFTWARE/Microsoft/Windows/CurrentVersion/Policies/System/EnableLUA = 1 (REG_DWORD)
        # - HKEY_LOCAL_MACHINE/ -> SOFTWARE/Microsoft/Windows/CurrentVersion/Policies/System/EnableLUA = 1 (REG_DWORD)
        # - HKEY_CLASSES_ROOT/ -> SOFTWARE/Microsoft/Windows/CurrentVersion/Policies/System/EnableLUA = 1 (REG_DWORD)

        def make_list(key, key_value, key_type):
            if key_type == 'REG_SZ': key_value = str(key_value) # convert to string
            elif key_type == 'REG_DWORD': key_value = get_DWORD(key_value) # convert from hex to string
            elif key_type == 'REG_BINARY': key_value = get_BINARY(key_value) # Convert from binary to string: 01110100011001010111001101110100 -> 'test'
            else:
                raise Exception('Invalid type')

            return str("        " + key + (" " * (28 - len(key))) + " = " + key_value + (" " * (24 - len(key_value))) + " (" + key_type + ")")

        try:
            reglist = ""
            conn = sqlite3.connect(path)
            c = conn.cursor()
            c.execute("SELECT * FROM HKEY_CURRENT_USER")
            reglist += " - HKEY_CURRENT_USER/\n"
            for row in c.fetchall():
                reglist += make_list(row[0], row[1], row[2]) + "\n"
            c.execute("SELECT * FROM HKEY_LOCAL_MACHINE")
            reglist += " - HKEY_LOCAL_MACHINE/\n"
            for row in c.fetchall():
                reglist += make_list(row[0], row[1], row[2]) + "\n"
            c.execute("SELECT * FROM HKEY_CLASSES_ROOT")
            reglist += " - HKEY_CLASSES_ROOT/\n"
            for row in c.fetchall():
                reglist += make_list(row[0], row[1], row[2]) + "\n"
            conn.close()
            return reglist
        except:
            return None


def REG_routines():
    # TODO: implement REG_routines
    pass
