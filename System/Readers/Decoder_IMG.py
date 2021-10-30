import base64
import tkinter as tk

"""
    This indexes and decodes the Base64 encoded images to try to improve execution time

        Images encoded:

        - Logon (The system boot logo)
"""

with open("Assets/Encoded Assets/Logon_IMG", "rb") as Logon_IMG_encoded:  # Decode the Logon image
    Logon_IMG_decoded = base64.b64decode(Logon_IMG_encoded.read())


with open("Assets/Encoded Assets/Loading_GIF", "rb") as Loading_GIF_encoded:  # Decode the Logon image
    Loading_GIF_decoded = base64.b64decode(Loading_GIF_encoded.read())



# IMG Test

root = tk.Tk()
root.geometry("256x256")
# image = tk.PhotoImage(data=Logon_IMG_decoded)
# label = tk.Label(root, image=image, padx=20, pady=20)
# label.pack()



# GIF Test
frameCnt = 60
frames = [
    tk.PhotoImage(data=Loading_GIF_decoded, format="gif -index %i" % (i))
    for i in range(frameCnt)
]

def update(ind):

    frame = frames[ind]
    ind += 1

    if ind == frameCnt:
        ind = 0

    loading.configure(image=frame)
    root.after(50, update, ind)

loading = tk.Label(root, padx=20, pady=20)
loading.pack()



root.after(1, update, 0)

root.mainloop()