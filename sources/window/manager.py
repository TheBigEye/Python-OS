import tkinter as tk
from PIL import Image, ImageTk
from .window import Window, WindowFlags

class WindowManager:
    """Main window manager class that handles the desktop environment.

    Provides the main application window and manages creation of child windows.
    """

    def __init__(self, root):
        """Initialize the window manager.

        Args:
            root: The root Tkinter window
        """
        self.root = root
        self.root.title("Window Manager")
        self.root.geometry("1024x600")
        self.windows = []

        self.root.iconbitmap("./assets/icon.ico")
        self.root.config(cursor="@./assets/cursor_a.cur")

        self.main_frame = tk.Frame(self.root, bg="#29A97E")
        self.main_frame.pack(fill="both", expand=True)

        # Splash imagein the centrer of the screen
        self.background_image = ImageTk.PhotoImage(Image.open("./assets/splash.bmp"))
        self.background_label = tk.Label(self.main_frame, image=self.background_image, bd= 0)

        self.test_label = tk.Label(
            self.main_frame,
            text="Python WM - This is a test",
            fg="#ffffff",
            bg="#29A97E",
            font=("Fixedsys", 8)
        )

        self.update_on_resize()

        # Bind the <Configure> event to update the position of the splash image
        self.main_frame.bind("<Configure>", lambda event: self.update_on_resize())

    def update_on_resize(self):
        """ Update UI elements positioning when main window is resized """
        # Update the position of the splash image
        # self.background_label.place(x=(self.main_frame.winfo_width() / 2) - (self.background_image.width() / 2), y=(self.main_frame.winfo_height() / 2) - (self.background_image.height() / 2))

        self.test_label.place(x=self.main_frame.winfo_width() - 214, y=self.main_frame.winfo_height() - 20)

    def create_window(self, title="Window", content=None, size=(50, 50, 210, 200), flags=0):
        """
        Create a new top-level window

        Args:
            title: The title of the window
            content: The content widget to be placed inside the window
            size: A tuple of (x, y, width, height) for the window's initial position and size
            flags: Bitmap flags for window options

        Returns:
            Window: The newly created window
        """

        window = Window(self.main_frame, title, content, size, flags)
        self.windows.append(window)

        return window

    def create_child(self, parent: Window, title="Window", content=None, size=(50, 50, 210, 200), flags=0):
        """
        Create a new child window inside the given parent window

        Args:
            parent: The parent Window instance

        Returns:
            Window: The newly created child window
        """

        child = parent.create_child(title, content=content, size=size, flags=flags)
        self.windows.append(child)

        return child
