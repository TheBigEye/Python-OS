# Color list :)

# Colors VGA (16 only | name | code |)
White =        "#FFFFFF"
Light_gray =   "#C0C0C0"
Dark_gray =    "#808080"
Black =        "#000000"
High_red =     "#FF0000"
Low_red =      "#800000"
Yellow =       "#FFFF00"
Brown =        "#808000"
Lime =         "#00FF00"
Green =        "#008000"
Aqua =         "#00FFFF"
Cyan =         "#008080"
High_blue =    "#0000FF"
Low_blue =     "#000080"
Magenta =      "#FF00FF"
Purple =       "#800080"

# NOTE: I know this is somewhat useless assuming writing the hex value is more flexible in tkinter


def color_str_rgb(string):
    """
    Convert string color to rgb
    """

    from System.Utils.Utils import print_error

    string = string.lower()

    if string == "black": return (0, 0, 0)
    elif string == "white": return (255, 255, 255)
    elif string == "red": return (255, 0, 0)
    elif string == "green": return (0, 255, 0)
    elif string == "blue": return (0, 0, 255)
    elif string == "yellow": return (255, 255, 0)
    elif string == "cyan": return (0, 255, 255)
    elif string == "magenta" or string == "fuchsia": return (255, 0, 255)
    elif string == "grey": return (128, 128, 128)
    elif string == "darkgrey": return (64, 64, 64)
    elif string == "lightgrey": return (192, 192, 192)
    elif string == "darkred": return (128, 0, 0)
    elif string == "lightred": return (255, 128, 128)
    elif string == "darkgreen": return (0, 128, 0)
    elif string == "lightgreen": return (128, 255, 128)
    elif string == "darkblue": return (0, 0, 128)
    elif string == "lightblue": return (128, 128, 255)
    elif string == "darkyellow": return (128, 128, 0)
    elif string == "lightyellow": return (255, 255, 128)
    elif string == "darkcyan": return (0, 128, 128)
    elif string == "lightcyan": return (128, 255, 255)
    elif string == "darkmagenta" or string == "darkfuchsia": return (128, 0, 128)
    elif string == "lightmagenta" or string == "lightfuchsia": return (255, 128, 255)

    else:
        print_error(string + " color not found")
        return (0, 0, 0)


def color_hex_rgb(hex):
    """
    Convert hex color to rgb
    """

    from System.Utils.Utils import print_error

    if hex[0] == "#":
        hex = hex[1:]
        hex = hex.lstrip("#")
        hex = tuple(int(hex[i:i+2], 16) for i in (0, 2 ,4))
        return hex
    else:
        print_error(hex + " hex color not found")
        return (0, 0, 0)


def color_rgb_hex(rgb):
    """
    Convert rgb color to hex
    """

    from System.Utils.Utils import print_error

    if type(rgb) == tuple:
        return "#" + "".join(["%02x" % i for i in rgb])
    else:
        print_error(rgb + " rgb color not found")
        return "#000000"


def color_rgb_hsv(rgb):
    """
    Convert rgb color to hsv
    """

    from System.Utils.Utils import print_error

    if type(rgb) == tuple:
        r = rgb[0]/255
        g = rgb[1]/255
        b = rgb[2]/255

        min_value = min(r, g, b)
        max_value = max(r, g, b)
        delta = max_value - min_value

        if delta == 0:
            hue = 0
        elif max_value == r:
            hue = 60 * (((g - b) / delta) % 6)
        elif max_value == g:
            hue = 60 * (((b - r) / delta) + 2)
        elif max_value == b:
            hue = 60 * (((r - g) / delta) + 4)

        saturation = 0 if max_value == 0 else delta / max_value

        value = max_value

        hsv = (hue, saturation, value)
        return hsv
    else:
        print_error(rgb + " rgb color not found")
        return (0, 0, 0)


def color_hsv_rgb(hsv):
    """
    Convert hsv color to rgb
    """

    from System.Utils.Utils import print_error

    if type(hsv) == tuple:
        hue = hsv[0]
        saturation = hsv[1]
        value = hsv[2]

        hue_i = int(hue / 60)
        hue_f = hue / 60 - hue_i
        p = value * (1 - saturation)
        q = value * (1 - hue_f * saturation)
        t = value * (1 - (1 - hue_f) * saturation)

        if hue_i == 0:
            rgb = (value, t, p)
        elif hue_i == 1:
            rgb = (q, value, p)
        elif hue_i == 2:
            rgb = (p, value, t)
        elif hue_i == 3:
            rgb = (p, q, value)
        elif hue_i == 4:
            rgb = (t, p, value)
        elif hue_i == 5:
            rgb = (value, p, q)

        return rgb
    else:
        print_error(hsv + " hsv color not found")
        return (0, 0, 0)