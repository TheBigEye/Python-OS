from System.UI.Components.UI_Slider import UI_Slider
from System.UI.Components.UI_Checkbutton import UI_Checkbutton
from System.UI.Components.UI_Button import UI_Button
from System.UI.Components.UI_Titlebar import UI_Titlebar

win = Tk()
win.configure(bg="#4A4A4A")
win.geometry("900x500")

winlabel = Label(win, width=90, height=40,bg="#ffffff", fg="white")
winlabel.place(x=0, y=0)

sl = UI_Slider(winlabel, 10, 100, 255, 100, 1)
sl.set_value(50)
sl.place(x=10, y=100)

cb = UI_Checkbutton(winlabel, 10, 200, False)
cb.place(x=10, y=200)

def lol():
    print("lol")

ub = UI_Button(winlabel, 10, 300, "Accept", lol)
ub.place(x=10, y=300)

twin = Label(win, width=80, height=40,bg="#f0f0f0", fg="white")
twin.place(x=10, y=400)

tb = UI_Titlebar(twin, 0, 0, 500)
tb.place(x=0, y=10)

win.mainloop()
