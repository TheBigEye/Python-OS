"""
    Module Name:
        pyData.py

    Module Description:
        Contains functions to manipulate data objects.
"""

import json
import os
from typing import Union


# JSON ----------------------------------------------------------------------------------------------------------------------------
class JSON:
    """ Handles JSON files and data structures. """

    def get(path: str, key: str) -> Union[bool, str, int]:
        """
        Returns a JSON from a path.
        """

        # Checks if the file exists
        if not os.path.isfile(path):
            raise FileNotFoundError("The file " + path + " does not exist.")

        # Check if the JSON file is a JSON
        SUPPORTED_FORMATS = ["json"]

        file_extension = path.split(".")[-1]
        if file_extension not in SUPPORTED_FORMATS:
            raise TypeError("The file " + path + " is not a supported JSON format.")

        # Open the JSON file
        with open(path, "r") as f:
            data = json.load(f)

            if key not in data:
                raise KeyError("The key " + key + " does not exist.")

            return data[key]

    def set(path: str, key: str, value):
        """
        Sets a value in a JSON.
        """

        # Checks if the file exists
        if not os.path.isfile(path):
            raise FileNotFoundError("The file " + path + " does not exist.")

        # Check if the JSON file is a JSON
        SUPPORTED_FORMATS = ["json"]

        file_extension = path.split(".")[-1]
        if file_extension not in SUPPORTED_FORMATS:
            raise TypeError("The file " + path + " is not a supported JSON format.")

        # Open the JSON file
        with open(path, "r") as f:
            data = json.load(f)

        # Sets the value
        data[key] = value

        # Save the JSON file (also formats it)
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

    def make(path: str, data: dict):
        """
        Creates a JSON file.
        """

        # Checks if the file exists
        if os.path.isfile(path):
            raise FileExistsError("The file " + path + " already exists.")

        # Check if the JSON file is a JSON
        SUPPORTED_FORMATS = ["json"]

        file_extension = path.split(".")[-1]
        if file_extension not in SUPPORTED_FORMATS:
            raise TypeError("The file " + path + " is not a supported JSON format.")

        # Creates the JSON file
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

    def validate(path: str):
        """
        Validates a JSON file.
        """

        # Checks if the file exists
        if not os.path.isfile(path):
            raise FileNotFoundError("The file " + path + " does not exist.")

        # Check if the JSON file is a JSON
        SUPPORTED_FORMATS = ["json"]

        file_extension = path.split(".")[-1]
        if file_extension not in SUPPORTED_FORMATS:
            raise TypeError("The file " + path + " is not a supported JSON format.")

        # Open the JSON file
        with open(path, "r") as f:
            data = json.load(f)

        # Validates the JSON file
        try:
            json.dumps(data)
        except:
            raise ValueError("The JSON file is invalid.")

        return True

class TXT:
    """ Handles TXT files and plain data structures. """

    def get(path: str):
        """
        Returns a TXT from a path.
        """

        # Checks if the file exists
        if not os.path.isfile(path):
            raise FileNotFoundError("The file " + path + " does not exist.")

        # Check if the TXT file is a TXT
        SUPPORTED_FORMATS = ["txt", "text"]

        file_extension = path.split(".")[-1]
        if file_extension not in SUPPORTED_FORMATS:
            raise TypeError("The file " + path + " is not a supported TXT format.")

        # Open the TXT file
        with open(path, "r") as f:
            data = f.read()

        return data

    def set(path: str, data: str):
        """
        Sets a value in a TXT.
        """

        # Checks if the file exists
        if not os.path.isfile(path):
            raise FileNotFoundError("The file " + path + " does not exist.")

        # Check if the TXT file is a TXT
        SUPPORTED_FORMATS = ["txt", "text"]

        file_extension = path.split(".")[-1]
        if file_extension not in SUPPORTED_FORMATS:
            raise TypeError("The file " + path + " is not a supported TXT format.")

        # Open the TXT file
        with open(path, "w") as f:
            f.write(data)

    def make(path: str, data: str):
        """
        Creates a TXT file.
        """

        # Checks if the file exists
        if os.path.isfile(path):
            raise FileExistsError("The file " + path + " already exists.")

        # Check if the TXT file is a TXT
        SUPPORTED_FORMATS = ["txt", "text"]

        file_extension = path.split(".")[-1]
        if file_extension not in SUPPORTED_FORMATS:
            raise TypeError("The file " + path + " is not a supported TXT format.")

        # Creates the TXT file

        with open(path, "w") as f:
            f.write(data)

    def validate(path: str):
        """
        Validates a TXT file.
        """

        # Checks if the file exists
        if not os.path.isfile(path):
            raise FileNotFoundError("The file " + path + " does not exist.")

        # Check if the TXT file is a TXT
        SUPPORTED_FORMATS = ["txt", "text"]

        file_extension = path.split(".")[-1]
        if file_extension not in SUPPORTED_FORMATS:
            raise TypeError("The file " + path + " is not a supported TXT format.")

        # Open the TXT file
        with open(path, "r") as f:
            data = f.read()

        # Validates the TXT file
        try:
            data.encode("utf-8")
        except:
            raise ValueError("The TXT file is invalid.")

        return True
