from tkinter import Frame, Label
from System.Utils.Utils import Asset, Asset_color


class UI_Slider(Frame):
    def __init__(self, parent, x, y, width, max_value, min_value):
        Frame.__init__(self, parent)

        self.parent = parent
        self.x = x
        self.y = y
        self.width = width
        self.max_value = max_value
        self.min_value = min_value

        # Get the parent bg color
        self.parent_bg_color = parent.cget("bg")

        self.Thumb_slider_img = Asset_color("Thumb_slider.png", "#ff00ff", self.parent_bg_color)

        self.Track_slider_img = Asset("Track_slider.png")

        self.Track_slider = Label(parent, height = 20, width = self.width , image=self.Track_slider_img, borderwidth="0", bg=self.parent_bg_color)
        self.Track_slider.place(x=x, y=y)

        self.Thumb_slider = Label(self.Track_slider, image=self.Thumb_slider_img, borderwidth="0")
        self.Thumb_slider.place(x=0, y=1)

        def move_thumb(event):
            # Get the mouse position
            mouse_x = event.x
            mouse_y = event.y

            # Get the thumb position
            thumb_x = self.Thumb_slider.winfo_x()
            thumb_y = self.Thumb_slider.winfo_y()

            # Get the thumb width
            thumb_width = self.Thumb_slider.winfo_width()

            # Get the track slider width
            track_slider_width = self.Track_slider.winfo_width()

            # Get the track slider position
            track_slider_x = self.Track_slider.winfo_x()

            self.Thumb_slider.place_forget()

            # move, cannot be out of the track slider
            if mouse_x < 1:
                mouse_x = 1
            elif mouse_x > track_slider_width:
                mouse_x = track_slider_width - 1

            # set the thumb position
            self.Thumb_slider.place(x=mouse_x - thumb_width / 2, y=thumb_y)

            # Set the value
            self.value = int((mouse_x - track_slider_x) / track_slider_width * (self.max_value - self.min_value) + self.min_value)

        self.Track_slider.bind("<B1-Motion>", move_thumb)
        self.Thumb_slider.bind("<B1-Motion>", move_thumb)

    def get_value(self):
        return int(self.value)

    def set_value(self, value):
        self.value = value
        self.Thumb_slider.place(x=(self.value - self.min_value) / (self.max_value - self.min_value) * self.width, y=1)

    def set_max_value(self, max_value):
        self.max_value = max_value

    def set_min_value(self, min_value):
        self.min_value = min_value

    def set_width(self, width):
        self.width = width
        self.Track_slider.place(x=self.x, y=self.y, width=self.width, height=self.Track_slider.winfo_height())
        self.Thumb_slider.place(x=1, y=1)

    def set_bg_color(self, bg_color):
        self.parent_bg_color = bg_color
        self.Track_slider.config(bg=self.parent_bg_color)
        self.Thumb_slider.config(bg=self.parent_bg_color)
    
