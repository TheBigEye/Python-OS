# System variables (| Variable | True/False/int |)

Kernel_lvl = "NULL"  # Kernel main variable

Is_FAIL =           False  # 0
Is_in_BIOS =        False  # 1
Is_in_INSTALLER =   False  # 2
Is_in_Boot =        False  # 3
Is_in_Login =       False  # 4
Is_in_Desktop =     False  # 5
Is_Boot =           False  # NULL

# Boot order
if Kernel_lvl == 0:  # Fail message

    Is_FAIL = True

elif Kernel_lvl == 1:  # BIOS Screen

    Is_in_BIOS = True

elif Kernel_lvl == 2:  # OS Installer

    Is_in_INSTALLER = True

elif Kernel_lvl == 3:  # Bootloader

    Is_in_Boot = True

elif Kernel_lvl == 4:  # Login Screen

    Is_in_Login = True

elif Kernel_lvl == 5:  # In the desktop

    Is_in_Desktop = True

elif Kernel_lvl == "NULL":  # Normal boot

    Is_Boot = True



# Define the Routines() method, inside there will be functions and things that will be executed when calling this method.
def routines():
    pass

    
