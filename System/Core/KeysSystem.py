import datetime
import json
import os
import random
import sys
import time
from os import urandom

from System.Utils.Utils import print_error, print_info

# TODO: add commands to the terminal

Keys = [] # here we will store the registry keys
Keys_directory = "Disk/System/Registry/Keys.json" # the directory where the registry keys are stored

def rg_routines():
    # load the registry keys
    load_registry_keys()

    print_info("Registry keys has finished loading")


# Load the registry keys
def load_registry_keys():
    """
    Load the registry keys
    """

    global Keys

    with open(Keys_directory, "r") as file:
        Keys = json.load(file)


# Save the registry keys
def save_registry_keys():
    """
    Save the registry keys
    """

    global Keys

    with open(Keys_directory, "w") as file:
        json.dump(Keys, file, indent=4)


# Add a key to the registry
def add_key(root_key_name: str, sub_key_name: str, key_name: str, key_value: str):

    """
    Add a key to the registry
    """

    global Keys

    for key in Keys:
        if key["ROOT_KEY"] == root_key_name:
            for sub_key in key["ROOT_KEY_CONTENT"]:
                if sub_key["SUB_KEY"] == sub_key_name:
                    sub_key["SUB_KEY_CONTENT"].append(
                        {
                            "KEY": key_name,
                            "VALUE": key_value
                        }
                    )
                    save_registry_keys()
                    return

    Keys.append(
        {
            "ROOT_KEY": root_key_name,
            "ROOT_KEY_CONTENT": [
                {
                    "SUB_KEY": sub_key_name,
                    "SUB_KEY_CONTENT": [
                        {
                            "KEY": key_name,
                            "VALUE": key_value
                        }
                    ]
                }
            ]
        }
    )

    save_registry_keys()


# Delete a key from the registry
def delete_key(root_key_name: str, sub_key_name: str, key_name: str):

    """
    Delete a key from the registry
    """

    global Keys

    for key in Keys:
        if key["ROOT_KEY"] == root_key_name:
            for sub_key in key["ROOT_KEY_CONTENT"]:
                if sub_key["SUB_KEY"] == sub_key_name:
                    for key_to_delete in sub_key["SUB_KEY_CONTENT"]:
                        if key_to_delete["KEY"] == key_name:
                            sub_key["SUB_KEY_CONTENT"].remove(key_to_delete)
                            save_registry_keys()
                            return


# Get a key from the registry
def get_key(root_key_name: str, sub_key_name: str, key_name: str, return_as):
    """
    Get a key from the registry
    """

    global Keys

    # if return_as is not specified, return the value as a string, if is int , return the value without the quotes
    if return_as == "int":
        for key in Keys:
            if key["ROOT_KEY"] == root_key_name:
                for sub_key in key["ROOT_KEY_CONTENT"]:
                    if sub_key["SUB_KEY"] == sub_key_name:
                        for key_to_get in sub_key["SUB_KEY_CONTENT"]:
                            if key_to_get["KEY"] == key_name:
                                return int(key_to_get["VALUE"])
    else:
        for key in Keys:
            if key["ROOT_KEY"] == root_key_name:
                for sub_key in key["ROOT_KEY_CONTENT"]:
                    if sub_key["SUB_KEY"] == sub_key_name:
                        for key_to_get in sub_key["SUB_KEY_CONTENT"]:
                            if key_to_get["KEY"] == key_name:
                                return key_to_get["VALUE"]


# Get all the keys from a sub key
def get_all_keys(root_key_name: str, sub_key_name: str):
    """
    Get all the keys from a sub key
    """

    global Keys

    for key in Keys:
        if key["ROOT_KEY"] == root_key_name:
            for sub_key in key["ROOT_KEY_CONTENT"]:
                if sub_key["SUB_KEY"] == sub_key_name:
                    return sub_key["SUB_KEY_CONTENT"]


# Get all the sub keys from a root key
def get_all_sub_keys(root_key_name: str):
    """
    Get all the sub keys from a root key
    """

    global Keys

    for key in Keys:
        if key["ROOT_KEY"] == root_key_name:
            return key["ROOT_KEY_CONTENT"]


# tree, return the registry as a string tree
def reg_tree():
    """
    Tree, return the registry as a string tree
    """

    global Keys

    string_tree = ""

    for key in Keys:
        string_tree += key["ROOT_KEY"] + ":\n"
        for sub_key in key["ROOT_KEY_CONTENT"]:
            string_tree += "    " + sub_key["SUB_KEY"] + ":\n"
            for key_to_get in sub_key["SUB_KEY_CONTENT"]:
                string_tree += "        " + key_to_get["KEY"] + ": " + key_to_get["VALUE"] + "\n"

    return string_tree
