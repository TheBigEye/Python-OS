Kernel_lvl = 6  # Kernel main variable

Is_FAIL =           False  # 0
Is_in_BIOS =        False  # 1
Is_in_INSTALLER =   False  # 2
Is_in_Boot =        False  # 3
Is_in_Login =       False  # 4
Is_in_Desktop =     False  # 5
Is_Boot =           False  # 6


# Boot order
match Kernel_lvl:
    case 0:
        Is_FAIL = True  # Fail message
    case 1:
        Is_in_BIOS = True  # BIOS Screen
    case 2:
        Is_in_INSTALLER = True  # OS Installer
    case 3:
        Is_in_Boot = True  # Bootloader
    case 4:
        Is_in_Login = True  # Login Screen
    case 5:
        Is_in_Desktop = True  # In the desktop
    case 6:
        Is_Boot = True  # Normal boot


# Define the Routines() method, inside there will be functions and things that will be executed when calling this method.
def routines():
    pass


    

    
