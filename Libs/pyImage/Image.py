"""
    Module Name:
        Image.py

    Module Description:
        This module implements Images related utilities.
        - ImageToTk
        - TkToImage
        - getImage
        - setSize
        - replaceColor
        etc ...
"""

import os

from PIL import Image as Img
from PIL.Image import Image as PILImg
from PIL.ImageTk import PhotoImage

__author__ = "TheBigEye"

class Image:
    """ Implements an image. """

    def __init__(self):
        """ Constructor. """

        # Check if Pillow is installed
        if not Img:
            raise ImportError("Pillow is not installed, please install it with 'pip -m install Pillow'")

    # CONVERTIONS ----------------------------------------------------------------
    def ImageToTk(image: PILImg):
        """
        Converts an image to a Tkinter image.
        """

        # Checks if the image is a PIL.Image
        if not isinstance(image, Image):
            raise TypeError("The image must be a PIL.Image.")

        # Converts the image to a Tkinter image
        image = PhotoImage(image)
        return image

    def TkToImage(tk_image: PhotoImage):
        """
        Converts a Tkinter image to a PIL.Image.
        """

        # Checks if the image is a Tkinter image
        if not isinstance(tk_image, PhotoImage):
            raise TypeError("The image must be a Tkinter image.")

        # Converts the image to a PIL.Image
        image = PILImg.frombytes("RGBA", tk_image.size, tk_image.tk.getimage())
        return image

    # IMAGE PROCESSING -----------------------------------------------------------
    def getImage(path: str) -> PILImg:
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
        image = Img.open(path)
        image = image.convert("RGBA")
        return image

    def setSize(image: PILImg, size: tuple) -> PILImg:
        """
        Resizes an image.
        """

        # Checks if the image is a PIL.Image
        if not isinstance(image, PILImg):
            raise TypeError("The image must be a PIL.Image.")

        # Checks if the size is a tuple
        if not isinstance(size, tuple):
            raise TypeError("The size must be a tuple, example: (100, 100).")

        # Resizes the image
        image = image.resize(size)
        return image

    def replaceColor(image: PILImg, color: tuple | str, new_color: tuple | str ) -> PILImg:
        """
        Replaces a color in an image.
        """

        # Checks if the image is a PIL.Image
        if not isinstance(image, PILImg):
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

    def setHUE(image: PILImg, hue: int):
        """
        Sets the hue of an image.
        """

        # Checks if the image is a PIL.Image
        if not isinstance(image, PILImg):
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

    def setSaturation(image: PILImg, saturation: int) -> PILImg:
        """
        Sets the saturation of an image.
        """

        # Checks if the image is a PIL.Image
        if not isinstance(image, PILImg):
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

    def setValue(image: PILImg, value: int) -> PILImg:
        """
        Sets the value of an image.
        """

        # Checks if the image is a PIL.Image
        if not isinstance(image, PILImg):
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
    def getColor(image: PILImg, x: int, y: int):
        """
        Returns the color of a pixel.
        """

        # Checks if the image is a PIL.Image
        if not isinstance(image, PILImg):
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

    # getTkColor(image: PhotoImage, x: int, y: int): get the color of a pixel in a Tkinter PhotoImage
    def getTkColor(path: str, x: int, y: int) -> str:
        """
        Returns the color of a pixel in a image.
        """

        # Checks if the path is a string
        if not isinstance(path, str):
            raise TypeError("The path must be a string.")

        # Checks if the x and y are integers
        if not isinstance(x, int):
            raise TypeError("The x must be an integer.")
        if not isinstance(y, int):
            raise TypeError("The y must be an integer.")

        # Checks if the x and y are in the image
        if x < 0 or x >= Img.open(path).size[0]:
            raise ValueError("The x must be in the image.")
        if y < 0 or y >= Img.open(path).size[1]:
            raise ValueError("The y must be in the image.")

        # Returns the color
        image = Img.open(path)
        image = image.convert("RGBA")
        pixel = image.getpixel((x, y))
        color = "#%02x%02x%02x" % (pixel[0], pixel[1], pixel[2])
        return color


    # MY MASTERPIECE --------------------------------------------------------------------
    def setImage(path: str, size: tuple = None, fromColor: str | tuple = None, toColor: str | tuple = None, hue: int = None, saturation: int = None, value: int = None) -> PhotoImage:

        """
        Make a image from a path.

        Arguments:
            `path: [str]` The path to the image file (.PNG recomended).
            `size: [tuple]` The size of the image, put None if you want the image to be the same size as the original.
            `fromColor: [str | tuple]` The color to replace.
            `toColor: [str | tuple]` The color witch will replace the fromColor.
            `hue: [int]` The hue of the image.
            `saturation: [int]` The saturation of the image.
            `value: [int]` The value of the image (brightness 0 - 255).

        Returns:
            `image: [ImageTk]` The image.

        Raises:
            `TypeError` If the path is not a string.
            `ValueError` If the path is not a valid path.
            `TypeError` If the size is not a tuple.
            `TypeError` If the fromColor is not a string or a tuple (HEX or RGB).
            `TypeError` If the toColor is not a string or a tuple (HEX or RGB).
            `TypeError` If the hue is not an integer.
            `TypeError` If the saturation is not an integer.
            `TypeError` If the value is not an integer.

        """


        # Get the image
        image = Image.getImage(path)

        # Change the color
        if fromColor is not None and toColor is not None:
            image = Image.replaceColor(image, fromColor, toColor)

        # Change the hue
        if hue is not None:
            image = Image.setHUE(image, hue)

        # Change the saturation
        if saturation is not None:
            image = Image.setSaturation(image, saturation)

        # Change the value
        if value is not None:
            image = Image.setValue(image, value)

        # Resize the image (on the last for avoid problems with the color)
        if size is not None:
            image = Image.setSize(image, size)

        # Convert the image to RGBA, and then to TK
        image = image.convert("RGBA")
        image = PhotoImage(image)
        return image
