<!-- ----------------------------------------------------------------------- Python OS ----------------------------------------------------------------------------->

<!-- Text header -->
<p align="center">
    <a href="https://github.com/TheBigEye/Python-OS#gh-light-mode-only"> <!-- light mode -->
        <img
            width="100%"
            src="https://github.com/TheBigEye/TheBigEye/blob/main/assets/projects/Python-OS/Light-header.svg?raw=true" alt="Light mode Python OS logo!"
        />
    </a>
    <a href="https://github.com/TheBigEye#gh-dark-mode-only"> <!-- dark mode -->
        <img
            width="100%"
            src="https://github.com/TheBigEye/TheBigEye/blob/main/assets/projects/Python-OS/Dark-header.svg?raw=true" alt="Dark mode Python OS logo!!"
        />
    </a>
</p>

<!-- Badges -->
<p align="center"> 
     <a href="https://github.com/TheBigEye#gh-light-mode-only"> <!-- light mode -->
          <img 
               src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue&color=4f4f4f" 
               Title="Made with Python"  
          />
          <img 
               src="https://komarev.com/ghpvc/?username=Eye-Python-OS&label=Views&style=for-the-badge" 
               Title="Views" 
          />
          <img 
               src="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=ffffff&color=blue" 
               Title="Programmed using VScode" 
          />
     </a>
     <a href="https://github.com/TheBigEye#gh-dark-mode-only"> <!-- dark mode -->
          <img 
               src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue&color=4f4f4f" 
               Title="Made with Python"  
          />
          <img 
               src="https://komarev.com/ghpvc/?username=Eye-Python-OS&label=Views&color=000000&style=for-the-badge" 
               Title="Views" 
          />
          <img 
               src="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=blue&color=000000" 
               Title="Programmed using VScode" 
          />
     </a>
</p>



<!-- Light or dark according to the github theme that the user has when viewing it -->

<!-- Logo -->
<img 
    align="right"
    src="https://user-images.githubusercontent.com/63316583/175645873-207b9d4c-7bd9-40b5-8883-ebda57b07dc2.svg"
    title="Python OS"
/>

<!-- ----------------------------------------------------------------------------------------------------------------------------------------------------------------->

<!-- <img src="https://user-images.githubusercontent.com/63316583/156764802-7e1ffb65-f482-45ef-9c05-f82d9c4b4e23.svg" width="512" height="360"> UNUSED but usefuul -->

**Python OS** is an operating system simulator written in Python, with a graphical interface made with Tkinter, the graphical interface is inspired by Windows to make it more user-friendly.

This was developed from the beginning as a hobby, currently I use it to learn and apply my knowledge with Python and GUI design :).
## Features

#### Desktop environment:
- It is composed of a wallpaper along with a taskbar.
- The taskbar contains a clock, volume and internet icons.
- A start menu.
- Draggabble windows.

#### Programs:
- **Terminal** - you can write and execute commands.
- **File manager** - You can see files and folders, change directories and see the size of each file.
- **Browser** - You can browse the internet (currently it only uses html 3, so most of the pages don't work very well).

#### Miscellaneous:
- **Boot loader** (animation).
- **BIOS**.
- **RSOD** (Red Screen of Death).
- **BSOD** (Black Screen of Death).
- **GSOD** (Green Screen of death).
- **Login** (unused).
- **Desktop mode**.
- **Terminal mode.**
- **File system**.

#### Some current ideas:
- **Antivirus (fake).**
- **Control pane.**
- **Draggable desktop icons.**
- **Internet.**
- **System configuration.**
- **Reboot and shutdown.**

## Bugs
- Dragging windows can cause their content to flicker or no longer render.
- Sometimes taskbar buttons flicker.

## Installation

> **Note**: If you're on a on a minimal Linux installation:
> * You may need to install a desktop or window manager compatible with the `python-tk` package to work ._.

Download the code and unzip it, it is necessary to have Python 3.10 and have the following modules installed 

- [`Pillow`          ](https://github.com/python-pillow/Pillow)          Necessary so that the program can read the images and work.
- [`Psutil`          ](https://github.com/giampaolo/psutil)              Necessary for the neofetch command and some functions to work.
- [`Tkinterweb`      ](https://github.com/Andereoo/TkinterWeb)           Necessary for the browser to work.
- [`TkinterMapView`  ](https://github.com/TomSchimansky/TkinterMapView)  Necessary for the Map Viewer to work.

For a quick installation use the following command inside the project folder:

```sh
pip install -r requirements.txt
```

And double click on OS.py file to run the project or just in the command line you write 
```sh
python OS.py
```


<!-- -------------------------------------------------------------------------- Credits ------------------------------------------------------------------------------>
<!-- Header and footer svgs --- kyechan99/capsule-render -->
<!-- Views counter --- antonkomarev/github-profile-views-counter -->
<!-- ---------------------------------------------------------------------------- END -------------------------------------------------------------------------------->
