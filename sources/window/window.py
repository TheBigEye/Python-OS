import tkinter as tk
from PIL import Image, ImageTk
from enum import IntFlag


class WindowFlags(IntFlag):
    """
    Bitmap flags for window options.

    'WN' means 'Window Not', so 'WN_DRAGABLE' means 'Window Not Dragable',
    'WN_RESIZABLE' means 'Window Not Resizable', and so on.

    """
    WN_CONTROLS =  1
    WN_DRAGABLE =  2
    WN_RESIZABLE = 4


class Window:
    """
    A class representing a draggable, resizable window in the style of Windows 3.1.

    The window includes a title bar with minimize, maximize and close buttons,
    resizable corners, and a content area that can contain child windows.
    """
    def __init__(self, parent, title, content, size, flags):
        """Initialize a new window.

        Args:
            parent: The parent widget (either the main frame or another window's content area)
            title: The title of the window
            content: The content widget to be placed inside the window
            size: A tuple of (x, y, width, height) for the window's initial position and size
            flags: Bitmap flags for window options
        """
        self.parent = parent
        self.title = title
        self.content = content
        self.size = size
        self.flags = flags

        # Initialize window state variables
        self.is_resizing = False
        self.is_maximized = False

        # Store the previous size and position for restoration when un-maximizing
        self.resize_offset_x = 0
        self.resize_offset_y = 0

        # Create a list to store child windows references
        self.childs = []

        self.create_window()
        if self.content:
            self.set_content(self.content)


    def create_window(self):
        """ Create the window's visual elements and set up event bindings """

        # Unpack the size tuple
        x, y, width, height = self.size

        # Create the main window frame
        self.window_frame = tk.LabelFrame(
            self.parent,
            relief="flat",
            padx=2,
            pady=2,
            background="#154095",
            highlightthickness=1,
            highlightcolor="#000000",
            highlightbackground="#000000"
        )
        self.window_frame.place(x=x, y=y, width=width, height=height)

        # Add resizable corners if the window is resizable
        if not self.flags & WindowFlags.WN_RESIZABLE:
            self.corner_A = tk.LabelFrame(
                self.window_frame,
                width=31,
                height=31,
                bg="#184AA5",
                highlightthickness=1,
                bd=1,
                highlightcolor="#000000",
                highlightbackground="#000000",
                relief="flat"
            )
            self.corner_A.place(x=-5, y=-5)

            self.corner_B = tk.LabelFrame(
                self.window_frame,
                width=31,
                height=31,
                bg="#184AA5",
                highlightthickness=1,
                bd=1,
                highlightcolor="#000000",
                highlightbackground="#000000",
                relief="flat"
            )
            self.corner_B.place(relx=1.0, x=5, y=-5, anchor='ne')

            self.corner_C = tk.LabelFrame(
                self.window_frame,
                width=31,
                height=31,
                bg="#184AA5",
                highlightthickness=1,
                bd=1,
                highlightcolor="#000000",
                highlightbackground="#000000",
                relief="flat"
            )
            self.corner_C.place(relx=1.0, x=5, rely=1.0, y=5, anchor='se')

            self.corner_D = tk.LabelFrame(
                self.window_frame,
                width=31,
                height=31,
                bg="#184AA5",
                highlightthickness=1,
                bd=1,
                highlightcolor="#000000",
                highlightbackground="#000000",
                relief="flat"
            )
            self.corner_D.place(rely=1.0, x=-5, y=5, anchor='sw')


        # Create the title bar with a close button
        self.title_bar = tk.Frame(
            self.window_frame,
            relief="raised",
            borderwidth=1,
            background="#FFFFFF",
            highlightthickness=0,
            highlightcolor="#FCFCFC",
            highlightbackground="#FCFCFC"
        )
        self.title_bar.pack(fill="x")

        self.close_icon = ImageTk.PhotoImage(Image.open("./assets/close_button.bmp"))
        self.close_button = tk.Button(
            self.title_bar,
            command=self.close_window,
            image=self.close_icon,
            width=20,
            height=20,
            borderwidth=1,
            relief="flat",
            anchor="center",
            background="#C0C7C8",
            activebackground="#C0C7C8",
            foreground="black"
        )
        self.close_button.pack(side="left")

        self.title_label = tk.Label(
            self.title_bar,
            text=self.title,
            font=("Arial", 10, "bold"),
            anchor="center",
            background="#154095",
            foreground="#FCFCFC"
        )
        self.title_label.pack(side="left", fill="both", expand=True)

        # Add maximize and minimize buttons if the window has controls
        if not self.flags & WindowFlags.WN_CONTROLS:
            self.maximize_icon = ImageTk.PhotoImage(Image.open("./assets/maximize_button.bmp"))
            self.maximize_button = tk.Button(
                self.title_bar,
                command=self.maximize_window,
                image=self.maximize_icon,
                width=20,
                height=20,
                borderwidth=1,
                relief="raised",
                anchor="center",
                bg="#C0C7C8",
                activebackground="#C0C7C8",
                fg="#000000",
                highlightthickness=1,
                highlightcolor="#000000",
                highlightbackground="#000000"
            )
            self.maximize_button.pack(side="right")

            self.shrink_icon = ImageTk.PhotoImage(Image.open("./assets/minimize_button.bmp"))
            self.shrink_button = tk.Button(
                self.title_bar,
                command=self.minimize_window,
                image=self.shrink_icon,
                width=20,
                height=20,
                borderwidth=1,
                relief="raised",
                anchor="center",
                bg="#C0C7C8",
                activebackground="#C0C7C8",
                fg="#000000",
                highlightthickness=1,
                highlightcolor="#000000",
                highlightbackground="#000000"
            )
            self.shrink_button.pack(side="right")

        # Create the content area of the window
        self.window_content = tk.Frame(
            self.window_frame,
            bg="#ffffff",
            highlightthickness=1,
            highlightcolor="#000000",
            highlightbackground="#000000"
        )
        self.window_content.pack(fill="both", expand=True)

        # Add a canvas with a circle as a placeholder for content
        self.circle_canvas = tk.Canvas(
            self.window_content,
            width=200,
            height=200,
            bg="white"
        )
        self.circle_canvas.pack(fill="both", expand=True)
        self.circle = self.circle_canvas.create_oval(50, 50, 150, 150, fill="#008000")

        # Bind drag events if the window is draggable
        if not self.flags & WindowFlags.WN_DRAGABLE:
            self.window_frame.bind("<ButtonPress-1>", self.start_drag)
            self.window_frame.bind("<ButtonRelease-1>", self.stop_drag)
            self.window_frame.bind("<B1-Motion>", self.drag)

            self.title_label.bind("<ButtonPress-1>", self.start_drag)
            self.title_label.bind("<ButtonRelease-1>", self.stop_drag)
            self.title_label.bind("<B1-Motion>", self.drag)

        # Bind resize events if the window is resizable
        if not self.flags & WindowFlags.WN_RESIZABLE:
            self.corner_A.bind("<ButtonPress-1>", self.start_resize)
            self.corner_A.bind("<ButtonRelease-1>", self.stop_resize)
            self.corner_A.bind("<B1-Motion>", self.resize)

            self.corner_B.bind("<ButtonPress-1>", self.start_resize)
            self.corner_B.bind("<ButtonRelease-1>", self.stop_resize)
            self.corner_B.bind("<B1-Motion>", self.resize)

            self.corner_C.bind("<ButtonPress-1>", self.start_resize)
            self.corner_C.bind("<ButtonRelease-1>", self.stop_resize)
            self.corner_C.bind("<B1-Motion>", self.resize)

            self.corner_D.bind("<ButtonPress-1>", self.start_resize)
            self.corner_D.bind("<ButtonRelease-1>", self.stop_resize)
            self.corner_D.bind("<B1-Motion>", self.resize)

        # Track window size and position changes
        self.window_frame.bind("<Configure>", self.track_window_size_and_position)
        self.title_label.bind("<Configure>", self.track_window_size_and_position)


    def close_window(self):
        """ Destroy the window and remove it from the display """
        self.window_frame.destroy()


    def maximize_window(self):
        """
        Maximize the window to fill the entire parent widget

        Stores the previous size and position for restoration when un-maximizing
        """

        # If the window is already maximized, do nothing
        if self.is_maximized:
            return

        # Store the current size and position for restoration
        x = self.window_frame.winfo_x()
        y = self.window_frame.winfo_y()

        width = self.window_frame.winfo_width()
        height = self.window_frame.winfo_height()

        self.previous_size_and_position = (x, y, width, height)

        # Get parent dimensions
        parent_width = self.parent.winfo_width()
        parent_height = self.parent.winfo_height()

        # Maximize the window to fill the parent widget
        self.window_frame.place(x=-6, y=-6, width=parent_width + 12, height=parent_height + 13)
        self.is_maximized = True

        # Update all maximized child windows to fit new size
        for child in self.childs:
            if child.is_maximized:
                content_width = self.window_content.winfo_width()
                content_height = self.window_content.winfo_height()
                child.window_frame.place(x=-6, y=-6, width=content_width + 12, height=content_height + 13)


    def minimize_window(self):
        """ Restore the window to its previous size and position if maximized """

        # If the window is not minimized, do nothing
        if self.is_maximized:
            # Restore to previous size and position
            x, y, width, height = self.previous_size_and_position
            self.window_frame.place(x=x, y=y, width=width, height=height)
            self.is_maximized = False

            # Update all child windows that are maximized
            for child in self.childs:
                if child.is_maximized:
                    child.maximize_window()


    def start_drag(self, event):
        """ Begin window dragging operation """

        # Bring the window to the front
        self.lift(event)

        # Store initial mouse position and window position
        self.drag_start_x = event.x_root
        self.drag_start_y = event.y_root
        self.window_start_x = self.window_frame.winfo_x()
        self.window_start_y = self.window_frame.winfo_y()

        # Prevent conflict with resize operations
        self.is_dragging = True


    def stop_drag(self, event: tk.Event):
        """ End window dragging operation """
        self.is_dragging = False
        self.drag_start_x = None
        self.drag_start_y = None


    def drag(self, event: tk.Event):
        """ Handle window movement during drag operation """

        # Prevent dragging if the window is not being dragged (Yeah, crazy LOL)
        if not hasattr(self, 'is_dragging') or not self.is_dragging or self.is_maximized:
            return

        # Calculate the displacement from the start position
        deltax = event.x_root - self.drag_start_x
        deltay = event.y_root - self.drag_start_y

        # Update window position based on initial position plus displacement
        new_x = self.window_start_x + deltax
        new_y = self.window_start_y + deltay

        self.window_frame.place(x=new_x, y=new_y)


    def start_resize(self, event):
        """ Begin window resizing operation """
        self.lift(event)

        # Prevent conflict with drag operations
        if hasattr(self, 'is_dragging'):
            self.is_dragging = False

        corner = event.widget

        # Store initial window geometry
        self.resize_start_x = event.x_root
        self.resize_start_y = event.y_root
        self.window_start_width = self.window_frame.winfo_width()
        self.window_start_height = self.window_frame.winfo_height()
        self.window_start_x = self.window_frame.winfo_x()
        self.window_start_y = self.window_frame.winfo_y()

        # Determine which corner was clicked and set the cursor accordingly
        if corner == self.corner_A:
            cursor = "top_left_corner"
            handle_x = self.window_frame.winfo_width() - 1
            handle_y = self.window_frame.winfo_height() - 1
        elif corner == self.corner_B:
            cursor = "top_right_corner"
            handle_x = 0
            handle_y = self.window_frame.winfo_height() - 1
        elif corner == self.corner_C:
            cursor = "bottom_right_corner"
            handle_x = 0
            handle_y = 0
        elif corner == self.corner_D:
            cursor = "bottom_left_corner"
            handle_x = self.window_frame.winfo_width() - 1
            handle_y = 0

        # Store the handle position relative to the window and the root window
        handle_pos_x_root = handle_x + self.window_frame.winfo_rootx()
        handle_pos_y_root = handle_y + self.window_frame.winfo_rooty()

        # Store the handle position relative to the window
        self.handle_pos_x = handle_x
        self.handle_pos_y = handle_y

        # Store the handle position relative to the root window
        self.handle_pos_x_root = handle_pos_x_root
        self.handle_pos_y_root = handle_pos_y_root

        # Set the cursor and start resizing
        self.cursor = cursor
        self.window_frame.config(cursor=cursor)
        self.is_resizing = True

        # Store the initial mouse position for resizing
        self.resize_offset_x = event.x
        self.resize_offset_y = event.y


    def stop_resize(self, event: tk.Event):
        """
        End window resizing operation

        Args:
            event: The mouse event that triggered the end of resizing
        """
        if hasattr(self, 'is_resizing') and self.is_resizing:
            # Only stop resizing if we are already resizing (to prevent stopping a resize that never started)
            # This can happen if you release the mouse button while not resizing (which can happen accidentally while dragging fast)
            # If we don't prevent that we will end up with an inconsistent state that will make the window flicker and behave erratically while dragging or resizing
            self.window_frame.config(cursor="")
            self.is_resizing = False


    def resize(self, event: tk.Event):
        """Handle window resizing during resize operation.

        Args:
            event: The mouse motion event

        Updates window dimensions while maintaining minimum size constraints.
        """
        self.lift(event)
        if not self.is_resizing:
            return

        # Calculate the displacement from the start position
        deltax = event.x_root - self.resize_start_x
        deltay = event.y_root - self.resize_start_y

        # Calculate new dimensions based on which corner is being dragged
        if self.handle_pos_x == 0:
            # Left corners
            new_width = max(200, self.window_start_width + deltax)
            new_x = self.window_start_x
        else:
            # Right corners
            new_width = max(200, self.window_start_width - deltax)
            new_x = self.window_start_x + deltax

        if self.handle_pos_y == 0:
            # Bottom corners
            new_height = max(150, self.window_start_height + deltay)
            new_y = self.window_start_y
        else:
            # Top corners
            new_height = max(150, self.window_start_height - deltay)
            new_y = self.window_start_y + deltay

        # Update window geometry in a single operation
        self.window_frame.place(x=new_x, y=new_y, width=new_width, height=new_height)

        # Update canvas size if needed
        canvas_width = new_width - 20
        canvas_height = new_height - 60

        if canvas_width > 0 and canvas_height > 0:
            self.circle_canvas.config(width=canvas_width, height=canvas_height)

    def track_window_size_and_position(self, event: tk.Event):
        """Store window geometry for restore operations.

        Args:
            event: The Configure event containing new geometry

        Used to remember window size/position before maximize/minimize.
        """
        # Track changes in the window's size and position to remember its size before it was maximized or shrinked
        # This is used to restore the window to its previous size when it is un-maximized or un-shrinked
        x = event.x
        y = event.y

        width = event.width
        height = event.height

        if not hasattr(self, 'is_maximized') or not (self.is_maximized):
            # Only track changes in size and position when the window is not maximized or shrinked
            # Otherwise we would overwrite the previous size and position with the maximized or shrinked size and position
            # And then when we un-maximize or un-shrink the window it would be restored to the wrong size and position (the maximized or shrinked size and position instead of the previous size and position)
            if not hasattr(self,'is_shrinked') or not (self.is_shrinked):
                # Only track changes in size and position when the window is not shrinked or maximized
                # Otherwise we would overwrite the previous size and position with the shrinked or maximized size and position
                # And then when we un-shrink or un-maximize the window it would be restored to the wrong size and position (the shrinked or maximized size and position instead of the previous size and position)
                self.previous_size_and_position = (x, y, width, height)

        # Update maximized child windows when parent size changes
        if hasattr(self, 'childs'):
            for child in self.childs:
                if hasattr(child, 'is_maximized') and child.is_maximized:
                    # Get parent content area dimensions
                    content_width = self.window_content.winfo_width()
                    content_height = self.window_content.winfo_height()
                    # Update child window size to match new parent content area
                    child.window_frame.place(x=-6, y=-6,
                                          width=content_width + 12,
                                          height=content_height + 13)

    def lift(self, event: tk.Event):
        """
        Raise window above other windows in z-order.

        Args:
            - event: The event that triggered the raise operation
        """

        # Yeah, thsi is easy, just lift the window frame above all other windows
        self.window_frame.lift()


    def create_child(self, title, content, size, flags):
        """Create a new window as a child of this window's content area.

        Returns:
            Window: The newly created child window
        """
        child_window = Window(self.window_content, title, content, size, flags)  # Create a new Window instance as a child
        self.childs.append(child_window)  # Add the child window to the list of windows
        return child_window


    def set_content(self, content):
        """
        Set the content widget inside the window and ensure it adapts to the window size.

        Arguments:
            - content: The content widget to be placed inside the window (Must be a class, not an instance)
        """
        # The circle canvas works like a reference content widget
        self.circle_canvas.pack_forget() # We need to destroy it

        # We need to destroy the existing content widget before adding a new one
        self.content = content(self.window_content) # content must be a class, not an instance
        self.content.pack(fill="both", expand=True) # then we can place the widget inside the window
