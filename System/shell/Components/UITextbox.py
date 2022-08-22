# Custom tkinter Text widget with

import random
from tkinter import *
from tkinter import ttk

from tkinter import Label
from typing import Optional

from Libs.pyLogger.Logger import Logger

# UI Textbox class -> the class uses the Text widget -> UITextbox(master: Misc, size: tuple, colored_words: list of tuples (word, color), text: str)
class UITextbox(Text):
    def __init__(self, master: Label, colored_words: None = None, **kwargs) -> None:
        super().__init__(master)
        # make tag
        self.tag_config('colored', foreground='red')
        if colored_words is not None:
            for word, color in colored_words:
                self.tag_config(word, foreground=color)
        # set text
        self.set_text(kwargs.get('text', ''))
        # set size
        self.config(width=kwargs.get('width', 20), height=kwargs.get('height', 5))
        # set font
        self.config(font=kwargs.get('font', ('Courier', 12)))
        # set wrap
        self.config(wrap=kwargs.get('wrap', 'word'))
        # set scrollbar
        self.config(yscrollcommand=kwargs.get('yscrollcommand', lambda f, l: None))
        self.config(xscrollcommand=kwargs.get('xscrollcommand', lambda f, l: None))
        # set state
        self.config(state=kwargs.get('state', 'normal'))
        # set relief
        self.config(relief=kwargs.get('relief', 'sunken'))
        # set borderwidth
        self.config(borderwidth=kwargs.get('borderwidth', 1))

    def set_text(self, text: str) -> None:
        self.delete(1.0, END)
        self.insert(INSERT, text)
        self.see(END)
        self.update()

    def get_text(self):
        return self.get(1.0, END)

    def clear(self):
        self.delete(1.0, END)
        self.update()

    def append(self, text):
        self.insert(END, text)
        self.see(END)
        self.update()

    def append_colored(self, text, color):
        tag_name = 'colortag_' + ''.join(random.choice('0123456789abcdef') for _ in range(8))

        self.insert(END, text, tag_name)
        self.tag_config(tag_name, foreground=color)
        self.see(END)
        self.update()

    def append_newline(self):
        self.insert(END, '\n')
        self.see(END)
        self.update()

    def insert_color_word(self, text: str, word: list) -> None:

        # list format:
        # [
        #   (word, color),
        #   (word, color),
        #   (word, color)
        # ]

        # get the words and colors
        words = [word[0] for word in word]
        colors = [word[1] for word in word]

        def update_tag():
            tag_name = 'colortag_' + ''.join(random.choice('0123456789abcdef') for _ in range(8))
            return tag_name

        # make a list of words from the text splitted by space
        words_list = text.split(' ')
        # make a list of tags for each word
        tags_list = [update_tag() for _ in range(len(words_list))]

        for i in range(len(words_list)):
            # if the word is in the list of words
            if words_list[i] in words:
                # get the index of the word in the list of words
                index = words.index(words_list[i])
                # set the tag for the word
                self.tag_config(tags_list[i], foreground=colors[index])
                # set the word with the tag
                self.insert(END, words_list[i], tags_list[i])
            else:
                # set the word without the tag
                self.insert(END, words_list[i])
            # insert a space
            self.insert(END, ' ')

        self.see(END)
        self.update()

    def insert_colored(self, text: str, color: str) -> None:
        # generate random tag name for avoid update a tag that is already used
        tag_name = 'colortag_' + ''.join(random.choice('0123456789abcdef') for _ in range(8))

        Logger.info("-> Made tag for color: " + tag_name)
        Logger.info("Color: " + color)
        Logger.info("Text: " + text + "...")

        self.tag_config(tag_name, foreground=color)
        self.insert(INSERT, text, tag_name)
        self.see(END)
        self.update()

    def insert_text(self, text: str, fg_color: Optional[str] = None, bg_color: Optional[str] = None, font: Optional[str] = None) -> None:
        # generate random tag name for avoid update a tag that is already used
        tag_name = 'colortag_' + ''.join(random.choice('0123456789abcdef') for _ in range(8))

        if fg_color is not None:
            self.tag_config(tag_name, foreground=fg_color)
        if bg_color is not None:
            self.tag_config(tag_name, background=bg_color)
        if font is not None:
            self.tag_config(tag_name, font=font)
        self.insert(INSERT, text, tag_name)
        self.see(END)
        self.update()
