
<p align="center">
  <img src="https://user-images.githubusercontent.com/63316583/156767604-3dae9cb2-a1af-4c2e-86fd-a003445cba60.svg" alt="Python OS Logo" />
</p>

# Python OS
<!-- <img src="https://user-images.githubusercontent.com/63316583/156764802-7e1ffb65-f482-45ef-9c05-f82d9c4b4e23.svg" width="512" height="360"> UNUSED but usefuul -->

Python OS is an operating system simulator written in Python, with a graphical interface made with Tkinter, the graphical interface is inspired by Windows to make it more user-friendly

## Features

#### Desktop environment:
- It is composed of a wallpaper along with a taskbar
- The taskbar contains a clock, volume and internet icons.
- A start menu.
- Draggabble window (Bugged)

#### Programs:
- Terminal - you can write and execute commands
- File manager - for now it is a static image, functions will be added later.
- Browser - You can browse the internet (currently it only uses html 3, so most of the pages don't work very well)

#### Miscellaneous:
- Boot loader (animation).
- BIOS.
- RSOD (Red Screen of Death).
- BSOD (Black Screen of Death).
- GSOD (Green Screen of death).
- Login (unused).
- Desktop mode.
- Terminal mode.
- File system.

### Some current ideas...
- Antivirus (fake)
- Control panel
- Draggable desktop icons
- Internet
- System configuration

## Installation

Download the code and unzip it, it is necessary to have Python 3.10 and have the following modules installed 

- ```Pillow```       Necessary so that the program can read the images and work.
- ```Psutil```      Necessary for the neofetch command and some functions to work.
- ```Tkinterweb```   Necessary for the browser to work.

For a quick installation use the following command inside the project folder:

```sh
pip install -r requirements.txt
```

And double click on OS.py file to run the project or just in the command line you write 
```sh
python OS.py
```
**NOTE**: If you're on a on a minimal Linux installation, you need a desktop or window manager for tkinter to work, like xorg, xfce, etc.


