# explore the Tkinter GUI toolkit
# drag one image on the canvas
# tested with Python 3.1.1 and Tkinter 8.5

import tkinter as tk

class MyCanvas(tk.Frame):
    def __init__(self, master, photo):
        tk.Frame.__init__(self, master)
        # use pack layout in the class
        # expand frame to fit as window is resized
        self.pack(expand='yes')
        self.master = master
        self.photo = photo
        self.canvas = tk.Canvas()
        self.canvas.pack(side='top', fill='both', expand='yes')
        # initial image upper left corner ('nw') at x=0 and y=0
        self.img = self.canvas.create_image(0, 0, image=photo, anchor='nw')
        # drag upper left corner of image
        self.canvas.bind("<B1-Motion>", self.move_image)

    def move_image(self, event):
        # delete the old image
        self.canvas.delete(self.img)
        # get the mouse position
        x = event.x
        y = event.y
        # create the new image at position x, y
        self.img = self.canvas.create_image(x, y, image=self.photo,
            anchor='nw')
        self.canvas.update()


root = tk.Tk()
root.title("drag upper left corner of image")
# pick an image file you have in your working directory
# or specify full path (without PIL you have to use .gif files)
image_file = "Assets/Info_MessageBox.png"
photo = tk.PhotoImage(file=image_file)
MyCanvas(root, photo)
root.mainloop()