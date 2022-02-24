import json

#from System.Utils.Utils import print_error, print_info

# TODO: add commands to the terminal

Keys = [] # here we will store the registry keys
Keys_directory = "Disk/System/Registry/Keys.json" # the directory where the registry keys are stored

def rg_routines():
    # load the registry keys
    load_registry_keys()

    #print_info("Registry keys has finished loading")


# Load the registry keys
def load_registry_keys():
    """
    Load the registry keys
    """

    global Keys

    with open(Keys_directory, encoding='utf-8') as file:
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
def add_key(root: str, category: str, name: str, key: str, value: str, type: str):
    """
    Add a key to the registry
    """

    # load the registry keys
    ##load_registry_keys()

    global Keys

    for root_key in Keys:
        if root_key["root"] == root:
            for category_key in root_key["content"]:
                if category_key["category"] == category:
                    for key_key in category_key["keys"]:
                        if key_key["name"] == name:
                            for value_key in key_key["values"]:
                                if value_key["key"] == key:
                                    value_key["value"] = value
                                    value_key["type"] = type
                                    save_registry_keys()
                                    return True



    # save the registry keys
    save_registry_keys()


# get the value of a key
def get_value(root: str, category: str, name: str, key: str):
    """
    Get the value of a key
    """

    # load the registry keys
    load_registry_keys()

    global Keys

    for root_key in Keys:
        if root_key["root"] == root:
            for category_key in root_key["content"]:
                if category_key["category"] == category:
                    for key_key in category_key["keys"]:
                        if key_key["name"] == name:
                            for value_key in key_key["values"]:
                                if value_key["key"] == key:
                                    return value_key["value"]


# Tree view
def reg_tree_view():
    """
    Tree view
    """

    global Keys

    tree = ""

    # This is a HELL, REALLY!!!
    for root_key in Keys:
        tree += root_key["root"] + "/" + "\n"
        for category_key in root_key["content"]:

            if category_key == Keys[-1]:
                tree += "|   " + "\n"
                tree += "└───" + category_key["category"] + "\n"
                for key_key in category_key["keys"]:

                    if key_key == category_key["keys"][-1]:
                        tree += "    └───" + key_key["name"] + "\n"
                        for value_key in key_key["values"]:

                            if value_key == key_key["values"][-1]:
                                tree += "        └───" + value_key["key"] +  "\n"
                                tree += "            ├──> " + value_key["value"] + "\n"
                                tree += "            └──> " + value_key["type"] + "\n"
                            else:
                                tree += "        ├───" + value_key["key"] + "\n"
                                tree += "        │   ├──> " + value_key["value"] + "\n"
                                tree += "        │   └──> " + value_key["type"] + "\n"

                    else:
                        tree += "    ├───" + key_key["name"] + "\n"
                        for value_key in key_key["values"]:
                            if value_key == key_key["values"][-1]:
                                tree += "    │   └───" + value_key["key"] + "\n"
                                tree += "    │       ├───> " + value_key["value"] + "\n"
                                tree += "    │       └───> " + value_key["type"] + "\n"
                            else:
                                tree += "    │   ├───" + value_key["key"] + "\n"
                                tree += "    │   │   ├───> " + value_key["value"] + "\n"
                                tree += "    │   │   └───> " + value_key["type"] + "\n"

            else:
                tree += "├───" + category_key["category"] + "\n"
                for key_key in category_key["keys"]:

                    if key_key == category_key["keys"][-1]:
                        tree += "│    └───" + key_key["name"] + "\n"
                        for value_key in key_key["values"]:
                            if value_key == key_key["values"][-1]:
                                tree += "│        └───" + value_key["key"] + "\n"
                                tree += "│            ├───> " + value_key["value"] + "\n"
                                tree += "│            └───> " + value_key["type"] + "\n"
                            else:
                                tree += "│        ├───" + value_key["key"] + "\n"
                                tree += "│        │   ├───> " + value_key["value"] + "\n"
                                tree += "│        |   └───> " + value_key["type"] + "\n"

                    else:
                        tree += "│    ├───" + key_key["name"] + "\n"
                        for value_key in key_key["values"]:
                            if value_key == key_key["values"][-1]:
                                tree += "│    │    └───" + value_key["key"] + "\n"
                                tree += "│    │         ├───> " + value_key["value"] + "\n"
                                tree += "│    │         └───> " + value_key["type"] + "\n"
                            else:
                                tree += "│    │    ├───" + value_key["key"] + "\n"
                                tree += "│    │    │    ├───> " + value_key["value"] + "\n"
                                tree += "│    │    │    └───> " + value_key["type"] + "\n"
    return tree






