from io import BytesIO
import os
from tkinter import *
from typing import Literal
from PIL import Image, ImageTk

__author__ = "TheBigEye"

# CONVERTIONS ----------------------------------------------------------------
def ImageToTk(image: Image):
    """
    Converts an image to a Tkinter image.
    """

    # Checks if the image is a PIL.Image
    if not isinstance(image, Image.Image):
        raise TypeError("The image must be a PIL.Image.")

    # Converts the image to a Tkinter image
    image = ImageTk.PhotoImage(image)
    return image

def TkToImage(tk_image: ImageTk.PhotoImage):
    """
    Converts a Tkinter image to a PIL.Image.
    """

    # Checks if the image is a Tkinter image
    if not isinstance(tk_image, ImageTk.PhotoImage):
        raise TypeError("The image must be a Tkinter image.")

    # Converts the image to a PIL.Image
    image = Image.frombytes("RGBA", tk_image.size, tk_image.tk.getimage())
    return image

# IMAGE PROCESSING -----------------------------------------------------------
def getImage(path: str):
    """
    Returns an image from a path.
    """

    # Checks if the file exists
    if not os.path.isfile(path):
        raise FileNotFoundError("The file " + path + " does not exist.")

    # Check if the image file is a image
    SUPPORTED_FORMATS = ["png", "jpg", "jpeg", "bmp"]

    file_extension = path.split(".")[-1]
    if file_extension not in SUPPORTED_FORMATS:
        raise TypeError("The file " + path + " is not a supported image format.")

    # Open the image file
    image = Image.open(path)
    image = image.convert("RGBA")
    return image

def setSize(image: Image, size: tuple):
    """
    Resizes an image.
    """

    # Checks if the image is a PIL.Image
    if not isinstance(image, Image.Image):
        raise TypeError("The image must be a PIL.Image.")

    # Checks if the size is a tuple
    if not isinstance(size, tuple):
        raise TypeError("The size must be a tuple, example: (100, 100).")

    # Resizes the image
    image = image.resize(size)
    return image

def replaceColor(image: Image, color: tuple | str, new_color: tuple | str):
    """
    Replaces a color in an image.
    """

    # Checks if the image is a PIL.Image
    if not isinstance(image, Image.Image):
        raise TypeError("The image must be a PIL.Image.")

    # Checks if the color is a tuple or string, if is a string, it must be a hex color, example: "#FFFFFF", if not, it must be a tuple, example: (255, 255, 255)
    if isinstance(color, str):
        if len(color) != 7:
            raise ValueError("The color must be a hex color, example: #FFFFFF.")
        color = color[1:]
        color = (int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16))

    elif isinstance(color, tuple):
        if len(color) != 3:
            raise ValueError("The color must be a tuple, example: (255, 255, 255).")
        color = (color[0], color[1], color[2])

    else:
        raise TypeError("The color must be a string or tuple, example: #FFFFFF or (255, 255, 255).")

    # same for the new color
    if isinstance(new_color, str):
        if len(new_color) != 7:
            raise ValueError("The new color must be a hex color, example: #FFFFFF.")
        new_color = new_color[1:]
        new_color = (int(new_color[0:2], 16), int(new_color[2:4], 16), int(new_color[4:6], 16))

    elif isinstance(new_color, tuple):
        if len(new_color) != 3:
            raise ValueError("The new color must be a tuple, example: (255, 255, 255).")
        new_color = (new_color[0], new_color[1], new_color[2])

    else:
        raise TypeError("The new color must be a string or tuple, example: #FFFFFF or (255, 255, 255).")

    # replace colors
    image = image.convert("RGBA")
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pixel = image.getpixel((x, y))
            if pixel[0] == color[0] and pixel[1] == color[1] and pixel[2] == color[2]:
                image.putpixel((x, y), new_color)
    return image

def setHUE(image: Image, hue: int):
    """
    Sets the hue of an image.
    """

    # Checks if the image is a PIL.Image
    if not isinstance(image, Image.Image):
        raise TypeError("The image must be a PIL.Image.")

    # Checks if the hue is an integer
    if not isinstance(hue, int):
        raise TypeError("The hue must be an integer.")

    # Sets the hue
    image = image.convert("RGBA")
    image = image.convert("HSV")
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            h, s, v = image.getpixel((x, y))
            h = hue
            image.putpixel((x, y), (h, s, v))
    image = image.convert("RGBA")
    return image

def setSaturation(image: Image, saturation: int):
    """
    Sets the saturation of an image.
    """

    # Checks if the image is a PIL.Image
    if not isinstance(image, Image.Image):
        raise TypeError("The image must be a PIL.Image.")

    # Checks if the saturation is an integer
    if not isinstance(saturation, int):
        raise TypeError("The saturation must be an integer.")

    # Sets the saturation
    image = image.convert("RGBA")
    image = image.convert("HSV")
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            h, s, v = image.getpixel((x, y))
            s = saturation
            image.putpixel((x, y), (h, s, v))
    image = image.convert("RGBA")
    return image

def setValue(image: Image, value: int):
    """
    Sets the value of an image.
    """

    # Checks if the image is a PIL.Image
    if not isinstance(image, Image.Image):
        raise TypeError("The image must be a PIL.Image.")

    # Checks if the value is an integer
    if not isinstance(value, int):
        raise TypeError("The value must be an integer.")

    # Sets the value
    image = image.convert("RGBA")
    image = image.convert("HSV")
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            h, s, v = image.getpixel((x, y))
            v = value
            image.putpixel((x, y), (h, s, v))
    image = image.convert("RGBA")
    return image

# GETTERS --------------------------------------------------------------------
def getColor(image: Image, x: int, y: int):
    """
    Returns the color of a pixel.
    """

    # Checks if the image is a PIL.Image
    if not isinstance(image, Image.Image):
        raise TypeError("The image must be a PIL.Image.")

    # Checks if the x and y are integers
    if not isinstance(x, int):
        raise TypeError("The x must be an integer.")
    if not isinstance(y, int):
        raise TypeError("The y must be an integer.")

    # Checks if the x and y are in the image
    if x < 0 or x >= image.size[0]:
        raise ValueError("The x must be in the image.")
    if y < 0 or y >= image.size[1]:
        raise ValueError("The y must be in the image.")

    # Returns the color
    pixel = image.getpixel((x, y))
    return pixel


# MY MASTERPIECE --------------------------------------------------------------------
def setImage(path: str, size: tuple = None, fromColor: str | tuple = None, toColor: str | tuple = None, hue: int = None, saturation: int = None, value: int = None):
    """
    Sets the image.
    """

    # Get the image
    image = getImage(path)

    # Change the color
    if fromColor is not None:
        if toColor is not None:
            image = replaceColor(image, fromColor, toColor)

    # Change the hue
    if hue is not None:
        image = setHUE(image, hue)

    # Change the saturation
    if saturation is not None:
        image = setSaturation(image, saturation)

    # Change the value
    if value is not None:
        image = setValue(image, value)

    # Resize the image (on the last for avoid problems with the color)
    if size is not None:
        image = setSize(image, size)

    # Convert the image to RGBA, and then to TK
    image = image.convert("RGBA")
    image = ImageToTk(image)
    return image
