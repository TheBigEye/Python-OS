import os
# Important variables

# Relative paths (used to be able to execute the program from anywhere)
# WARNING: don't touch this unless you know what you're doing.

Assets_directory = os.path.join(os.getcwd(), "Assets")
Assets_directory = Assets_directory.replace("\\", "/")

Disk_directory = os.path.join(os.getcwd(), "Disk")
Disk_directory = Disk_directory.replace("\\", "/")

Logs_directory = os.path.join(os.getcwd(), "Logs")
Logs_directory = Logs_directory.replace("\\", "/")

# Cursors for Windows
Cursor_wn = "Assets/Cursors/Windows/Cursor.cur"
XCursor_wn = "Assets/Cursors/Windows/XCursor.cur"
XCursor_2_wn = "Assets/Cursors/Windows/XCursor-2.cur"
Hand_wn = "Assets/Cursors/Windows/Hand.cur"
Hand_2_wn = "Assets/Cursors/Windows/Hand-2.cur"
Loading_wn = "Assets/Cursors/Windows/Loading.cur"

# Cursors for Linux
Cursor_lx = "Assets/Cursors/Linux/Cursor.xbm"
XCursor_lx = "Assets/Cursors/Linux/XCursor.xbm"
XCursor_2_lx = "Assets/Cursors/Linux/XCursor-2.xbm"
Hand_lx = "Assets/Cursors/Linux/Hand.xbm"
Hand_2_lx = "Assets/Cursors/Linux/Hand-2.xbm"
Loading_lx = "Assets/Cursors/Linux/Loading.xbm"

