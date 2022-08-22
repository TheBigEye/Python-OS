"""
    Module Name:
        pyDatabase.py

    Module Description:
        Contains functions to manipulate database objects.
"""

import sqlite3
import os

def isDigit(s):
    """
    Checks if the given string have a number digit.
    :param s: String to be checked.
    :return: True if the string is a digit, False otherwise.
    """
    try:
        int(s)
        return True
    except ValueError:
        return False

def PythonizeValue(value):
    """
    Converts a value to a Python object.
    :param value: Value to be converted.
    :return: Python object.
    """
    if value == "None" or value == "none":
        return None
    elif isDigit(value) == True:
        return int(value)
    elif value == "True" or value == "true":
        return True
    elif value == "False" or value == "false":
        return False
    else:
        return value

class DB:
    """
    Class for handling databases.
    """

    def create(path: str):
        """
        Create a new database.
        """
        db_name = path.split("/")[-1]

        if os.path.exists(path):
            raise FileExistsError("The database " + db_name + " already exists.")

        conn = sqlite3.connect(path)
        c = conn.cursor()
        c.execute(
            """CREATE TABLE IF NOT EXISTS data (
                id INTEGER PRIMARY KEY,
                key TEXT,
                value TEXT
            )"""
        )
        conn.commit()
        conn.close()

    def write(path: str, key: str, value: str | bool | int):
        """
        Write a value to a database.
        """
        db_name = path.split("/")[-1]

        if not os.path.exists(path):
            raise FileNotFoundError("The database " + db_name + " does not exist.")

        conn = sqlite3.connect(path)
        c = conn.cursor()

        # Convert value to string
        if isinstance(value, bool) or isinstance(value, int):
            value = str(value)
        else:
            value = str(value)

        c.execute(
            """INSERT INTO data (key, value) VALUES (?, ?)""",
            (key, value)
        )
        conn.commit()
        conn.close()

    def read(path: str, key: str):
        """
        Return a value from a key
        """
        db_name = path.split("/")[-1]

        if not os.path.exists(path):
            raise FileNotFoundError("The database " + db_name + " does not exist.")

        conn = sqlite3.connect(path)
        c = conn.cursor()
        c.execute(
            """SELECT * FROM data WHERE key = ?""",
            (key,)
        )
        # get key value from key array
        data = c.fetchall()
        for i in data:
            if i[1] == key:
                value = i[2]
        conn.close()
        return PythonizeValue(value)


    def update(path: str, key: str, value: str | bool | int):
        """
        Update a value in a database.
        """
        db_name = path.split("/")[-1]

        if not os.path.exists(path):
            raise FileNotFoundError("The database " + db_name + " does not exist.")

        conn = sqlite3.connect(path)
        c = conn.cursor()

        # Convert value to string
        if isinstance(value, bool):
            value = str(value)
        elif isinstance(value, int):
            value = str(value)
        else:
            value = str(value)

        c.execute(
            """UPDATE data SET value = ? WHERE key = ?""",
            (value, key)
        )
        conn.commit()
        conn.close()

    def delete(path: str, key: str):
        """
        Delete a key from a database.
        """
        db_name = path.split("/")[-1]

        if not os.path.exists(path):
            raise FileNotFoundError("The database " + db_name + " does not exist.")

        conn = sqlite3.connect(path)
        c = conn.cursor()
        c.execute(
            """DELETE FROM data WHERE key = ?""",
            (key,)
        )
        conn.commit()
        conn.close()

    def delete_all(path: str):
        """
        Delete all keys from a database.
        """
        db_name = path.split("/")[-1]

        if not os.path.exists(path):
            raise FileNotFoundError("The database " + db_name + " does not exist.")

        conn = sqlite3.connect(path)
        c = conn.cursor()
        c.execute(
            """DELETE FROM data"""
        )
        conn.commit()
        conn.close()

    def list(path: str):
        """
        List all keys in a database.
        """
        db_name = path.split("/")[-1]

        if not os.path.exists(path):
            raise FileNotFoundError("The database " + db_name + " does not exist.")

        conn = sqlite3.connect(path)
        c = conn.cursor()
        c.execute(
            """SELECT * FROM data"""
        )
        data = c.fetchall()
        conn.close()
        return data


# test
if __name__ == "__main__":
    DB.create("./test.db")
    DB.write("./test.db", "keystr", "value")
    DB.write("./test.db", "keybool", False)
    DB.write("./test.db", "keyint", 1)
    print(str(DB.read("./test.db", "keystr")))
    print(str(DB.read("./test.db", "keybool")))
    print(str(DB.read("./test.db", "keyint")))
