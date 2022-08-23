# Beginner's Handbook

> **NOTE**: For now, the key shortcuts applies only to Terminal, windows of other programs can still be dragged normally
- This manual explains the keyboard shortcuts to navigate on the new Window Manager (the mouse is still necessary XD).
- For keyboard shortcuts to have an effect on a window, that window must be active or focused
- All the Terminal commands

---
### Terminal keyboard shortcuts:
- Can be placed on the Right by pressing:
`<alt> + <right-arrow>`
- Also can be placed on the Left by pressing:
`<alt> + <left-arrow>`
- To focus a Terminal window, `<double-click>` on it
- To bring the Terminal window to the front of the others, press `<right-click>` on it
- To close it just press `<alt> + <q>`, or type the `exit` command

---
### Terminal commands:
- It is recommended to always write the commands in lowercase

| Commands                           | Info                                                                               | Example usage
|------------------------------------|------------------------------------------------------------------------------------|-----------------------------------------------------------
| CAT                                | Prints and return the files content                                                | `cat Notes.txt`
| CD                                 | Change the current directory                                                       | `cd Folder` \| `cd ..` \| `cd <-`
| CLEAR \| CLS                       | Clear the Terminal screen                                                          | `clear`
| DIR \| LS \| DIRS \| LSDIRS \| ?   | Shows a list of files and directories in the current directory                     | `dir`
| ECHO \| PRINT                      | Prints a message or string on the screen                                           | `echo "Hello World" -color=red -bgcolor=blue -font=arial`
| MKDIR \| MD \| MKFOLDER            | Make a new direcotry in the current directory                                      | `mkdir new_folder`
| RNDIR \| RN \| RENAMEDIR           | Rename a directory                                                                 | `rndir folder folder2`
| RMDIR \| RD \| RMFOLDER \| DFOLDER | Remove a directory from the current directory                                      | `rmdir folder`
| TOUCH \| MF \| MKFILE              | Make a new empty file                                                              | `touch Notes.txt`
| MV                                 | Move a file to a directory                                                         | `mv Notes.txt folder` \| `mv Notes.txt ..` \| `mv Notes.txt <-`
| DFILE                              | Remove a file from the current directory                                           | `dfile Notes.txt`
| EFILE                              | Edit the content of a file (re-editing a file will overwrite the previous content) | `efile Notes.txt "This is a examaple text"`
| METAFILE                           | Show the file metadata                                                             | `metafile Notes.txt`
| TIME                               | Show the current time (HH, MM, SS)                                                 | `time`
| EXIT                               | Exit from the Terminal                                                             | `exit`
| >>>                                | Python interpreter                                                                 | `>>> print("Hello World!")` \| `>>>  `
| BACKGROUND                         | Change the Terminal background color                                               | `background "#0faa00"`
| FOREGROUND                         | Change the Terminal foreground color                                               | `foreground "#ffffff"`
| NEOFETCH                           | Display a mini-neofetch output                                                     | `neofetch`
