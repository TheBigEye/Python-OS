import tkinter as tk
from PIL import Image, ImageTk

### Windows 3.1 Simulator

class Window:
    def __init__(self, parent):
        self.parent = parent

        self.is_resizing = False
        self.is_maximized = False

        self.resize_offset_x = 0
        self.resize_offset_y = 0

        self.childs = []

        self.create_window()


    def create_window(self):

        self.window_frame = tk.LabelFrame(
            self.parent,
            relief="flat",
            padx=2,
            pady=2,
            background="#C0C0C0",
            highlightthickness=1,
            highlightcolor="#000000",
            highlightbackground="#000000"
        )
        self.window_frame.place(x=50, y=50)

        self.corner_A = tk.LabelFrame(
            self.window_frame,
            width=32,
            height=34,
            bg="#C0C0C0",
            highlightthickness=1,
            bd=1,
            highlightcolor="#000000",
            highlightbackground="#000000",
            relief="flat"
        )
        self.corner_A.place(x=-5, y=-5)

        self.corner_B = tk.LabelFrame(
            self.window_frame,
            width=34,
            height=34,
            bg="#C0C0C0",
            highlightthickness=1,
            bd=1,
            highlightcolor="#000000",
            highlightbackground="#000000",
            relief="flat"
        )
        self.corner_B.place(relx=1.0, x=5, y=-5, anchor='ne')

        self.corner_C = tk.LabelFrame(
            self.window_frame,
            width=34,
            height=34,
            bg="#C0C0C0",
            highlightthickness=1,
            bd=1,
            highlightcolor="#000000",
            highlightbackground="#000000",
            relief="flat"
        )
        self.corner_C.place(relx=1.0, x=5, rely=1.0, y=5, anchor='se')

        self.corner_D = tk.LabelFrame(
            self.window_frame,
            width=34,
            height=34,
            bg="#C0C0C0",
            highlightthickness=1,
            bd=1,
            highlightcolor="#000000",
            highlightbackground="#000000",
            relief="flat"
        )
        self.corner_D.place(rely=1.0, x=-5, y=5, anchor='sw')

        self.title_bar = tk.Frame(
            self.window_frame,
            relief="flat",
            borderwidth=0,
            background="#000080",
            highlightthickness=1,
            highlightcolor="#000000",
            highlightbackground="#000000"
        )
        self.title_bar.pack(fill="x")

        self.close_icon = ImageTk.PhotoImage(Image.open("./assets/close_button.bmp"))
        self.close_button = tk.Button(
            self.title_bar,
            command=self.close_window,
            image=self.close_icon,
            width=20,
            height=20,
            borderwidth=2,
            relief="raised",
            anchor="center",
            background="#C0C7C8",
            activebackground="#C0C7C8",
            foreground="black"
        )
        self.close_button.pack(side="left")

        self.title_label = tk.Label(
            self.title_bar,
            text="Mini-Ventana",
            font=("Arial", 10, "bold"),
            anchor="center",
            background="#0000A8",
            foreground="white"
        )
        self.title_label.pack(side="left", fill="both", expand=True)

        self.maximize_icon = ImageTk.PhotoImage(Image.open("./assets/maximize_button.bmp"))
        self.maximize_button = tk.Button(
            self.title_bar,
            command=self.maximize_window,
            image=self.maximize_icon,
            width=20,
            height=20,
            borderwidth=2,
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
            borderwidth=2,
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

        self.window_content = tk.Frame(
            self.window_frame,
            bg="#ffffff",
            highlightthickness=1,
            highlightcolor="#000000",
            highlightbackground="#000000"
        )
        self.window_content.pack(fill="both", expand=True)

        # Testing only
        self.circle_canvas = tk.Canvas(
            self.window_content,
            width=200,
            height=200,
            bg="white"
        )
        self.circle_canvas.pack(fill="both", expand=True)
        self.circle = self.circle_canvas.create_oval(50, 50, 150, 150, fill="#008000")

        self.window_frame.bind("<ButtonPress-1>", self.start_drag)
        self.window_frame.bind("<ButtonRelease-1>", self.stop_drag)
        self.window_frame.bind("<B1-Motion>", self.drag)

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

        # Added a binding for the <Configure> event to track changes in the window's size and position
        # This is used to remember the window's size before it was maximized
        self.window_frame.bind("<Configure>", self.track_window_size_and_position)

    def close_window(self):
        self.window_frame.destroy()

    def maximize_window(self):
        if self.is_maximized:
            return

        x = self.window_frame.winfo_x()
        y = self.window_frame.winfo_y()

        width = self.window_frame.winfo_width()
        height = self.window_frame.winfo_height()

        self.previous_size_and_position = (x, y, width, height)
        self.window_frame.place(x=-6, y=-6, width=self.parent.winfo_width() + 12, height=self.parent.winfo_height() + 13)
        self.is_maximized = True

    def minimize_window(self):
        if self.is_maximized:
            # Restore to previous size and position
            x, y, width, height = self.previous_size_and_position
            self.window_frame.place(x=x, y=y, width=width, height=height)
            self.is_maximized = False

    def start_drag(self, event):
        self.bring_to_front(event)
        # Check if the user clicked near one of the corners of the window
        # If so, start resizing instead of dragging
        x = event.x
        y = event.y

        width = self.window_frame.winfo_width()
        height = self.window_frame.winfo_height()

        if x < 10 and y < 10:
            # Top-left corner
            self.start_resize(event)
        elif x > width - 10 and y < 10:
            # Top-right corner
            self.start_resize(event)
        elif x < 10 and y > height - 10:
            # Bottom-left corner
            self.start_resize(event)
        elif x > width - 10 and y > height - 10:
            # Bottom-right corner
            self.start_resize(event)
        else:
            # Not near any corner, start dragging instead of resizing
            self.x = x
            self.y = y


    def stop_drag(self, event):
        if hasattr(self, 'is_resizing') and self.is_resizing:
            # Stop resizing instead of dragging
            self.stop_resize(event)
        else:
            # Stop dragging instead of resizing
            self.x = None
            self.y = None


    def drag(self, event):
        self.bring_to_front(event)
        if hasattr(self, 'is_resizing') and self.is_resizing:
            # Resize instead of drag
            self.resize(event)
        else:
            # Drag instead of resize
            deltax = event.x - self.x
            deltay = event.y - self.y
            x = self.window_frame.winfo_x() + deltax
            y = self.window_frame.winfo_y() + deltay
            self.window_frame.place(x=x, y=y)


    def start_resize(self, event):
        self.bring_to_front(event)
        if not hasattr(self, 'is_resizing') or not (self.is_resizing):
            corner = event.widget  # Get the clicked corner (corner_A, corner_B, corner_C or corner_D)

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

            handle_pos_x_root = handle_x + self.window_frame.winfo_rootx()
            handle_pos_y_root = handle_y + self.window_frame.winfo_rooty()

            self.handle_pos_x = handle_x
            self.handle_pos_y = handle_y

            self.handle_pos_x_root = handle_pos_x_root
            self.handle_pos_y_root = handle_pos_y_root

            self.cursor = cursor
            self.window_frame.config(cursor=cursor)
            self.is_resizing = True

            self.resize_offset_x = event.x
            self.resize_offset_y = event.y


    def stop_resize(self, event):
        if hasattr(self, 'is_resizing') and self.is_resizing:
            # Only stop resizing if we are already resizing (to prevent stopping a resize that never started)
            # This can happen if you release the mouse button while not resizing (which can happen accidentally while dragging fast)
            # If we don't prevent that we will end up with an inconsistent state that will make the window flicker and behave erratically while dragging or resizing
            self.window_frame.config(cursor="")
            self.is_resizing = False


    def resize(self, event):
        self.bring_to_front(event)
        if self.is_resizing:
            deltax = event.x - self.resize_offset_x
            deltay = event.y - self.resize_offset_y

            new_width = max(200, self.window_frame.winfo_width() + deltax * (1 if self.handle_pos_x == 0 else -1))
            new_height = max(150, self.window_frame.winfo_height() + deltay * (1 if self.handle_pos_y == 0 else -1))

            new_x = self.window_frame.winfo_x() + (0 if self.handle_pos_x == 0 else deltax)
            new_y = self.window_frame.winfo_y() + (0 if self.handle_pos_y == 0 else deltay)

            self.window_frame.place(x=new_x, y=new_y, width=new_width, height=new_height)

            canvas_width = new_width - 20
            canvas_height = new_height - 60

            if canvas_width > 0 and canvas_height > 0:
                self.circle_canvas.config(width=canvas_width, height=canvas_height)

            self.resize_offset_x = event.x
            self.resize_offset_y = event.y


    def track_window_size_and_position(self, event):
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

    def bring_to_front(self, event):
        self.window_frame.lift()

    def create_child_window(self):
        child_window = Window(self.window_content)  # Create a new Window instance as a child
        self.childs.append(child_window)  # Add the child window to the list of windows
        return child_window


class WindowManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Window Manager")
        self.root.geometry("1024x600")
        self.windows = []

        self.root.iconbitmap("./assets/icon.ico")
        self.root.config(cursor="@./assets/cursor_a.cur")

        self.main_frame = tk.Frame(self.root, bg="#008080")
        self.main_frame.pack(fill="both", expand=True)

        # Splash imagein the centrer of the screen
        self.background_image = ImageTk.PhotoImage(Image.open("./assets/splash.bmp"))
        self.background_label = tk.Label(self.main_frame, image=self.background_image, bd= 0)

        self.copyright_label = tk.Label(self.main_frame, text="Python WM - This is a test", fg="#ffffff", bg="#008080", font=("Arial", 8, "bold"))

        self.update_on_resize()

        # Bind the <Configure> event to update the position of the splash image
        self.main_frame.bind("<Configure>", lambda event: self.update_on_resize())

    def update_on_resize(self):
        # Update the position of the splash image
        # self.background_label.place(x=(self.main_frame.winfo_width() / 2) - (self.background_image.width() / 2), y=(self.main_frame.winfo_height() / 2) - (self.background_image.height() / 2))

        self.copyright_label.place(x=self.main_frame.winfo_width() - 154, y=self.main_frame.winfo_height() - 20)

    def create_window(self):
        window = Window(self.main_frame)
        self.windows.append(window)

        return window

    def create_child(self, parent: Window):
        child = parent.create_child_window()
        self.windows.append(child)

        return child


def main():
    root = tk.Tk()
    app = WindowManager(root)

    app.create_window()
    app.create_window()

    parent_window = app.create_window()
    app.create_child(parent_window)
    # app.create_child(parent_window)

    root.mainloop()

if __name__ == "__main__":
    main()
