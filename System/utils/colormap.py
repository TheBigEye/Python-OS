"""
    Module name:
        Colormap.py

    Abstract:
        This module contains:
            - A list of colors
            - A function to convert colors to rgb
            - A function to convert colors to hex
            - A function to convert colors to hsv

        in general, the module contains color utilities

    Author:
        TheBigEye 6-sep-2021
"""

colors = { # TODO: Add support for other colors
    "white": "#ffffff", "black": "#000000",
    "light gray": "#d3d3d3", "gray": "#808080", "dark gray": "#404040",
    "light red": "#ff0000", "red": "#dd0000", "dark red": "#800000",
    "light yellow": "#ffff00", "yellow": "#dddd00", "dark yellow": "#808000",
    "light lime": "#00ff00", "lime": "#00dd00", "dark lime": "#008000",
    "light cyan": "#00ffff", "cyan": "#00dddd", "dark cyan": "#008b8b",
    "light blue": "#0000ff", "blue": "#0000dd", "dark blue": "#000080",
    "light magenta": "#ff00ff", "magenta": "#dd00dd", "dark magenta": "#800080",
    "light orange": "#ffa500", "orange": "#dd8000", "dark orange": "#800000",
    "light purple": "#800080", "purple": "#800040", "dark purple": "#400000",
    "light brown": "#a52a2a", "brown": "#804000", "dark brown": "#402000",
    "light pink": "#ffc0cb", "pink": "#ff8080", "dark pink": "#c08080",
    "light sky": "#87ceeb", "sky": "#87ceff", "dark sky": "#00bfff",
    "light violet": "#ee82ee", "violet": "#ee82ff", "dark violet": "#b452cd",
    "light indigo": "#4b0082", "indigo": "#4b0082", "dark indigo": "#310066",
    "light puce": "#a0522d", "puce": "#a0522d", "dark puce": "#8b4513",
    "light peach": "#ffdab9", "peach": "#ffdab9", "dark peach": "#e9967a",
    "light mauve": "#e0b0ff", "mauve": "#e0b0ff", "dark mauve": "#cc66cc",
    "light rose": "#ffc0cb", "rose": "#ffc0cb", "dark rose": "#ff8080",
    "light salmon": "#ffa07a", "salmon": "#ffa07a", "dark salmon": "#e9967a",
    "light beige": "#f5f5dc", "beige": "#f5f5dc", "dark beige": "#e6e6c3",
    "light tan": "#d2b48c", "tan": "#d2b48c", "dark tan": "#b8860b",
    "light khaki": "#f0e68c", "khaki": "#f0e68c", "dark khaki": "#bdb76b",
    "light olive": "#808000", "olive": "#808000", "dark olive": "#6b8e23",
    "light maroon": "#800000", "maroon": "#800000", "dark maroon": "#660000",
    "light navy": "#000080", "navy": "#000080", "dark navy": "#000066",
    "light teal": "#008080", "teal": "#008080", "dark teal": "#006666"
}

class Color:
    """
    Color utilities and functions
    """

    def str_to_rgb(color):
        """
        Convert string color to rgb

        Arguments:
            `string : [str]` The string color to convert

        Returns:
            `[tuple]` The rgb color

        Example:
            >>> color_str_rgb("white")
            (255, 255, 255)
        """

        from Libs.pyLogger.Logger import Logger

        color = color.lower()

        # converts the colors dict, from hex to rgb
        for key, value in colors.items():
            colors[key] = tuple(int(value[i:i+2], 16) for i in (1, 3, 5))

            if color in colors:
                return colors[color]
            else :
                Logger.error("Color {} not found, returning black", color)
                return (0, 0, 0)

    def str_to_hex(color):
        """
        Convert string color to hex

        Arguments:
            `string` : `[str]` The string color to convert

        Returns:
            `[str]` The hex color

        Example:
            >>> color_str_hex("white")
            >>> "#ffffff"
        """

        from Libs.pyLogger.Logger import Logger

        color = color.lower()

        # get the hex color from the colors dict
        for key, value in colors.items():
            if color in colors:
                return value
            else :
                Logger.error("Color {} not found, returning black", color)
                return "#000000"

    def hex_to_rgb(hex_color):
        """
        Convert hex color to rgb

        Arguments:
            `hex : [str]` The hex color to convert

        Returns:
            `rgb : [tuple]` The rgb color

        Example:
            >>> color_hex_rgb("#ffffff")
            (255, 255, 255)
        """

        from Libs.pyLogger.Logger import Logger

        # converts the hex_color to rgb
        hex_color = hex_color.lower()
        if hex_color[0] == "#":
            rgb_color = hex_color[1:]
            rgb_color = tuple(int(rgb_color[i:i+2], 16) for i in (0, 2, 4))
            return rgb_color
        else :
            Logger.error("Hex color {} not found, returning black", hex_color)
            return (0, 0, 0)

    def rgb_to_hex(rgb_color):
        """
        Convert rgb color to hex

        Arguments:
            `rgb : [tuple]` The rgb color to convert

        Returns:
            `hex : [str]` The hex color

        Example:
            >>> color_rgb_hex((255, 255, 255))
            "#ffffff"
        """

        from Libs.pyLogger.Logger import Logger

        # converts the rgb_color to hex
        if type(rgb_color) == tuple:
            hex_color = "#"
            for i in rgb_color:
                hex_color += "{:02x}".format(i)
            return hex_color
        else :
            Logger.error("RGB color {} not found, returning black", rgb_color)
            return "#000000"

    def rgb_to_hsv(rgb_color):
        """
        Convert rgb color to hsv

        Arguments:
            `rgb : [tuple]` The rgb color to convert

        Returns:
            `hsv : [tuple]` The hsv color

        Example:
            >>> color_rgb_hsv((255, 255, 255))
            (0.0, 0.0, 1.0)
        """

        from Libs.pyLogger.Logger import Logger

        # converts the rgb_color to hsv
        if type(rgb_color) == tuple:
            r = rgb_color[0] / 255.0
            g = rgb_color[1] / 255.0
            b = rgb_color[2] / 255.0

            max_color = max(r, g, b)
            min_color = min(r, g, b)

            h = 0.0
            s = 0.0
            v = max_color

            if max_color != min_color:
                if max_color == r:
                    h = (g - b) / (max_color - min_color)
                elif max_color == g:
                    h = 2.0 + (b - r) / (max_color - min_color)
                elif max_color == b:
                    h = 4.0 + (r - g) / (max_color - min_color)

                h *= 60.0
                if h < 0.0:
                    h += 360.0

                s = (max_color - min_color) / max_color

            return (h, s, v)
        else:
            Logger.error("RGB color {} not found, returning black", rgb_color)
            return (0, 0, 0)

    def hsv_to_rgb(hsv_color):
        """
        Convert hsv color to rgb

        Arguments:
            `hsv : [tuple]` The hsv color to convert

        Returns:
            `rgb : [tuple]` The rgb color

        Example:
            >>> color_hsv_rgb((0.0, 0.0, 1.0))
            (255, 255, 255)
        """

        from Libs.pyLogger.Logger import Logger

        # converts the hsv_color to rgb
        if type(hsv_color) == tuple:
            hue = hsv_color[0]
            saturation = hsv_color[1]
            value = hsv_color[2]

            hue_i = int(hue / 60.0) % 6
            f = hue / 60.0 - hue_i
            p = value * (1.0 - saturation)
            q = value * (1.0 - f * saturation)
            t = value * (1.0 - (1.0 - f) * saturation)

            if hue_i == 0: rgb_color = (value, t, p)
            elif hue_i == 1: rgb_color = (q, value, p)
            elif hue_i == 2: rgb_color = (p, value, t)
            elif hue_i == 3: rgb_color = (p, q, value)
            elif hue_i == 4: rgb_color = (t, p, value)
            elif hue_i == 5: rgb_color = (value, p, q)

            return rgb_color
        else:
            Logger.error("The value isnt a tuple, returning black", hsv_color)
            return (0, 0, 0)
