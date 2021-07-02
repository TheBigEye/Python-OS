from OS import Kernel

# System variables (for now they will be basic variables until something similar to control over the hardware is implemented)

Is_FAIL = False

Is_in_BIOS = False
Is_in_INSTALLER = False
Is_in_Boot = False
Is_in_Login = False
Is_in_Desktop = False


# In case the variable "Kernel" in Os.py has a value between 0 and 5:
if (Kernel == 0):

    Is_FAIL = True

elif (Kernel == 1):

    Is_in_BIOS = True

elif (Kernel == 2):

    Is_in_INSTALLER = True

elif (Kernel == 3):

    Is_in_Boot = True    

elif (Kernel == 4):

    Is_in_Login = True  

elif (Kernel == 5):

    Is_in_Desktop = True          



