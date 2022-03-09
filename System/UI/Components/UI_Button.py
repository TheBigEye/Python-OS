from tkinter import Frame, Label
from System.Utils.Utils import Asset_color, Image_getcolor

class UI_Button(Frame):
    def __init__(self, parent, x, y, text, command):
        Frame.__init__(self, parent)

        self.parent = parent
        self.x = x
        self.y = y
        self.text = text
        self.command = command

        # parent bg color
        self.parent_bg_color = parent.cget("bg")

        self.Button_img = Asset_color("Button2.png", "#ff00ff", self.parent_bg_color)
        self.Button_img_hover = Asset_color("Button_hover.png", "#ff00ff", self.parent_bg_color)
        self.Button_img_pressed = Asset_color("Button_pressed.png", "#ff00ff", self.parent_bg_color)

        self.uButton = Label(self.parent, image=self.Button_img, borderwidth="0", bg=self.parent_bg_color)
        self.uButton.place(x=x, y=y)

        self.buttoncolor = Image_getcolor("Button2.png", 5, 5)

        # put text in the button, tahoma font 8
        self.text = Label(self.uButton, text=text, bg=self.buttoncolor, fg="white", font=("Tahoma bold", 8))
        self.textlen = len(text)
        self.text.place(x=(self.uButton.winfo_width() + 30) / 2, y=(self.uButton.winfo_height() / 2))


        global on_enter, on_leave, on_press, on_release
        def on_enter(event):
            self.text.place_forget()
            self.uButton.configure(image=self.Button_img_hover)
            self.text.configure(bg=Image_getcolor("Button_hover.png", 5, 5), fg="white")
            self.text.place(x=(self.uButton.winfo_width() - self.textlen * 6 + 4) / 3, y=(self.uButton.winfo_height() / 8))

        def on_leave(event):
            self.text.place_forget()
            self.uButton.configure(image=self.Button_img)
            self.text.configure(bg=Image_getcolor("Button2.png", 5, 5), fg="white")
            self.text.place(x=(self.uButton.winfo_width() - self.textlen * 6 + 4) / 3, y=(self.uButton.winfo_height() / 8))

        def on_press(event):
            self.text.place_forget()
            self.uButton.configure(image=self.Button_img_pressed)
            self.text.configure(bg=Image_getcolor("Button_pressed.png", 5, 5), fg="white")
            self.command()
            self.text.place(x=(self.uButton.winfo_width() - self.textlen * 6 + 4) / 3, y=(self.uButton.winfo_height() / 8))
        
        def on_release(event):
            self.text.place_forget()
            self.uButton.configure(image=self.Button_img)
            self.text.configure(bg=Image_getcolor("Button2.png", 5, 5), fg="white")
            self.text.place(x=(self.uButton.winfo_width() - self.textlen * 6 + 4) / 3, y=(self.uButton.winfo_height() / 8))

        self.uButton.bind("<Enter>", on_enter)
        self.uButton.bind("<Leave>", on_leave)
        self.uButton.bind("<Button-1>", on_press)
        self.uButton.bind("<ButtonRelease-1>", on_release)

        self.text.bind("<Enter>", on_enter)
        self.text.bind("<Leave>", on_leave)
        self.text.bind("<Button-1>", on_press)
        self.text.bind("<ButtonRelease-1>", on_release)




