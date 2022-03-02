# Python OS

<p align="center">
  <img src="https://user-images.githubusercontent.com/63316583/150565735-6f2cedf3-a69b-4091-8fce-7b344025f2cd.png" />
</p>

Python OS is an operating system simulator written in Python, with a graphical interface made with Tkinter.

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

It is necessary to have Python 3.10 and have the following modules installed 

- ```Pillow```       Necessary so that the program can read the images and work.
- ```Psutils```      Necessary for the neofetch command and some functions to work.
- ```Tkinterweb```   Necessary for the browser to work.

NOTE: If you're on a Linux distribution, you need a desktop or window manager for tkinter to work.

Download the code, unzip it and double click on OS.py file to run the project or just in the command line you write 
```sh
python OS.py
```
